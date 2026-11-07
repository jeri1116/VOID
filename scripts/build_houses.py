"""시연용 houses.json 생성 (reports/27 규칙의 입력값).

사용: python -I -X utf8 scripts/build_houses.py
입력: data/안산 빈집정비계획 공람안 빈집목록.csv, data/안산 빈집 158호 위치 근사.csv,
      data/안산 건물 전체 (GIS건물통합정보 202610).csv, data/안산 주택 최근접빈집거리.csv
출력: data/houses.json (방문지 단위, 같은 가린 지번은 한 점)
"""
import csv, json, math, collections, os, datetime as dt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda f: os.path.join(ROOT, 'data', f)

# EPSG:5186 (GRS80, 중부원점 38N 127E, k0=1, FE=200000, FN=600000) -> WGS84 근사(동일 타원체)
A = 6378137.0; F = 1 / 298.257222101
E2 = F * (2 - F); EP2 = E2 / (1 - E2)
LAT0 = math.radians(38); LON0 = math.radians(127); K0 = 1.0; FE = 200000.0; FN = 600000.0
def meridian(phi):
    e4, e6 = E2 * E2, E2 ** 3
    return A * ((1 - E2/4 - 3*e4/64 - 5*e6/256) * phi - (3*E2/8 + 3*e4/32 + 45*e6/1024) * math.sin(2*phi)
                + (15*e4/256 + 45*e6/1024) * math.sin(4*phi) - (35*e6/3072) * math.sin(6*phi))
M0 = meridian(LAT0)
def tm_inverse(x, y):
    M = M0 + (y - FN) / K0
    mu = M / (A * (1 - E2/4 - 3*E2**2/64 - 5*E2**3/256))
    e1 = (1 - math.sqrt(1 - E2)) / (1 + math.sqrt(1 - E2))
    phi1 = (mu + (3*e1/2 - 27*e1**3/32) * math.sin(2*mu) + (21*e1**2/16 - 55*e1**4/32) * math.sin(4*mu)
            + (151*e1**3/96) * math.sin(6*mu) + (1097*e1**4/512) * math.sin(8*mu))
    C1 = EP2 * math.cos(phi1)**2; T1 = math.tan(phi1)**2
    N1 = A / math.sqrt(1 - E2 * math.sin(phi1)**2)
    R1 = A * (1 - E2) / (1 - E2 * math.sin(phi1)**2) ** 1.5
    Dd = (x - FE) / (N1 * K0)
    lat = phi1 - (N1 * math.tan(phi1) / R1) * (Dd**2/2 - (5 + 3*T1 + 10*C1 - 4*C1**2 - 9*EP2) * Dd**4/24
          + (61 + 90*T1 + 298*C1 + 45*T1**2 - 252*EP2 - 3*C1**2) * Dd**6/720)
    lon = LON0 + (Dd - (1 + 2*T1 + C1) * Dd**3/6 + (5 - 2*C1 + 28*T1 - 3*C1**2 + 8*EP2 + 24*T1**2) * Dd**5/120) / math.cos(phi1)
    return math.degrees(lat), math.degrees(lon)

rows = list(csv.DictReader(open(D('안산 빈집정비계획 공람안 빈집목록.csv'), encoding='utf-8-sig')))
plan = {r['빈집코드']: r for r in rows if r['구분'].startswith('계획')}
loc = {r['빈집코드']: r for r in csv.DictReader(open(D('안산 빈집 158호 위치 근사.csv'), encoding='utf-8-sig'))}
B = list(csv.DictReader(open(D('안산 건물 전체 (GIS건물통합정보 202610).csv'), encoding='utf-8-sig')))
H = list(csv.DictReader(open(D('안산 주택 최근접빈집거리.csv'), encoding='utf-8-sig')))

G = 100
def grid(pts):
    g = collections.defaultdict(list)
    for p in pts: g[(int(p[0] // G), int(p[1] // G))].append(p)
    return g
def count_within(g, x, y, R):
    k = int(math.ceil(R / G)); cx, cy = int(x // G), int(y // G); c = 0
    for i in range(cx - k, cx + k + 1):
        for j in range(cy - k, cy + k + 1):
            for p in g.get((i, j), ()):
                if (p[0] - x) ** 2 + (p[1] - y) ** 2 <= R * R: c += 1
    return c
house_g = grid([(float(h['x']), float(h['y'])) for h in H])
fac_g = grid([(float(b['x']), float(b['y'])) for b in B if b['용도명'] in ('교육연구시설', '노유자시설') and b['x']])
DENSITY_MEDIAN = 44  # 주택별 반경 100m 주택 수의 시 중앙값 (reports/27)

key = lambda c: (plan[c]['법정동'], plan[c]['지번(가림)'])
groups = collections.defaultdict(list)
for c in plan: groups[key(c)].append(c)
pts = {k: (sum(float(loc[c]['x']) for c in cs) / len(cs), sum(float(loc[c]['y']) for c in cs) / len(cs)) for k, cs in groups.items()}

PLAN_RANK = {'철거': 3, '안전조치': 2, '개보수': 1, '상시관리': 0}
out = []
for k, cs in groups.items():
    x, y = pts[k]
    lat, lng = tm_inverse(x, y)
    facility = count_within(fac_g, x, y, 100) > 0
    cluster = len(cs) >= 2 or any(kk != k and math.hypot(px - x, py - y) <= 100 for kk, (px, py) in pts.items())
    density = count_within(house_g, x, y, 100) >= DENSITY_MEDIAN
    exp_n = facility + cluster + density
    worst = max(cs, key=lambda c: (PLAN_RANK[plan[c]['정비방식']], plan[c]['등급']))
    r = plan[worst]
    types = sorted({plan[c]['유형'] for c in cs})
    grades = sorted({int(plan[c]['등급']) for c in cs})
    fast = any(t in ('단독', '그외') for t in types) or max(grades) >= 2 or exp_n >= 2
    out.append({
        'id': f"{k[0]}-{k[1]}", 'dong': k[0], 'jibun': k[1],
        'lat': round(lat, 6), 'lng': round(lng, 6),
        'units': len(cs), 'codes': cs, 'types': types, 'grade': max(grades),
        'plan': r['정비방식'], 'planYear': r['시행년도'],
        'exposure': {'facility': facility, 'cluster': cluster, 'density': density}, 'exposureCount': exp_n,
        'cycleMonths': 6 if fast else 12,
        'lastChecked': '2026-01-01',
        'hazardStage': '시판정' if r['정비방식'] in ('안전조치', '철거') else None,
        'actionDone': False,
        'timeline': [{'date': '2025-12-31', 'type': '실태조사', 'note': f"시 판정 {max(grades)}등급, 정비방식 {r['정비방식']}"}],
    })

# 시작 색 확인 (reports/27 규칙, 기준일 2026-11-08)
def color(h, today=dt.date(2026, 11, 8)):
    stage = h['hazardStage']
    lvl_h = {1: 4, 2: 3, '시판정': 3, 3: 2}.get(stage, 0) if not h['actionDone'] else 0
    last = dt.date.fromisoformat(h['lastChecked'])
    due = last + dt.timedelta(days=round(h['cycleMonths'] * 30.44))
    left = (due - today).days
    lvl_t = 2 if left < 0 else (1 if left <= 30 else 0)  # 주황 / 노랑 / 초록
    lvl = max(lvl_h, {2: 2, 1: 1, 0: 0}[lvl_t])
    return ['초록', '노랑', '주황', '빨강', '진한빨강'][lvl]
cnt = collections.Counter(color(h) for h in out)
json.dump(out, open(D('houses.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('방문지', len(out), dict(cnt))
lats = [h['lat'] for h in out]; lngs = [h['lng'] for h in out]
print('위도 범위', min(lats), max(lats), '경도 범위', min(lngs), max(lngs))
