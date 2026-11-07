---
target: 관리자 화면 /admin (시연 우선)
total_score: 21
max_score: 40
na_heuristics: 
p0_count: 1
p1_count: 3
target_identity: "file:D:\\dev\\VOID\\app\\app\\admin\\page.tsx"
target_fingerprint: "sha256:622ffc944af70e2541897a410905ef29a22f5684f089dc4a25b685320fe0e83d"
target_path: "D:\\dev\\VOID\\app\\app\\admin\\page.tsx"
timestamp: 2026-11-07T18-35-32Z
slug: app-app-admin-page-tsx
---
Method: dual-agent (A: design review agent · B: detector agent)

# Impeccable critique: /admin (demo-first)

Viewports: 1366x768, 1920x1080. Demo flow walked: select house → photo → AI → stage 1 confirm → action complete. Yellow report zone and 30-day list not built yet.

## Design Health Score (21/40, Acceptable)
| # | Heuristic | Score | Key Issue |
|---|---|---|---|
| 1 | Visibility of System Status | 2 | Stage-1 confirm (RED→DARK_RED) leaves KPI 24/65/41 unchanged: "긴급(빨강 이상)" merges both |
| 2 | Match System / Real World | 3 | Units mixed (호/곳); DARK_RED action says "조치" not "봉쇄 필요" |
| 3 | User Control and Freedom | 2 | No undo/confirm for stage confirm and action complete |
| 4 | Consistency and Standards | 2 | "조치 완료(봉쇄 완료 사진 등록)" takes no photo; all KPI icons blue |
| 5 | Error Prevention | 2 | Stage select pre-filled with AI candidate "1단계" |
| 6 | Recognition Rather Than Recall | 3 | Legend below the fold (y=694 at 768) |
| 7 | Flexibility and Efficiency | 2 | No Esc to close panel; 130 markers in tab order |
| 8 | Aesthetic and Minimalist Design | 2 | Inverted hierarchy; 5 dead menu items; OSM labels outweigh data |
| 9 | Error Recovery | 1 | upload/confirm/act have no catch; silent failure; no AI cache badge |
| 10 | Help and Documentation | 2 | No contextual help for 피해 범위 / 점검 주기 |

## Design Specificity
LLM: mixed — content product-specific (먼저 갈 곳, reasons on every row, 3/3 exposure chips with strikethrough, "점수·가중치 없음", masked jibun, approximation notice, 4-step panel), frame generic shadcn/v0 admin (navy sidebar + 6 icon menus with 5 "준비 중", 5 KPI cards, segmented filter, rounded cards, default OSM).
Deterministic: CLI 0 (regex-only on .tsx, undercount). Browser main view 15: undersized-ui-text 5 (admin-sidebar.tsx:47 10px "준비 중"), low-contrast 1 (sidebar "시 담당자" 4.4:1, dark mode), flat-type-hierarchy (body/h1/h2 16px), buried-raster 6 (FP, Leaflet fade), cramped-padding 1 (FP, Leaflet attribution), nested-cards 1 (mostly FP, legend overlay). Panel open adds: low-contrast building-panel.tsx:202 1.0:1 (yellow-50 card + dark-mode foreground), :200/:203 2.5:1, SosBadge text-white/80 on red 3.5:1 (:56), reasons white/90 4.1:1 (:60-62), tiny-text 11px chip (:180), list buttons with empty accessible names.
Overlay: injected in [Human] tab, console "15 anti-patterns found".

## Priority Issues
- [P0] Demo changes not visible in one frame: page 991px/1303px tall; confirm button below fold at 768; KPI merges DARK_RED+RED. Fix: h-dvh shell, panel-only scroll, sticky confirm/action footer, KPI split into 4 SOS colors, 600ms pulse on changed number/marker. Commands: layout, animate.
- [P1] Projector legibility: 10–12px labels, h1 16px, markers 14–18px with DARK_RED=RED size, OSM yellow/orange roads clash with ORANGE dots and future yellow zone, white/80 on red 3.5:1. Fix: grayscale basemap, marker sizes 14/16/20/26 + white ring + "1" glyph on DARK_RED, white selection halo, KPI ≥40px. Commands: typeset, bolder.
- [P1] Map bugs + dark mode: gray strip under map (no invalidateSize), scrollWheelZoom hijacks page scroll, OS dark mode half-inverts theme (yellow card 1.0:1), Next dev indicator "N" covers sidebar footer. Fix: ResizeObserver invalidateSize, disable wheel zoom, force light, disable devIndicators. Command: harden.
- [P1] Inverted hierarchy / template frame: strongest element is static "158호" navy card; 5 dead sidebar items; report KPI not tied to yellow. Fix: 158/130 into header sentence, yellow border on report KPI, icon rail sidebar. Commands: distill, colorize.
- [P2] "Human confirms" principle weak: stage pre-selected; no 초안/캐시 tags; 3 of 5 observation items; button label doesn't state outcome; no "link report" step; silent errors. Fix: empty select + "AI 후보" chip, dynamic label "1단계로 확정 → 진한 빨강(봉쇄 필요)", fixed 5 items, error text. Commands: clarify, harden.

## Persona Red Flags
- Judge (projector, 5m): 12px KPI labels; 24 unchanged after confirm; DARK_RED dot reads as black target inside navy ring; gray strip; 5 "준비 중"; dev "N".
- Officer (route planning): top 7 rows share identical reason; sort keys (exposure count, overdue days) not shown; no 30-day D-day in list.
- Sam: red #dc2626 vs green #16a34a hard for red-green CVD; DARK_RED vs RED differ only by lightness; list buttons unnamed.
- Alex: 130 markers before list in tab order; no Esc / keyboard list nav.

## Minor Observations
- "다음 점검 2027-05-08" already visible at confirm time, so +6 months is not read as a change.
- New timeline entries land at top of panel, out of view; citizen report missing from timeline.
- Progress bar step 1 fixed as done from the start.
- No slot for 30-day list; suggest tabs "먼저 갈 곳 | 제보 30일" above list.
- Demo risk: state is per browser tab; /report submission may not reach /admin tab.

## Questions to Consider
1. What would judges lose if the 240px sidebar went to the map?
2. Could one SOS 4-color distribution replace legend + KPI + scene-change cue?
3. Can a judge 5m away notice the DARK_RED confirm moment today?
4. Does "yellow = report" survive on a basemap full of yellow/orange roads?
