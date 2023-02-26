---
tags: [spring, web-socket, auto-configure]
title: 웹 소켓 자동 설정
date: 2023-02-03
---

### 의존성

`implementation("org.springframework.boot:spring-boot-starter-websocket")`

### 0. 자동 설정 뿌시기

```kotlin
@Bean  
fun run(report: ConditionEvaluationReport) = ApplicationRunner {  
    val count = report.conditionAndOutcomesBySource.entries  
        .filter { condition -> condition.value.isFullMatch }  
        .filter { condition -> condition.key.contains("websocket") }  
        .map { condition ->  
            println(condition.key)  
            condition.value.forEach { println("\t${it.outcome}") }  
            println()  
            condition  
        }  
        .count()  
    println("자동 등록된 빈은 총 $count 개!")  
}
```

```text title="s"
2023-02-03T17:14:16.251+09:00  INFO 9265 --- [           main] com.example.demo.DemoApplicationKt       : Started DemoApplicationKt in 1.035 seconds (process running for 1.18)
org.springframework.boot.autoconfigure.websocket.servlet.WebSocketMessagingAutoConfiguration
	@ConditionalOnClass found required class 'org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer'
	found 'session' scope

org.springframework.boot.autoconfigure.websocket.servlet.WebSocketServletAutoConfiguration
	@ConditionalOnClass found required classes 'jakarta.servlet.Servlet', 'jakarta.websocket.server.ServerContainer'
	found 'session' scope

org.springframework.boot.autoconfigure.websocket.servlet.WebSocketServletAutoConfiguration$TomcatWebSocketConfiguration
	@ConditionalOnClass found required classes 'org.apache.catalina.startup.Tomcat', 'org.apache.tomcat.websocket.server.WsSci'

org.springframework.boot.autoconfigure.websocket.servlet.WebSocketServletAutoConfiguration$TomcatWebSocketConfiguration#websocketServletWebServerCustomizer
	@ConditionalOnMissingBean (names: websocketServletWebServerCustomizer; SearchStrategy: all) did not find any beans

자동 등록된 빈은 총 4 개!
```

### 1. @EnableWebSocket, @EnableWebSocketMessageBroker

#### 1. @EnableWebSocket

사용 간단 프로젝트 - [링크](https://github.com/ndy2/study-webrtc-and-websocket/tree/aa92d61f92faf8bd76cc9fe720c86463509939f1)

![[excalidraws/auto-configure-1.excalidraw.png|400]]

#### 2. @EnableWebSocketMessageBroker

사용 간단 프로젝트 - [링크](https://github.com/ndy2/study-webrtc-and-websocket/tree/fae9f20b84571701ff9134a0dfce5c6a87982f08) 

- `WebSocket-based` 메시징을 위한 자동 설정 클래스이다.
- 하지만 이 설정 클래스는 기본적으로 아무 빈도 등록하지 않는다.
- `WebSocketMessagingAutoConfiguration` 의 내부 static class 인 `WebSocketMessageConverterConfiguration` 의 `Conditional` 중 `DelegatingWebSocketMessageBrokerConfiguration` 이 빈이 필요하다는 조건이 있는데 얘가 없기 때문이다. 
- DelegatingWebSocketMessageBrokerConfiguration 는 `@EnableWebSocketMessageBroker` 를 등록하면 @Import 되고 이때 `WebSocketMessageConverterConfiguration` 이 동작한다.

`WebSocketMessageConverterConfiguration` 는 

- StringMessageConverter
- ByteArrayMessageConverter
- MappingJackson2MessageConverter   

세가지 메시지 컨버터를 등록한다.

![[excalidraws/auto-configure-2.excalidraw.png]]

---

### 2. WebSocketServletAutoConfiguration

웹 소켓 자동 설정에는 

- 서블릿 웹 소켓 설정
- 리액티브 웹 소켓 설정이 있다.

기본적으로 `Tomcat` 컨디션이 충족되기 때문에 `TomcatWebSocketConfiguration` 설정 클래스가 동작한다.

이 클래스는 `TomcatWebSocketServletWebServerCustomizer` 빈을 등록한다.

```java title="WebSocketServletAutoConfiguration 의 static class TomcatWebSocketConfiguration"

@Configuration(proxyBeanMethods = false)  
@ConditionalOnClass({ Tomcat.class, WsSci.class })  
static class TomcatWebSocketConfiguration {  
  
   @Bean  
   @ConditionalOnMissingBean(name = "websocketServletWebServerCustomizer")  
   TomcatWebSocketServletWebServerCustomizer websocketServletWebServerCustomizer() {  
      return new TomcatWebSocketServletWebServerCustomizer();  
   }  
  
}
```

TomcatWebSocketServletWebServerCustomizer 는 TomcatServletWebServerFactory 에 WebSocket 설정을 커스텀 하는 역할을 한다. `WsSci` 라는 녀석을 `TomcatContextCustomizer` 를 이용해 추가한다.
