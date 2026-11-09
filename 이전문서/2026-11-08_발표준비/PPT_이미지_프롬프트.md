# PPT 이미지 생성 프롬프트

> 슬라이드의 점선 칸(이미지 1~4)에 들어갈 그림. ChatGPT 이미지 생성에 그대로 붙여 넣는다.
> **공통 규칙:** 그림 안에 글자를 넣지 않는다(한글이 깨지기 쉬움). 사람 얼굴·차량번호·실제 주소가 보이지 않게 한다.
> 덱 색: 남색 #14213D, 종이색 #F5F3EE, 진한 빨강 #7F1D1D, 빨강 #DC2626, 주황 #F97316, 초록 #16A34A, 보라 #7C3AED.

## 공통 스타일 문장 (모든 프롬프트 끝에 붙임)

```
Flat vector illustration, clean minimal shapes, soft shadows, limited palette: navy #14213D, warm paper #F5F3EE, accents dark red #7F1D1D, red #DC2626, orange #F97316, green #16A34A, purple #7C3AED. No text, no letters, no numbers, no logos, no human faces.
```

## 이미지 1 · 표지 (오른쪽, 760×620, 가로:세로 약 5:4)

```
A quiet Korean residential alley in Ansan with 3–4 storey red-brick multi-family villa buildings (dasedae housing). One building has a dark, empty unit with a boarded window. A large translucent magnifying glass hovers over that vacant unit and reveals it in a soft warm light, as if the hidden empty house is becoming visible. Small map pins in dark red, orange and green float above other buildings. Calm dusk sky in navy. Wide composition, 5:4 aspect ratio.
```
+ 공통 스타일 문장

## 이미지 2 · SOS 긴급도 지도 카드 (가로 넓은 칸, 약 3:1)

```
A simplified top-down city map with light streets and blocks. Scattered circular markers in four colors: a few dark red, several red, many orange, many green. One translucent purple square area with a dashed border marks a citizen report zone. A small navy panel on the right side suggests a priority list. Wide banner composition, 3:1 aspect ratio.
```
+ 공통 스타일 문장

## 이미지 3 · 시민 제보 연결 카드 (약 3:1)

```
A hand holding a smartphone; the phone screen shows a simple map with a purple translucent square grid cell and a camera icon. Next to the phone, a small calendar card with one date circled suggests a 30-day deadline. Friendly, civic, minimal. Wide banner composition, 3:1 aspect ratio.
```
+ 공통 스타일 문장

## 이미지 4 · AI 점검 일지 초안 카드 (약 3:1)

```
A tablet on a desk showing a photo of a small building facade on the left and five checklist rows on the right, each row with a simple icon: a lock, a flame, a trash bag, a cracked wall, a leaf. A pen and a clipboard beside the tablet. One row is highlighted, another row is greyed out as "unknown". Wide banner composition, 3:1 aspect ratio.
```
+ 공통 스타일 문장

## 스크린샷 (그림 생성 아님 · 앱에서 직접 캡처)

| 칸 | 화면 | 캡처 방법 |
|---|---|---|
| 스크린샷 1 | 시민 제보 작성(카테고리·사진) | `/report`를 휴대폰 폭(개발자 도구 모바일 보기)으로 열고 캡처 |
| 스크린샷 2 | 250m 구역 선택 | 같은 화면 2단계, 지도에서 구역을 고른 뒤 |
| 스크린샷 3 | 접수 완료(접수번호) | 제출 직후 |
| 스크린샷 4 | AI 판독 결과 | `/admin` 상세 패널 3단계. 실제 현장 사진으로 판독한 결과 |
| 현장 사진 | 판독에 쓴 빈집 외관 사진 | 공공도로에서 찍은 외관, 얼굴·차량번호·주소 없게 |
| 스크린샷 5 | 담당자 화면 전체 | `/admin` 첫 화면(4색 지도 + 현황판). 라이브가 안 될 때의 백업 |
