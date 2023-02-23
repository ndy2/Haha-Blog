Spring 을 이루는 핵심 철학 3가지와 POJO 를 의미하는 Spring Triangle 이라는 용어가 있습니다. 각 요소에 궁금하신 분은 [이 링크](https://www.notion.so/ndy-dev/IOC-AOP-PSA-b867f8a62ebb47bca2d1a3d0674effa7) 를 참고해 주세요.

### AOP 개요

![spring-triangle.png](images/spring-triangle.png)

이 절에서는 Spring Triangle 의 한 축을 차지하는 관점 지향 프로그래밍(AOP)에 대해 이야기합니다.

관점은 *여러 클래스에 걸쳐 공통적으로 실행되는 기능을 모듈로 분리한 것*입니다. 관점은 각 클래스의 실제 역할과 분리되는 자신만의 실행 목적을 분명히 가집니다. 관점 지향 프로그래밍의 목적은 {==클래스의 코드가 관점의 코드와 분리되게 하여 의존으로 발생하는 복잡도를 낮추는 것==} 입니다.

중요한 것은 의존입니다. AOP는 단순히 클래스의 분리를 의미하지 않습니다. AOP는 클래스 혹은 메서드로 관점을 분리하고 주 클래스에서 관점을 호출하는 것에 만족하지 않습니다. {==프록시 패턴을 활용하여 주 클래스 에서는 관점에 대해 전혀 알 수 없도록 하는 것이 AOP의 핵심==}입니다. Spring은 동적 프록시 생성을 통한 AOP 를 통해 개발자가 프록시를 직접 생성, 제어하는 수고를 덜어줍니다. 또한 Spring 은 이미 Transaction, Cache 와 같은 다양한 기능에 AOP를 적용하고 있습니다.

![images/aop.png](images/aop.png)

---

### AOP 용어 정리

aop 가 어렵게 느껴지는 이유는 크게 두가지 라고 생각합니다.

1. 관련 용어가 많다.
2. 직접 다룰 일이 드물어 익숙해지기 어렵다.

익숙해지지 않으니 AOP를 직접 설정할 때마다 이전에 작성했던 코드나 관련 예제를 찾아보며 어드바이스와 포인트컷 표현식을 설정하며 제대로 동작하는지 확인 하는 과정에 시간이 오래걸립니다. 2번 문제는 여기서 해결하기는 어려우니 오늘은 1번 문제를 해결해봅시다!

- `Traget Object` 
	- AOP 적용 대상 객체
- Proxy Object
	- 프록시 객체
	- targetObject 를 필드로 가지며 advice 로직을 targetObject의 호출전에 실행해준다고 생각하면 좋다!
	- Spring AOP 는 `o.s.aop.framework.ProxyFactory` 를 이용해 프록시를 생성한다.
		- `ProxyFactory` 는 JDK 동적 프록시와 CGLIB 두가지 기술을 합쳐 놓은 것이다.

- Aspect
	- Advice + PointCut
	- Spring AOP 에서는 `@Aspect` 애너테이션으로 클래스를 선언함으로써 내부의 어드바이스 메서드와 어드바이스 애너테이션 내부의 포인트컷을 함께 표현한다.
	- Note - `@Aspect` 애너테이션과 `@Around`, `@After` 과 같은 어드바이스 애너테이션은 모두 `org.aspect.lang.annotation` 패키지에 포함되어 있다.
	- 즉 `@Aspect` 만 선언한다고 스프링 이 인식할 수 없다 빈을 꼭 직접 등록 해 주어야 한다.

- Advice
	- AOP 를 통해 적용하고자 하는 로직을 작성한 공통 모듈을 의미한다.
	- Spring AOP 에서는 어드바이스 애너테이션을 가지는 메서드로 어드바이스를 표현한다.
	- Spring AOP는 JDK 동적 프록시의 `InvocationHandler` 와 CGLIB 의 `MethodInterceptor` 를 통합한 개념인 `Advice` 를 도입하였고 이를 어드바이스 애너테이션을 이용해 제공한다.
	- Spring 이 지원하는 다섯가지 `Advice` 는 `@Befter`, `@After`, `@AfterReturning`, `@AfterThowing`, `@Around` 이다. 

- PointCut
	- 어드바이스를 적용할 위치를 선정하는 설정을 의미한다.
	- 포인트 컷은 포인트 컷 표현식을 사용하여 설정할 수 있으며, 특정 애너테이션을 지정하여 설정 할 수도 있다.

- JoinPoint 
	- 어드바이스가 적용된 위치를 의미한다.
	- 타겟 클래스의 어드바이스 적용대상 메서드를 의미한다.
	- 포인트컷은 조인포인트를 선정하는 것을 의미한다.
	- Spring AOP 에서는어드바이스 메서드에 `JoinPoint` 나 `ProceedingJoinPoint` 를 인자로 선언하여 활용한다.

- Weaving
	- 조인 포인트에 어드바이스를 끼워 넣는 과정을 의미한다.
	- 런타임에 어드바이스 로직을 호출하는 프록시 객체를 생성하는 의미를 가지기도 한다.