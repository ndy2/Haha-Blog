---
tags: [web, security, attack, ddos, network, tcp]
title: DDos 와 SYN Flood 공격
author: ndy2
date: 2023-05-14
description: >-
  
---
 
> [!quote] 참고 자료
> * ALEX XU on bytebytego
>     - [`『What is a DDoS (Distributed Denial-of-Service) Attack?』`](https://blog.bytebytego.com/i/91155806/what-is-a-ddos-distributed-denial-of-service-attack) 
> * Hussein Nasser on Youtube
>     * [`『SYN Flood Attack Explained』`](https://youtu.be/tClcCMrXzek)
>     * [`『TCP Half-Open Explained』`](https://youtu.be/SJq61Rhr6N4)

### 1. DDoS 공격

![[ddos-and-syn-fllod.png|What is DDoS - bytebytego]]

DDos 공격의 목적은 비정상 요청으로 대상 서버의 트래픽을 방해하는것입니다. 서버는 비정상 요청을 처리하느라 정상 요청을 처리할 버퍼가 모자라게 됩니다.

- `Step 1` and `Step 2`: 공격자는 Bot/Zombie 네트워크를 컨트롤러를 이용해 원격으로 제어합니다.
- `Step 3` : 좀비는 대상 서버로 요청을 보냅니다. 이는 서버의 리소르를 갉아먹습니다. DDoS 트래픽과 정상 트래픽을 구분하는 것이 어렵습니다.

### 2. Syn Flood 공격

> [!quote] 
>  - RFC 4987 - [`『TCP SYN Flooding Attacks and Common Mitigations』`](https://datatracker.ietf.org/doc/html/rfc4987)
>  - 신기하게도 SYN Flooding 공격은 RFC 에도 정의되어 있다.


Syn Flood 공격은 DDoS의 예시입니다. Bot/Zombie 는 서버에 TCP 커넥션을 위한 SYN 요청을 보내고 서버는 이에대해 `SYN ACK` 을 응답합니다. 이때 클라이언트인 Bot/Zombie 는 HandShake의 마지막 과정으로 `ACK` 을 전송해야하지만 하지 않습니다.

결과적으로 대상 서버는 `half-open TCP connection` 이 남아 리소스가 낭비됩니다.

`ACK` 을 전송하지 않는 방법으로 표현되는 위 그림과 같은 Syn 공격도 있지만 ACK 을 전송하지 않는다는 흉악한 목적을 달성하기 위해 low 레벨에서 패킷 자체를 조작해서 남의 IP 를 src ip 로 바꾸어 전송하는 아래 그림과 같은 방법도 있습니다. (`IP Spoofing`)

![[syn-flood.excalidraw.png]]

### 3. TCP half-open

> [!quote] [`TCP half-open`](https://en.wikipedia.org/wiki/TCP_half-open) on Wikipedia
>  half-open 이란 두 호스트 간에 동기화 되지 않은 커넥션을 의미합니다. 커넥션간의 동기화가 깨지는 이유는 대부분 한쪽이 커넥션 생성 과정에서 crash 하거나 SYN Flood 공격과 같은 악의적인 공격에 의해서 입니다.
>  
>  추가로 커넥션이 맺어지는 과정에서의 커넥션을 embroynic connection (배아 커넥션) 이라고도 부르며 half-open connection 은 이 중 하나입니다.

### 4. Syn flood 공격의 방어

RFC 문서에서는 Syn Flood 공격에 대한 일반적인 방어 방법을 여러가지 소개합니다. 각각의 글이 매우 짧은 편이니 관심가는 방어 방법을 읽어보아도 좋을거 같습니다. 이 글에서는 제가 눈길이 가는 몇몇 방법에 대해서만 정리 (RFC 문서 그냥 번역...) 해보겠습니다.

1.  Filtering
2.  Increasing backlog
3.  Reducing SYN-RECEIVED timer
4.  Recycling the oldest half-open TCP
5.  SYN cache
6.  SYN cookies
7.  Hybrid approaches
8.  Firewalls and proxies

#### 1. Flitering

공격자의 IP 주소를 통해 패킷을 필터링하는 방법입니다. 단순하고 TCP에 변경이 필요없기 때문에 효율적입니다. 반면 공격자가 여러 IP 를 통해 분산하거나 빠르게 변경하며 공격을 하는 경우 filtering 은 별 소용이 없습니다.

#### 2. SYN-RECEIVED 타이머를 줄이기

![[syn-received-timer.png|TCP 3way handshake를 Host B 의 입장에서 살펴보기]]

또 다른 간단하지만 별로 좋지 않은 해결 방법은 SYN-RECEIVED 타이머를 줄이는 것입니다. SYN 을 받은 호스트는 SYN-RECEIVED 상태의 TCB을 생성하고 SYN Backlog에 저장합니다. Timeout 시간동안 ACK 이 돌아오지 않으면 이를 부셔버립니다. 그럼 이 TCB가 half-open 커넥션으로 인해 낭비되는 리소스라는 뜻인데 그 타임아웃을 줄여버리면 syn-flood 공격에 대한 영향을 최소화 할 수 있습니다.

하지만... 이는 정상 요청에 대해서도 커넥션 수립을 정상적으로 처리하지 못할 가능성도 있고 공격자가 단순히 공격 요청의 주기를 조절하는것 만으로 효용이 없어질 수 있습니다. 

### 3. Syn Cookie

 
> [!quote] 참고 자료
> * [SYN cookies](https://en.wikipedia.org/wiki/SYN_cookies) on wikipedia

SYN cookie 기능은 SYN backlog 가 꽉찬경우에 동작하며 원래라면 램덤한 값으로 생성되는 ISN 값에 추가적인 의미를 부여하여 ACK 가 오지 않는 경우 커넥션을 half-open 상태로도 생성하지 않고 아예 만들지 않는 것을 의미합니다.
