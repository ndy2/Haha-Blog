---
tags: [network]
title: Socket, Port, TCP Connection 용어 정리
author: ndy2
date: 2023-04-27
description: >-
  
---
 
> [!quote] 참고 자료
> * 쉬운코드 - [`『[1부] 프로토콜 표준 스펙에서 정의한 Socket(소켓), Port(포트), TCP connection(연결) 개념』`](https://youtu.be/X73Jl2nsqiE)

### 1. TCP/IP Stack

- 인터넷이 발명되면서 함께 개발된 프로토콜 스택
- IETF 에서 인터넷 표준을 관리 (RFC)
- TCP, UDP, IP ,... 스펙은 RFC 에서 정의

![[tcp-ip-stack.excalidraw.png]]

### 2. Port

- process 와 연결된 data path 혹은 data channel
- port name 을 통해 식별
- 혹은 인터넷 상에서 port 를 식별하기 위한 port (number) 를 의미하기도 한다.

![[network-conn.excalidraw.png]]

- Internet 연결 (`IP`) 는 기본적으로 unreliable 하다.
- 프로세스간의 통신에서는 데이터를 안정적으로 주고받을 수 있는 프로토콜이 필요
- -> ==TCP== 의 등장

### 3. Connection

- 프로세스 간의 안정적이고 논리적인 통신 통로
- Connection을 열고, 데이터를 주고 받고, connection을 닫는다.
    - a.k.a `connection-oriented`

### 4. Socket

- internet address + port number
- 인터넷 상에 존재하는 각 port 를 유니크하게 식별하기 위한 주소
- e.g. `41.199.222.3:80`, `177.41.72.6:3022`

### 5. Connection Identifier

- 한 쌍의 socket 은 connection 을 유니크하게 식별한다.
- 한 쌍의 소켓 
    - = `src-socket` + `dest-socket`
    - = `src-ip + src-port` + `dest-ip + dest-port`
    - e.g.`(41.199.222.3:80, 177.41.72.6:3022)`