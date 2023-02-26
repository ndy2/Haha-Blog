스프링 4.2 이후 등장한 새로운 이벤트 처리 방법에 따라 아래와 같이 변경될 수 있습니다.

---

- 이벤트 클래스 - POJO 클래스

```java title="UserCouponEvent"
@Getter
public class UserCouponEvent {

	private final String email;

	public UserCouponEvent(final String email) {
		this.email = email;
	}
}
```

<br>
- 리스너 클래스

```java title="UserCouponEventListener"
@Slf4j
@Component
public class UserCouponEventListener {

	@EventListener
	public void onApplicationEvent(final UserCouponEvent event) {
		log.info("register user email : {}", event.getEmail());
	}
}
```

<br>

- 사용하는 법

```java title="UserServiceImpl"
import org.springframework.context.ApplicationEventPublisher;
...

@Service
@RequiredArgsContructor
public class UserServiceImpl implements UserService {

	private final UserRepository userRepository;
	private final ApplicationEventPublisher eventPublisher;

	@Transactional
	@Override
	public void registerUser(UserRegisterRequest request){
	
		...
		userRepository.save(user);
		eventPublisher.publishEvent(new UserCouponEvent(user.email));
	}
}
```

앞선 방식의 단점이 모두 해결되었습니다!

@EventListenr 애너테이션의 JavaDoc 을 읽어 보면 아래와 같은 내용이 있습니다.

```
- 이벤트 처리의 핵심이 되는 애너테이션입니다.
- 이벤트 리스너 클래스 (빈 등록 필요) 에 정의된 메서드에 @EventListner 애너테이션을 추가하고 인자로 처리하고자 하는 이벤트의 타입을 추가하면 그 메서드가 이벤트 리스너로서 동작하게 됩니다.
- 애너테이션의 `classes` 프로퍼티를 통해 여러 이벤트를 동시에 처리 하도록 할 수 있습니다.
	- `javadoc` 에서는 이 방식을 그리 권장하지는 않습니다. 
	- 굳이 필요하다면 상속 계층을 고려하라고 합니다.
```

```
 @EventListener 메서드가 처리할 수 있는 이벤트의 타입은 기존의 `ApplicationEvent` 혹은 임의의 `Object` 모두 가능합니다.
```

```
EventListener 메서드의 호출을 내부적으로 `EventListenerMethodProcessor`에 의해서 이루어 진다. 
```

```
EventListener 메서드가 void 가 아닌 타입의 리턴을 가진다면
대상 메서드의 리턴은 새로운 이벤트로서 동작한다.

리턴 타입이 배열 혹은 컬렉션이라면 각 원소가 새로운 이벤트로서 발행된다.
```

추가로 event 를 비동기 처리할 때 @Async 애너테이션과 함께 사용할 때의 주의점을 이야기 하는데 이는 다음 페이지에서 알아보겠습니다.
