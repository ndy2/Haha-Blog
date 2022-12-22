@참고 자료)

- 한국기술교육대학교박승철교수 - https://youtu.be/R2dWNQTABcI
- 문동욱(Evan Moon) - https://evan-moon.github.io/2019/11/26/tcp-congestion-control/

TCP 의 주요한 특징은연결 지향 프로토콜 이면서 신뢰성있는 프로토콜 이라는 점입니다.

- TCP 의 연결지향은 3-way, 4-way handshake 로 달성됩니다.
- TCP 의 신뢰성은 많은 이유가 있지만 보통 흐름제어 (flow-control), 혼잡제어 (congestion-control) 를 통해 이루어진다고 이야기 됩니다.

이중 혼잡 제어 (Congestion Control) 란 트래픽 증가로 인해 라우터/스위치 버퍼의 큐잉 지연시간 증가 및 오버플로 발생 상태를 막기위해 혼잡 윈도우 라는 개념을 통해 Sender 가 전송하는 segment의 양을 조절하는 것입니다.  이 문서에서는 바로이 혼잡 제어에 대해서 알아보겠습니다.

---

### 혼잡제어와 흐름제어

- 혼잡제어와 흐름제어는 다른 개념입니다!
- 혼잡제어는 두 노드 간의 link - 라우터, 스위치 가 overflow 하는 것을 방지하는 것입니다.
- 반면 흐름제어는 두 노드 (end-node), 특히 수신측 노드의 receiver 버퍼가 overflow 하는 것을 방지하는 것입니다.

### 네트워크 혼잡을 인식하는 방식

- 심각한 혼잡 - Timeout 발생
	- 전송한 segment 에 대해 지정한 timeout 시간 이내 ack 가 도착하지 않을 시 심각한 혼잡 상태라고 파악합니다.
- 경미한 혼잡 - 중복 ack 발생 (3 duplicated ACKs)
	- 중복 ack 가 발생했다는 것은 송신한 데이터가 유실되어 수신측이 데이터 재 전송을 요청하고 있는 상황입니다.
	- 이때는 경미한 혼잡 상태라고 파악합니다.

### 혼잡 제어의 핵심!

- 세그먼트 전송률 (transmission rate) 를 축소 조정합니다.
- 혼잡 윈도우 (cwnd) 라는 가상의 개념을 통해 너무많은 데이터가 한번에 전송되는것을 제어합니다.
- 혼잡 제어를 위한 TCP 전송률 제어
	- 마지막 송신 바이트 번호 - 마지막 수신 확인 바이트 번호 <= min(수신 윈도우, 혼잡 윈도우)
	- LastByteSent - LastByteAcked <= min (rwnd, cwnd)
- {==혼잡 윈도우란 ack 를 수신하지 않고 보낼 수 있는 세그먼트의 양을 의미합니다.==}

### 혼잡 제어 방식

- 1. Slow Start
	- ACK 수신시 cwnd 를 1 (MSS) 늘립니다.
	- 즉 RTT 마다 cwnd 를 두배씩 (지수적으로) 늘립니다.

- 2. Congestion Avoidance
	- 계속해서 Slow Start 알고리즘을 적용하면 cwnd 가 계속 지수적으로 커지게 됩니다. 
	- 이를 방지하기 위해 특정 임계치가 넘어가는 경우 RTT 마다 cwnd 를 1씩 늘릴 수 있도록 조정해줍니다.
	- 이때 ACK 수신시 cwnd 를 1/cwnd 만큼 늘리면 됩니다.

- 3. Fast Recovery
	- 경미한 혼잡 상황에서 cwnd 를 다시 1로 drop 시키고 slow start 를 적용하는 것은 비합리적입니다.
	- TCP 최신 버전인 TCP Reno 버전에서는 이를 Fast Recovery 방식으로 해결합니다.
	- fast recovery 알고리즘은  3 Ack Duplicated 감지시 임계치를 반으로 줄인 후 RTT 마다 cwnd 를 1씩 늘릴 수 있도록 합니다. 혼잡이 해결되면 cwnd 를 다시 복구하고 Congestion Avoidance 를 시작합니다.

### TCP Taheo 와 Reno
- TCP Taheo 는 Timeout 과 3 duplicated ACKs 발생시 모두 cwnd 를 1로 줄이고 Slow Start 를 시작합니다.
- TCP Reno 는 Timout 시에는 TCP Taheo 와 같이 동작하지만 3 duplicated ACKs 시에는 Fast Recovery 를 적용합니다.


### 추가로...
- 맨 위 참고 자료에 있는 문동욱 님의 글에 따르면 TCP Taheo 와 Reno 모두 현재는 그리 잘 사용되는 방식은 아니라고 한다. 
- 최근에는 과거에 비해 네트워크 대역폭이 훨씬 여유가 있기 때문에 송신측이 혼잡 윈도우를 팍팍 늘려도 덜 문제가 된다고 한다. 최근의 혼잡제어 정책들은 얼마나 빠르고 똑똑하게 혼잡 윈도우의 크기를 조절하고 혼잡 감지를 하는가에 초점이 맞추어져 있다고 한다.
