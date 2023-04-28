---
tags: [hussein, web]
title: 제목
author: ndy2
date: 2023-04-28
description: >-
  
---
 
> [!quote] 참고 자료
> * Hussein Nasser - [`『Fundamentals of Backend Engineering』`](https://www.udemy.com/course/fundamentals-of-backend-communications-and-protocols) on Udemy

### 0. 들어가며

이 절에서는 기본적인 `Request-Response` 패턴을 기준으로 `Push`, `Polling`, `Pub/Sub` 등 다양한 Backend Communication 의 Design Patterns 에 대해 정리한다.

후세인이 강의를 하면서도 `Request-Response` 나 `SSE` 등에 대해서 이들을 패턴으로 분류하는것이 조금은 어색하다고 이야기 하긴 했지만 정리하기 좋은 주제라는 생각이 들어 추가했다고 한다.

강의의 주제들 모두 한번씩 들어보고 학습했던 내용들 이지만 이들을 `Backend Communication Design Patterns` 라는 분류로 모아서 생각하지는 못했다. 이런 비슷한 개념을 모아서 가르치고 본인이 이해하는것이 참 마음에 든다. 

### 1. Request-Response

> Classic, Simple and Everywhere

![[req-resp.excalidraw.png]]

> [!example] Where it is used?
> * Web, HTTP, DNS, SSH
> * RPC
> * SQL and Database Protocols
> * APIs(REST/SOAP/GraphQL)

> [!warning] Doesn't work everywhere
> - Notification service
> - Chatting application
> - Very Long requests
> - What if client disconnects?

### 2. Synchronous vs Asynchronous

> Can I do work while waiting? 

기존 글과 많이 중복되어 스킵 - [[blocking-non-blocking-and-sync-async/README]]

### 3. Push

> I want it as soon as possible

![[push.excalidraw.png]]

> [!note] Pros & Cons
> - Pros
>     - Real time
> - Cons
>     - Clients must be online
>     - Clients might not be able to handle
>     - Requires a bidirectional protocol
>     - polling is preferred for light clients

> [!example]
> * WebSocket
> * SSE
> * Used by RabbitMQ

### 4. Short Polling (Polling)

>-  Request is taking a while, I’ll check with you later
>- 약간 OS의 Spin Lock의 일반화된 버전 같은 느낌이다.

![[short-polling.excalidraw.png]]


> [!note] Pros & Cons
> - Pros
>     - Simple
>     - Good for long running requests
>     - Client can disconnect
> - Cons
>     - Too chatty
>     - Network bandwidth
>     - Wasted Backend resources

### 5. Long Polling

> Request is taking long, I’ll check with you later But talk to me only when it's ready

- Short Polling is a good but chatty 
- Meet Long polling (Kafka uses it)

> 기본방식은 polling처럼 무한히 물어보는 것이다.  하지만 차이점이 있다면 일반 polling은 주기적으로 물어본다면, **long polling은 일단 보내고 time out될 때까지 무한정 기다린다는 것이다.** 서버가 만약 "**너 너무 나랑 오래 연결 되있어, 그럼 이만 끊을께"** 하고 답을 보내

![[long-polling.excalidraw.png]]

> [!note] Pros & Cons
> - Pros
>     - Less chatty and backend friendly
>     - Client can still disconnect
>     - 사실상 실시간
> - Cons
>     - 항상 연결이 유지되어 있어야 한다.

### 6. Streaming

> - One Request, a very very long response
> - Hussein 은 이 절에 SSE를 소개하고 SSE를 패턴으로 소개하는것이 애매하다고 말했는데 조금 찾아보니 Streaming을 패턴으로 분류하고 SSE를 Streaming을 이용한 기술로 이해하는 것이 더 맞는것 같다.
> - 하지만 아래 그림과 Pros & Cons 는 SSE를 기준으로 작성하였다.

![[server-sent-event.excalidraw.png]]

> [!note] Pros & Cons
> - Pros
>     - Real time
>     - Compatible with Req/Resp 
> - Cons
>     - Client must be online
>     - Clients might not be able to handle
>     - Polling is preferred for light clients
>     - HTTP/1.1 problem (6 connections)


### 7. Pub/Sub

### 8. Multiplexing & Demultiplexing

### 9. Stateful vs Stateless

### 10. Sidecar Pattern
