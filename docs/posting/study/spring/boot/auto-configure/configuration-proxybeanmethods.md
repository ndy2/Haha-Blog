---
tags: [spring, spring-boot]
title: Configuration과 proxyBeanmethods
date: 2023-02-03
---

### @Configuration 의 proxyBeanMethods 엘리먼트와 관련된 부분

```java title="@Configuration 의 proxyBeanMethods 엘리먼트와 관련된 부분"
/*
Configuration classes must be non-final (allowing for subclasses at runtime), unless the proxyBeanMethods flag is set to false in which case no runtime-generated subclass is necessary
*/
@Target(ElementType.TYPE)  
@Retention(RetentionPolicy.RUNTIME)  
@Documented  
@Component  
public @interface Configuration {  
  
  
   /**  
    * Specify whether {@code @Bean} methods should get proxied in order to enforce  
    * bean lifecycle behavior, e.g. to return shared singleton bean instances even    * in case of direct {@code @Bean} method calls in user code. This feature  
    * requires method interception, implemented through a runtime-generated CGLIB    * subclass which comes with limitations such as the configuration class and    * its methods not being allowed to declare {@code final}.  
    * <p>The default is {@code true}, allowing for 'inter-bean references' via direct  
    * method calls within the configuration class as well as for external calls to    * this configuration's {@code @Bean} methods, e.g. from another configuration class.  
    * If this is not needed since each of this particular configuration's {@code @Bean}  
    * methods is self-contained and designed as a plain factory method for container use,    * switch this flag to {@code false} in order to avoid CGLIB subclass processing.  
    * <p>Turning off bean method interception effectively processes {@code @Bean}  
    * methods individually like when declared on non-{@code @Configuration} classes,  
    * a.k.a. "@Bean Lite Mode" (see {@link Bean @Bean's javadoc}). It is therefore  
    * behaviorally equivalent to removing the {@code @Configuration} stereotype.  
    * @since 5.2  
    */   boolean proxyBeanMethods() default true;  

   //...
}
```

### proxyBeanMethods 속성이란?

- @Configuration 클래스는 @Bean 메서드의 싱글턴을 보장하기 위해 프록시를 적용합니다. 
- 하지만 @Configuration 클래스의 @Bean 메서드에서 내부 @Bean 메서드를 호출하는 방식으로 빈 주입을 처리하지 않는다면 이 과정을 불필요합니다. 
- proxyBeanMethods 속성은 이경우 불필요한 proxy 생성을 막는 옵션입니다.
