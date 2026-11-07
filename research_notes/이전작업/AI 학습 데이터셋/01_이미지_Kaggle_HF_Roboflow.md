# 빈집 외관 상태 분류용 공개 이미지 데이터셋 조사 (Kaggle · Hugging Face · Roboflow Universe)

조사일: 2026-11-07 / 검색·페치 18회 사용 (검색 13, 페치 5)
표기: [확인] = 페이지를 직접 열어 내용 확인 / [검색요약] = 검색 결과 요약으로만 확인 / [미검증] = 조사자 사전지식, 이번 조사에서 확인 못 함
주의: Roboflow Universe 페이지는 WebFetch 시 전부 HTTP 403이 떠서 직접 열지 못했다. 따라서 Roboflow 항목은 모두 [검색요약]이며 이미지 수·라이선스·클래스는 사용 전에 브라우저로 다시 확인해야 한다. Kaggle 역시 검색엔진 색인이 빈약해 직접 해당하는 데이터셋을 찾지 못했다.

공통 결론 요약: 이 과제(한국 다세대·단독주택 외관, 공공도로 시점, 9개 항목)에 그대로 맞는 공개 데이터셋은 세 플랫폼 어디에도 없다. 항목별로 쪼개서(쓰레기 투기, 깨진 창, 낙서, 균열) Roboflow의 소형 검출 데이터셋을 퓨샷·보조 평가용으로 쓰고, **최종 평가셋은 안산 현장에서 직접 찍은 사진에 라벨을 붙여 만드는 것**이 현실적이다.

---

## 1. 빈집·폐가·도시 쇠퇴(blight) 이미지 데이터셋

### Takeaway
Kaggle에서 빈집·폐가 외관 이미지 데이터셋은 찾지 못했다. Roboflow에 소형 "Abandoned Buildings"·"blight" 프로젝트가 있지만 상세 정보를 확인하지 못했다. 미국 연구용 데이터(Detroit 등)는 공개 이미지셋으로 풀린 것이 확인되지 않는다. 이 과제는 빈집 여부를 판정하지 않으므로 이 범주가 꼭 필요하지는 않다.

### Cited Findings
- Kaggle 도메인 한정 검색("abandoned"/"derelict" house images) 결과 건물 데이터셋은 없었다. 걸린 것은 버려진 물건(수하물) 영상 데이터셋 하나뿐이었다. 1,062개 영상이고 판매사에 연락해야 전체를 받을 수 있는 미리보기판이라 이 과제와 무관하다 — [Kaggle: Abandoned Object Detection Dataset](https://www.kaggle.com/datasets/unidpro/abandoned-object-detection-video-dataset) [검색요약]
- Roboflow "Abandoned Buildings" 프로젝트(maps-anyom)가 있다. 인용 BibTeX와 관련 프로젝트(roofs, buildings)가 페이지에 있는데, 이로 보아 항공 이미지일 가능성이 있다(추정). 이미지 수와 클래스는 확인하지 못했고 페이지 페치는 403 — [Roboflow: Abandoned Buildings](https://universe.roboflow.com/maps-anyom/abandoned-buildings) [검색요약]
- Roboflow "blight" 프로젝트(college-5t5ly). 세부 정보 없음 — [Roboflow: blight](https://universe.roboflow.com/college-5t5ly/blight-wan5t) [검색요약]
- Roboflow "Demolished Buildings"는 철거 건물을 다룬다. v1이 176장, v2가 349장이고 train/valid/test로 나뉜다 — [Roboflow: Demolished Buildings v2](https://universe.roboflow.com/disaster-response-project/demolished-buildings/dataset/2) [검색요약]
- Development Seed의 Urban Blight Tracker는 2022년 5월에 스트리트뷰 이미지 18만 장 이상을 수집했고 7,500장 이상에 blight 라벨을 붙였다. 데이터 공개 여부는 확인되지 않았다 — [Development Seed 블로그](https://developmentseed.org/blog/2024-07-29-urban-blight-tracker/) [검색요약]
- 미국 legacy city 빈집을 Google Street View로 검출한 위계적 딥러닝 연구(ISPRS, 2021)가 있다. 공개 데이터셋 링크는 확인되지 않았다 — [UB Research Connect](https://researchconnect.buffalo.edu/en/publications/detecting-individual-abandoned-houses-from-google-street-view-a-h/) [검색요약]
- 한국 농촌 빈집 분류 연구(Real Estate Management and Valuation, 2023)는 정확도 86.2%를 보고했다. 데이터 공개 여부는 확인되지 않았다 — [reference-global](https://reference-global.com/article/10.2478/remav-2023-0021) [검색요약]
- TUM의 BIC_GSV(스트리트뷰 건물 파사드 유형 분류 벤치마크, Kang et al. 2018)는 www.sipeo.bgu.tum.de/downloads/BIC_GSV 에서 받을 수 있다고 한다 — [검색결과(arXiv 1802.09026)](https://www.arxiv.org/pdf/1802.09026) [검색요약]

### Inferences
- 이 서비스는 빈집 여부를 판정하지 않으므로 abandoned/occupied 이진 데이터셋은 우선순위가 낮다. 쓴다면 "방치 외관" 퓨샷 예시 몇 장 정도다.
- 한국 농촌 빈집 연구(remav-2023-0021)의 저자에게 데이터를 요청해 보는 것이 한국 유사도 면에서 가장 가치가 있을 수 있다(추정).

### Gaps
- Kaggle에 "vacant house", "urban decay" 같은 이미지셋이 실제로 없는지는 Kaggle 사이트 내부 검색으로 다시 확인해야 한다. 검색엔진에 Kaggle 색인이 빈약했다.
- Roboflow Abandoned Buildings의 시점(항공인지 지상인지), 규모, 라이선스는 미확인.

---

## 2. 건물 외벽 손상(균열·박리·깨진 창·구조 손상, 지진 피해 포함)

### Takeaway
Hugging Face에 균열·구조 손상 검출셋 두 개를 [확인]했다. elliemci/building_damages(7,257장, CC BY 4.0, 게이트)와 UAV2K(2,000장, 비상업 학술 전용)다. 하지만 하나는 근접·구조부재 위주로 보이고 다른 하나는 드론 시점 RC 건물이라 공공도로에서 찍은 한국 주택 사진과는 거리가 있다. 깨진 창은 Roboflow 소형셋(YOURAY "깨진 집과 창")이 가장 직접적이다.

### Cited Findings
- **elliemci/building_damages (HF)**: 7,257장(train 5,255 / valid 1,266 / test 736), 객체 검출(COCO), 9개 클래스(combined damage, flexural, minorrotation, moderaterotation, severerotation, shear, undamage, cracks, water). CC BY 4.0. HF 로그인 후 조건에 동의해야 받을 수 있다. Roboflow 프로젝트 elliemci/building-damages-nnk2b v2를 2025-02-03에 내보낸 것이다. 촬영 시점(외관인지 근접인지)은 명시돼 있지 않다 — [HF: elliemci/building_damages](https://huggingface.co/datasets/elliemci/building_damages) [확인]
- **RealUAV-SD/UAV2K (BFD-UAV2K, HF)**: 철근콘크리트 건물 42동을 찍은 2,000장(1,600/200/200, 건물 단위 분할), 7.02GB, 결함 5,020개(hollow 1,391 / spalling 2,528 / crack 1,101), 배경만 있는 이미지 720장, bbox(YOLO·COCO). DJI 드론으로 정면 파사드를 촬영했다. 라이선스는 "UAV2K Academic Research License"로 비상업 학술·교육 목적만 허용하고, 재배포는 서면 허가, 상업 이용은 별도 승인이 필요하다. 연락처가 .edu.cn이고 지역은 명시돼 있지 않다 — [HF: RealUAV-SD/UAV2K](https://huggingface.co/datasets/RealUAV-SD/UAV2K) [확인]
- elliemci/building_cracks와 lipi17/building-cracks는 Roboflow에서 내보낸 균열 검출셋이다(약 2,000~2,400장). 게이트가 있거나 viewer가 비활성(임의 코드 실행 필요) 상태다 — [HF: elliemci/building_cracks](https://huggingface.co/datasets/elliemci/building_cracks), [HF: lipi17/building-cracks](https://huggingface.co/datasets/lipi17/building-cracks) [검색요약]
- bit-cell/damage_desc(1~3)는 건물 이미지에 손상을 서술한 텍스트 데이터셋이다(균열, 깨진 창 언급, 실내외 혼재). 라벨된 이미지셋이 아니다 — [HF: bit-cell/damage_desc](https://huggingface.co/datasets/bit-cell/damage_desc) [검색요약]
- **Roboflow "Разбитые дома и окна"(YOURAY)**: 클래스 3개(broken-house, broken-window, window-without-glass), Public Domain으로 표시돼 있다. 페치는 403 — [Roboflow: youray/-nshli](https://universe.roboflow.com/youray/-nshli) [검색요약]
- Roboflow "Windows Complete or Broken"(Heikki Hietanen): CC BY 4.0, 클래스 1개, 설명 없음 — [Roboflow](https://universe.roboflow.com/heikki-hietanen-zpohx/windows-complete-or-broken) [검색요약]
- Roboflow "Broken-windows and Damaged building facade"(test workspace): 클래스와 라이선스 미확인 — [Roboflow](https://universe.roboflow.com/test-didr5/test-gkgv1) [검색요약]
- Roboflow post_disaster_buildings(quake): 소형 지진 피해 건물셋 — [Roboflow](https://universe.roboflow.com/quake/post_disaster_buildings/dataset/2) [검색요약]
- (플랫폼 범위 밖, 참고) IEEE DataPort Facade Damage Dataset은 지진 후 파사드 손상 심각도로 분류한 이미지 링크 스프레드시트다 — [IEEE DataPort](https://ieee-dataport.org/documents/facade-damage-dataset) [검색요약]. Eucentre IDEA는 구조공학자가 주석한 실제 피해 이미지 5,400장 이상이다 — [Eucentre](https://www.eucentre.it/en/?p=38761) [검색요약]. MDPI Data 2024 다중스케일 지진 피해 건물셋은 7,062장, 피해 3등급이다 — [MDPI](https://www.mdpi.com/2306-5729/9/7/88/html) [검색요약]. UAVs-TEBDE(튀르키예, 드론, 1,636장, 3등급)도 있다 — [Mendeley](https://data.mendeley.com/datasets/5m349hfvkb/2) [검색요약]
- Kaggle에서는 지진 관련 이미지셋을 찾지 못했다. 걸린 것은 네팔 고르카 지진 건물 피해 표 데이터뿐이다 — [검색결과](https://baselight.app/u/kaggle/dataset/arashnic_earthquake_magnitude_damage_and_impact) [검색요약]

### Inferences
- "외벽 균열·구조 손상" 항목은 LLM 퓨샷 예시로 elliemci/building_damages의 cracks 이미지 몇 장을 쓰는 정도가 적당하다. 클래스 체계(flexural/shear/rotation)가 구조부재 평가용이라 우리 항목과 맞지 않는다.
- UAV2K는 라이선스상 해커톤 결과물이 상용 서비스로 이어지면 쓸 수 없다. 학술·데모 내부 평가로만 쓰고, 미세조정 모델을 배포하는 데는 쓰지 말아야 한다.
- 지진 피해셋은 붕괴 수준의 극단 사례가 많아 "경미한 균열" 판독 평가에는 분포가 맞지 않는다.

### Gaps
- elliemci/building_damages의 실제 촬영 시점과 원 출처 라이선스 승계 여부(Roboflow 원 프로젝트의 원천 이미지 출처)는 미확인.
- YOURAY 셋의 이미지 수와 지역(러시아어 제목이라 동유럽 주택일 가능성, 추정)은 미확인.

---

## 3. 불법투기·쓰레기·생활폐기물(거리)

### Takeaway
Roboflow에 지상·CCTV 시점의 불법투기 검출셋이 여러 개 있다(400~2,200장, 다수 CC BY 4.0). 이 범주가 공개 데이터로 가장 잘 채워진다. 거리 시점 대규모셋으로는 암스테르담 GIGO(25k)가 있지만 Kaggle/HF 등재는 확인하지 못했다.

### Cited Findings
- **Roboflow Illegal Dumping (development-outcomex)**: 2,198장, 객체 검출, CC BY 4.0(인용 블록 기준) — [Roboflow](https://universe.roboflow.com/development-outcomex/illegal-dumping) [검색요약]
- Roboflow illegal dumping_Object Detection (0727)(prometheusCCTV): 클래스 3개, CCTV 시점 — [Roboflow](https://universe.roboflow.com/prometheuscctv/illegal-dumping_object-detection-0727) [검색요약]
- Roboflow Illegal dumping w/o people(garbage-chute): 클래스 9개(여행가방, 비닐봉지, 쇼핑카트 등), 사람을 제외하도록 설계 — [Roboflow](https://universe.roboflow.com/garbage-chute/illegal-dumping-w-o-people) [검색요약]
- Roboflow Garbage Dumping(cloudcam): 636장 — [Roboflow](https://universe.roboflow.com/cloudcam/garbage-dumping-6avsy) [검색요약]
- Roboflow illegal-dumping-detection-5jvsg: 441장 — [Roboflow](https://universe.roboflow.com/pothole-6mon4/illegal-dumping-detection-5jvsg) [검색요약]
- Roboflow garbage dumping detection(myspace-vwrde): 클래스 4개(garbage, garbage_bag 등) — [Roboflow](https://universe.roboflow.com/myspace-vwrde/garbage-dumping-detection) [검색요약]
- Roboflow Dumpsite Detection: 드론 2,115장(1280×1280). 시점이 달라 부적합 — [Roboflow](https://universe.roboflow.com/igor-dimitrovski-qowpq/dumpsite-detection) [검색요약]
- GIGO(Garbage In, Garbage Out, UvA): 암스테르담 거리 사진 25k장, 클래스는 garbage, garbage bag, litter, bulky waste, cardboard. figshare에 공개 — [figshare](https://figshare.com/articles/media/GIGO_Garbage_in_Garbage_out_An_Urban_Garbage_Classification_Dataset/20750044) [검색요약]
- Kaggle 출처라고 하는 Street Cleanliness 데이터셋(clean/dirty street/recycling bin)이 gts.ai에 재게시돼 있다. 원 Kaggle 링크와 라이선스는 미확인 — [gts.ai](https://gts.ai/dataset-download/street-cleanliness-and-recycling-bin-dataset/) [검색요약]
- Kaggle Garbage Dataset(Suman Kunwar, 13,348장)은 분리배출용 물체 사진이라 거리 장면이 아니다 — [검색결과](https://paperswithcode2.com/dataset/11663) [검색요약]

### Inferences
- 한국 대문 앞 종량제 봉투, 폐가구, 스티로폼 투기와 시각적으로 가장 비슷한 것은 "w/o people"(비닐봉지·가구류)과 GIGO(bulky waste, garbage bag)일 것으로 본다(추정).
- 소형 YOLO 미세조정에 쓴다면 이 범주가 가장 쉽다. 단, "우편물·전단 적체"와 "인화성 물질 방치"는 어떤 공개셋에도 없으므로 자체 라벨이 필요하다.

### Gaps
- Kaggle 내부의 "street litter" 장면셋(예: TACO는 근접 물체 위주로 알고 있음, [미검증])은 이번 예산으로 확인하지 못했다.

---

## 4. 문·창 개방/폐쇄, 판자로 막은 창(boarded-up)

### Takeaway
"문 열림/닫힘"이나 "합판으로 막은 창"을 라벨로 가진 공개셋은 찾지 못했다. 깨진 창(위 2번)과 일반 창·문 검출셋만 있다.

### Cited Findings
- Roboflow Windows and doors(Assembli): 클래스 11개(door, window, Exterior wall 등). 실내 도면·주택 요소 위주이고 손상이나 개폐 라벨은 없다 — [Roboflow](https://universe.roboflow.com/assembli/windows-and-doors-wyj6n) [검색요약]
- Roboflow door(brahmaduttas-workspace): 세부 미확인 — [Roboflow](https://universe.roboflow.com/brahmaduttas-workspace/door-ydgvy) [검색요약]
- boarded/open door 전용셋은 검색에서 확인되지 않았다 — [검색결과 요약(Roboflow 검색)](https://universe.roboflow.com/youray/-nshli) [검색요약]

### Inferences
- 이 항목은 멀티모달 LLM 제로샷에 맡기고, 평가셋은 자체 촬영·라벨로 만드는 수밖에 없다. 한국 빈집은 합판보다는 방범창·셔터·출입문 개방이 많을 것이므로(추정) 해외셋이 있어도 도메인이 맞지 않는다.

### Gaps
- Roboflow에서 "boarded", "plywood", "vacant house"로 추가 검색하지 못했다(예산).

---

## 5. 낙서(graffiti)

### Takeaway
Roboflow에 소형 낙서 검출셋이 여럿 있다(대체로 수백 장, 다수 CC BY 4.0). Kaggle 전용셋은 확인하지 못했다. 한국 빈집 낙서(락카 스프레이, 경고 문구)와는 대체로 비슷할 것으로 본다.

### Cited Findings
- Roboflow Graffiti Detection(mpl2): 객체 검출, CC BY 4.0, 설명 없음 — [Roboflow](https://universe.roboflow.com/mpl2/graffiti-detection-shzgr) [검색요약]
- Roboflow GraffitiDetection(telegrammbot): CC BY 4.0, 클래스 11개(graffiti_1~11) — [Roboflow](https://universe.roboflow.com/telegrammbot/graffitidetection-nimjx) [검색요약]
- Roboflow Graffiti-garage(sabah): CC BY 4.0 — [Roboflow](https://universe.roboflow.com/sabah/graffiti-garage) [검색요약]
- Roboflow graffiti_detection_model(sumanthrao369): Public Domain, 약 1년 전 업데이트 — [Roboflow](https://universe.roboflow.com/sumanthrao369/graffiti_detection_model) [검색요약]
- Roboflow Graffiti detection(project-ynhfw): YOLOv8 체크포인트 있음. 유사 프로젝트들은 124~619장 규모 — [Roboflow](https://universe.roboflow.com/project-ynhfw/graffiti-detection-ibxz4) [검색요약]
- Kaggle 낙서 전용셋은 검색에서 확인되지 않았다 — [검색결과](https://arxiv.org/pdf/2602.10500) [검색요약]

### Inferences
- LLM 퓨샷 예시와 소규모 보조 평가셋으로는 충분하다. 해외 낙서는 "예술형 태깅"이 많아 한국의 단순 문구형 낙서와 차이가 있을 수 있다(추정).

### Gaps
- 각 셋의 정확한 이미지 수는 미확인.

---

## 6. 도시 인지(Place Pulse 2.0 등 안전 인식) 스트리트뷰

### Takeaway
Place Pulse 2.0과 그 파생셋 PP2-M(HF, 약 111k행, Google Street View 기반)은 존재를 확인했지만, 라이선스는 "other"로만 표기돼 있고 원 이미지가 GSV라서 상업 서비스 학습에는 위험하다. 우리 항목(개별 결함)과도 맞지 않아 "쓸모 낮음"이다.

### Cited Findings
- PP2-M(HF, DominikM198): 약 111k행, GSV 이미지 + Sentinel-2 + OSM 타일 + POI 텍스트의 다중모달, votes 컬럼, split은 train/validation_in_region/validation_out_region, license 태그는 "other" — [HF: PP2-M](https://huggingface.co/datasets/DominikM198/PP2-M) [확인]
- PP2-M README에는 모달리티별로 라이선스가 다르다(LICENSES 폴더)고 적혀 있다 — [HF 미러 README](https://hf-proxy-en5.pages.dev/datasets/DominikM198/PP2-M/blob/main/README.md) [검색요약]
- HyperAI 미러에는 placepulse.zip 113.24MB, 라이선스 "Other"로 등재돼 있다 — [hyper.ai](https://hyper.ai/datasets/20362) [검색요약]
- 의미 분할을 더한 파생셋 moritzef/semantic_edges_and_segmentation_placepulse(HF)도 있다 — [HF](https://huggingface.co/datasets/moritzef/semantic_edges_and_segmentation_placepulse/tree/main) [검색요약]

### Inferences
- 장면 단위 "안전해 보임" 점수라 "깨진 유리 있음/없음" 같은 개별 항목 판독 평가에 쓸 수 없다. 해커톤에서는 제외해도 된다.
- GSV 이미지는 Google 약관상 재배포·학습 이용이 제한될 수 있다. 원 약관은 이번 조사에서 확인하지 못했다.

### Gaps
- MIT Media Lab 원 Place Pulse 2.0의 이용 조건은 공식 페이지를 확인하지 못했다.

---

## 7. 한국 특화 거리·건물 이미지(Kaggle/HF)

### Takeaway
Kaggle·HF에서 한국 주택 외관 데이터셋은 찾지 못했다. 한국 관련으로는 HF의 Korean Signs(간판, CC BY 4.0)와 논문 기반 서울 스트리트뷰 DB(Naver, 423,353장, 2010~2023)가 있지만, 후자는 HF/Kaggle에 없고 페이지도 열리지 않았다(Springer 인증 리다이렉트).

### Cited Findings
- Seoul street-view database for urban environment research(Computational Urban Science, 2026): Naver 지도 거리뷰 423,353장(2010~2023), 객체 마스크와 특징셋 포함, "연구 커뮤니티에 공개"라고 한다 — [Springer](https://link.springer.com/article/10.1007/s43762-026-00246-9) [검색요약, 페치 시 인증 리다이렉트], [journal.hep.com.cn](https://journal.hep.com.cn/cus/EN/10.1007/s43762-026-00246-9) [검색요약]
- HumynLabs/Korean-Signs-Image-Dataset(HF): 한국 거리 간판·상점 간판·공공안내판 고해상도 이미지, CC BY 4.0 — [HF README](https://huggingface.co/datasets/HumynLabs/Korean-Signs-Image-Dataset/blob/main/README.md) [검색요약]
- 서울 교통 랜드마크 데이터셋(IEEE DataPort, 약 15만 장, 랜드마크 약 47만 개). 건물 외관용이 아니다 — [IEEE DataPort](https://ieee-dataport.org/user/44779) [검색요약]
- HF Ning802/hk-streetview-images는 이름상 홍콩으로 보인다 — [HF: Ning802](https://huggingface.co/Ning802) [검색요약]

### Inferences
- 서울 거리뷰 DB가 공개되어 있다면 한국 다세대·단독 외관과 가장 비슷한 원천이다. 다만 Naver 거리뷰 이미지의 재배포·학습 이용 조건이 불분명하므로 내부 평가용으로만 검토해야 한다.
- Korean Signs셋은 "경고판·출입금지 표지 유무" 항목의 퓨샷 예시(한국어 경고문)로 일부 쓸 만하다(추정, 해당 이미지 포함 여부 미확인).
- 한국 주택 외관 데이터는 이 세 플랫폼보다 AI Hub(과기정통부/NIA) 쪽에 있을 가능성이 크다. 범위 밖이라 다른 조사 파트에서 확인이 필요하다.

### Gaps
- 서울 거리뷰 DB의 실제 다운로드 위치와 라이선스는 미확인(논문 Data Availability를 직접 확인해야 함).

---

## 바로 쓸 만한 데이터셋 Top 5

| 순위 | 데이터셋 | 플랫폼 | 규모/라벨 | 관련 항목 | 라이선스 | 한국 주택 유사도 | 용도 | 검증 |
|---|---|---|---|---|---|---|---|---|
| 1 | [Illegal Dumping (development-outcomex)](https://universe.roboflow.com/development-outcomex/illegal-dumping) | Roboflow | 2,198장, 검출 | 쓰레기·폐기물 투기 | CC BY 4.0(표기) | 중 (지상 시점, 해외 거리) | 퓨샷 + 보조 평가 + YOLO 미세조정 | [검색요약] |
| 2 | [Illegal dumping w/o people (garbage-chute)](https://universe.roboflow.com/garbage-chute/illegal-dumping-w-o-people) | Roboflow | 9클래스, 검출 | 투기(비닐봉지·가구 등) | 미확인 | 중 | 퓨샷, 클래스 체계 참고 | [검색요약] |
| 3 | [Разбитые дома и окна (YOURAY)](https://universe.roboflow.com/youray/-nshli) | Roboflow | 3클래스(broken-house/window, window-without-glass) | 깨진 유리, 문·창 파손 | Public Domain(표기) | 중~하 (해외 주택 추정) | 퓨샷 + 보조 평가 | [검색요약] |
| 4 | [Graffiti Detection (mpl2) 외 CC BY 낙서셋](https://universe.roboflow.com/mpl2/graffiti-detection-shzgr) | Roboflow | 수백 장, 검출 | 낙서 | CC BY 4.0 | 중 | 퓨샷 + 보조 평가 | [검색요약] |
| 5 | [elliemci/building_damages](https://huggingface.co/datasets/elliemci/building_damages) | HF | 7,257장, 검출(COCO), cracks 등 9클래스 | 외벽 균열·구조 손상 | CC BY 4.0, 게이트 | 하~중 (구조부재 근접 추정) | cracks 클래스만 골라 퓨샷 | [확인] |

공통 권고: 위 셋은 모두 "보조"용이다. LLM 판독 정확도의 본 평가셋은 안산 현장·시민 제보 형태의 한국 주택 사진(200~500장 규모, 9개 항목 다중라벨)을 자체 구축해야 한다. Roboflow 항목은 403 때문에 직접 확인하지 못했으므로 이미지 수와 라이선스를 브라우저로 재확인해야 한다.

## 쓰면 안 되는 것 (라이선스·도메인 불일치)

- **RealUAV-SD/UAV2K**: 비상업 학술 전용, 재배포는 서면 허가, 상업 이용은 별도 승인. 드론 시점 RC 건물이라 도메인도 다르다. 서비스용 모델 학습에는 쓰면 안 된다 — [HF](https://huggingface.co/datasets/RealUAV-SD/UAV2K) [확인]
- **Place Pulse 2.0 / PP2-M**: 라이선스 "other", Google Street View 원천. 장면 단위 인지 점수라 개별 항목 판독과 맞지 않는다 — [HF](https://huggingface.co/datasets/DominikM198/PP2-M) [확인]
- **Dumpsite Detection·Aerial-Dumping-Sites 등 드론/항공 투기셋**: 시점이 맞지 않는다(공공도로 지상 촬영과 다름) — [Roboflow](https://universe.roboflow.com/igor-dimitrovski-qowpq/dumpsite-detection) [검색요약]
- **Kaggle Garbage Dataset(분리배출) 류 근접 물체 사진**: 거리 장면이 아니다 — [검색결과](https://paperswithcode2.com/dataset/11663) [검색요약]
- **Kaggle Abandoned Object Detection(unidpro)**: 버려진 수하물 영상이고 유료 판매 미리보기다 — [Kaggle](https://www.kaggle.com/datasets/unidpro/abandoned-object-detection-video-dataset) [검색요약]
- **지진 피해셋(UAVs-TEBDE, MDPI 7,062장, Kaggle 고르카 표 데이터)**: 붕괴 수준 피해나 드론·표 데이터라 경미한 외벽 균열 판독과 분포가 다르다 — [Mendeley](https://data.mendeley.com/datasets/5m349hfvkb/2) [검색요약]
- **Assembli Windows and doors**: 실내·도면 요소 중심이고 손상·개폐 라벨이 없다 — [Roboflow](https://universe.roboflow.com/assembli/windows-and-doors-wyj6n) [검색요약]
- **서울 거리뷰 DB(Naver)**: 한국 유사도는 높지만 Naver 이미지 재배포·학습 조건이 미확인이다. 확인 전에는 상용 학습에 쓰지 말고 내부 참고용으로만 검토 — [journal.hep.com.cn](https://journal.hep.com.cn/cus/EN/10.1007/s43762-026-00246-9) [검색요약]
- **Roboflow 셋 전반의 주의**: CC BY 4.0이라고 표기돼 있어도 원천 이미지가 웹 크롤링일 수 있다. 출처 표기 의무(CC BY)를 지켜야 하고, 라이선스가 미표기된 셋은 쓰지 않는다.
