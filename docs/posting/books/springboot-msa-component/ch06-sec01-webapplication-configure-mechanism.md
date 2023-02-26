앞서 `@EnableXXX` 애너테이션의 일반적인 활용 방식을 비롯해서 다양한 설정 클래스 활용방식을 살펴보았습니다. 이를 바탕으로 `@EnableWebMvc` 가 어떻게 동작하는지 구체적으로 살펴보겠습니다.

### 1. @EnableWebMvc 와 WebMvcConfigurationSupport

```java title="@EnableWebMvc 애너테이션과 DelegatingWebMvcConfiguration 클래스"

@Import(DelegatingWebMvcConfiguration.class) // (1)
public @interface EnableWebMvc {}

public class DelegatingWebMvcConfiguration extends WebMvcConfigurationSupport { // (2)

	private final webMvcConfiguerComposite configurers 
		= new WebMvcConfigurerComposite; // (3)

	//  생략
}

```

1. `WebMvcConfigurerComposite` 는 `List<WebMvcConfigurer>` 를 가지는 Wrapper 클래스이다. 
2. `WebMvcConfigurationSupport` 는 `DispatcherServlet` 과 같이 동작하는 여러 컴포넌트를 생성하고 설정한다.

`WebMvcConfigurationSupport` 가 설정하는 컴포넌트는 다음과 같다.

- `RequestMappingHandlerMapping` 
- `RequestMappingHandlerAdapter`
- `HttpMessageConverter`
- `HandlerExceptionResolver` 
- ...

사용자가 `WebMvcConfigurer` 를 상속한 클래스를 하나 커스텀 하게 빈으로 등록하면 그 클래스는 `WebMvcConfigurerComposite` 가 가지는 `List<WebMvcConfigurer>` 에 포함되어 `WebMvcConfigurationSupport` 에 의해 그 콜백이 호출되며 설정이 이루어 지게 된다.

### 2. `WebMvcConfigurer`

그럼 이제 `WebMvcConfigurationSupport` 가 호출하는 콜백. 즉, 개발자가 재정의 수 있는 `WebMvcConfigurer` 의 확장포인트 중에 자주 쓸만한 것에 대해서 요약해보겠습니다.

#### `configurePathMatch()`

- 디스패처서블릿이 요청 정보에서 Path 매칭을 하는 방식을 설정합니다.
- 전체 컨트롤러에 일괄적으로 prefix 를 설정하는 기능을 제공합니다. 이를 통해 `"/api/v1"` 과 같은 prefix 를 일괄적으로 제공할 수 있습니다.

#### `addInterceptors()`

인터셉터는 사용자의 요청과 응답을 처리하는 과정에서 추가적인 작업을 할 수 있는 스프링 웹 MVC 의 기능입니다.

#### `addCorsMapping()`

cors 의 의미와 preflight 과정을 포함한 cors 정책의 흐름에 대한부분은 생략하겠습니다.

```java title="addCorsMapping()"
@Override
public void addCorsMappings(CorsRegistry registry){
	registry.addMapping("/**") // (1)
			.allowedOrigins("www.springtour.io") // (2)
			.allowedMethods("GET", "POST", "PUT") // (3)
			.allowedHeaders("*") // (4)
			.maxAge(24 * 60 * 06); // (5)
}
```

1. 모든 리소스에 대해 CORS 를 적용한다.
2. 허용하는 출처는 www.springtour.io 이다.
3. 허용하는 메서드는 GET, POST, PUT 이다.
4. 허용하는 헤더는 전부 `(*)` 이다.
5. CORS 정책의 유효시간은 하루 이다.

#### `addFormatter()`

핸들러 메서드의 `@PathVariable` 나 `@RequestParam` 파라미터을 원하는 객체타입으로 받기 위해 확장할 수 있습니다.

보통 `Converter` 타입과 `Formmater` 타입 두가지를 활용하는데 차이점은 다국어 기능 처리 여부입니다.

#### `addArgumentResolver()`

ArgumentResolver 는 Formatter 보다 훨씬 강력한 기능을 제공합니다. 대상 데이터를 지정하지않고 사용자가 요청한 HTTP 메시지에서 필요한 모든 정보를 조회해 객체로 반환할 수 있습니다.
