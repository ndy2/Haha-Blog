---
tags: [network, layer7, http]
title: http-method
author: ndy2
date: 2023-04-21
description: >-
  
---
  
> [!quote] 참고 자료
> * 김영한 - [`『모든 개발자를 위한 HTTP 웹 기본 지식』`](https://www.inflearn.com/course/http-웹-네트워크) on Inflearn
> * [`『HTTP Request Methods』`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/) on mozila.developer

### 1. HTTP Method

- `HTTP Method` 란 HTTP 요청에 따라 서버에서 수행하길 기대하는 액션을 표현하는 것입니다.
- 주요 메서드로 `GET`/`POST`/`PUT`/`PATCH`/`DELETE` 가 있고 기타 메서드로 `HEAD`/`OPTIONS`/`TRACE`/`CONNECT` 가 있다.
- 메서드는 HTTP 요청 Start Line의 맨 처음에 작성한다.

### 2. 주요 메서드

`GET`/`POST`/`PUT`/`PATCH`/`DELETE` 는 CRUD 연산에 매핑되며 아래와 같이 요약할 수 있다.

| Http Method | CRUD          | 특징                                                                                         |
| ----------- | ------------- | -------------------------------------------------------------------------------------------- |
| `GET`         | Read          |                                                                                              |
| `POST`        | Create        | Controller Resource에도 활용한다.                                                            |
| `PUT`         | Update/Create | 존재하면 Update 존재하지 않으면 Create, Update 의 경우 전체 필드에 대해 덮어쓰기를 수행한다. |
| `PATCH`       | Update        | Partial Update                                                                               |
| `DELETE`      | Delete              |                                                                                              |


### 3. HTTP 메서드의 속성

-   안전 (Safe Methods)
    -   호출해도 리소스를 변경하지 않는다.
-   멱등(Idempotent Methods)
    -   여러번 호출하여도 ==결과가 같다==. (**aside from error or expiration issues**)
    -   대상 리소스를 기준으로 한다.
-   캐시가능(Cacheable Methods)
    -   응답 결과 리소스를 캐시하여 사용해도 되는가?
    -   실제로는 GET, HEAD 정도만 캐시로 사용

| HTTP Method | 안전 | 멱등 | 캐시 가능 |
| --- | --- | --- | --- |
| `GET` | ✅ | ✅ | ✅ |
| `POST` | ❌ | ❌ | ✅ |
| `PUT` | ❌ | ✅ | ❌ |
| `PATCH` | ❌ | ❌ | ✅ |
| `DELETE` | ❌ | ✅ | ❌ |

> [!warning] `PATCH` 와 멱등성
>  - Patch 는 언뜻 생각했을때 멱등하지만 멱등하지 않은 경우도 있다.
>  예를 들어 다음과 같은 리소스에 대한 이동을 `Patch` 로 정의하는 경우에 두번째 호출에 대해서는 에러가 발생할 수 있다. `{ "op": "move", "from": "/a/b/c", "path": "/a/b/d" }`
>  - [Why PATCH is neither safe nor idempotent?](https://stackoverflow.com/questions/41390997/why-patch-is-neither-safe-nor-idempotent)

> [!warning] `DELETE` 와 멱등성
> - DELETE 는 언뜻 생각했을때 멱등하지 않다.
> - `DELETE http://example.com/account/123` 를 처음 호출하면 정상적으로 - 계정이 삭제되고 `200 OK` 응답이 올태지만 두번 이상 호출한다면 `404 NOT FOUND` 응답이 올것이기 때문이다.
> - 하지만 이는 멱등성을 잘못 이해한 것으로 멱등성은 응답/예외/만료시간 등과 관계없이 결과의 상태가 같다는 것에만 집중한다.
> - 모든 경우에 123 계정이 삭제되었다는 결과는 동일하기 때문에 DELETE 요청은 멱등하다
> - [Is REST DELETE really idempotent?](https://stackoverflow.com/questions/4088350/is-rest-delete-really-idempotent)

### 4. 기타 메서드

`HEAD`/`OPTIONS`/`TRACE`/`CONNECT` 에 대해서도 간단히 정리해보자.

#### 1. `HEAD`

- GET 과 동일하지만 응답 Body를 가지지 않는다.
- 즉 헤더만 응답한다.

#### 2. `OPTIONS`

- 대상 리소스에 대한 통신 가능 옵션(메서드)을 설명
- 주로 CORS의 Preflight 요청에서 사용한다.
- 응답 메시지의 Allow 헤더에 통신 가능한 메서드를 알려준다.

#### 3. `TRACE`

- The `TRACE` method performs a message loop-back test along the path to the target resource.

#### 4. `CONNECT`

- The `CONNECT` method establishes a tunnel to the server identified by the target resource.