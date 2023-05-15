---
tags: [web, security, authorization, oauth]
title: OAuth2 에 대해 알아보자.
author: ndy2
date: 2023-05-15
description: >-
  
---
 
> [!quote] 참고 자료
> * [`『OAuth』`](https://en.wikipedia.org/wiki/OAuth) on Wikipedia
> * RFC 6749 -  [`『The OAuth 2.0 Authorization Framwork』`](https://datatracker.ietf.org/doc/html/rfc6749)
> * OktaDev -  [`『OAuth 2.0 and OpenID Connect』`](https://youtu.be/996OiexHze0) on Youtube 

### 1. What is OAuth

![[logo.png| The OAuth logo]]

> [!note] `OAuth` 요약
> * `Open Authorization`
> * an open standard for access delegation
>     * 권한 위임 표준이다.

> [!note] OAuth 2.0 의 정의 in `『RFC 6749』` Abstract
> OAuth 2.0 인가 프레임워크는 third-party application 이 HTTP 서비스를 통해 제한된 권한을 획득하는 것을 가능하게합니다.
> 
> 이 과정에서 OAuth 2.0 프레임워크는 resource owner 를 대신하여 HTTP service 간의 승인 과정을 대신 수행하거나 third-party application 이 자신이 해야될 승인 과정을 대신 수행하도록 합니다.

> [!warning] OAuth - 인가
>  - 중요한 점은 `OAuth` 는 `권한 위임 표준`이다.
>  - 인증 아니다. 인가이다.!!!!!
>  - 인증은 `OIDC`, `SAML` 을 이용한다!!!!
>  - OAuth is an _authorization_ protocol, rather than an _authentication_ protocol. - ``『link@wikipedia』``

OAuth 와 OIDC 의 설계에 있어 한가지 아쉬운점은 OIDC 가 OAuth 위에서 동작한다는 것이다. 인증/인가의 관계를 생각했을때 인가를 했더는 것은 인증이 되었다는 의미로 볼 수 있을거 같은데 오히려 반대로 OAuth 위에서 OIDC가 동작하도록 설계되었다. 그래서인지 OAuth 라는 용어가 더 유명하고 널리 활용되고 흔히 `OAuth 로그인` 과 같은 개인적으로 생각했을때 모호한 용어가 퍼지는것 같아 아쉽다.

`OIDC`, `SAML` 등의 표준은 다음 기회에 더 자세히 알아보고 이번 포스팅에서는 `권한 위임 표준`인 `OAuth`에 대해 자세히 알아보자!

### 2. Terminologies

#### 2.1 Roles

OAuth defines four roles:
-   `Resource owner` (the user)
-   `Resource server` (the API)
-   `Authorization server` (can be the same server as the API)
-   `Client` (the application)

### 2.2 Tokens

요청에 사용하는 토큰이다. 타입에 대한 정의가 표준에 되어 있지 않지만 대부분 JWT를 사용한다.

OAuth defines two types of tokens:
- `access token` (권한 토큰)
    - 리소스 서버에 인가가 필요한 요청을 수행하기 위해 포함되어야 하는 토큰
    - 보통 만료시간, scope (요청 가능 범위) 
- `refresh token` (리프레시 토큰)
    - access token 을 재발급하기 위해 사용한다.
    - 필수는 아니다.

#### 2.3 `Authorization Code`

인가 코드는 OAuth Flow 중 `Authorization Code Grant` Flow 에서 사용되는 작은 문자열이다. 해당 Flow 에서 클라이언트는 이 코드 값을 이용해 Access Token 을 교환(exchange)한다.

#### 2.4 `Redirect URI`

`Redirect URI`는 OAuth Flow 중 `code`/`Token` 을 발급한 후 Client 의 브라우저를 Redirection 하기 위해 약속된 URI 이다. 이를 

### 3. OAuth Flow

```
TODO
```

#### 3.1 Authorization Code Grant

### 4. OAuth Endpoints

```
TODO
```


### 5. OAuth Vulunabilities

```
TODO
```

#### 5.1 Covert Redirect

### 6. What is the difference between OAuth2.0 & OAuth2.1
 
> [!quote] 참고 자료
> * draft-ietf-oauth-v2-1-07 - [`『The OAuth 2.1 Authorization Framework』`](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-07#section-1.1)
> * `Dan Moore` - [`『Differences between OAuth 2 and OAuth 2.1』`](https://fusionauth.io/learn/expert-advice/oauth/differences-between-oauth-2-oauth-2-1) on FusionAuth
>     * [번역 - by worn29](https://velog.io/@worn29/Differences-between-OAuth-2-and-OAuth-2.1번역)

OAuth 에 대한 개발이 활발히 진행중이다. 아직 표준이 나오진 않았지만 위와 같은 자료도 돌아다니고 공식문서에 대안 초안이 활발히 정리중인것 같다. 특히 [`Spring Authorization Server`](https://github.com/spring-projects/spring-authorization-server) 의 README 에서도 OAuth 2.0 이 아니라 OAuth 2.1 을 지원하는 것을 목표로 한다고 명시되어 있다. [관련 커밋](https://github.com/spring-projects/spring-authorization-server/commit/b5db5ffe546111d0545244b7a9b63786fe74034d)

위 문서들을 통해 알아낸 사실은 OAuth 2.1 은 OAuth 2.0 에 새로운 기능을 추가하는 것이 아니라 보안상의 Best Practice 를 기본적으로 채택한 단순한 확장이라는 것이다.

이 [링크](https://velog.io/@worn29/Differences-between-OAuth-2-and-OAuth-2.1번역#what-is-changing-from-oauth-20-to-oauth-21) 에서 소개하는 여섯가지 변경사항을 요약해보자.

1. `Authorization Code Grant` Flow 에서 PKCE 를 항상 활용해야 한다.
2. Redirection URI 의 문자열 검증에는 정확한 문자열 일치를 사용해야 한다.
3. `Implicit Grant` Flow 는 제거되었다.
4. `Resource Owner Password Credentials Grant` Flow 도 제거되었다.
5. 쿼리 문자열에 토큰 박지 마라
6. Refresh Token 은 발신자를 제한하던가 일회성으로 사용 되어야 한다.

와우! 정말 좋은 변경들이다. 뭔가 공부할게 줄어든 느낌이라서 특히 3번과 4번 변경사항이 아주 마음에 든다. 

또한 1번 `PKCE` 와 6번에서 일회성 사용을 보장하기위한 `Refresh Token Rotation` 기법 그리고 개인적으로 관심가졌던 Covert Redirect 취약성과 관련된 2번 변경사항 역시 아주 흥미롭다.

이들에 관해서는 다음 포스팅에서 알아보겠다.