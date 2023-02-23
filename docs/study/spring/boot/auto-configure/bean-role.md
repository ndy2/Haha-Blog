---
tags: [spring, spring-boot]
title: 빈 오브젝트의 역할과 구분
date: 2023-02-03
---

@참고 자료)

- 토비의 스프링 부트 - 이해와 원리 on[Inflearn](https://www.inflearn.com/course/토비-스프링부트-이해와원리)
- 토비의 스피링 - Vol2. 1.5.1 빈의 역할과 구분

---

스프링 컨테이너에 올라가는 빈의 종류를 알아보자

### 1. 빈의 역할

- 애플리케이션 로직 빈

	- 애플리케이션 주요 로직을 담고 있는 주요 클래스의 오브젝트
	- e.g.) DAO, Service, Controller 등이 대표적이다.


- 애플리케이션 인프라 빈

	- 애플리케이션이 동작하는데 밀접하게 동작하지만 애플리케이션 로직을 담고 있지는 않은 오브젝트
	- e.g.) DAO 가 사용하는 `DataSource` 오브젝트,  트랜잭션 추상화에 사용되는 `DataSourceTransactionManager`


- 컨테이너 인프라스트럭처 빈

	- 애플리케이션 로직과 관계없이 스프링 켄테이너의 기능에 관여하는 빈
	- ApplicationContext/BeanFactory, Environment
	- BeanPostProcessor, BeanFactoryPostProcessor
	- DefaultAdvisorAutoProxyCreator  - Advisort 타입 빈의 포인트컷 정보를 이용해 타깃 빈을 선정하고 선정된 빈을 프록시로 바꾼다.


### 2. 빈의 역할을 확인하는 법

```java title="org.springframework.beans.factory.config.BeanDefinition"
public interface BeanDefinition extends AttributeAccessor, BeanMetadataElement {

//...

/**  
 * Role hint indicating that a {@code BeanDefinition} is a major part  
 * of the application. Typically corresponds to a user-defined bean. */
 int ROLE_APPLICATION = 0;  
  
/**  
 * Role hint indicating that a {@code BeanDefinition} is a supporting  
 * part of some larger configuration, typically an outer * {@link org.springframework.beans.factory.parsing.ComponentDefinition}.  
 * {@code SUPPORT} beans are considered important enough to be aware  
 * of when looking more closely at a particular * {@link org.springframework.beans.factory.parsing.ComponentDefinition},  
 * but not when looking at the overall configuration of an application. */
 int ROLE_SUPPORT = 1;  
  
/**  
 * Role hint indicating that a {@code BeanDefinition} is providing an  
 * entirely background role and has no relevance to the end-user. This hint is * used when registering beans that are completely part of the internal workings * of a {@link org.springframework.beans.factory.parsing.ComponentDefinition}.  
 */
 int ROLE_INFRASTRUCTURE = 2;

/**  
 * Get the role hint for this {@code BeanDefinition}. The role hint  
 * provides the frameworks as well as tools an indication of * the role and importance of a particular {@code BeanDefinition}.  
 * @see #ROLE_APPLICATION  
 * @see #ROLE_SUPPORT  
 * @see #ROLE_INFRASTRUCTURE  
 */
 int getRole();

//...

} 
```


### 3. Spring Boot 가 빈을 컨테이너에 등록하는 방식

- 애플리케이션 로직 빈 -> `@ComponentScan`
- 애플리케이션 인프라 빈/ 컨테이너 인프라 빈 -> `Auto-Configuration`


