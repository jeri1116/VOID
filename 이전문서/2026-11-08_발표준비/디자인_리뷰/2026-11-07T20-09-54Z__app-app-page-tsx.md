---
target: 홈 화면 / (시연 우선)
total_score: 19
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 3
target_identity: "file:D:\\dev\\VOID\\app\\app\\page.tsx"
target_fingerprint: "sha256:4e2a94afd0a760322f5a4e003a5cc7fecea71b3f336b13c7bc55959c9a954eda"
target_path: "D:\\dev\\VOID\\app\\app\\page.tsx"
timestamp: 2026-11-07T20-09-54Z
slug: app-app-page-tsx
---
Method: dual-agent (A: design review agent · B: detector agent)
# Impeccable critique: home / (demo-first)
Score 19/32 (59%, Acceptable). n/a: 7, 10.
H1 2 no as-of date/demo notice; H2 2 dev/marketing words (/report chip, 대시보드, 모바일 최적화, 로그인 필요(추후)); H3 3; H4 2 same screen named 4 ways, home vs /admin look like different products; H5 3 dead # links; H6 3 no phone nav; H8 2 name repeated 4x, decorative photo half of fold; H9 2 dead links silent.
Specificity: generic v0/shadcn civic landing. Tells: eyebrow pill (hero.tsx:12), split hero + rounded photo + gradient, filled+outline CTA pair, 3 identical icon cards, blur sticky header, dead legal footer, v0 favicon, generator v0.app. No SOS colors/map on home.
Detector: CLI 0 (regex-only undercount), URL scan 0, overlay desktop+phone 0.
Priority:
- [P1] No product identity on home → replace photo with /admin map still or 4-color+purple legend with reasons and start state; two roles side by side above fold. shape, layout
- [P1] Hero photo not Ansan (hanok alley) vs alt "안산시 저층 주택가" (hero.tsx:36) → remove or real sourced photo. distill
- [P1] Copy misframes product (report-first, not periodic inspection) and leaks dev notes → copy table. clarify
- [P2] Korean line break "현/장점검" → break-keep, remove <br/> (hero.tsx:17). typeset
- [P2] No phone nav, 40px card CTA, fake legal footer, v0 leftovers → adapt, polish
Copy table: hero.tsx:13,16-18,21,29,36; service-cards.tsx:21,23,29,30,31,36-38,48,62; site-header.tsx:5,7,9; site-footer.tsx:12-14; layout.tsx:15-16.
Personas: judge (cut title, v0 tab icon, hanok, no SOS, cards below fold at 1366); citizen (no answers on privacy/30 days/119); Casey (nav gone, 540px photo); Jordan (SOS undefined, 로그인 필요(추후)).
