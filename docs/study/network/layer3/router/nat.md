---
tags: [network, layer3, router]
title: NAT
author: ndy2
---

### 0. 들어가며

라우터는 경로찾기와 패킷 스위칭이라는 기본적인 역할 외에도

- 보안과 관련된 처리 (방화벽 역할)
- NAT - 네트워크 주소 변환
- 패킷의 단편화 및 재조립

과 같은 역할을 수행합니다.
오늘은 그 중 NAT 에 대해서 알아보겠습니다.

---

### 1. NAT 란?

NAT<sup>Network Address Translation</sup> 은 IP 패킷의 TCP/UDP 포트 숫자와 출발/목적지의 IP 주소 등을 재기록하면서 라우터를 통해 네트워크 트래픽을 주고 받는 기술을 말합니다.

패킷에 변화가 생기기 때문에 IP, TCP/UDP 헤더의 체크섬도 다시 계산되어 재 기록해야 합니다.

NAT 를 이용하는 이유는 대부분 사설 네트워크에 속한 여러 개의 호스트가 하나의 Public IP 를 이용해 네트워크에 접속하기 위해서 입니다.

![[excalidraws/nat.excalidraw.png]]

### 2. 동작 원리

![[images/nat.png]]

- SNAT<sup>Source Network Adress Translation</sup> 
    - 공공 IP 대역으로 나갈 때는 출발지 IP 가 공유기의 Public IP 로 변경됩니다.
- DNAT<sup>Destination Network Adress Translation</sup> 
    - 반대로 사설 IP 대역으로 들어올 때는 목적지 IP가 호스트의 Private IP 로 변경됩니다.

upstream 패킷에 대해서 NAT 는 NAT 테이블에 출발지 사설 IP, 포트, 도착지 공용 IP, 포트 등을 기록해두고 downstream 패킷에 대해서 테이블을 참조해 DNAT 를 적용합니다.