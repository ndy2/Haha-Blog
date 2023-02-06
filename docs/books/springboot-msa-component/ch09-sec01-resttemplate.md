`o.s.web.client.RestTemplate` 클래스를 몇번 사용해보긴 했지만 그때마다 관련 코드를 찾아보고 혹은 intellij의 code assitant 의 도움을 크게 받으면서 코드를 작성했었습니다. 또한 대충 이름만 보고 템플릿 메서드 패턴을 활용한 다는 것은 알았지만 내부 구조가 어떻게 동작하는 지는 알지 못했습니다. 이번 정리를 통해 확실히 정리하겠습니다.

<figure markdown>
  ![my-profile.jpeg](../../images/my-profile.jpeg)
  <figcaption> 렛츠 고! </figcaption>
</figure>

---

### 1. RestTemplate 의 특징

#### 컨버팅 기능
- 자바 객체 -> HTTP 요청 메시지의 바디
- HTTP 응답 메시지 바디 -> 자바 객체
- 컨버터는 확장 가능, 기본적으로 Content-type 에 따라 적절하게 동작

#### HTTP 프로토콜과 일치하는 메서드 이름
- `getForEntity()`, `postForEntity()`, `delete()`, `put()` ...
- 쉽게 사용할 수 있다!
- +) `exchange()`

#### 템플릿 메서드 패턴
- 커넥션 관리나 메시지를 주고받는 저수준 네트워킹 작업은 별도의 클래스 (`ClientHttpRequestFactory`)에 위임한다

#### 인터셉터 기능
- 인터셉터를 통해 메시지를 주고받을 때 기능을 확장 할 수 있다.

#### Thread-safe
- 스프링 빈으로 객체를 생성해 필요한 곳에 주입해서 사용해도 된다.


### 2. RestTemplate 구조
restTemplate 을 구성하는 주요 클래스와 요청 처리흐름은 아래와 같다

![resttemplate.excalidraw.png](excalidraws/resttemplate.excalidraw.png)

`ClientHttpRequestFactory` 는 서버와 클라이언트 사이에 커넥션을 사용해 요청 전송 및 응답 수신 과정을 처리한다. `ClientHttpRequestInterceptor` 는 요청을 날리기 전 가로채서 추가적인 작업을 할 수 있다. 헤더를 추가하는 작업등을 할 수 있다. `RestponseErrorHandler` 는 응답 코드를 보고 예외를 발생시킨다.

### 3. Connection Timeout 과 Read Tieout 설정
ClientHttpRequestFactory 빈을 직접 RestTemplate 에 등록할 때는 connection timeout 과 read timeout 설정이 가장 중요하다.

Connection Timeout
- 서버와 클라이언트가 TCP 3-way handshake를 통해 커넥션을 획득하는 시간에 대한 timeout
- `java.net.ConnectionException: Connection timed out connect`

Read Timeout
- 커넥션이 수립된 이후 api를 요청하고 응답 받을때 까지 걸리는 시간에 대한 timeout
- `java.net.SocketTimeoutException: Read timed out`

timeout 을 찾기위한 정답은 없다. 적당히 설정하고 스카우터나 제니퍼 같은 APM 툴로 모니터링 하는 것이 중요하다. 클라이언트는 timeout 설정을 통해 자신의 리소스를 보호해야 한다.

MSA 에서는 timeout 등으로 인해 발생한 문제가 시스템 전체에 전파될 위험이 있다. 이를 해결하는 것을 fallback 처리라고 한다. MSA 에서는 주로 서킷 브레이커 패턴을 통해 이를 해결하고자 한다.


### 4. keep-alive 와 커넥션 풀

`RestTemplate` 의 기본 설정은 `SimpleClientHttpRequestFactory` 를 사용합니다. 이 클래스는 jdk의 기본 네트워크 라이브러리를 통해 커넥션(`java.net.HttpUrlConnection`)을 맺으며 매 요청마다 커넥션을 수립하고 해제 합니다.

만약 커넥션 풀을 사용하고 싶다면 `HttpComponentsClientHttpRequestFactory` 를 사용해야합니다.
이 구현채는 아파치 httpcomponents 프로젝트의 `HttpClient` 를 활용합니다. 이를 위해서는 꼭 서버가 keep-alive 기능을 지원해야 합니다.

MSA 구조에서 한 클라이언트가 여러 서버에 RestApi를 호출해야 한다면 각기 다른 RestTemplate 빈을 등록해 사용하는 것도 고려해봄직 할 것 같습니다.

참고 - [RestTemplate connection pool 설정하기](https://multifrontgarden.tistory.com/249)