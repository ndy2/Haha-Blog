---
tags: [spring, spring-data]
title: exception translation in spring-data
author: ndy2
date: 2023-03-23
description: >-
  
---

 
> [!quote] 참고 자료
> * 토비의 스프링 3.1 Vol1 스프링의 이해와 원리 4장 2절 예외 전환

### 1. Let's Read Javadoc of `@Repository`!

```text title="org.springframework.stereotype.Repository - javadoc"
지정된 클래스가 DDD에서의 "Repository" 임을 명시한다.

팀에 따라 전통적인 Java EE 패턴에서의 DAO 를 의미할 수도 있다.
물론 두 패턴에서 의미하는 영속성 접근에 대한 개념 차이를 잘 이해해야 한다.
 
PersistenceExceptionTranslationPostProcessor 와 함께 사용되는 경우 DataAccessException 으로의 예외 변환을 담당한다. 다른 Stereotype 애너테이션과 마찬가지로 전체적인 애플리케이션 아키텍쳐 내에서의 aspect 로서 동작할 수도 있다.

Spring 2.5 부터 이 애너테이션은 @Component 의 meta annotation 으로 취급되었다.
```

아주 흥미로운 이야기가 많다. 이번 시간에는 세번째 문단에서 소개하는 예외 변환 기능에 대해서 알아보자.

### 2. `PersistenceExceptionTranslationPostProcessor`

* @Repository 가 적용된 클래스에 `PersistenceExceptionTranslationAdvisor` 를적용하는 빈 후처리를 한다.

해당 Advisor 의 advice 인 `PersistenceExceptionTranslationInterceptor` 의 invoke ``메서드

```java
@Override  
@Nullable  
public Object invoke(MethodInvocation mi) throws Throwable {  
   try {  
      return mi.proceed();  
   }  
   catch (RuntimeException ex) {  
      // Let it throw raw if the type of the exception is on the throws clause of the method.  
      if (!this.alwaysTranslate && ReflectionUtils.declaresException(mi.getMethod(), ex.getClass())) {  
         throw ex;  
      }  
      else {  
         PersistenceExceptionTranslator translator = this.persistenceExceptionTranslator;  
         if (translator == null) {  
            Assert.state(this.beanFactory != null,  
                  "Cannot use PersistenceExceptionTranslator autodetection without ListableBeanFactory");  
            translator = detectPersistenceExceptionTranslators(this.beanFactory);  
            this.persistenceExceptionTranslator = translator;  
         }  
         throw DataAccessUtils.translateIfNecessary(ex, translator);  
      }  
   }  
}
```

계속 타고 들어가다 보면 jpa/hibernate 를 사용하는 경우 실질적인 예외 변환이 일어나는 곳을 찾을 수 있다.

```java title="org.springframework.orm.jpa.EntityManagerFactoryUtils.convertJpaAccessExceptionIfPossible"
@Nullable  
public static DataAccessException convertJpaAccessExceptionIfPossible(RuntimeException ex) {  
   // Following the JPA specification, a persistence provider can also  
   // throw these two exceptions, besides PersistenceException.   if (ex instanceof IllegalStateException) {  
      return new InvalidDataAccessApiUsageException(ex.getMessage(), ex);  
   }  
   if (ex instanceof IllegalArgumentException) {  
      return new InvalidDataAccessApiUsageException(ex.getMessage(), ex);  
   }  
  
   // Check for well-known PersistenceException subclasses.  
   if (ex instanceof EntityNotFoundException) {  
      return new JpaObjectRetrievalFailureException((EntityNotFoundException) ex);  
   }  
   if (ex instanceof NoResultException) {  
      return new EmptyResultDataAccessException(ex.getMessage(), 1, ex);  
   }  
   if (ex instanceof NonUniqueResultException) {  
      return new IncorrectResultSizeDataAccessException(ex.getMessage(), 1, ex);  
   }  
   if (ex instanceof QueryTimeoutException) {  
      return new org.springframework.dao.QueryTimeoutException(ex.getMessage(), ex);  
   }  
   if (ex instanceof LockTimeoutException) {  
      return new CannotAcquireLockException(ex.getMessage(), ex);  
   }  
   if (ex instanceof PessimisticLockException) {  
      return new PessimisticLockingFailureException(ex.getMessage(), ex);  
   }  
   if (ex instanceof OptimisticLockException) {  
      return new JpaOptimisticLockingFailureException((OptimisticLockException) ex);  
   }  
   if (ex instanceof EntityExistsException) {  
      return new DataIntegrityViolationException(ex.getMessage(), ex);  
   }  
   if (ex instanceof TransactionRequiredException) {  
      return new InvalidDataAccessApiUsageException(ex.getMessage(), ex);  
   }  
  
   // If we have another kind of PersistenceException, throw it.  
   if (ex instanceof PersistenceException) {  
      return new JpaSystemException(ex);  
   }  
  
   // If we get here, we have an exception that resulted from user code,  
   // rather than the persistence provider, so we return null to indicate   // that translation should not occur.   
   return null;  
}
```

### 3. `DataAccessException` Hierarchy

위 예외 변환 코드를 살펴보면 반환 예외는 모두 `DataAccessException` 의 하위 타입임을 알 수 있다.`DataAccessException` 는 회복 가능성을 기준으로 크게 세가지로 구분된다.

* abstract `TransientDataAccessException` - 재시도 하면 성공 가능성 있음
* abstract `NonTransientDataAccessException` - 재시도 해도 실패함
* non-abstract `RecoverableDataAccessException` - recovery operation 을 포함한 경우 활용하는 예외 
