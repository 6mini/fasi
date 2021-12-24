<div align=center>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F6mini%2Ffasi&count_bg=%23AAAAAA&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Hits&edge_flat=false)](https://github.com/6mini/fasi)

</div>

![Project4 001](https://user-images.githubusercontent.com/79494088/141001615-ad6d41ac-2b66-419f-9c9c-94eb166c7ae2.png)

<div align=center>

<img src="https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=Keras&logoColor=white"/></a>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/></a>
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=TensorFlow&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/></a>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=Selenium&logoColor=white"/></a>

<img src="https://img.shields.io/badge/Amazon S3-569A31?style=flat-square&logo=Amazon S3&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=AmazonAWS&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Heroku-430098?style=flat-square&logo=Heroku&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/></a>



# Welcome to FASI 🙋🏻‍♂️

</div>

- '인공지능이 분류하는 나의 패션은?'이라는 주제의 딥러닝 프로젝트: 패션 스타일 분류 앱 'FASI'
- [웹 어플리케이션 바로가기](https://fasi.herokuapp.com/)
- [블로그 포스팅 바로가기](https://6mini.github.io/project/2021/11/13/fasi/)

# 문제 정의

![Project4 003](https://user-images.githubusercontent.com/79494088/141001889-df9f1841-e800-47cb-af97-924a3ef07470.png)

- 데이터에 대해 접하고 난 후 데이터를 활용한 초개인화 서비스를 만들고 싶은 마음이 컸다.
- 만약 패션에 관련된 커뮤니티가 형성되고, 개개인의 옷사진을 분석하여 데이터화할 수 있다면 추천 알고리즘에 큰 도움이 되지 않을까란 생각을 했다. 굳이 커뮤니티가 아니더라도 각종 SNS 등에 게시된 사진으로도 개인화 광고 등에 유용하게 쓰일 거라 판단했다.
- 여러가지 패션 스타일을 고유한 특징점을 찾아 기계 학습으로 분류할 수 있을 지에 대한 가설로 시작한 프로젝트이다.

# 데이터 파이프라인

![image](https://user-images.githubusercontent.com/79494088/143801116-9f065bb0-59a2-4e8a-b298-2166c6c1284d.png)

- 셀레니움을 활용하여 무신사 커뮤니티의 스트릿 스냅 이미지 크롤링 하여 로컬에 저장했다.
  - [크롤러 레포지토리 바로가기](https://github.com/6mini/musinsa-snap-crawler)
- 플라스크(Flask) & 헤로쿠(Heroku)를 이용하여 웹 어플리케이션을 구축 및 배포하였다.
- AWS S3과 연동 이용자의 업로드 이미지 행동 데이터가 자동으로 로드되도록 만들었다.

# 딥러닝 모델링

- [딥러닝 모델링 과정 포스팅 바로가기](https://6mini.github.io/project/2021/11/14/fasi2/)

![Project4 005](https://user-images.githubusercontent.com/79494088/141001901-f840ad98-b149-4ed9-8fde-4791243efa0f.png)

- 이미지를 인식하기 위한 패턴을 찾는데 유용한 CNN 모델을 사용했다.
- 기존 수집 데이터에서 추가 크롤링을 하고 'ResNet-50'을 이용한 전이 학습 후 7가지 클래스에서 60% 정확도의 성능을 가진 모델을 완성했다.

# 간단한 회고

![Project4 007](https://user-images.githubusercontent.com/79494088/141003154-19c67885-1774-4cd5-b9cd-3bf25664bc23.png)

- 패션 스타일 자체가 사람도 구분하기 애매할 정도로 정답이 없는 분야라고 할 수 있기 때문에 딥러닝의 학습 자체가 어려웠을 것 같다.
- 사람들은 굉장히 다양한 포즈와 배경에서 사진을 찍기 때문에 사진 전체적으로 분류 학습을 한 것이 아쉬운 진행이라고 생각한다.
- 객체 탐지나 분할을 사용했다면 훨씬 좋은 모델을 만들 수 있을 것 같다.
- 조금 더 공부한 후에 추후 보완을 진행해보고 싶다.

# 미리보기

### 메인 홈페이지

<div align=center>

![image](https://user-images.githubusercontent.com/79494088/141002523-2ac9e0b8-9f0c-4246-830f-9481cbbb68f5.png)

</div>

### 업로드 이미지

<div align=center>

![image](https://user-images.githubusercontent.com/79494088/141002588-e4ade56a-b12d-4197-8c82-430ee45a7386.png)

</div>

### 결과 페이지

<div align=center>

![image](https://user-images.githubusercontent.com/79494088/141002645-7b466eec-d4df-4d63-8306-47a30beae6bd.png)

</div>
