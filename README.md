# LOL2Youtube

## 설명

롤의 재밌는 장면을 수집, 녹화, 업로드하는 프로세스를 자동화하는 프로젝트입니다.

## 사용 기술

- django, restframework, python
- docker, dodcker-compose
- selenium
- riot-data-api, riot-client-api
- html, css, django-template-engine
- gcp
- 반디캠

## 자체사이트

https://lol2youtube.com

## 모든 유튜브 채널

1. [Pentakill Collector2](https://www.youtube.com/channel/UCs25KVMmHqCpkMqcecEIRjQ)
2. [Pentakill Collector3](https://www.youtube.com/channel/UCmhM703LbZ1r86r8CKsyEkA)
3. [Pentakill Collector4](https://www.youtube.com/channel/UCOt3LsX2wMC3JUTV_IPzt5w)
4. [Pentakill Collector5](https://www.youtube.com/channel/UCk7tNq10DyUmboClA6t6q_A)

## 모든 저장소

1. [api 크롤링 서버](https://github.com/gghotted/lol2youtube-server)
2. [로컬 pc](https://github.com/gghotted/lol2youtube-client)
3. [자체 사이트 서버](https://github.com/gghotted/lol2youtube)(이 저장소)

## 시스템 구성 및 프로세스

<img src="./docs_images\l1.png" style="zoom:67%;" />

riot api를 통해 펜타킬 정보를 수집하는 크롤링 서버가 gcp 위에서 상시 구동중입니다.

------

<img src="./docs_images\l2.png" style="zoom:67%;" />

로컬 PC에서 크롤링 서버로 부터 녹화할 데이터를 받아오고, 반디캠을 통해 녹화, moviepy를 통해 간단한 편집을 합니다.

------

<img src="./docs_images\l3.png" style="zoom:67%;" />

준비된 영상을 selenium을 통해 업로드하고 youtube로 부터 url을 받아옵니다.

------

<img src="./docs_images\l4.png" style="zoom:67%;" />

url과 녹화 및 펜타킬 정보를 자체 사이트 서버에 전달하여 저장합니다.

------

<img src="./docs_images\l5.png" style="zoom:67%;" />

유저는 유튜브 shorts 추천과, 자체 사이트를 통해 영상을 볼 수 있습니다.

## 운영 및 수익화

하루 1분 이하의 영상 약 300~400개를 만들 수 있는 것에 비해 유튜브 채널당 하루 업로드 제한은 100개 입니다. 그래서 4개의 채널에 분산하여 업로드 중입니다. 후에 분산된 영상을 모아 한 사이트에서 보고, 검색할 수 있게 만들면 좋겠다 생각해서 자체 사이트를 만들었습니다.

lol client로 랜더링한 영상을 녹화하기 때문에 로컬 pc가 필요합니다. 로컬 pc를 사용하지 않을 때(잘 때) 프로그램을 켜두면서 운영하고 있습니다.

하루 약 20만~30만의 총 조회수(쇼츠)를 내고 있지만 쇼츠 영상의 조회수는 수익이 발생하지 않습니다. 그래서 댓글에 쿠팡 파트너스 링크를 달아 수익을 내는 방식을 테스트해본 결과 1주일간 약 4만원의 수익을 낼 수 있었습니다. 생각보다 적은 수익이지만 댓글 유입을 늘리고, 자체 사이트에 애드센스를 넣는 등의 방법으로 더 높은 수익을 기대하고 있습니다.







