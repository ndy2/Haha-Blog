---
tags: [network, layer2]
title: ARP
author: ndy2
---

### 0. 들어가며 들어가며

ARP<sup>Address Resolution Protocol</sup> 는 개인적으로 전송 계층 이하의 프로토콜 중에 기본 캡슐화와 직접적으로 관련이 깊은 부동의 4탑 `TCP`,`UDP`, `IP`, `Ethernet` 를 제외하면 가장 중요하다고 생각합니다. 오늘은 이 ARP 에 대해서 이해해봅시다!

---

### 0.5 들어가기 전에

ARP 에 관한 자료를 찾아보면 가장 의문스러운 점은 이 녀석은 도대체 어느 계층의 프로토콜인가 하는 점입니다.

![[excalidraws/what-layer-arp-blongs-to.excalidraw.png]]

실제로 다양한 문서에서 ARP 를 Layer 2, 혹은 Layer 3 으로 나타내고 있었습니다. 이에 관해선 마지막에 알아보겠습니다.

### 1. ARP - 주소 결정 프로토콜, ARP 프로세스

ARP<sup>Address Resolution Protocol</sup> 는 같은 ***네트워크 내에서*** 통신을 하기 위해 필요한 MAC 주소를 IP 주소를 이용해서 알아오는 프로토콜입니다.

한 네트워크 내에서 ARP 요청 응답이 처리되는 과정은 아래 그림과 같습니다.

핵심은 요청은 ==Broadcast==, 응답은 ==Unicast==!

`ARP 요청` - Host A 가 Host B 의 Mac 주소를 알고 싶다.

![[arp-req.excalidraw.png]]

`ARP 응답` - Host B 를 제외한 호스트는 요청을 무시한다.

![[arp-resp.excalidraw.png]]

ARP Process 가 적용 될 수 있는 경우는 아래와 같이 다양합니다 . 원리는 같으니 아래 캡쳐를 따라 그림을 상상하며 따라가면 그 과정을 이해 할 수 있습니다! 위 그림은 `CASE-1 - Use ARP to find another hosts's physical address` 과정입니다.

![[images/arp-cases.png]]

### 2. What Layer ARP Belongs To?

관련 Wikipedia 링크 - [여기](https://en.wikipedia.org/wiki/Address_Resolution_Protocol#Layering)

이 [링크](https://www.quora.com/Is-ARP-is-a-layer-3-protocol-If-yes-why-it-is-not-a-layer-2-protocol) 에서는 이에 관한 다양한 의견을 확인 할 수 있습니다. ARP 가 Layer 3 라고 이야기 하는 의견과 Layer 2 라고 이야기 하는 의견 모두 동의 하는 것은 이 프로토콜은 Layer 2 혹은 Layer 3 에 명확하게 규정 내릴 수 없다는 것입니다. 각자 자신의 생각을 들어 어느 계층에 조금더 가까운 것 같다는 의견들입니다.

#### 1. ARP 는 2계층에 더 가깝다!

- ARP 는 `IP` 주소를 이용해 `MAC` 주소를 얻어온다. MAC 주소는 layer 2 의 식별자 이다!
- ARP 의 브로드 캐스트는 `LAN` 이라는 한정된 공간에서 동작한다. 이는 3계층의 주요한 특징인 라우터를 이용한 서로다른 네트워크 간의 데이터 전송에 부합하지 않는다!

#### 2. 아니다. ARP 는 3 계층에 더 가깝다!

- 하지만 ARP 요청,응답 메시지는 IP 를 이용해 이루어 진다!
- ARP 가 MAC 주소를 얻어오는 이유도 모두 IP를 이용한 통신을 하기 위해서이다! 이는 다른 Layer 2 의 프로토콜과는 성격이 많이 다르다. 
    - e.g. ethernet (802.3), wifi (802.11), token ring (802.5)

치열한 논쟁을 먼 발치에서 지켜본 끝에 개인적으로 ARP 는 2.5 계층이지만 따지자면 2계층에 더 가깝다고 결론내리기로 하였습니다. 일번적인 IP 패킷 처럼 라우터에 의해 네트워크간 경로찾기와 포와딩이 이루어지지 않는다 (not-routable)는 점에서 2계층 프로토콜에 더 가깝다고 생각합니다.

> [!quote] 추가로 읽어볼 링크
>  - https://superuser.com/questions/702834/how-does-a-router-find-the-mac-address-of-next-hop-router
