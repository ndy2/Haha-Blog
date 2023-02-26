---
tags: [network, layer4, tcp]
title: TCP flow control
author: ndy2
---

@참고 자료)

- Brian Storti - [tcp-flow-control](https://www.brianstorti.com/tcp-flow-control/)
- 널널한 개발자 - https://www.youtube.com/watch?v=K9L9YZhEjC0 - 26분

TCP 의 주요한 특징은연결 지향 프로토콜 이면서 신뢰성있는 프로토콜 이라는 점입니다.

- TCP 의 연결지향은 3-way, 4-way handshake 로 달성됩니다.
- TCP 의 신뢰성은 많은 이유가 있지만 보통 흐름제어 (flow-control), 혼잡제어 (congestion-control) 를 통해 이루어진다고 이야기 됩니다.

이중 흐름 제어 (Flow-Control) 이란 Sender 가 전송하는 데이터의 양을 조절하여 receiver 의 over-flow 를 방지하는 것입니다. 이 문서에서는 바로이 흐름 제어에 대해서 알아보겠습니다.

---

### 흐름제어 (Flow Control) 란?

- 수신측이 송신측보다 데이터 처리 속도가 빠르면 문제없지만, 송신측의 속도가 빠를 경우 문제가 생깁니다.
    
- 수신측에서 제한된 저장 용량을 초과한 이후에 도착하는 데이터는 손실 될 수 있으며, 만약 손실 된다면 불필요하게 응답과 데이터 전송이 송/수신 측 간에 빈번이 발생합니다.
    
- 이러한 위험을 줄이기 위해 송신 측의 데이터 전송량을 수신측에 따라 조절합니다.

### Sliding Window Protocol

- 소켓은 TCP/IP 를 추상화 한 파일입니다.
- 소켓에는 `send()` 와 `recieve()` 라는 두가지 기능이 있으며 각각 버퍼를 통해 관리됩니다.
- node A 에서 node B 로 TCP 통신을 해야한다면 이때 중요한 것은 node B 의 receive 버퍼, 즉, 수신 측의 버퍼입니다.
- sliding window 동작

![[images/sliding-window.png]]

- 먼저 윈도우에 포함되는 모든 패킷을 전송하고, 그 패킷들의 전달이 확인되는대로 이 윈도우를 옆으로 옮김으로써 그 다음 패킷들을 전송합니다.
- 이 방식으로 현재 공중에 떠있는 패킷 수를 항상 sliding window 의 사이즈 보다 작거나 같도록 유지 할 수 있습니다.
- 마지막 송신 바이트 번호 - 마지막 수신 확인 바이트 번호 <= 수신윈도우
	- lastByteSent - LastByteAcked <= rwnd

### 아주아주 중요한것

- tcp 전송에는 항상 ack 응답이 따르는데 이때 항상 수신측의 window size 를 함께 응답합니다.
- Receiver 가 버퍼를 비우는 속도가 Sender 가 segment를 보내는 속도에 너무 느리게 되면 window size 자체를 줄여버리고 아예 0으로 만들어 버릴 수도 있습니다. (zero window in tcp)
- 이 때 송신측은 segment 를 더 전송해도 되는지 판단합니다.
	- `window size > segment size ? send() : wait()`
- wait 이후에는 계속 기다리지 않고 한번씩 수신측에게 윈도우에 여유가 있는지 확인하는 요청을 보냅니다.
