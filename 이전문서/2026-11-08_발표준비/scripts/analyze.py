import csv, sys, re, math, collections
bpath, vpath, out_bld, out_vac = sys.argv[1:5]
B = []
for r in csv.DictReader(open(bpath, encoding='utf-8-sig')):
    dong = r['법정동명'].split()[-1] if r['법정동명'] else ''
    B.append(dict(dong=dong, jibun=r['지번'], use=r['용도명'], apr=r['사용승인일'], struct=r['구조명'],
                  x=float(r['x']), y=float(r['y']), pnu=r['PNU']))
RES = {'단독주택', '공동주택'}
res = [b for b in B if b['use'] in RES]
by_dong = collections.defaultdict(list)
for b in B: by_dong[b['dong']].append(b)

vac, vrows, fallback2 = [], [], []
for r in csv.DictReader(open(vpath, encoding='utf-8-sig')):
    if r['구분'] != '계획대상': continue
    masked = r['지번(가림)']
    prefix = masked.split('*')[0]
    cand = []
    for k in (1, 2):
        pat = re.compile('^' + re.escape(prefix) + '.{%d}$' % k)
        cand = [b for b in by_dong[r['법정동']] if pat.match(b['jibun'])]
        if cand:
            if k == 2: fallback2.append(masked)
            break
    cres = [b for b in cand if b['use'] in RES]
    use = cres or cand
    if not use:
        vrows.append([r['빈집코드'], r['법정동'], masked, 0, 0, '', '', '']); continue
    cx = sum(b['x'] for b in use) / len(use); cy = sum(b['y'] for b in use) / len(use)
    spread = max(math.hypot(b['x'] - cx, b['y'] - cy) for b in use)
    vac.append((cx, cy, r['법정동'], masked))
    vrows.append([r['빈집코드'], r['법정동'], masked, len(cand), len(cres), round(cx, 1), round(cy, 1), round(spread)])
with open(out_vac, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['빈집코드', '법정동', '지번(가림)', '후보건물수', '후보주택수', 'x', 'y', '후보최대퍼짐m']); w.writerows(vrows)

located = len(vac); spreads = sorted(v[7] for v in vrows if v[3])
print(f'건물 전체 {len(B)}동, 주택(단독·공동) {len(res)}동')
print(f'빈집 158호 중 위치 잡힘 {located}호, 못 잡음 {158 - located}호 (두 글자 가림으로 대체 매칭 {len(fallback2)}호)')
print('못 잡은 빈집:', [(v[1], v[2]) for v in vrows if not v[3]])
if spreads:
    print(f'위치 근사 오차(후보 건물 최대 퍼짐): 중앙값 {spreads[len(spreads)//2]}m, 90% {spreads[int(len(spreads)*0.9)]}m, 최대 {spreads[-1]}m')

cell = 500.0
g = collections.defaultdict(list)
for vx, vy, _, _ in vac: g[(int(vx // cell), int(vy // cell))].append((vx, vy))
def stats(pop, label):
    n = len(pop); radii = (150, 300, 500)
    cnt = {r: collections.Counter() for r in radii}; near = []
    for b in pop:
        cx, cy = int(b['x'] // cell), int(b['y'] // cell)
        ds = [math.hypot(b['x'] - vx, b['y'] - vy) for i in (-2, -1, 0, 1, 2) for j in (-2, -1, 0, 1, 2) for vx, vy in g.get((cx + i, cy + j), [])]
        for r in radii: cnt[r][min(sum(1 for d in ds if d <= r), 10)] += 1
        near.append(min(ds) if ds else 1e9)
    print(f'\n[{label}] {n}동')
    for r in radii:
        c = cnt[r]; z = c[0]
        parts = ', '.join(f"{k if k < 10 else '10+'}개 {c[k] / n:.1%}" for k in sorted(c))
        print(f'  반경 {r}m: 0개 {z / n:.1%} | {parts}')
    fin = sorted(d for d in near if d < 1e9)
    q = lambda p: fin[min(len(fin) - 1, int(p * len(fin)))]
    print(f'  최근접 빈집 거리(1km 안에 빈집 있는 {len(fin)}동, {len(fin)/n:.1%}): 25% {q(.25):.0f}m, 중앙값 {q(.5):.0f}m, 75% {q(.75):.0f}m')
    return near
stats(B, '안산 건물 전체')
near = stats(res, '주택(단독·공동)')
by = collections.defaultdict(list)
for b, d in zip(res, near): by[b['dong']].append(d)
print('\n[동별 주택 중 반경 500m 안에 빈집 있는 비율]')
for dg, ds in sorted(by.items(), key=lambda kv: -sum(1 for d in kv[1] if d <= 500) / len(kv[1])):
    print(f'  {dg}: {sum(1 for d in ds if d <= 500) / len(ds):.0%} (주택 {len(ds)}동)')
with open(out_bld, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['PNU', '법정동', '지번', '용도', '구조', '사용승인일', 'x', 'y', '최근접빈집m'])
    for b, d in zip(res, near): w.writerow([b['pnu'], b['dong'], b['jibun'], b['use'], b['struct'], b['apr'], b['x'], b['y'], round(d) if d < 1e9 else ''])
