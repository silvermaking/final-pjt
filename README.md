### final-pjt





# Daily Project Progressing

## 2021-11-17(WED)

### Today Goal 

- [x] Vue + django rest API baseline project Create

- [x] Modeling 

  - 데이터베이스 관계 ERD 만들기
  - Tool : [draw.io](https://app.diagrams.net/)
  - 커뮤니티, 영화, User

- [x] 팀장 : 이은성 , 팀원 : 성당현

- [x] 추천 알고리즘 선택

  - 이은성 내일까지 준비

- [x] 11/18계획
- ERD 수정 및 skeleton file 만들기

![ERD](https://lab.ssafy.com/silvermaking/final-pjt/uploads/0d74e0906cf4906cb82262b39e6e40a5/ERD.png)

## 2021-11-18(Thu)

### Today Goal 

- [x] 오전 스크럼 미팅

- [x] 전체 프로젝트 일정 설계

![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/821f8846a03f4c66927c01a04df7b276/image.png)![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/d2b4c8dda29ca43e571ea393e3b9c9ca/image.png)성당현

- [x] - skeleton -front 

  - vue.js, router, node.js, vuex

- [x] 이은성

  - skeleton -back

  - django restful API

## 2021-11-19(Fri)

### Today Goal 

- [x] 오전 스크럼 미팅

![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/0b744a929fc5bd16714993364716431f/image.png)

- [x] 스켈레톤 마무리
- [ ] 연결 확인 
- [x] 성당현
  - 디자인구상 

- [x] 이은성

  - 추천알고리즘 구상



## 2021-11-22(MON)

### Today Goal 

- [x] 오전 스크럼 미팅

- [x] ![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/d41500c26ac345546ee177e3a4e85473/image.png)back-front 연결 확인 
- [x] 성당현
  - 디자인구상 
  - 오류수정

- [x] 이은성

  - 크롤링
  - 추천알고리즘 구현



## 2021-11-23(Tue)

### Today Goal 

- [x] 오전 스크럼 미팅

- [x] ![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/8b20ae5f6841e2fc4f3eaab4dde6a2c3/image.png)성당현
  - 디자인만들기
  - login error
- [x] 이은성

  - 크롤링
  - view함수 구현
  - accounts 에러

## 2021-11-24~25

### Today Goal 

- [x] 오류 수정 및 최종 제출



## 1. 팀원정보 및 업무 분담 내역

### 이은성 : backend

- Django-Restful-API



### 성당현 : frontend

- vue.js, node.js, vuex, router



## 2. 목표 서비스 구현 및 실제 구현 정도

#### 목표

- 사용자 친화적 디자인
- 추천시스템 협업필터링 알고리즘
- 평점 
- board



### 구현
- [x] 오류
- [ ] 추천시스템
  - 시간 관계상 vote_count 정렬로 간단히 바꿈 
- [ ] 평점
  - 오류가 계속 떠서 결국 해결하지 못하고 구현 x
- [x] board



## 3. ERD

![ERD](https://lab.ssafy.com/silvermaking/final-pjt/uploads/0d74e0906cf4906cb82262b39e6e40a5/ERD.png)

## 4. 필수 기능

### 디자인

- Home : movie card + 평점

- ![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/2b4b017f0bde2da4904b9a7de6970c6c/image.png)Recommend : vote_count 내림차순으로 정렬해서 사용자에게 추천

- ![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/8539d5f28a548ec457c4f8ad1d1e6fcc/image.png)Board : 게시판 

- ![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/8b221a9d1d1ef6aed87c88f80a1a6fbf/image.png)UI

![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/fc321a8f21deea82feab18326fd6284b/image.png)



### 추천알고리즘

```python
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def recommendMovie(request):
    movies = Movie.objects.all().order_by('-vote_count')[:6]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
```



### 관리자 페이지

![image](https://lab.ssafy.com/silvermaking/final-pjt/uploads/fc321a8f21deea82feab18326fd6284b/image.png)

## 5. 배포

- 배포는 시간관계상 하지 못함



### 6. 느낀점

- 성당현

```tex
서버와 프론트로 나눠서 진행하면 쉽게 될줄 알았는데 에러의 연속이었고 CSS를 통한 디자인도 하나를 바꾸면 다른게 다 바뀌는 등 원하는대로 적용시키는게 어려웠습니다. 잘안될 때 적극 소통하면서 했어야 했는데 너무 혼자 고민하며 시간을 허비해 이도저도 못한거 같아 미안한 마음입니다.
```



- 이은성

```tex
교육을 받을 때는 교수님의 도움으로 에러들을 쉽게 해결했지만 혼자 하려하니 밤을 샐 정도로 오래걸리거나 끝까지 해결하지 못한 오류들이 많았다.
또한 local 환경 문제로 협업이 원할하지 않아 front와 back을 따로 작업하는 경우가 많았는데 서로의 연결 test를 제대로 하지 못했다. 
목표를 거창하게 잡았지만 많은 에러들과 사용하는 tool에 대한 이해부족으로 많은 것을 구현하지 못해 아쉬웠다.
```

