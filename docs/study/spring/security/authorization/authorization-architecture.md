---
tags: [spring, spring-security, authorization]
title: Authorization Architecture
date: 2023-02-06
---

@ 참고 자료)

- spring-security reference - [Authorization Architecture](https://docs.spring.io/spring-security/reference/6.0.0-M5/servlet/authorization/architecture.html)
---

### 1. 공식문서 뿌시기

#### Authorities

[`Authentication`](https://docs.spring.io/spring-security/reference/6.0.0-M5/servlet/authentication/architecture.html#servlet-authentication-authentication) 에서는 어떻게 모든 `Authentication` 타입의 구현체가 `GrantedAuthority` 목록을 저장하는지 알아보았습니다. `GrantedAuthority` 객체는 `AuthenticationManager` 에 의해 `Authentication` 에 추가되며 추후에 `AccessDecisionManager` 는 이를 확인하고 통해 권한 결정을 내립니다.


GrantedAuthority 인터페이스는 하나의 메서드만을 가집니다.

```java
String getAuthority();
```

#### The AuthorizationManager

- `AuthorizationManager` 는 `AccessDecisionManager` 와 `AccessDecisionVoter` 를 모두 대체합니다.
- `AuthorizationManager`  는 AuthorizationFilter 에 의해 사용되며 최종적인 접근 제어 결정에 대한 책임을 가집니다.

- `AuthorizationManager` 인터페이스는 두가지 메서드를 가집니다.

```java
AuthorizationDecision check(Supplier<Authentication> authentication, T secureObject);

default AuthorizationDecision verify(Supplier<Authentication> authentication, T secureObject)
        throws AccessDeniedException {
    // ...
}
```


- `check` 메서드의  secureObject 는 인가 결정을 내리기 위해 필요한 모든 관련된 정보를 의미합니다. 
- `check` 결과 
	- `ACCESS_GRANTED` ->  positive `AuthorizationDecision` 반환
	- `ACCESS_ABSTAIN`  ->  null
	- `ACCESS_DENIED`    -> negative `AuthorizationDecision` 반환


- `verify` 메서드는 `check` 를 호출하고 `ACCESS_DENIED` 인 경우 `AccessDeniedException` 예외를 던집니다.

---

다음 장에서는 권한 설정을 하는 다양한 방식에 대해서 알아보겠습니다.