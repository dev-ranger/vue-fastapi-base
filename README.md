<p align="center">
  <a href="https://github.com/mizhexiaoxiao/vue-fastapi-admin">
    <img alt="Vue FastAPI Admin Logo" width="200" src="https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/logo.svg">
  </a>
</p>

<h1 align="center">vue-fastapi-admin</h1>

[English](./README-en.md) | 한국어

FastAPI + Vue3 + Naive UI 기반의 현대적인 프론트엔드-백엔드 분리 개발 플랫폼으로, RBAC 권한 관리, 동적 라우팅 및 JWT 인증을 통합하여 중소 규모 애플리케이션의 빠른 구축을 지원하며 학습 참고용으로도 사용할 수 있습니다.

### 특징
- **최신 기술 스택**: Python 3.11 및 FastAPI 고성능 비동기 프레임워크를 기반으로 하며, Vue3 및 Vite와 같은 최첨단 기술을 결합하여 개발되었으며 효율적인 npm 패키지 관리자인 pnpm을 사용합니다.
- **코드 규범**: 프로젝트에는 풍부한 규범 플러그인이 내장되어 코드 품질과 일관성을 보장하고 팀 협업 효율성을 효과적으로 향상시킵니다.
- **동적 라우팅**: 백엔드 동적 라우팅은 RBAC(Role-Based Access Control) 권한 모델과 결합되어 세분화된 메뉴 라우팅 제어를 제공합니다.
- **JWT 인증**: JSON Web Token(JWT)을 사용하여 신원 확인 및 권한 부여를 수행하여 애플리케이션 보안을 강화합니다.
- **세분화된 권한 제어**: 버튼 및 인터페이스 수준의 권한 제어를 구현하여 다양한 사용자 또는 역할이 인터페이스 작업 및 인터페이스 액세스 시 서로 다른 권한 제한을 갖도록 보장합니다.

### 온라인 미리보기
- [http://47.111.145.81:3000](http://47.111.145.81:3000)
- username: admin
- password: 123456

### 로그인 페이지

![image](https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/login.jpg)
### 작업 공간

![image](https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/workbench.jpg)

### 사용자 관리

![image](https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/user.jpg)
### 역할 관리

![image](https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/role.jpg)

### 메뉴 관리

![image](https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/menu.jpg)

### API 관리

![image](https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/api.jpg)

### 빠른 시작
#### 방법 1: Docker Hub에서 이미지 가져오기

```sh
docker pull mizhexiaoxiao/vue-fastapi-admin:latest 
docker run -d --restart=always --name=vue-fastapi-admin -p 9999:80 mizhexiaoxiao/vue-fastapi-admin
```

#### 방법 2: Dockerfile로 이미지 빌드
##### Docker 설치 (버전 17.05+)

```sh
yum install -y docker-ce
systemctl start docker
```

##### 이미지 빌드

```sh
git clone https://github.com/mizhexiaoxiao/vue-fastapi-admin.git
cd vue-fastapi-admin
docker build --no-cache . -t vue-fastapi-admin
```

##### 컨테이너 시작

```sh
docker run -d --restart=always --name=vue-fastapi-admin -p 9999:80 vue-fastapi-admin
```

##### 접속

http://localhost:9999

username：admin

password：123456

### 로컬에서 시작하기
#### 백엔드
프로젝트를 시작하려면 다음 환경이 필요합니다:
- Python 3.11

#### 방법 1 (권장): uv를 사용하여 의존성 설치
1. uv 설치
```sh
pip install uv
```

2. 가상 환경 생성 및 활성화
```sh
uv venv
source .venv/bin/activate  # Linux/Mac
# 또는
.\.venv\Scripts\activate  # Windows
```

3. 의존성 설치
```sh
uv add pyproject.toml
```

4. 서비스 시작
```sh
python run.py
```

#### 방법 2: Pip를 사용하여 의존성 설치
1. 가상 환경 생성
```sh
python3 -m venv venv
```

2. 가상 환경 활성화
```sh
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

3. 의존성 설치
```sh
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

4. 서비스 시작
```sh
python run.py
```

이제 서비스가 실행 중이어야 합니다. API 문서를 보려면 http://localhost:9999/docs 에 접속하세요.

#### 프론트엔드
프로젝트를 시작하려면 다음 환경이 필요합니다:
- node v18.8.0+

1. 프론트엔드 디렉토리로 이동
```sh
cd web
```

2. 의존성 설치 (pnpm 사용 권장: https://pnpm.io/zh/installation)
```sh
npm i -g pnpm # 이미 설치된 경우 무시
pnpm i # 또는 npm i
```

3. 시작
```sh
pnpm dev
```

### 디렉토리 설명

```
├── app                   // 애플리케이션 디렉토리
│   ├── api               // API 인터페이스 디렉토리
│   │   └── v1            // 버전 1 API 인터페이스
│   │       ├── apis      // API 관련 인터페이스
│   │       ├── base      // 기본 정보 인터페이스
│   │       ├── menus     // 메뉴 관련 인터페이스
│   │       ├── roles     // 역할 관련 인터페이스
│   │       └── users     // 사용자 관련 인터페이스
│   ├── controllers       // 컨트롤러 디렉토리
│   ├── core              // 핵심 기능 모듈
│   ├── log               // 로그 디렉토리
│   ├── models            // 데이터 모델 디렉토리
│   ├── schemas           // 데이터 스키마/구조 정의
│   ├── settings          // 구성 설정 디렉토리
│   └── utils             // 유틸리티 디렉토리
├── deploy                // 배포 관련 디렉토리
│   └── sample-picture    // 샘플 이미지 디렉토리
└── web                   // 프론트엔드 웹 디렉토리
    ├── build             // 빌드 스크립트 및 구성 디렉토리
    │   ├── config        // 빌드 구성
    │   ├── plugin        // 빌드 플러그인
    │   └── script        // 빌드 스크립트
    ├── public            // 공용 리소스 디렉토리
    │   └── resource      // 공용 리소스 파일
    ├── settings          // 프론트엔드 프로젝트 구성
    └── src               // 소스 코드 디렉토리
        ├── api           // API 인터페이스 정의
        ├── assets        // 정적 리소스 디렉토리
        │   ├── images    // 이미지 리소스
        │   ├── js        // JavaScript 파일
        │   └── svg       // SVG 벡터 이미지 파일
        ├── components    // 컴포넌트 디렉토리
        │   ├── common    // 공용 컴포넌트
        │   ├── icon      // 아이콘 컴포넌트
        │   ├── page      // 페이지 컴포넌트
        │   ├── query-bar // 검색 바 컴포넌트
        │   └── table     // 테이블 컴포넌트
        ├── composables   // 조합 가능한 기능 블록
        ├── directives    // 디렉티브 디렉토리
        ├── layout        // 레이아웃 디렉토리
        │   └── components // 레이아웃 컴포넌트
        ├── router        // 라우터 디렉토리
        │   ├── guard     // 라우트 가드
        │   └── routes    // 라우트 정의
        ├── store         // 상태 관리 (pinia)
        │   └── modules   // 상태 모듈
        ├── styles        // 스타일 파일 디렉토리
        ├── utils         // 유틸리티 디렉토리
        │   ├── auth      // 인증 관련 유틸리티
        │   ├── common    // 공용 유틸리티
        │   ├── http      // axios 래퍼
        │   └── storage   // localStorage 및 sessionStorage 래퍼
        └── views         // 뷰/페이지 디렉토리
            ├── error-page // 오류 페이지
            ├── login      // 로그인 페이지
            ├── profile    // 개인 프로필 페이지
            ├── system     // 시스템 관리 페이지
            └── workbench  // 작업 공간 페이지
```

### 그룹 채팅 참여
그룹에 참여하는 조건은 프로젝트에 스타를 주는 것입니다. 작은 스타는 작가가 계속 유지하는 원동력입니다.

그룹에서 어떤 질문이든 할 수 있으며, 최대한 빨리 답변해 드리겠습니다.

<img width="300" src="https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/group.jpg">

## 후원
프로젝트가 도움이 되었다면 작가에게 커피 한 잔 사주실 수 있습니다~

<div style="display: flex">
    <img src="https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/1.jpg" width="300">
    <img src="https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/2.jpg" width="300">
</div>

## 맞춤 개발
이 프로젝트를 기반으로 한 맞춤 개발 요구 사항이나 기타 협력이 있으시면 아래 위챗을 추가하고 방문 목적을 알려주십시오.

<img width="300" src="https://github.com/mizhexiaoxiao/vue-fastapi-admin/blob/main/deploy/sample-picture/3.jpg">

### Visitors Count

<img align="left" src = "https://profile-counter.glitch.me/vue-fastapi-admin/count.svg" alt="Loading">
