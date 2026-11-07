import struct, sys, csv, os, collections
NAMES = ['원천도형ID','통합식별번호','PNU','법정동코드','법정동명','지번','특수지코드','특수지구분명',
         '용도코드','용도명','구조코드','구조명','건축면적','사용승인일','연면적','대지면적','높이',
         '건폐율','용적률','건축물ID','위반여부','참조키','기준일자','시군구코드','건물명','동명',
         '지상층수','지하층수','변경일자']
KEEP = ['PNU','법정동코드','법정동명','지번','특수지코드','용도코드','용도명','구조명','사용승인일',
        '연면적','건축면적','높이','지상층수','위반여부','건물명']
TARGET = (b'41271', b'41273')

def fields_of(f):
    h = f.read(32)
    n = struct.unpack('<I', h[4:8])[0]; hl = struct.unpack('<H', h[8:10])[0]; rl = struct.unpack('<H', h[10:12])[0]
    flds, off = [], 1
    while True:
        d = f.read(32)
        if d[0] == 0x0D: break
        ln = d[16]; flds.append((off, ln)); off += ln
    return n, hl, rl, flds

def run(base, writer, stats):
    dbf = open(base + '.dbf', 'rb'); shx = open(base + '.shx', 'rb'); shp = open(base + '.shp', 'rb')
    n, hl, rl, flds = fields_of(dbf)
    assert len(flds) == len(NAMES), len(flds)
    o3, l3 = flds[3]
    dbf.seek(hl)
    CH = 20000
    i = 0
    while i < n:
        k = min(CH, n - i)
        buf = dbf.read(rl * k)
        for j in range(k):
            r = buf[j*rl:(j+1)*rl]
            code = r[o3:o3+5]
            if code in TARGET:
                vals = {NAMES[t]: r[o:o+ln].decode('cp949', 'replace').strip() for t, (o, ln) in enumerate(flds)}
                idx = i + j
                shx.seek(100 + idx * 8)
                off = struct.unpack('>i', shx.read(4))[0] * 2
                shp.seek(off + 8)
                st = struct.unpack('<i', shp.read(4))[0]
                if st == 0:
                    stats['null_shape'] += 1; continue
                xmin, ymin, xmax, ymax = struct.unpack('<4d', shp.read(32))
                row = [vals[c] for c in KEEP] + [round((xmin+xmax)/2, 2), round((ymin+ymax)/2, 2)]
                writer.writerow(row)
                stats[code.decode()] += 1
        i += k
    stats['scanned'] += n

if __name__ == '__main__':
    folder, out = sys.argv[1], sys.argv[2]
    stats = collections.Counter()
    with open(out, 'w', newline='', encoding='utf-8-sig') as fo:
        w = csv.writer(fo); w.writerow(KEEP + ['x', 'y'])
        for b in ['AL_D010_41_20261009', 'AL_D010_41_20261009(2)', 'AL_D010_41_20261009(3)']:
            run(os.path.join(folder, b), w, stats)
            print(b, dict(stats), flush=True)
