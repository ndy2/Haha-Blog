### 스프링 빈 & 스프링 빈 컨테이너

 - 스프링 빈 컨테이너가 관리하는 순수 자바 객체
 - 빈 컨테이너는 빈 정의 (Bean Definition) 설정을 읽고 빈 객체를 생성한다.
 - 그리고 서로 의존성이 있는 빈 객체들을 주입하는 과정을 거친 후 애플리케이션이 실행 준비 상태가된다.
	- 물론 생성자 주입 방식으로 DI 를 설정한 경우에는 빈 객체 생성시 의존성 주입이 이루어진다.
- 스프링 빈 컨테이너는 빈 스코프 (Bean Scope)에 따라 빈의 생명주기 (Bean Life Cycle) 를 관리하는 역할을 한다.

### Bean LifeCycle

- 스프링 빈의 생명주기는 스프링 빈이 생성되고 소멸될 때까지 거치는 여러 단계의 과정을 의미한다.
- 생성 후, 소멸 전에, 초기화 전후 (빈 후처리)에 개발자가 정의한 콜백 함수를 다양한 방식으로 제공할 수 있다.
	- 빈의 생성과 초기화 시점을 구분한다는 것에 유의하자.

### 콜백 함수를 제공하는 다양한 방법

> 1. InitializingBean, DisposableBean 상속
> 2. @Bean의 initMethod 와 destroyMethod 속성
> **3. @PostContruct 와 @PreDestroy <- 일반적으로 사용**
> 3. 빈 후처리 - BeanPostProcessor 상속

### 애플리케이션 컨텍스트에게 빈 정의를 제공하는 다양한 방법

> 1. 자바 설정 클래스 + @Bean 애너테이션
> 2. 스테레오 타입 애너테이션 (@Component)
> 3. BeanDefinition 을 직접 생성하여 전달
> 4. XML 설정 제공

현재는 99.9%의 상황에서 1, 2 방식만을 사용한 개발이 이루어진다.

### 자바 설정 클래스와 관련된 애너테이션 목록

- @Configuration
	- 자바 설정 클래스를 의미한다.
	- 내부의 @Bean 이 선언된 메서드에 의해 생성된 객체를 싱글톤으로 생성하여 애플리케이션 컨텍스트에 등록한다.
- @Bean
	- 빈을 정의하는 애너테이션이다.
	- 빈의 이름, 생명주기 메서드 등을 제공할 수 있다.
	- 빈의 이름은 기본적으로 메서드의 이름을 따르고 Scope는 Singleton 이다.
		- Scope는 @Scope 애너테이션을 통해 제공한다.
- @ComponentScan
	- 패키지를 기준으로 존재하는 모든 자바 설정 클래스를 스캔할 수 있도록 하는 애너테이션이다.
- @Import
	- 설정클래스를 하나의 그룹으로 묶는 역할을 한다.
	- 일반적으로 @ComponentScan을 많이 사용하기 때문에 잘 사용하지 않는다.

### 스테레오 타입 애너테이션 목록

- @Component - 가장 일반적인 애너테이션
- @Controller 	- Spring MVC 프레임워크에서 사용 - 해당 클래스를 HandlerMapping의 조회 대상으로 등록한다. 
- @Service - DDD의 서비스 역할을 하는 클래스에 사용, 추가적인 기능은 없다.
- @Repository - DDD의 리포지터리 역할을 하는 클래스에 사용 - Spring Data 는 이 클래스에 예외 변환 AOP 기능을 제공한다.

### @Bean Vs @Component

- 등록하고자 하는 빈이 애플리케이션의 설정과 관련된 빈이라면 @Bean 을
- 애플리케이션의 비즈니스 로직과 관련된 빈이라면 스테레오 타입 애너테이션을
사용하는 것이 일반적이다.
- @Component 를 포함한 스테레오타입 애너테이션을 직접 정의해 내부 아키텍처를 구성하는 컴포넌트의 역할과 의도를 명시적으로 드러낼 수 있다. (e.g. @PersistenceAdapter)
