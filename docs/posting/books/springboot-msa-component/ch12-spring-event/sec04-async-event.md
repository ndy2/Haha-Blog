별도의 처리를 하지 않으면 스프링 이벤트는 이벤트를 발행시킨 쓰레드에서 동기적으로 처리됩니다. @Async 애너테이션을 이벤트 리스너 클래스에 추가하면 스프링은 기본값으로 `SimpleAsyncTaskExecutor` 를 통해서 별도의 쓰레드에서 이벤트 리스너 메서드를 실행합니다.

---

### 1. @Async 애너테이션을 사용할 때 두가지 주의 사항

1. 비동기 이벤트 리스너가 예외를 던진다면 호출자에게 전달되지 않습니다.

	- `비동기` 가 가지는 의미를 생각해보면 당연한 내용입니다.
	- `AsyncUncaughtExceptionHandler` 를 구현하여 커스텀 비동기 예외처리 로직을 구성할 수 있습니다.


2. 비동기 이벤트 리스너의 메서드의 반환값으로 새로운 이벤트를 발행할 수 없습니다.

	- 만약 메서드의 처리 이후 추가적인 이벤트 발행이 필요한 경우 ApplicationEventPublisher 를 통해 수동으로 발행해야 합니다

---
### 2. 설정 방법

- 설정 클래스에 `@EnableAsync` 애너테이션을 꼭 추가해야 합니다.
- 추가적인 설정이 필요없다면 `@SpringBootApplication` 클래스에 추가해도 되지만 가능하면 별도의 `@Configuration` 클래스에서 비동기 처리 관련 설정을 해주는 것이 좋습니다.

<br>
- Aysnc 와 관련된 설정에는 크게 `Executor` 를 빈 등록하는 것과 `AsyncConfigurer` 를 구현하는 방식이 있습니다. 
---
### 3.  `@TransactionalEventListener`

기본적인 @EventListner 에서는 이벤트 처리를 담당하는 쓰레드가 이벤트를 감지하는 즉시 이벤트 리스너 메서드가 동작합니다. `@TransactionalEventListener` 를 사용하면  `@Transactional` 와 연동해서 트랜잭션과 관련된 시점에 정교하게 이벤트 리스너 메서드 실행시점을 조작할 수 있습니다. 

```
TransactionPhase 에 따라 호출 되는 `EventLisner` 임
요 인터페이스를 구현 한 것과 같음 TransactionalApplicationListener
```

TransactionPhase 에 따라 정교하게 이벤트를 적용하고 싶다면 사용할 수 있습니다.

`TransactionPhase`

-   AFTER_COMMIT (기본값) - 트랜잭션이 성공적으로 마무리(commit)됬을 때 이벤트 실행
-   AFTER_ROLLBACK – 트랜잭션이 rollback 됬을 때 이벤트 실행
-   AFTER_COMPLETION – 트랜잭션이 마무리 됬을 때(commit or rollback) 이벤트 실행
-   BEFORE_COMMIT - 트랜잭션의 커밋 전에 이벤트 실행