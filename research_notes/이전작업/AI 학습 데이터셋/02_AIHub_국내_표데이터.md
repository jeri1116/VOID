# AI Hub·국내 대회·공공데이터포털 이미지 데이터 및 해외 빈집 표 데이터 (안산시 빈집 안전관리 해커톤용)

조사일: 2026-11-07. 검색·페치 18회 사용. 데이터는 내려받지 않고 웹페이지만 읽음.
표기: [확인] = 이번에 해당 페이지를 직접 열어 확인함 / [검색요약] = 검색엔진 요약이나 2차 자료로만 확인함 / [미확인] = 근거를 찾지 못했거나 추정임.
참고(재조사 안 함): 공주시·양산시 빈집 한 채 단위 공개 데이터(공공데이터포털) [검색요약], 안산시 빈집정비계획 공람안 158호 목록.

---

## A. AI Hub 이미지 데이터 (노후 건축물 손상, 폐기물·투기, 거리, 광고물·낙서, 화재, 빈집)

### Takeaway
가장 잘 맞는 것은 **「서울시 노후 주택 균열 데이터」(dataSetSn=567)**입니다. 20년 이상 된 주택 외관을 찍었고 점검 항목이 7종(균열, 박리·박락, 철근노출, 대지, 마감, 생활, 창호)이며 노후도 등급(우수/보통/불량)도 붙어 있어 우리 분류 항목과 거의 그대로 겹칩니다. 「건물 균열 탐지 이미지」(162)는 균열·박리 보조용, 「이상행동 CCTV 영상」(171)의 '투기' 클래스와 「생활 폐기물 이미지」(140)는 쓰레기 투기 항목 보조용입니다. AI Hub에서 낙서·불법광고물 전용 데이터와 빈집·폐가 전용 데이터는 찾지 못했습니다. 모든 AI Hub 데이터는 **내국인만 신청할 수 있고 승인이 나야 내려받을 수 있습니다.**

### Cited Findings

**A-1. 서울시 노후 주택 균열 데이터** [확인] — https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=567
- 구축 연도와 기관: 2021년. 주관은 ㈜미디어그룹사람과숲, 참여는 에이치씨아이플러스·인피닉·이에이트. v1.0은 2022-07-29에 공개됐고, v1.1(원천·라벨 추가)은 2023-10-25에 공개됨 — [AI Hub 567](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=567)
- 규모: 813,908건(RGB 406,954장 + 열화상 406,954장). 서울 25개 구에서 20년 이상 된 건물 1,350동 이상을 RGB 카메라와 열화상 카메라로 동시에 촬영함 — [AI Hub 567](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=567)
- 라벨:
  - 점검 항목 7종: 구조물(균열), 구조물(박리·박락), 구조물(철근노출), 대지, 마감, 생활, 창호
  - 노후도 등급 3단계: 우수/보통/불량
  - 주택 유형 5종: 단독, 다세대, 연립, 아파트, 비주거용
  - 형식: bbox와 polygon, JSON 파일
  — [AI Hub 567](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=567)
- 파일 형식: JPG(RGB 1440×1080, 열화상 384×288), 원천 영상은 mp4 — [AI Hub 567](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=567)
- 신청 조건: 내국인만 신청 가능. 다운로드 버튼을 누르면 승인 절차를 거침. 분할 압축 파일을 API로 받으며, 압축을 합치려면 Linux가 필요함(Windows는 WSL). K-ICT 빅데이터센터에서 오프라인으로 이용하는 방법도 안내돼 있음 — [AI Hub 567](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=567)
- 주의: 페이지를 읽은 결과에 "본 데이터는 국방데이터로 … 별도 신청" 문구가 섞여 나왔음. 데이터 성격상 공통 안내문이 함께 추출된 것으로 보이지만 [미확인]이므로, 신청할 때 직접 확인해야 함.
- 용도: **평가셋과 미세조정의 1순위.** '창호' 항목은 문·창 상태, '생활' 항목은 쓰레기·적치물 상태와 연결될 가능성이 있음(클래스 정의를 아직 보지 못해 [미확인]). 노후도 등급은 우선순위 점수 기준을 정할 때 참고할 수 있음.
- 한계: 서울 노후 주택이며 빈집 여부는 라벨에 없음. '문·창 개방', '방치 식생', '낙서', '인화물' 라벨이 있는지 확인하지 못함. 용량이 매우 큼(목록 표기값 약 4.6×10^11, 단위 표기는 없었으나 바이트로 보임).

**A-2. 건물 균열 탐지 이미지** [확인] — https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=162
- 2020년 구축, v1.4가 2024-04-04에 갱신됨. 이미지 500,000건 — [AI Hub 162](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=162)
- 대상 구조물: 콘크리트(교량, 댐, 옹벽, 건물)와 강재 구조물 — [AI Hub 162](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=162)
- 클래스: 콘크리트 균열, 박리, 백태/누수, 철근 노출, 강재 손상, 도장 손상. 형식은 bbox이고, 예시 이미지는 2880×2160 — [AI Hub 162](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=162)
- 라이선스 단서: 어노테이션 예시에 이미지 라이선스가 "CC BY-NC"로 표기돼 있음. 소개 문구에는 "재사용에 제한이 없도록 저작권 문제를 완전히 해결한 원천 데이터를 확보"라고 돼 있음. 내국인만 신청 가능하고 승인 후 내려받음 — [AI Hub 162](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=162)
- 고도화 버전: 「건물 균열 탐지 이미지 (고도화) - SOC 시설물 균열패턴 이미지 데이터」(dataSetSn=71769)가 있음 [확인: 목록에서만 봄] — [AI Hub 균열 검색](https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex=1&currMenu=115&topMenu=100&srchdataClCode=DATACL001&searchKeyword=균열)
- 학술 활용: 이 데이터로 YOLO 균열 검출을 한 연구들이 있음. 공개 데이터가 현장 조건과 달라서 직접 찍은 데이터를 추가한 사례도 있음 — [koreascience](https://koreascience.kr/article/CFKO202323672006729.pdf) [검색요약]
- 용도: '균열·구조 손상' 항목의 미세조정 보조. 근접 촬영된 외벽 사진이 많아 시민이 찍은 전경 사진과는 분포가 다를 가능성이 큼(추정).

**A-3. 이상행동 CCTV 영상** [확인] — https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=171
- 2019년 구축(갱신 2019-12). 717시간, 8,436컷(구축량 항목에는 700시간/8,400컷으로 표기돼 페이지 안에서 수치가 다름) — [AI Hub 171](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=171)
- 12개 클래스에 **'투기'**가 포함됨(폭행, 싸움, 절도, 기물파손, 실신, 배회, 침입, 투기, 강도, 데이트폭력 및 추행, 납치, 주취행동). 형식은 MP4와 XML 이벤트 라벨. 내국인만 신청 가능하고 승인 필요 — [AI Hub 171](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=171)
- 용도: 투기 '행위'를 찍은 CCTV 영상이라, 정지 사진에서 '쓰레기가 쌓인 상태'를 찾는 우리 용도와는 차이가 있음. 프레임 일부를 뽑아 퓨샷 예시로 쓰는 정도로 한정됨. '기물파손' 클래스는 낙서·파손 쪽으로 참고 가능.
- 관련: 「공원 주요시설 및 불법행위 감시 CCTV 영상 데이터」(477)도 '투기' 키워드로 검색됨 [확인: 목록에서만 봄] — [AI Hub 투기 검색](https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex=1&currMenu=115&topMenu=100&srchdataClCode=DATACL001&searchKeyword=투기)

**A-4. 생활 폐기물 이미지** [확인] — https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=140
- 2020년 구축(갱신 2021-06, 샘플은 2022-10-13 공개). 150,000건 / 750,000장 — [AI Hub 140](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=140)
- 15종 클래스: 가구, 고철류, 나무, 도기, 비닐, 스티로폼, 유리병, 의류, 자전거, 전자제품, 종이, 캔류, 페트병, 플라스틱, 형광등. 형식은 Box/Polygon이고 촬영장소 필드 값은 실내/실외/스튜디오. 내국인만 신청 가능하고 승인 필요 — [AI Hub 140](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=140)
- 용도: 쓰레기 투기 사진에서 '무엇이 버려졌는지'(대형 가구·전자제품 등)를 세분하거나, 스티로폼·비닐 같은 가연성 적치물을 '인화물' 위험 단서로 쓰는 데 활용 가능.
- 다른 폐기물 데이터 [확인: 목록에서만 봄]: 생활폐기물 데이터 활용·환류(71385), 재활용품 분류 및 선별 데이터(71362), 폐플라스틱 이미지(495), 산업 폐기물 이미지(137) — [AI Hub 폐기물 검색](https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex=1&currMenu=115&topMenu=100&srchdataClCode=DATACL001&searchKeyword=폐기물)
- 2차 자료: AI Hub의 쓰레기봉투 영상·이미지를 써서 YOLOv5로 무단투기를 검출한 KISTI 대회 발표자료가 있음(학습 2,885장, 테스트 371장) — [KISTI 발표자료](https://aida.kisti.re.kr/data/cb06974e-c406-4bde-b490-fc2bf1e5294b/713be8c7-b429-498a-8c93-dfe413444a08/01.발표자료.pdf) [검색요약]

**A-5. 화재** [확인: 목록에서만 봄]
- 「화재 발생 예측 영상 (고도화) - 영상 기반 화재 감시 및 발생 위치 탐지 데이터」(71751) 등 '화재'로 검색한 결과는 54건이었음. 대부분 불꽃·연기 감지나 산업설비 데이터임 — [AI Hub 화재 검색](https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex=1&currMenu=115&topMenu=100&srchdataClCode=DATACL001&searchKeyword=화재)
- 상세 페이지를 열지 않았으므로 '인화물 적치' 같은 화재 전 위험요소 라벨이 있는지는 [미확인].

**A-6. 거리·보행자 시점** [확인: 목록에서만 봄]
- '보행'으로 검색하면 69건이 나옴. 후보는 다각도 CCTV 생활안전 데이터(71953), 어린이 보호구역 내 등하교 및 시설물 영상(71796), 생활도로 객체인식 자율주행 데이터(71784), 로봇 관점 주행 영상(71755) 등 — [AI Hub 보행 검색](https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex=1&currMenu=115&topMenu=100&srchdataClCode=DATACL001&searchKeyword=보행)
- 「생활도로 객체인식 자율주행 데이터」는 이면도로 시점이라 주택가 배경 이미지로 쓸 여지가 있음(추정).

**A-7. 불법 광고물·낙서** [확인]
- AI Hub에서 '광고물'로 검색하면 2건만 나오고 둘 다 관련이 없음(특허 분류, 야외 한글 이미지). 낙서·불법광고물 전용 데이터는 찾지 못함 — [AI Hub 광고물 검색](https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex=1&currMenu=115&topMenu=100&srchdataClCode=DATACL001&searchKeyword=광고물)
- 해외 대안: Kaggle 'Urban Issues' 데이터셋(도로 손상, 불법주차, 쓰레기 투기, 기물파손 등) — [hyper.ai](https://hyper.ai/ko/datasets/44058) [검색요약]. 리스본 차량 카메라 낙서 데이터베이스 연구 — [ISCTE](https://repositorio.iscte-iul.pt/bitstream/10071/28214/1/article_95006.pdf) [검색요약]

**A-8. 시설물 외관 점검 관련** [확인: 목록에서만 봄]
- 교량 외관점검 입면정사영상 데이터(71774), 지자체 도로 정비 AI 학습용 데이터(557), 하수관로 내부 이미지(139) — [AI Hub 균열 검색](https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex=1&currMenu=115&topMenu=100&srchdataClCode=DATACL001&searchKeyword=균열)

### Inferences
- 우리 분류 항목별로 보면 다음과 같음.
  - 균열·구조 손상: 567과 162로 충분
  - 문·창: 567의 '창호' 항목이 있음
  - 쓰레기: 567의 '생활' 항목, 140, 171 투기
  - 방치 식생, 낙서, 인화물: 국내 공개 라벨이 거의 없음 → VLM 제로샷·퓨샷으로 처리하고, 안산 현장 사진을 직접 라벨링해 소규모 평가셋을 만드는 편이 현실적임
- 해커톤 기간에 수백 GB를 받기는 어려움. 샘플 데이터(AI Hub는 보통 샘플을 따로 제공함)와 라벨 JSON 일부만 써서 평가셋을 구성하는 전략이 맞음.
- 해커톤은 비영리이고 국내 연구·개발 목적이므로 AI Hub 신청 취지에 맞을 가능성이 높음. 다만 공식 이용약관 조항은 직접 확인하지 못함.

### Gaps
- AI Hub 공통 이용약관(상업적 이용, 2차 배포, 해외 반출, 출처 표시, 결과물 공개 의무)은 원문을 열지 못해 [미확인]. 162 예시의 "CC BY-NC" 표기가 데이터셋 전체에 적용되는지도 불명확함.
- 승인에 걸리는 기간: 공식 수치를 찾지 못함 [미확인].
- 567 페이지에 섞인 '국방데이터' 문구가 실제로 이 데이터에 해당하는지 [미확인].
- 567의 '생활', '창호', '대지', '마감' 항목의 세부 정의를 확인하지 못함.
- AI Hub에서 '빈집', '폐가', '낙서', '식생' 키워드는 검색 횟수 제한 때문에 따로 검색하지 못함.

---

## B. DACON 등 국내 대회 데이터

### Takeaway
DACON에서 빈집이나 건물 외관 손상 대회는 확인하지 못했습니다. 가장 가까운 것은 실내 하자를 다룬 **「도배 하자 유형 분류 AI 경진대회」**(19개 클래스, 3,457장)이고, 건물 외관 사진에 직접 쓰기는 어렵습니다.

### Cited Findings
- DACON '도배 하자 유형 분류 AI 경진대회': 19개 클래스, 학습 이미지 3,457장, 클래스 불균형이 심함 — [블로그 정리](https://geunuk.tistory.com/487) [검색요약]. Roboflow에 같은 이름의 사본이 있음(crack damage, spot, rust pollution 등 19개 클래스) — [Roboflow](https://universe.roboflow.com/konkuk-unvi/dacon-x4sy3) [검색요약]
- 재활용 쓰레기 객체검출(부스트캠프)은 DACON 대회가 아님 — [tistory](https://sonstory.tistory.com/57) [검색요약]
- KISTI AIDA 대회에 AI Hub 쓰레기봉투 데이터로 무단투기를 검출한 사례가 있음 — [KISTI 매뉴얼](https://aida.kisti.re.kr/data/cb06974e-c406-4bde-b490-fc2bf1e5294b/2391ea70-f766-42eb-89da-5ac101cd7020/02.매뉴얼.pdf) [검색요약]

### Inferences
- DACON 대회 데이터는 보통 대회 참가자만 쓸 수 있고 대회 목적 외 사용이 제한되는 경우가 많음(일반적 관행, [미확인]). 해커톤 결과물에 쓰기 전에 대회별 규정을 확인해야 함.

### Gaps
- dacon.io를 직접 검색하지 못함(검색 횟수 제한). '건물', '균열', '쓰레기', '빈집' 대회 목록과 각 데이터 라이선스는 [미확인].

---

## C. 해외 빈집·블라이트 표 데이터 (Kaggle·미국 시 오픈데이터)

### Takeaway
**Detroit Blight Ticket**(Kaggle·Coursera 과제, 위반 티켓 단위, 납부 여부 예측)과 **Philadelphia Vacant Property Indicators**(필지 단위 빈집 가능성 점수 BUILD_RANK)가 우선순위·예측 프로토타입에 가장 쓸모 있습니다. Baltimore Vacant Building Notices는 2011년부터 공개된 행정 빈집 통지 목록입니다. 모두 미국 필지·행정 체계를 전제로 하므로 한국에는 **변수 아이디어와 파이프라인 시연 용도**로만 써야 합니다.

### Cited Findings
**C-1. Detroit Blight Ticket Compliance** [검색요약]
- 학습 데이터 250,306행 × 34열, 테스트 데이터 61,001행 × 27열. 타깃은 `compliance`(Null = 책임 없음, 0 = 책임 있으나 미납, 1 = 납부) — [노트북 정리](https://luisangelmendozavelasco.github.io/portfolio/Applied_Data_Science_with_Python_Specialization/portfolio-4.html), [노트북](https://ravi-chandrika-05.github.io/PREDICTING_PROBABILITY_OF_PAYING_BLIGHT_TICKETS)
- 컬럼: ticket_id, agency_name, inspector_name, violator_name, 위반지 주소·ZIP, fine_amount, late_fee, judgment_amount, payment_amount, balance_due, payment_date, payment_status, compliance_detail 등 — 같은 출처
- 미시간대 MDST 팀은 필지, 범죄, 철거, Improve Detroit(311) 데이터를 결합해 사용함 — [MIDAS](https://midas.umich.edu/mdst-partners-with-city-of-detroit-to-improve-blight-enforcement)
- 원본은 디트로이트 오픈데이터 Blight Violations/Blight Tickets — [detroitdata.org](https://detroitdata.org/dataset/blight-violations1), [Blight Tickets](https://detroitdata.org/dataset/blight-tickets)
- 라이선스: Kaggle 사본과 원본 모두 [미확인].

**C-2. Philadelphia Vacant Property Indicators** [검색요약]
- 시가 만든 모델의 결과로, Buildings 레이어와 Land 레이어 2개로 나뉨 — [Source Cooperative 미러](https://source.coop/nlebovits/phl-housing-demo), [data.gov](https://catalog.data.gov/dataset/vacant-property-indicators)
- 빈 건물로 모델링된 필지 9,041개, 빈 땅 28,737개. `BUILD_RANK` ≥ 0.50이면 빈 건물일 가능성이 높다고 봄. 그 밖에 opa_id(재산평가 계정), councildistrict, zoningbasedistrict, bldg_desc 컬럼이 있음 — [AGENTS.md](https://data.source.coop/nlebovits/phl-housing-demo/vacant_indicators_bldg/AGENTS.md)
- 블록 단위 비율 데이터도 있음 — [OpenDataPhilly](https://opendataphilly.org/datasets/vacant-property-indicators-percentage-by-block/)
- 시 보도자료 — [phila.gov](https://www.phila.gov/press-releases/kenney/city-releases-open-data-on-vacant-property-indicators/)
- 지표 원천(수도 사용 중단, 체납, 위반 등)의 정확한 목록과 라이선스는 [미확인].

**C-3. Baltimore Vacant Building Notices (VBN)** [검색요약]
- 2011년부터 Open Baltimore에 공개됨. 대시보드에서 통지, 리모델링, 철거 현황을 볼 수 있고 지역·기간·주택시장 유형별로 필터할 수 있음 — [Community Progress](https://communityprogress.org/resources/vacant-land/elements/examples/open-baltimore/)
- ArcGIS FeatureServer(DHCD Open Baltimore Datasets) — [egisdata.baltimorecity.gov](https://egisdata.baltimorecity.gov/egis/rest/services/Housing/DHCD_Open_Baltimore_Datasets/FeatureServer)
- 통지 건수는 출처마다 다름. 13,796건 — [Baltimore Heritage](https://baltimoreheritage.github.io/vacant-buildings-101/guides/counting-vacants). 2016년 16,000건 이상에서 2025년 10월 12,349건으로 감소 — [AFRO](https://afro.com/reinvest-baltimore-initiative-progress/cut2_-dhcd-chart-as-of-october-282/)
- 데이터 정확성에 대한 비판이 있음 — [Technical.ly](https://technical.ly/uncategorized/vacant-housing-data-set-not-accurate-says-baltimore-slumlord-watch-blogger.md)
- 빈집 화재로 인한 사망 사고가 반복돼, 빈집 관리와 화재 위험이 함께 거론됨 — [CBS Baltimore](https://www.cbsnews.com/baltimore/news/baltimore-continues-to-grapple-with-vacant-properties-in-wake-of-another-fatal-fire/)
- 컬럼 목록과 라이선스는 [미확인].

**C-4. 기타**
- 미국 도시들의 311 '방치 건물' 신고 데이터(시카고 등)는 이번에 조사하지 못함 [미확인].

### Inferences
- **우선순위 점수에 쓸 변수 아이디어**:
  - 반복 신고·위반 횟수 (Detroit 티켓, 311)
  - 체납·미납 (Detroit의 compliance 개념)
  - 철거·화재 이력 (Baltimore)
  - 행정 지표를 결합한 모델 점수 (Philadelphia의 BUILD_RANK)
  - 한국에서 대응할 수 있는 지표: 시민 제보 누적 횟수, 사진 AI의 위험 항목 수·심각도, 건축연도(노후도), 빈집 등급(공주·양산 데이터 형식 참고), 학교·통학로 근접성, 단전·단수(협약 필요)
- **예측 모델 프로토타입**: Detroit 데이터로 '표 데이터 → 확률 → 순위' 파이프라인을 시연할 수 있음. 다만 타깃이 '빈집 여부'가 아니라 '과태료 납부 여부'라는 점을 분명히 밝혀야 함.
- **한국 적용 한계**:
  - 필지 ID·행정 체계가 다르고 주택 유형 분포(단독·다세대 대 미국 단독주택)가 다름
  - 공개 데이터의 정확성 문제가 있음(Baltimore 비판)
  - 개인정보 컬럼(violator_name 등)이 들어 있음
  - "타 지역 데이터로 학습해 안산에 적용"은 미국 데이터로는 사실상 불가능함. 국내 공주·양산 데이터와 건축물대장을 결합하는 쪽이 현실적임

### Gaps
- Kaggle 데이터 카드의 정확한 URL과 라이선스, Detroit 오픈데이터 라이선스, Baltimore VBN 컬럼, Philadelphia 지표 산출식은 원문을 보지 못함.

---

## D. 공공데이터포털 이미지·영상 데이터 (건물 외관·거리)

### Takeaway
공공데이터포털에서 지자체가 공개한 '건물 외관' AI 학습 이미지는 찾지 못했습니다. 비슷한 사례로 경기 양평군 폐기물 이미지 라벨링 데이터(300장)와 대전시 CCTV AI 학습용 데이터(63만 장)가 있습니다.

### Cited Findings
- 경기 양평군 'AI 학습용 폐기물 이미지 라벨링 데이터': 주민이 수거를 신청한 폐기물 사진 300장, 2026년 1~6월 수집 — [data.go.kr 메타데이터 15159048](https://www.data.go.kr/biz/dcat/metadata/15159048.do) [검색요약]
- 대전시가 공공데이터포털에 AI 학습용 데이터 등 46건을 개방했고, 그중 CCTV AI 학습용 데이터가 63만 장임 — [스마트시티 종합포털](https://smartcity.go.kr/?p=23503) [검색요약]
- 공공누리 1·3유형 공공저작물을 AI 학습용으로 가공하도록 허용하는 실증 특례가 있음 — [byline.network](https://byline.network/2025/09/9119/) [검색요약]

### Inferences
- 양평군 폐기물 사진은 '주민이 찍은 폐기물 사진'이라 우리 시민 제보 사진과 촬영 분포가 비슷해, 쓰레기 항목 퓨샷이나 평가에 유용할 수 있음. 300장이라 규모는 작음.

### Gaps
- 양평군 데이터의 라벨 형식과 라이선스(공공누리 유형), data.go.kr의 '건물 외관/건축물 이미지' 직접 검색은 [미확인].

---

## E. 종합: 바로 쓸 만한 것 Top 5, 미리 신청해야 할 것

### 바로 쓸 만한 것 Top 5

| 순위 | 이름 | 플랫폼·URL | 규모 | 라벨/컬럼 | 조건 | 용도 | 한계 |
|---|---|---|---|---|---|---|---|
| 1 | 서울시 노후 주택 균열 데이터 [확인] | AI Hub [567](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=567) | 813,908장 (RGB와 열화상), 2021년 구축, v1.1(2023-10) | 점검 항목 7종(균열, 박리·박락, 철근노출, 대지, 마감, 생활, 창호), 노후도 등급 3단계, bbox/polygon JSON | 내국인만 신청, 승인 필요 | 평가셋, 미세조정, 우선순위 등급 기준 | 빈집 라벨 없음, 서울 지역, 용량 큼 |
| 2 | 건물 균열 탐지 이미지 [확인] | AI Hub [162](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=162) | 50만 장, v1.4(2024-04) | 균열, 박리, 백태/누수, 철근노출 등 6종 bbox | 내국인만 신청, 승인 필요, 예시에 CC BY-NC 표기 | 균열 항목 미세조정·평가 | 근접 촬영 위주, 교량·댐 등 비주택 포함 |
| 3 | 생활 폐기물 이미지 [확인] | AI Hub [140](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=140) | 15만 건 / 75만 장, 2020년 구축 | 15종 품목, Box/Polygon | 내국인만 신청, 승인 필요 | 투기 쓰레기 세분, 가연물 단서 | 투기 '현장' 사진이 아님(스튜디오 포함) |
| 4 | 이상행동 CCTV 영상 ('투기' 클래스) [확인] | AI Hub [171](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=171) | 717시간, 8,436컷, 2019년 구축 | 12개 행동 클래스(투기, 기물파손 포함), XML | 내국인만 신청, 승인 필요 | 투기·기물파손 퓨샷 | 행위 영상이라 정지 상태 사진과 다름 |
| 5 | Philadelphia Vacant Property Indicators / Detroit Blight Ticket [검색요약] | [OpenDataPhilly·data.gov](https://catalog.data.gov/dataset/vacant-property-indicators), [Detroit](https://detroitdata.org/dataset/blight-violations1) | 빈 건물 9,041개 필지 / 티켓 25만 행 | BUILD_RANK, opa_id 등 / compliance, 벌금·납부 컬럼 | 신청 불필요, 라이선스 [미확인] | 우선순위 변수 아이디어, 예측 파이프라인 시연 | 미국 행정체계, 한국 이전 불가 |

(참고로 빠진 후보: 양평군 폐기물 사진 300장은 즉시 받을 수 있을 가능성이 있으나 [검색요약]이고 규모가 작음.)

### 신청에 시간이 걸리는 것 (미리 신청해야 할 것)
1. **AI Hub 567 서울시 노후 주택 균열 데이터**: 내국인 팀원 계정으로 신청하고 승인을 받아야 함. 분할 압축을 합치려면 Linux/WSL이 필요하고 용량이 큼. 오프라인(K-ICT 빅데이터센터) 이용 안내가 있으므로 신청 페이지에서 반드시 확인해야 함. 가장 먼저 신청할 것.
2. **AI Hub 162 건물 균열 탐지 이미지**와 고도화 버전 71769: 승인 필요.
3. **AI Hub 140 생활 폐기물 이미지**: 승인 필요.
4. **AI Hub 171 이상행동 CCTV 영상**(그리고 477 공원 불법행위 CCTV): 승인 필요, 영상이라 용량이 매우 큼.
5. **DACON 도배 하자 등 대회 데이터**: 대회 참가나 규정 동의가 필요할 수 있음 [미확인].
6. **향후 빈집 예측용 국내 행정 데이터**(단전·단수, 건축물대장 결합): 안산시와 데이터 협약이 필요함. 해커톤 이후 계획에 넣을 것.
- 공통 팁: AI Hub는 보통 상세 페이지에서 샘플 데이터를 따로 제공함. 승인 전에 샘플로 라벨 구조를 먼저 확인하는 것을 권장함(이번 조사에서는 140에 샘플이 있다는 것만 확인). 승인에 걸리는 기간은 [미확인]이므로 해커톤 일정보다 최대한 앞서 신청해야 함.

### Gaps
- AI Hub의 공식 이용약관(비영리·해커톤 사용 가능 여부, 결과물 공개 시 출처 표시)을 직접 확인하지 못함. 신청 화면의 약관 동의 단계에서 확인이 필요함.
