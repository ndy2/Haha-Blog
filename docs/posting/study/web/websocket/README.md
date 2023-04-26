---
tags: [bookmarks]
title: 웹소켓이 뭐나면
date: 2023-02-03
---
 
> [!quote] 참고 자료
> * Hussein Nasser - [`『WebSockets Crash Course - Handshake, Use-cases, Pros & Cons and more』`](https://youtu.be/2Nt-ZrNP22A?list=PLQnljOFTspQUGjfGdg8UvL3D_K9ACL6Qh)
> * 우아한 테크 - [`『[10분 테코톡] ✨ 아론의 웹소켓&스프링』`](https://youtu.be/rvss-_t6gzg)
> * 코딩애플 - [`『오늘의 테크용어 : 웹소켓이 뭐냐면』`](https://youtu.be/yXPCg5eupGM)

### 1. 웹소켓의 등장 배경

> [!quote] 코딩애플 
>  - 전통적인 HTTP 통신은 마치 선톡을 하지 않는 소개팅녀와의 문자메시지와 같다.
> - 소개팅녀가 선톡을 하게 하는 방법 두가지가 등장하였는데 각각 `SSE`<sup>`Server Sent Event`</sup> 와 `Web Socket` 이다.
> - SSE는 라디오와 같다. 양방향 통신이 불가능하다.
> - 반면 Web Socket은 전화와 같다. 양방향 통신이 가능하다.

### 2. 웹소켓 개요 with References

> [!quote] mozilia dev - `『개발자를 위한 웹 기술 > 웹 소켓』`
>  웹 소켓은 사용자의 브라우저와 서버 사이의 ==인터액티브 통신 세션==을 설정할 수 있게 하는 고급 기술입니다. 개발자는 웹 소켓 API를 통해 서버로 메시지를 보내고 서버의 응답을 위해 서버를 폴링하지 않고도 이벤트 중심 응답을 받는 것이 가능합니다.


> [!quote] wikipedia - [`『웹소켓』`](https://ko.wikipedia.org/wiki/웹소켓)
>  `WebSocket`은 하나의 TCP Connection 에 ==full-duplex== 커뮤니테이션을 지원하는 통신 프로토콜이다.
>  
>  `WebSocket` 은 `HTTP`와 다르다. 두 프로토콜 모두 OSI 모델의 응용계층 (layer 7)의 프로토콜이며 전송계층 (layer 4)의 TCP에 의존한다. 두 프로토콜은 다른 프로토콜이지만 "RFC 6455"에 따르면 웹소켓은 HTTP Port 80 과 433 위에 동작하도록 설계되었다. 또한 HTTP 프록시 및 호환을 지원하도록 설계되었다. 호환을 달성하기 위해 웹소켓 핸드셰이크는 HTTP Upgrade 헤더를 사용하여 HTTP 프로토콜에서 웹소켓 프로토콜로 변경한다.

> [!note] 웹소켓의 URI Scheme
> * `ws`(WebSocket) - 암호화되지 않은 연결
> * `wss`(WebSocket Secure) - 암호화된 연결

> [!example] WebSocket use cases
> * Chatting
> * Live Feed
> * Multiplayer gaming
> * Showing client progress/logging

### 3. WebSocket HandShake

```http title="client request"
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
Origin: http://example.com
```

```http title="server response"
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk=
Sec-WebSocket-Protocol: chat
```


### 4. Pros & Cons

Pros
- full-duplex (no polling)
- HTTP compatiable
- Firewall friendly (standard)

Cons
- Proxying is tricky
- L7 L/B chanllenging (timeouts)
- Stateful -> difficult to scale out