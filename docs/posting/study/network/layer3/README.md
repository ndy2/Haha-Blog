---
tags: [network, layer3]
title: Network Layer, Internet
author: ndy2
description: 네트워크 계층, 인터넷에 대해서 알아봅시다!
---
  
> [!quote] 참고 자료
> - cloud flare - [학습센터/네트워크 계층](https://www.cloudflare.com/ko-kr/learning/network-layer/what-is-the-network-layer/)
> - 널널한 개발자 
>     - [Host, Switch, Network 이들의 관계에 대해](https://youtu.be/kGst-VftN1w)
>     - [LAN과 WAN을 구별하는 방법](https://youtu.be/N8pE-vDsJ38)
> - ibm - [네트워크 계층 프로토콜](https://www.ibm.com/docs/ko/aix/7.1?topic=protocols-internet-network-level)

### 1. 네트워크 계층이란? 네트워크란? 인터넷 이란?

!!! note "네트워크 계층이란 무엇인가요?"

    [cloudflare] <br>
    네트워크 계층은 OSI 모델에서 계층 3 이며, 상이한 네트워크들 간의 라우팅 및 데이터 전송을 담당합니다.

!!! note "네트워크란 무엇인가요?, 인터넷이란 무엇인가요"

    [cloudflare] <br>
    네트워크는 두 대 이상의 연결된 컴퓨팅 장치의 그룹을 말합니다. 
    
    네트워크에 연결된 컴퓨터는 서로 데이터를 전송할 수 있습니다. **컴퓨터 네트워크**는 마치 서로 알고 정보를 주고받으며 함께 활동하는 **소셜 서클** 과 같습니다.
       
    보통 하나의 네트워크에 있는 모든 장치는 중앙에 있는 하나의 허브 (e.g. 라우터)에 연결된 경우가 많습니다. 네트워크에는 해당 네트워크를 작게 구분한 서브네트워크가 포함되기도 합니다. 
    
    인터넷은 네트워크의 네트워크라고 생각할 수 있습니다. 이러한 인터넷이 동작하는 가장 중요한 두가지 컨셉은 ***패킷*** 과 ***프로토콜***입니다.

!!! note "인터넷이란 무엇인가요?"

    [널널한 개발자] <br>
     인터넷은 가장 대표적인 네트워크의 한 종류입니다.
    인터넷을 구성하는 요소중 가장 중요한것 두가지는 ***라우터***와 ***DNS*** 입니다.
     
    ![host-switch-network.png](images/host-switch-network.png)

!!! note "인터넷이 동작하도록 하는 physical infrastructure에는 어떤것이 있나요?"

    [cloudflare] <br>
    다양한 하드웨어와 infrastructure 가 인터넷을 구성합니다. 가장 중요한 것들은 다음과 같습니다. - 라우터, 스위치, 웹 서버

---

### 2. 라우터란? 스위치란? 웹 서버란?

!!! note "라우터란?"

    [cloudflare] <br>
    라우터는 목적지 (IP 주소)를 기반으로 네트워크간 패킷 포워딩을 수행합니다. 라우터는 인터넷의 트래픽이 올바른 네트워크로 향하도록 하는 교통 경찰 (traffic cop)과 같습니다.
    
    [널널한 개발자] <br>
    라우터는 ***경로 찾기^Routing^***를 목적으로 하는 L3 스위치입니다.

!!! note "호스트란? 엔드포인트란?"

    [널널한 개발자]
    호스트 - 네트워크에 연결된 컴퓨터
    엔드포인드 - 네트워크를 이용하는 호스트
                      - e.g. Peer, Server, Client, Web Server, ...
    스위치 - 네트워크 자체를 이루는 호스트
               - e.g. Router, Firewall, IPS ...

!!! note "스위치란?"

    [cloudflare] <br>
    스위치는 네트워크를 공유하는 기기(device)를 연결합니다. 스위치는 올바른 기기에 패킷을 전달하는 ***패킷 스위칭*** ^Packet^ ^Switching^을 수행합니다. 

!!! note "웹 서버란?"

    [cloudflare] <br>
    웹 서버는 웹 페이지, 이미지, 비디오와 같은 컨텐츠를 저장하고 제공하기 위한 목적의 호스트입니다. 웹 서버는 또한 DNS 쿼리에 응답하는 등의 인터넷이 동작하도록 하는 중요한 역할등을 합니다.

    DNS 에 대해서는 다른 문서에서 추가적으로 이야기 하겠습니다.

---

### 2. 네트워크 계층의 데이터 단위 - 패킷!

!!! note "패킷이란?"

    [cloudflare] <br>
    인터넷을 통해 발송되는 모든 데이터는 패킷이라는 작은 조각으로 나뉘어집니다. 패킷에는 패킷에 대한 메타데이터를 담는 헤더와 데이터 자체를 담은 바디로 두 부분이 있습니다.
    
    네트워크 계층은 패킷을 보낼 때 헤더를 추가하며 (encapsulation) 패킷을 받을 때 헤더를 이용해 패킷 처리 방법 (decapsulation or forwarding)을 이해할 수 있습니다.
    
    헤더에는 각 패킷의 내용, 출발지, 목적지에 대한 정보가 포함됩니다. 예를 들어 IP 헤더에는 각 패킷의 IP 주소, 패킷의 전체 크기, fragmentation 여부, 패킷이 통과한 네트워크 수 (~ TTL) 등이 포함됩니다.

---

### 3. 네트워크 계층의 프로토콜

이 계층에서 주요 프로토콜은 IP^Internet^ ^Protocol^ 와 ICMP^Internet^ ^Control^ ^Message^ ^Protocol^ 입니다. (+ARP ^Address^ ^Resolution^ ^Protocol^)

!!! note "인터넷 프로토콜(IP)란 무엇인가요?"

    [cloudflare] <br>
    인터넷 프로토콜은 패킷의 라우팅과 주소에 대한 프로토콜입니다. IP의 목적은 패킷이 올바른 목적지로 도착하도록 하는 것입니다.
    
    [ibm] <br>
    IP는 인터넷에 대해 신뢰할 수 없는 비연결 패킷 전달을 제공합니다.

!!! note "인터넷 제어 메시지 프로토콜 (ICMP)은 무엇인가요?"

    [ibm] <br>
    ICMP는 오류를 처리하고 IP 메시지를 제어합니다. ICMP는 모든 IP 구현의 필수 부분입니다. 

    ⚠️ ICMP는 통신 환경의 문제점에 관한 피드백을 제공하지만 IP가 신뢰 가능하도록 만들지는 않습니다. 즉, ICMP는 IP 패킷이 확실하게 전달된다거나 IP 패킷이 전달되지 않을 때 또는 올바르지 않게 전달될 때 ICMP 메시지가 소스 호스트로 리턴된다고 보장하지 않습니다.

!!! note "주소 해석 프로토콜(ARP)는 무엇인가요?"

    [ibm] <br>
    ARP는 IP를 MAC으로 동적으로 변환합니다. LAN (근거리 통신망) 내에서 노드는 MAC 을 통해 통신합니다.

!!! note "LAN 과 WAN은 어떻게 구분하나요?"

    [널널한 개발자 - 널피셜] <br>
    LAN(Local Area Network)과 WAN(Wide Area Network)은 지역의 크기로 구분되는 것이 아닙니다. 
    
    LAN <br>
    -  물리적인 영역 (OSI - 1계층, 2계층, TCP/IP - Access 계층)에서 설명되는 영역 <br>
    - 즉, MAC Address 가 중요한 영역 <br>
    - ARP 방송 주소 (ARP Broadcast Address) 트레픽이 도달할 수 있는 영역
    
    WAN <br> 
    - 논리적인(가상의) 영역 (OSI - 3 계층(네트워크 계층), TCP - 인터넷 계층 이상) 에서 설명 되는 영역.
