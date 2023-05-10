---
tags: [network]
title: 네트워크 장비
author: ndy2
date: 2023-05-10
description: >-
  
---
  
> [!quote] 참고 자료
> * Practical Networking - [`『Hub, Bridge, Switch, Router - Network Devices - Networking Fundamentals - Lesson 1b』`](https://youtu.be/H7-NR3Q3BeI)

### 1. L1 - 리피터 (Repeater)

- 전기적 신호를 증폭

![[repeater.png]]

### 2. L1 - 허브 (Hub)

- 호스트를 직접 연결하는 것은 scale 하지 않다.
- 허브를 통해 LAN 내의 호스트를 모두 연결 할 수 있다!
- 허브는 간단히 말해서 multi-port 리피터 이다.
- 하지만 허브는 모든 전기적 신호를 Flooding 시킨다.
    - 특정 호스트를 지정하여 전기적 신호를 전달 할 수 없다.
    - Everyone receives everyone else's data!

![[hub.png]]

### 3. L2 - 브릿지 (Bridge)

- 브릿지는 Hub로 연결된 호스트 그룹의 사이에 위치한다.
- 브릿지는 두개의 포트 만을 가진다.
- 브릿지는 각 포트가 가진 호스트를 학습하여 목적지가 아닌 경우 프레임을 차단한다.

![[bridge.png]]

### 4. L2 - 스위치 (Switch)

- 스위치는 여러 포트를 가진다.
- 스위치는 호스트의 그룹이 아니라 각 포트에 지정된 단 하나의 호스트에 대해서 학습한다.
    - 즉, 불필요한 프레임 전송이 없어졌다.
- 스위치는 여러 포트를 가진다는 점에서 허브와 유사하고 학습을 바탕으로 불필요한 신호를 차단한다는 점에서 브릿지와 유사하다. 
    - `L2 Switch ~= Hub + Bridge`
- 스위치는 한 네트워크 내에서의 통신을 가능하게 한다.
    - 네트워크 = Group of hosts which require similar connectivity
    - 네트워크의 호스트 들을 같은 IP 주소 공간을 가진다.

![[switch.png]]

![[switch-lan.png]]

### 5. L3 - 라우터 (Router)

- 네트워크 간의 통신을 담당한다.
- Traffic control point(보안, 필터링, 리디렉션) 을 제공한다.
- 라우터는 네트워크별 라우팅 정보를 IP 주소 기반으로 제공하며 라우팅 테이블을 통해 이를 보관하고 라우팅 프로토콜을 통해 인접한 라우터와 통신하며 학습한다.
- 라우터는 네트워크 내의 Private IP 를 Public IP 로 혹은 그 반대로 전환하는 NAT 를 수행한다.

![[router.png]]

- 라우터는 계층을 이루어 거대한 인터넷을 구성한다.

![[router-internet.png]]


### 6. 게이트웨이 (Gateway)

- 게이트웨이는 각 호스트가 LAN (Local Network) 를 탈출하는 진입/출입 점이다. 대부분의 경우 라우터가 그 역할을 한다.

### 7. 요약

- Router faciliate communication between networks
    - Routing = moving data between networks

- Switch facilitate communication within a network
    - Witch = moving data within a network