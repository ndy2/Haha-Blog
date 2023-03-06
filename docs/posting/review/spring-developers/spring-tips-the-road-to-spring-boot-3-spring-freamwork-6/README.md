---
tags: []
title: Spring Tips 1
date: 2023-03-06
description: >-
  
---

```preview
https://youtu.be/aUm5WZjh8RA
```

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

### 2. Client

```java title="client"

public class ClientApplication {
    // psvm ...

    @Bean
    ApplicationListener<ApplicationReadyEvent> ready(GreetinsClient gc) {
        return event -> {
            var response = gc.greet("haha");
            System.out.println("response : " + response);
        }
    }

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
}

// (3) !
record Greeting(String message){}

interface GreetingClient {

    @GetExchnage("/greetins/{name}")
    Greeting greeting (@PathVariable String name);
}

```
