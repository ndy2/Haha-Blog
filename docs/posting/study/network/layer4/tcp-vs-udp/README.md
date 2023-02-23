---
tags: [network, layer4, tcp, udp]
title: TCP vs UDP
author: ndy2
date: 2023-02-23
---

@참고 자료)

- 위키피디아 - [전송계층](https://ko.wikipedia.org/wiki/전송_계층)
- GeeksforGeeks - [Differences between TCP and UDP](https://www.geeksforgeeks.org/differences-between-tcp-and-udp/?ref=rp)



전송 계층은 `연결 지향 데이터 스트림 지원`, `신뢰성`, `흐름 제어`, 그리고 `다중화`와 같은 편리한 서비스를 제공합니다.  전송 프로토콜 중 가장 잘 알려진 것은 연결 지향 전속 방식을 사용하는 `TCP` 입니다. 보다 단순한 전송에서 사용되는 `UDP` 도 있습니다.

전송 계층은 

이 문서에서는 둘을 간단히 비교 정리하겠습니다.

---

### TCP vs UDP 간단 비교
  
| Basis       | TCP                                                                                                                     | UDP                                                                                                                                   |
| ----------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 핵심 컨셉   | 연결 지향 프로토콜 <br /> 연결 지향이란 데이터를 주고받기 전과 후에 연결을 수립하고 끊는 과정이 있어야 한다는 것을 의미 | 데이터그램 지향 프로토콜 <br /> 연결을 맺고 유지, 종료하는 것에 대한 오버헤드가 없음 방송과 multicast 타입의 네트워크 전송에 효율적임 |
| 단위        | Segment                                                                                                                 | Datagram                                                                                                                              |
| 신뢰성      | TCP 는 목적지 라우터로의 데이터 전송에 신뢰성을 보장함                                                                  | UDP 는 목적지로의 데이터 전송에 대한 신뢰성을 하지 않음                                                                               |
| 에러 체킹   | TCP 는 흐름 제어와 ack, checksum 을 통해 에러 체킹을 지원함                                                             | UDP 는 Basic 한 checksum 방식의 에러 체킹만을 제공함                                                                                  |
| ack         | Acknowledgment 세그먼트가 있음                                                                                          | Acknowledgment 세그먼트가 없음                                                                                                        |
| sequence    | TCP 에서는 메시지가 보내진 순서를 보장함                                                                                | UDP 에서는 메시지 도착 순서를 예측할 수 없음    필요하다면 application 계층에서 제공해야함                                            |
| 속도        | UDP 보다 느림                                                                                                           | TCP 보다 빠름                                                                                                                         |
| 재전송      | 잃어버린 packet 에 대한 재전송 가능                                                                                     | 재전송 기능 없음                                                                                                                      |
| 크기        | 무거움, 헤더 : 20~60 바이트                                                                                             | 가벼움, 헤더 : 8 바이트 고정                                                                                                          |
| Handshake   | 연결 수립, 종료시 SYNm ACK, SYN-ACK 같은 Handshake 가 일어남                                                            | UDP는 connectionless protocol 임 i.e. No handshake!                                                                                   |
| Protocols   | TCP is used by HTTP, HTTPS, FTP, SMTP …                                                                                 | UDP is used by DNS, DHCP, VoIP                                                                                                        |
| Stream Type | byte stream                                                                                                             | message stream                                                                                                                        |
| Overhead    | UDP 보다 큼                                                                                                             | 낮음                                                                                                                                  |


### TCP 상태 다이어그램
![[images/tcp-state-diagram.png]]

### TCP, UDP 와 관련된 질문들

#### 1. TCP 의 Handshake 에 대해서 설명해주세요

- TCP 는 연결지향형 프로토콜 입니다.
- TCP 는 연결 수립시 3-way handshake, 연결 종료시에는 4-way handshake 가 이루어집니다.
- 이 연결은 물리적 연결과 같은 특별한 의미를 가지는 것은 아니고 그냥 앞으로 TCP 를 통해 요청, 응답을 주고 받을 수 있다는 논리적인 약속같은 의미를 가집니다.
<br>
- 연결 수립시에는 ISN, MSS, Window Size (rwnd, cwnd), 혼잡제어 정책 과 같은 정보를 주고 받습니다.
- handshake 과정에서 body 는 사용하지 않고 header 필드 만을 주고 받습니다.


#### 1-1. 연결 수립시에는 3-Way, 연결 종료시에는 4-Way Handshake 가 발생하는데 왜 그런 차이가 있을까요?
- 연결 수립시 주고 받는 주요 Field 의 정보는 Syn, Syn-Ack, Ack 입니다. Syn 은 Sequence number 를 의미하고 요청, 응답의 ID 처럼 사용됩니다. Ack 은 이전 요청을 잘 받았음을 인정하는 신호입니다. 이전 전달 받은 Syn 필드의 값에 1을 더한 값을 응답합니다.

- 연결 종료시에는 Fin, Ack, Fin, Ack 입니다. 이때 연결 수립시와 달리 서버는 Ack 과 Fin 을 한번에 보내지 않고 사이에 텀을 가집니다. 그 이유는 클라이언트의 연결 종료 요청 (Fin) 을 받은 시점에 서버가 추가적인 정보를 응답할 수 있는 시간을 남겨두는 것입니다.

### 1-2 만약 Server에서 FIN 플래그를 전송하기 전에 전송한 패킷이 Routing 지연이나 패킷 유실로 인한 재전송 등으로 인해 FIN 패킷보다 늦게 도착하는 상황이 발생하면 어떻게 될까요?
- Client 는 서버의 FIN 응답을 받으면 바로 소켓을 닫는 것이 아니라 MSL (Maximum Segment Life) 의 두배 시간동안 Time-Wait 상태를 가진후 소켓을 닫습니다. 그 시간동안 클라이언트는 서버의 추가적인 패킷을 전달 받을 수 있습니다.


#### 1-3 초기 Sequence Number인 ISN을 0부터 시작하지 않고 난수를 생성해서 설정하는 이유?
- ISN 은 Initial Seqence Number 로 Handshake 시에  설정됩니다.
- 이전의 요청으로 오해할 수 있는 가능성이 있기 때문입니다.


#### 2. TCP 가 UDP 보다 빠른 이유가 무엇일까요?

- TCP는 UDP와 달리 연결지향형 프로토콜로 Handshake 에 대한 오버헤드가 있습니다.
	- 자세히 들어가서 TCP 기반에서 연결을 수립할 때에는 3-Way-Hadshake 과정이 필요하며, 여기에 암호화를 위해 TLS까지 적용된다면, 실제 통신이 이루어 지기 이전에 연결 수립만을 위한 지연이 약 4.5 RTT가 발생하게 됩니다.
	![[images/tcp-rtt.png|TCP는 핸드셰이크로 인한 라운드 트립이 발생한다!]]


- TCP는 UDP에 비해 Flow Control, Congestion Control 기능을 이용해 한번에 전송하는 패킷의 양을 조절하기 때문에 느립니다.
	- Flow Control - 수신측의 rwnd 사이즈를 계속해서 전달받으며 수신측의 버퍼가 터지지 않도록 패킷 전송을 조절하는 것입니다. (Sliding window)
	- Congestion Control - Ack 를 받기전에 계속해서 전송할 수 있는 패킷의 양 cwnd 사이즈를 통해 조절하는 것입니다.


### Video Streaming 과 UDP

!!! warn

    Video Streaming 같은 작업은 항상 udp 를 활용한다는 것은 오해입니다.
    
    가장 널리 활용되는 비디오 전송 프로토콜인 HLS (HTTP Live Protocl) 는 TCP 를 활용하도록 설계되었습니다.


> [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)와 [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)는 전송 프로토콜로서 인터넷을 통한 콘텐츠 전송을 담당합니다. TCP는 UDP보다 데이터 전송 신뢰성이 높지만 UDP는 전송 중 일부 데이터가 손실될 수 있지만 전송 속도가 훨씬 빠릅니다.
> 
> UDP가 빠르기 때문에 많은 스트리밍 프로토콜은 TCP 대신 UDP를 사용합니다. 하지만 HLS는 여러 가지 이유로 TCP를 사용합니다.
> 
> - CloudFlare  - [HTTP 라이브 스트리밍이란 무엇입니까? | HLS 스트리밍](https://www.cloudflare.com/ko-kr/learning/video/what-is-http-live-streaming/)

--- 
