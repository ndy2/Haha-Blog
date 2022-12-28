
먼저 Spring 4.2 이전에 활용되던 ApplicationEvent 와 ApplicationListener 상속 방식의 Spring Event 처리에 대해 알아보겠습니다.

사용자가 가입을 하면 사용자의 이메일에 쿠폰을 발송하기 위해 별도의 클래스로 구성하고 이벤트로 처리하는 프로세스를 구성해보겠습니다.

---

- 이벤트 클래스 - ApplicationEvent 상속

```java title = "UserCouponEvent"
@Getter
public class UserCouponEvent extends ApplicationEvent {

	private final String email;

	public UserCouponEvent(final Object source, final String email) {
		super(source);
		this.email = email;
	}
}
```
<br>

- 리스너 클래스 - ApplicationListener 상속

```java title = "UserCouponEventListner"
@Slf4j
@Component
public class UserCouponEventListener implements ApplicationListener<UserCouponEvent> {

	@Override
	public void onApplicationEvent(final UserCouponEvent event) {
		log.info("register user email : {}", event.getEmail());
	}
}
```

<br>
- 사용하는 법
```java title = "UserServiceImpl"
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
		eventPublisher.publishEvent(new UserCouponEvent(user, user.email));
	}
}

```

물론 event 를 퍼블리시 하는 책임을 user 자체로 넘기고 또한 ApplicationEventPublisher 를 감싼 도메인 서비스를 구축하는 방식으로 구체적인 기술을 조금 감출 수는 있습니다. 예시 코드에서는 간단히 사용 법 위주로 보아주세요.

---

`ApplicationEventPublisher` 는 `ApplicationContext` 가 상속하는 이벤트 중 하나입니다.
이벤트 퍼블리싱 만들 담당할 것이니 `ApplicationContext` 보단 적절한 인터페이스인 `ApplicationEventPublisher` 만을 주입 받아서 처리하는 것이 더 좋습니다.

심하게는 구닥다리라고도 표현되는 이 방식은 단점이 몇가지 있습니다.

1. 이벤트 클래스와 리스너 클래스가 상속을 이용하여 Spring 에 의존적입니다.
2. 리스너 클래스하나에서 여러 이벤트를 처리 할 수 없습니다.

이는 스프링 4.2 이후 등장한 @EventListener 애너테이션으로 해결할 수 있습니다.