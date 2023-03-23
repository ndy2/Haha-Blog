---
tags: [network, layer4, tcp]
title: Connection Timeout vs Read Timeout
author: ndy2
date: 2023-03-23
description: >-
  
---
 
 
> [!quote] 참고 자료
> * Aaron's Papa - [Connection Timeout과 Read Timeout 살펴보기](https://alden-kang.tistory.com/20)

![[1.png|Connection Timeout & Read Timeout]]

### Connection Timeout

- TCP 3 Way HandShake 를 통해 TCP 연결이 생성 중 발생하는 Timeout
- 즉, endpoint 간 연결을 위해 필요한 최대 시간


### READ Timeout

- 연결된 endpoint 간에 데이터를 주고 받을 때 소요되는 최대 시간

### Connection Timeout 시간 설정

> [!success] Connection Timeout 시간 설정시 고려해야 될 사항
> * 정상적인 네트워크에서도 언제든지 패킷 유실이 발생할 수 있다.
> * 3 way handshake 의 세가지 요청 - (syn/syn-ack/ack) 케이스를 적절히 고려해야 한다.

> 위 참고글의 작성자 분이 생각하는 적절한 값은 `3초` 

3초 정도면 클라이언트가 패킷 유실을 인지하고 (Syn/Ack) 재전송을 딱 한번 정도 수행 하고 그 이상 문제가 있다면 Timeout 을 발생시키기 좋은 시간이라고 한다.


### Read Timeout 시간 설정

> [!success] Read Timeout 시간 설정시 고려해야 될 사항
> * 서버의 요청 처리시간을 고려해야 한다.
> * 마찬가지로 패킷 유실에 따른 재전송을 고려해야 한다.

> 마찬가지로 위 참고글의 작성자 분이 생각하는 적절한 값은 `1초`

마찬가지로 패킷유실에 따른 한번의 재전송 정도를 허용할 수 있는 값이다. 물론 RTT, 서버의 요청 처리 시간, RTO (유실을 인지하고 재전송에 소요된 시간) 을 복합적으로 고려해야 한다.