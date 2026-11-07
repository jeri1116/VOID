"""빈집 밀집·노후 자체계산 (발표 근거 재현용).

사용: python -I -X utf8 scripts/density_stats.py
입력: data/ 의 공람안 목록, 158호 위치 근사, 주택 최근접빈집거리 CSV
출력: 콘솔(값을 docs/근거/03_반론대응_근거/06_자체계산_밀집_노후.md 에 옮겨 적음)
"""
import csv, collections, math, os, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda f: os.path.join(ROOT, 'data', f)

plan = {r['빈집코드']: r for r in csv.DictReader(open(D('안산 빈집정비계획 공람안 빈집목록.csv'), encoding='utf-8-sig'))
        if r['구분'].startswith('계획')}
loc = {r['빈집코드']: r for r in csv.DictReader(open(D('안산 빈집 158호 위치 근사.csv'), encoding='utf-8-sig'))}
H = list(csv.DictReader(open(D('안산 주택 최근접빈집거리.csv'), encoding='utf-8-sig')))

def yr(s):
    s = s.replace('-', '')
    return int(s[:4]) if s[:4].isdigit() else None

# 1) 유형
types = collections.Counter(r['유형'] for r in plan.values())
apt = sum(types[t] for t in ('다세대', '연립', '아파트'))
print('[유형]', dict(types), f'공동주택(다세대+연립+아파트) {apt}/158 = {apt/158:.1%}, 다세대 {types["다세대"]/158:.1%}')

# 2) 동 쏠림
hd = collections.Counter(h['법정동'] for h in H)
vd = collections.Counter(r['법정동'] for r in plan.values())
top4 = ['와동', '부곡동', '선부동', '일동']
print('[상위4동] 빈집', f'{sum(vd[d] for d in top4)/158:.1%}', '주택', f'{sum(hd[d] for d in top4)/len(H):.1%}')
print('[주택1000동당 빈집] 시', round(158/len(H)*1000, 1), {d: round(vd[d]/hd[d]*1000, 1) for d in ['부곡동', '와동', '팔곡이동']})

# 3) 노후 추이
ys = [yr(h['사용승인일']) for h in H if yr(h['사용승인일'])]
for ref in (2026, 2030, 2035):
    print(f'[30년 이상 {ref}]', f'{sum(1 for y in ys if ref - y >= 30)/len(ys):.1%}')
print('[1990~2004 준공]', f'{sum(1 for y in ys if 1990 <= y <= 2004)/len(ys):.1%}')

# 4) 평균최근접이웃 (방문지 고유 위치 vs 같은 수의 주택 무작위 표본, 199회)
pts = {}
for c, r in plan.items():
    pts[(r['법정동'], r['지번(가림)'])] = (float(loc[c]['x']), float(loc[c]['y']))
P = list(pts.values())
def mnn(ps):
    return sum(min(math.hypot(x - a, y - b) for j, (a, b) in enumerate(ps) if j != i) for i, (x, y) in enumerate(ps)) / len(ps)
HP = [(float(h['x']), float(h['y'])) for h in H]
random.seed(1)
obs = mnn(P)
sims = [mnn(random.sample(HP, len(P))) for _ in range(199)]
exp = sum(sims) / len(sims)
p = (1 + sum(1 for s in sims if s <= obs)) / (1 + len(sims))
print(f'[평균최근접이웃] 고유 위치 {len(P)}곳, 관측 {obs:.0f}m, 주택 무작위 기대 {exp:.0f}m, R={obs/exp:.2f}, p={p:.3f}')

# 5) 1ha(반경 56.4m) 안 최대 빈집 호수
V = [(float(loc[c]['x']), float(loc[c]['y']), plan[c]['법정동']) for c in plan]
best = max((sum(1 for a, b, _ in V if math.hypot(a - x, b - y) <= 56.4), d) for x, y, d in V)
print(f'[1ha 안 최대] {best[0]}호 ({best[1]}). 법정 빈집밀집구역 기준은 1만㎡ 안 10호')
