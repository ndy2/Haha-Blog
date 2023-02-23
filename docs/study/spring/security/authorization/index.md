---
tags: [spring, spring-security, authorization]
title: 인가 프로세스 업데이트
date: 2023-02-06
---

@ 참고 자료)

- spring-security reference - [서블릿 애플리케이션-인가](https://docs.spring.io/spring-security/reference/6.0.0-M5/servlet/authorization/index.html) 
	- 공식 레퍼런스도 아직 업데이트가 완벽하지 않습니다.

---

### 0. 들어가며

사실 기존 방식의 `Spring Security` 인가 처리에 대한 프로세스는 과거 노션에 정리하였던 적이 있습니다. [링크](https://www.notion.so/ndy-dev/Spring-Security-Authorization-Flow-30e3f30b2a74478398ddf9db23052489) 오늘은 Spring Security 5.8 업데이트에 따라 변경된 부분 및 인가 처리 프로세스를 정리하고자 합니다.

관련 깃헙 이슈
	- 1. Deprecated 처리 https://github.com/spring-projects/spring-security/issues/11302
	- 2. guide for migration https://github.com/spring-projects/spring-security/issues/11337

사실 개인적으로 인증 처리는 전부 각각 네이밍이 어쩌고 저쩌고 필터 인 반면 인가처리는 마지막 하나의 필터 그것도 이름이 FilterSecurityInterceptor 라는 점이 마음에 들지 않았었는데 더 일관성 있게 변경 된 것 같아서 좋습니다.

---

### 1. 주요 @Deprecated 된 인가 프로세스 관련 타입들

![[images/legacy-authorization-process.png]]

- `FilterSecurityInterceptor`
	- Use `AuthorizationFilter` instead
- `AccessDecisionManager`  
	- 하위 타입 모두 (e.g. `AffirmativeBased`, `ConsensusBased`, `UnanimousBased`)
	- Use `AuthorizationManager` instead
- `AccessDecisionVoter`
	- 하위 타입 모두
	- Use `AuthorizationManager` instead
	 - i.e. `AuthorizationManager` supersedes both `AccessDecisionManager` and `AccessDecisionVoter`

즉, Authorization Process 자체가 통으로 갈아 엎어 졌다고 볼 수 있습니다. 변경된 인가 처리 프로세스와 관련 아키텍처는 다음 장에 알아보겠습니다!

---

### 2. 주요 @Deprecated 된 인가 설정 방식들

- `HttpSecurity.authorizeRequests` -> `HttpSecurityauthorizeHttpRequests` 
	- 코드내용은 다름
	- 둘다 String 처럼 보이지만 기존의 `antMatchers` 방식은 `AntPathRequestMatcher` 타입의 `RequestMatcher` 를 권한 체크 여부 판단에 활용하고
	- 변경된 방식의 `requestMatchers` 방식은 mvcPresent 여부에 따라 MvcMatcher 라는 타입의 `RequestMatcher` 혹은 기존 처럼 `AntPathRequestMatcher` 를 생성해 주기도 함 만약 둘의 동작 방식이 약간씩 다르므로 테스트 필요함, 혹은 직접 AntPathRequestMatcher 타입의 vararg 를 넘겨주어도 됨

```java
// 변경 전 - authorizeRequests + antMatchers 설정이 일반적
http
	.authorizeRequests()
	.antMatchers("/", "/h2-console/**", "/error", "/**.js", "/**.ico").permitAll()
	.antMatchers(HttpMethod.POST, "/api/users", "/api/users/login").permitAll()


// 변경 후 - authorizeHttpRequests + requestMatchers 설정이 일반적
http
	.authorizeHttpRequests()  
	.requestMatchers("/webjars/**", "/", "/error/**").permitAll()  
	.requestMatchers("/chat/**").hasRole("USER")  
	.anyRequest().denyAll()

//or with lambda dsl
@Bean
SecurityFilterChain web(HttpSecurity http) throws Exception {
	http
		// ...
		.authorizeHttpRequests(authorize -> authorize
			.mvcMatchers("/resources/**", "/signup", "/about").permitAll()
			.mvcMatchers("/admin/**").hasRole("ADMIN")
			.mvcMatchers("/db/**").access("hasRole('ADMIN') and hasRole('DBA')")
			.anyRequest().denyAll()
		);

	return http.build();
}

```


- `HttpSecurity`.`antMatcher`  -> `HttpSecurity.securityMatcher()`

```java
// 변경 전
// The `http.antMatcher` states that this `HttpSecurity` is applicable only to URLs that start with `/api/`.
@Bean
@Order                                                        
public SecurityFilterChain apiFilterChain(HttpSecurity http) throws Exception {
		http
			.antMatcher("/api/**")                                  
			.authorizeHttpRequests(authorize -> authorize
				.anyRequest().hasRole("ADMIN")
			)
			.httpBasic(withDefaults());
		return http.build();
	}

// 변경 후
// The `http.securityMatcher` states that this `HttpSecurity` is applicable only to URLs that start with `/api/`
@Bean
@Order                                                   
public SecurityFilterChain apiFilterChain(HttpSecurity http) throws Exception {
		http
			.securityMatcher("/api/**")                                 
			.authorizeHttpRequests(authorize -> authorize
				.anyRequest().hasRole("ADMIN")
			)
			.httpBasic(withDefaults());
		return http.build();
	}
```


일단 사용하면서 알아차린 변경은 이정도 입니다. 문서를 살펴 더 디테일 하게 조사해보겠습니다!