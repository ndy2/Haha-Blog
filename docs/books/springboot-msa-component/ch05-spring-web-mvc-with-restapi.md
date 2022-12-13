
이 장에서는 Controller 구현시 활용하는 여러 Spring 의 기능들 을 소개합니다.

컨트롤러 클래스와 메서드에 활용되는 애너테이션
- @Controller
- @RequestMapping
- @PathVariable
- @RequestParam
- @RequestBody
- @ResponseBody

요청/응답 메시지 처리에 활용되는 애너테이션
- @JsonProperty, @JsonSerialize ... 
- JsonSerializer, JsonDeserializer ...

페이징, 정렬 을 다루는 스프링 표준 인터페이스
- Pageable, Slice, Sort ...

등등에 관해서는 스킵하겠습니당.

이 장에서 소개하는 내용중 가장 흥미로운 내용 두가지만 예제를 포함해서 정리하겠습니다.
두가지는
1. 요청 데이터의 검증을 프레젠테이션 레이어에서 진행하는 여러가지 방법
2. 파일 다운로드 기능을 구현하는 두가지 방법
입니다.

## 1. 요청 데이터 유효성 검증

아래에서 다루는 검증은 유효성 검증입니다. 유효성 검증이 수행되는 위치에 대해서 많은 논쟁이 있습니다. 여기서는 Spring Web Mvc 를 사용하여 표현 계층 에서 즉, 비즈니스 레이어를 진입하기 전에 처리하는 방식에 정리해보겠습니다.

#### 1. JSR-303 (a.k.a. javax validation, bean validation)
요청 객체 (DTO) 의 필드에 `javax.validation.constaints` 패키지의 제약사항 애너테이션을 달아서 검증하는 방식입니다.


#### 2. `@InitBinder` 애너테이션과 Spring 의 `Validator` 인터페이스 이용
- DTO 검증을 위한 별도의  `Validator` 를 구현한 검증 클래스를 구현하여 이를 `WebDataBinder` 에 제공하는 방식입니다.
- Spring 의 표준을 따르면서도 JSR-303 으로는 할 수 없는 복잡한 데이터 검증 까지도 가능합니다.
- 하지만 경우에 따라서는 WebDataBinder 에 일일이 추가해 주어야 한다는 것이 번거롭게 느껴질 수도 있습니다.

#### 3. 커스텀 검증기 클래스 구현
- 별도의 클래스를 직접 구현하는 방식입니다.
- 프레임워크에 의존적이지 않고 POJO 로 깔끔하게 유지할 수 있다는 장점이 있습니다.
- 검증 예외를 `Errors` 나 `BindingResult` 와 같은 클래스에 담지 않고 예외를 `throws` 해버리는 로직을 검증기가 포함하게 하여 Spring  의 `ControllerAdvice`, `@ExceptionHandler` 를 쉽게 활용할 수 있습니다.

#### 4. `SelfValidating`
- 추가로 3과 비슷한 아이디어로 톰 홈버그의 `만들면서 배우는 클린 아키텍처` 에서 소개하는 재미있는 아이디어로
[SelfValidating.java](https://github.com/thombergs/buckpal/blob/master/src/main/java/io/reflectoring/buckpal/common/SelfValidating.java) 가 있습니다. [활용 코드](https://github.com/thombergs/buckpal/blob/master/src/main/java/io/reflectoring/buckpal/account/application/port/in/SendMoneyCommand.java)

- 각 요청 dto 가 상속을 통해 validator 필드를 가지고 있으며 생성자의  마지막에 항상 `validateSelf` 를 호출하여 예외가 있다면 터트려 버림으로써 해당 클래스가 말그대로 Self 로 Validate 해 버리도록 하는 방식입니다.

- 생성자의 마지막에  `validateSelf()` 를 빼먹지 않고 직접 호출해야 한다는 단점은 있지만 참 괜찮은 아이디어라고 생각합니다.
 - 기본 구현에서는 각 DTO 에 별도의 validator 가 생성되는데 singleton 을 활용하도록 개선하면 좋을것 같습니다.


--- 

### 2. 파일 다운로드를 구현하는 방법

#### 1. `HttpMessageConverter` 사용
- 그냥 재주껏 `byte[]` 로 변경하여 `ResponseEntity<byte[]>` 애 담아 반환하면 `ByteArrayHttpMessageConverter` 가 처리한다.
- 이때 Content-type 헤더 application/octet-stream 가 추가된다.
- 간단하지만 파일의 크기가 크면 애플리케이션의 메모리 사용량에 문제가 되고 성능에 문제가 생길 수 있다.

```java
public ResponsoeEntity<byte[]> getImage(... ){
	...
	InputStream is = ...
	byte[] bytes = StreamUtils.copyToByteArray(is);
	return new ResponseEntity<>(bytes, HttpStatus.OK);
}
```

#### 2. `HttpServletReponse` 를 사용하여 직접 `OutputStream` 을 다루기

- InputStream 을 한번에 byte[] 로 메모리에 로딩하여 응답하는것 이 아니라 Response 의 OutputStream 을 직접 다루기위해 StreamUtils.copy 메서드를 활용한다.
- 이 메서드는 내부 버퍼를 이용하여 버퍼사이즈 (4096) 만큼씩 copy 를 하기때문에 한번에 올라오는 메모리의 양이 줄어들게 된다.

```java
public void getImage(... , HttpServletResponse response){
	...
	InputStream is = ...
	OutputStream os = response.getOutputStream();
	StreamUtils.copy(is, os);
}
```

#### 3. 근데...
보통 `Resource` 클래스를 많이 활용하는 것 같아 찾아보니 `ResourceHttpMessageConverter` 도 내부에 protected 메서드 `writeContent` 를 통해 응답 메시지를 작성하는데 여기에서도 `StreamUtils.copy` 메서드를 활용하고 있다.

헤더의 처리나 예외처리도 자동으로 해준다.
아무래도 저자분이 위 방식들을 비교, 소개하신 이유는 이런 인사이트를 주기 위해서였던것 같다.









