---
tags: [session, spring]
title: Spring Tips 1
date: 2023-03-06
description: >-
  
---

### 오늘의 세션

```preview
https://youtu.be/aUm5WZjh8RA
```

아래 code annotation 으로 표시한 내용들은 모드 Spring 6 에 추가된 내용인 것은 아니지만 눈길이 가는 녀석들 위주로 표시한 것입니다.

### 1. 서비스 애플리케이션

```java title="service"
@RestController
class GreetingHttpController {

    @Autowired
    private ObservationRegistry registry;

   @GetMapping("/greetings/{name}")
   Greeting greet(@PatthVariable String name){
        if(!(StringUtils.hasText(name) && Character.isUpperCase(name.charAt(0)))) {
            throw new IllegalArgumentException("the name must start with a capital letter");
        }

        // (1) !
        return new Observation
            .createNotStarted("greetins.name", this.registry)
            .observe(() -> new Greeting("Hello, " + name + "!"));
        // return new Greeting("Hello, " + name + "!");
   }

}

class ProblemDetailErrorHandlingControllerAdvice {

    // (2) !
    @ExceptionHandler(IllegalArgumentException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ProblemDetail onException(IllegalArgumentException argumentException){
// public ProblemDetail onException(HttpServletRequest request){

        return ProblemDetail
        .forStatusAndDetail(HttpStatusCode.valuOf(404), "the name is invalid");
    }
}

// (3) !
record Greeting(String message){
}


```

1. Spring boot 3 의 ***Observability API*** 이다.
   - 참고자료 [@Baeldung](https://www.baeldung.com/spring-boot-3-observability)
2. Spring boot 3 에 새롭게 추가된 클래스인 [`ProblemDetail`](https://docs.spring.io/spring-framework/docs/6.0.0-M3/javadoc-api/org/springframework/http/ProblemDetail.html) 을 @ExceptionHandling 메서드에서 활용하고 있다.
3. Java 16에 정식 도입된 `record` 를 DTO 로 활용하고 있다.

### 2. Client 애플리케이션

```java title="client"

@Bean
ApplicationListener<ApplicationReadyEvent> ready(GreetinsClient gc) {
    return event -> {
        var response = gc.greet("haha");
        System.out.println("response : " + response);
    }
}

// (1) !
static class GreetingsClientRuntimeHintsRegisterar implements RuntimeHintsRegistrar {

    @Override
    public void registerHints(RuntimeHints hints, ClassLoader classLoader){

        hints.proxies().registerJdkProxy(
            GreetingsClients.class,
            SpringProxy.class,
            Adviced.class,
            DecoratingProxy.class
        )
    }
}

@Bean
@ImportRuntimeHints(GreetingsClientRuntimeHintsRegisterar.class)
@RegisterReflectionForBinding(Greeting.class) 
GreetinsClient greetinsClient(HttpServiceProxyFactory factory){
    return factory.createClient(GreetinsClient.class)
}

// (2) !
@Bean
HttpServiceProxyFactory httpServiceProxyFactory(WebClient.Builder builder){
    var wc = builder.baseUrl("http://localhost:8080")
    return WebClientAdapter
        .createHttpServiceProxyFactory(wc);
}

record Greeting(String message){}
// (3) !
interface GreetingClient {
    @GetExchnage("/greetins/{name}")
    Greeting greeting (@PathVariable String name);
}
```

1. `RestTemplate` 없이 Interface 만으로 요청/응답의 처리를 처리할 수 있다.
