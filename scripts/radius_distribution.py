"""반경 내 등록 빈집 수 / 최근접 거리 분포 계산.

입력
  buildings.csv : 주거용 건물 목록. 컬럼 법정동, 본번, x, y (미터 단위 투영좌표, 예: EPSG:5179)
  vacancy CSV   : 공람안 빈집목록 (법정동, 본번, 구분)
빈집 위치는 같은 (법정동, 본번) 건물들의 좌표 평균으로 근사한다(지번 끝자리 가림 때문).
실행: python radius_distribution.py buildings.csv "안산 빈집정비계획 공람안 빈집목록.csv" [반경m ...]
"""
import csv, sys, math, collections

def load_buildings(path):
    out = []
    for r in csv.DictReader(open(path, encoding='utf-8-sig')):
        out.append((r['법정동'], r['본번'], float(r['x']), float(r['y'])))
    return out

def locate_vacancies(buildings, vac_path):
    pos = collections.defaultdict(list)
    for d, b, x, y in buildings:
        pos[(d, b)].append((x, y))
    pts, miss = [], 0
    for r in csv.DictReader(open(vac_path, encoding='utf-8-sig')):
        if r['구분'] != '계획대상':
            continue
        p = pos.get((r['법정동'], r['본번']))
        if not p:
            miss += 1
            continue
        pts.append((sum(a for a, _ in p) / len(p), sum(c for _, c in p) / len(p)))
    return pts, miss

def grid_index(pts, cell):
    g = collections.defaultdict(list)
    for x, y in pts:
        g[(int(x // cell), int(y // cell))].append((x, y))
    return g

def main():
    bpath, vpath = sys.argv[1], sys.argv[2]
    radii = [float(v) for v in sys.argv[3:]] or [150.0, 300.0, 500.0]
    blds = load_buildings(bpath)
    vac, miss = locate_vacancies(blds, vpath)
    print(f'건물 {len(blds)}동, 위치 잡힌 빈집 {len(vac)}호, 위치 못 잡은 빈집 {miss}호')
    rmax = max(radii)
    g = grid_index(vac, rmax)
    counts = {r: [] for r in radii}
    nearest = []
    for _, _, x, y in blds:
        cx, cy = int(x // rmax), int(y // rmax)
        ds = [math.hypot(x - vx, y - vy)
              for i in (-1, 0, 1) for j in (-1, 0, 1)
              for vx, vy in g.get((cx + i, cy + j), [])]
        for r in radii:
            counts[r].append(sum(1 for d in ds if d <= r))
        nearest.append(min(ds) if ds else math.inf)
    n = len(blds)
    for r in radii:
        c = collections.Counter(min(v, 10) for v in counts[r])
        zero = c.get(0, 0)
        print(f'\n반경 {int(r)}m: 0개인 건물 {zero}동 ({zero / n:.1%})')
        for k in sorted(c):
            label = f'{k}개' if k < 10 else '10개 이상'
            print(f'  {label:>8}: {c[k]:>7}동 ({c[k] / n:.1%})')
    fin = sorted(d for d in nearest if math.isfinite(d))
    if fin:
        q = lambda p: fin[min(len(fin) - 1, int(p * len(fin)))]
        print(f'\n최근접 등록 빈집 거리(약 {int(rmax * 2)}m 근방에서 빈집을 찾은 건물 {len(fin)}동 기준): '
              f'중앙값 {q(0.5):.0f}m, 25% {q(0.25):.0f}m, 75% {q(0.75):.0f}m')

if __name__ == '__main__':
    main()
