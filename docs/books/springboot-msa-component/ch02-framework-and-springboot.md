
프레임워크란 용도에 맞는 일반적인 기능들을 보편적인 방식으로 제공한다.
> ❗ 면접 단골 질문 중 하나인 Framework/ Library/ API 의 차이도 이해하자!

## 스프링의 의미

스프링은 참 다양한 의미를 가진다.
- Spring (Framework) - 스프링 프레임워크
- Spring (Core Framework) - 스프링 핵심 프레임 워크
- Spring (Application Context, BeanFactory) - IOC 컨테이너

## 스프링과 스프링 부트

[스프링 프로젝트 공식문서](https://spring.io/projects/spring-framework) 의 소개글 첫머리와 그 특징이다.

[Spring Framework](https://spring.io/projects/spring-framework)
> The Spring Framework provides a comprehensive programming and configuration model for modern Java-based enterprise applications - on any kind of deployment platform.

- POJO 기반의 경량 컨테이너 제공
- 복잡한 비즈니스 영역의 문제를 쉽게 개발하고 운영하기 위한 철학 (the Spring Triangle)
- Module 식 프레임워크


[Spring Boot](https://spring.io/projects/spring-boot)
> Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that you can "just run".

-   Create stand-alone Spring applications
-   Embed Tomcat, Jetty or Undertow directly (no need to deploy WAR files)
-   Provide opinionated 'starter' dependencies to simplify your build configuration
-   Automatically configure Spring and 3rd party libraries whenever possible
-   Provide production-ready features such as metrics, health checks, and externalized configuration
-   Absolutely no code generation and no requirement for XML configuration


두 프로젝트에서 개발시 경험하는 스프링의 대부분의 마법같은 일이 일어난다.
IOC, AOP, AutoConfigure, Embedded WAS ...

## 스프링 애플리케이션이 실행되고 애플리케이션 컨텍스트가 준비되는 과정

스프링 애플리케이션은 자바 애플리케이션이므로 `main` 메서드에 의해 시작된다.
Spring Initializer로 프로젝트를 생성하게 되면 `SpringApplication.run` 메서드를 호출하는 코드가 달랑 한줄 있다. `run` 메서드가 의미하는 바를 간단히 정리해보자.

Static 메서드 `run` 은 `SpringApplication` 객체를 생성하고 Instance 메서드 `run` 을 실행한다. 
이때 `SpringApplication` 객체 생성 시 `Main` 클래스 정보가 `Class`  객체의 형태로 전달된다.

### 1. 클래스 정보를 이용하여 실행 준비

SpringApplication 의 생성자는 전달받는 Class 정보를 참고하여 여러가지 필드를 셋업한다.

주요 셋업 필드는 다음과 같다.
- `resourceLoader`
	- `ResourceLoader` 는 `Resource getResource(String location);` 라는 핵심 메서드를 가지는 인터페이스이다.
	- `Resource` 를 애플리케이션으로 로드하기위한 다양한 방법을 추상화한 전략 인터페이스이다.
	- `SpringApplication` 에서의 `ResourceLoader`는 스프링 배너 프린터, `ApplicationContext`  생성시 필요한 다양한 객체의 `ResourceLoader` 필드를 전달하기 위한 용도로 사용되며 
	- 참고로 `ApplicationContext` 자체도 `ResourceLoader` 를 구현하고 있다.
	- 기본적으로 SpringApplciation 의 ResourceLoader 는  null, ApplicationContext 
- `primarySources`
	- 전달 받은 Class 정보를 저장하는 필드이다.
- `webApplicationType`
	- `WebApplicationType.REACTIVE`, `WebApplicationType.NONE`, `WebApplicationType.SERVLET` 중 하나로 추론 된다.
	- `Environment` 의 타입을 결정하기 위해 사용된다.
- `bootstrapRegistryInitializers` 
	- 아직 뭔지 모르겠다.
- `mainApplicationClass`
	- 메인 애플리케이션 클래스를 셋업해둔다. 로깅을 위해서만 활용된다.
	- 셋업 과정에서 더미 런타임 예외를 만들어 스택 트레이스를 순회하며 `main` 메서드를 찾는 방식으로 추론한다.

### 2. 애플리케이션 컨텍스트 생성/초기화를 포함한 실행 과정

셋업이후의 실질적인 `run` 메서드의 흐름은 간단히 아래의 그림과 같다.

![[SpringApplication.run.png]]

역할을 요약하면
- Enviroment 준비
- ApplicationContext 생성 및 초기화
- Runner 실행 
	-  ApplicationRunner, CommandLineRunner 가 있다.
	-  둘은 스프링 컨텍스트의 생성이 완료된 시점에 단한번만 실행 되는 컴포넌트로서 사용된다.
	- CommandLineRunner 는 구닥다리이다. ApplicationRunner 를 사용하자! [참고](https://github.com/ndy2/study-with-code/blob/main/study-spring/application-context/TOBYSPRINGBOOT.md)

등이 있다.

run 메서드는 생성된 ApplicationContext 를 반환하므로 main 메서드에서 이를 받아 추가적인 처리를 해줄 수도 있다.
	e.g.) 애플리케이션 리스너 추가, 이벤트 발행, ...