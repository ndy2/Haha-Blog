---
title: Http 요청 인가 설정
date: 2023-02-06
---

@ 참고 자료)

-  spring-security reference - [링크](https://docs.spring.io/spring-security/reference/6.0.0-M5/servlet/authorization/authorize-http-requests.html)

### 0. shouldFilterAllDispatcherTypes() 옵션

authorizeHttpRequests 설정을 하며 shouldFilterAllDispatcherTypes flag 를 설정 할 수 있습니다.
이 flag 는 아래 세가지 옵션을 한번에 변경하는 flag 입니다.

![should-filter-all-dispatcher-types.png](images/should-filter-all-dispatcher-types.png)

---

### 1. method chaining

```java title="SecurityFilterChain Bean"

@Bean  
fun filterChain(http: HttpSecurity): SecurityFilterChain {  
    return http  
        .csrf().disable()  
        .httpBasic().disable()  
        .headers().frameOptions().sameOrigin()  
        .and()  
  
        .formLogin()  
        .defaultSuccessUrl("/chat/room")  
        .and()  
        .oauth2ResourceServer().jwt()  
        .and()  
        .and()  
        .authorizeHttpRequests()  
        .requestMatchers("/webjars/**", "/", "/error/**",".ico").permitAll()  
        .requestMatchers("/chat/**").hasRole("USER")  
        .anyRequest().denyAll()  
  
        .and()  
        .build()  
}

```

---

### 2. lambda dsl

```java
@Bean  
fun filterChain(http: HttpSecurity): SecurityFilterChain {  
    return http  
        .csrf().disable()  
        .httpBasic().disable()  
        .headers().frameOptions().sameOrigin()  
        .and()  
  
        .formLogin()  
        .defaultSuccessUrl("/chat/room")  
        .and()  
        .oauth2ResourceServer().jwt()  
        .and()  
        .and()  
        .authorizeHttpRequests {   
            it  
                .requestMatchers("/webjars/**", "/", "/error/**", ".ico").permitAll()  
                .requestMatchers("/chat/**").hasRole("USER")  
                .anyRequest().denyAll()  
        }  
        .build()  
}
```

포맷이 좀 불편하지만 바꿀 수 있고 관련된 것 끼리 Indent 가 잘 맞으니 보기 좋은것 같다.
참고로 `authorizeHttpRequests` 외 모든 설정이 `configurer` 를 인자로 받는 lambda dsl 설정이 가능하다.

---

### 3. bean-based approach 


```java
@Bean  
fun filterChain(  
    http: HttpSecurity,  
    access: AuthorizationManager<RequestAuthorizationContext>  
): SecurityFilterChain {  
    return http  
        .csrf().disable()  
        .httpBasic().disable()  
        .headers().frameOptions().sameOrigin()  
        .and()  
  
        .formLogin()  
        .defaultSuccessUrl("/chat/room")  
        .and()  
        .oauth2ResourceServer().jwt()  
        .and()  
        .and()  
        .authorizeHttpRequests { it.anyRequest().access(access) }  
        .build()  
}

@Bean // 물론 굳이 Bean 으로 관리하지 않고 별도의 클래스로 관리 해도 됩니다.
fun requestMatcherAuthorizationManager(introspector: HandlerMappingIntrospector): AuthorizationManager<RequestAuthorizationContext> {  
    val permitAll = OrRequestMatcher(  
        MvcRequestMatcher(introspector, "/webjars/**"),  
        MvcRequestMatcher(introspector, "/error/**"),  
        MvcRequestMatcher(introspector, "/"),  
        MvcRequestMatcher(introspector, ".ico"),  
    )  // 물론 풀어서 쓸 수도 있습니다.
    val user: RequestMatcher = MvcRequestMatcher(introspector, "/chat/**")  
  
    val manager = RequestMatcherDelegatingAuthorizationManager.builder()  
        .add(permitAll) { _, _ -> AuthorizationDecision(true) }  
        .add(user, AuthorityAuthorizationManager.hasRole("USER"))  
        .build()  
    return AuthorizationManager { a, context -> manager.check(a, context.request) }  
}
```


공식 문서에서 소개하는 방법 중 하나로 설정자 클래스의 access 메서드를 활용하는 방법이 있습니다.

위 처럼 설정을 하게되면 AccessManager 구조는 아래 그림 처럼 설정됩니다.

![accessmanager-tree.excalidraw.png](excalidraws/accessmanager-tree.excalidraw.png)

구조적으로 더 이뻐보이고 뭔가 Spring Security 를 더 잘 활용하는 것 같은 느낌이 들지만 괜히 코드만 복잡해지는 것 같은 느낌도 있습니다. 큰 규모의 프로젝트나 http 요청에 대한 인가 프로세스가 복잡한 경우라면 좋은 방식 같습니다.