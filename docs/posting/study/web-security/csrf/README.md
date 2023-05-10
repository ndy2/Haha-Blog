---
tags: [web, security, csrf]
title: 크로스 사이트 요청 위조, CSRF
author: ndy2
date: 2023-05-10
description: >-
  
---
 
 
> [!quote] 참고 자료
> * [`『[화이트해커][웹모의해킹] 24강. 아무도 모르게 비밀번호 변경을? CSRF 공격 개념』`](https://youtu.be/atNmPzdvPD4)

### 1. CSRF 란?

* victim 은 로그인을 한 상태
* 브우저에 저장되는 쿠키가 CSRF 공격의 매개체
* 링크를 위조하여 malicious 한 서버에 위조된 요청을 하는 공격
	* 이를 통해 비밀변호를 변경하거나
	* 계좌이체를 수행하는 등의 악성 요청을 수행할 수 있다.

### 2. CSRF 방어

#### 1. Referrer 검증

* 가장 기초적인 방법이다. Referrer 는 HTTP 헤더로서 요청한 페이지의 정보를 가지고 있다.
* 하지만 이는 프로그램을 이용해 조작이 가능하기 때문에 권장되지 않는다.

#### 2. CSRF 토큰 활용

진짜 사용자가 의도적으로 요청을 한 것인지 확인하기 위해 임의로 생성된 난수를 숨겨진 형태로 포함하여 실제 페이지에서 요청이 발생하는 경우에만 요청을 처리한다.

Java를 사용하신다면 아래와 같은 코드를 사용할 수 있습니다.

```java
//로그인시 session value에 CSRF_TOKEN값 저장
session.setAttribute("CSRF_TOKEN", UUID.randomUUID().toString());
```

```html
<!---요청시 CSRF_TOKEN 값을 전송하도록 해줌---->
<form action="http://example/path" method="POST">
   <input type="hidden" name="CSRF_TOKEN" value="${CSRF_TOKEN}">
 <!-- ... -->
</form>
 
```

```java
// 요청을 받을시, 인터셉터에서 CSRF_TOKEN값 검증하도록 함.
public class CsrfTokenInterceptor implements HandlerInterceptor {
    
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        HttpSession httpSession = request.getSession();
        String csrfTokenParam = request.getParameter("CSRF_TOKEN");
        String csrfTokenSession = (String) httpSession.getAttribute("CSRF_TOKEN");
        if (csrfTokenParam == null || !csrfTokenParam.equals(csrfTokenSession)) {
            response.sendRedirect("/");
            return false;
        }
        return true;
    }
}
```
