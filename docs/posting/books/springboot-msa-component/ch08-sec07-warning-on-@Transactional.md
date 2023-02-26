7절의 내용중 정리하고 싶은 내용은 `@Transactional` 애너테이션을 활용 때 주의 사항입니다.

## 1. @Transactional의 우선 순위

`@Transactional` 코드의 `@Target`을 살펴보면 `TYPE`, `METHOD` 로 선언되어 있습니다.

```java title="@Transactional 코드 일부"

pacakge o.s.transaction.annotation

@Target({ElementType.Type, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Inherited
@Documented
public @interface Transactional{
	// 생략
}
```

즉, @Transactional 은 타입 (클래스, 인터페이스)과 메서드에 모두 선언 될 수 있습니다.

```java
@Transactional // (1)
public interface UserService {
	@Transactional // (2)
	void saveUser(User user);
}

@RequiredArgsConstructor
@Transactional //(3)
public class UserServiceImpl extends UserService {

	private final UserRepository userRepository

	@Transactional // (4)
	@Override
	public void saveUser(User user){
		userRepository.save();
	}
}
```

이 코드에 총 몇개의 @Transactional 어노테이션이 관여할까요?

정답은 4개... 지만 높은 확률로 5개입니다.

그 이유는 높은 확률로 JpaRepository 를 활용할탠데 JpaRepository 의 save 메서드에서는 `@Transactional` 이 선언 되어 있기 때문입니다. 그 부분은 @Transactional 의 propagation 속성과 관련이 있는데 지금은 다루지 않겠습니다.

그러면 남은 4개의 @Transactional 애너테이션의 우선순위는 어떨까요? 지금은 4가지 애너테이션이 모두 같은 방식으로 선언되어 있지만 readOnly flag를 준다든가 propagation 속성, timeout 속성을 다르게 주면 어떤 선언이 동작할 까요?

{==정답은 **`(4) -> (3) -> (2) -> (1)`** 입니다.==} 가장 구체적인 선언이 가장 먼저 활용되는 것이니 합리적인 우선순위라고 생각됩니다. 하지만 interface 에 `@Transactional` 을 추가하는 방식은 활용하지 않는 것이 좋습니다. 클래스에 직접 선언되어 있지 않기 때문에 명시적이지 않으며 일부 버전에서는 aop 적용 방식에 따라 인터페이스의 `@Transactional` 애너테이션을 인식하지 못하는 문제가 있다고 합니다.

물론 이런 규칙은 같이 작업하는 팀원들과 통일해서 일관되게 적용하는것이 가장 중요합니다.

## 2. Public 접근 제어자 필수

@Transactional 애너테이션은 기본적으로 Proxy 기반의 aop 로 동작 (`ProxyMode`)하기 때문에 `private`, `protected` 메서드에 선언하면 동작하지 않는다. 물론 메서드 혹은 클래스에 `final` 키워드를 사용해서도 안된다. 

## 3. 프록시 내부 호출 문제

![transaction-internal-call.png](images/transaction-internal-call.png)

`@Transactional` 로직은 Proxy에 적용되어 있기 때문에 같은 클래스 내에서 `@Transational` 이 선언된 메서드를 직접 호출해도 트랜잭션이 적용되지 않는다. 트랜잭션 적용을 위해서는 항상 스프링 빈으로 주입된 객체의 메서드를 호출해야 한다.

이를 해결하는 일반적인 방식은

1. 클래스를 분리한다
	- 두 메서드의 클래스를 분리해 자연스럽게 빈을 주입받아 호출한다.
2. 자기 주입 방식을 한다.
	- 자기 자신을 주입 받는다.
3. 지연 조회를 한다. 
	- ApplicationContext (ObjectProvider) 를 주입받아 사용하는 시점에 빈을 조회해 사용)

정도가 있다.

실무에서는 보통 1번 방식을 활용한다.
