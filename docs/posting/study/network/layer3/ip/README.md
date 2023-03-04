---
tags: [network, layer3]
title: IP
author: ndy2
---
 
 
> [!quote] 참고 자료
> - wikipidia
> 	- [Internet Protocol](https://en.wikipedia.org/wiki/Internet_Protocol)
> 	- [Internet Protocol version 4](https://en.wikipedia.org/wiki/Internet_Protocol_version_4)
> - 널널한 개발자
> 	- [IPv4 주소 체계에 대한 암기사항](https://youtu.be/gOMljj6K2V0)
> - meridianoutpost.com - [Classes of IPv4 Addresses](https://www.meridianoutpost.com/resources/articles/IP-classes.php)

### 1. IP

![[images/encapsulation.png]]

IP <sup>Internet Protocol</sup> 는 네트워크 계층의 통신 프로토콜 입니다. IP 는 패킷 헤더의 IP 주소<sup>IP Address</sup> 를 통해 패킷을 송신 호스트에서 수신 호스트로 전달합니다. 이러한 목적으로 인터넷 프로토콜은 패킷의 구조를 정의하고 이를 캡슐화 하는 방식을 정의합니다. 또한 송/수신 정보를 통해 아래 계층의 데이터 단위인 Datagram 을 레이블링 하는 방법또한 정의합니다. 

---

### 2. IPv4

IP 에는 `IPv4` 와 `IPv6` 두가지 주요 버전이 있습니다. 그중 현재 (2023년) 널리 활용되는 IPv4 에 대해서 알아보겠습니다. 

![[images/ipv4.png]]

IP, IPv4 에 대한 주요 특징은 다음과 같습니다.

- 32bit 주소체계를 사용한다.
	- 최대 2<sup>32</sup>개 = 43억 개 존재 가능
- Connectionless
- 패킷을 분할/병합하는 기능을 수행하기도 한다.
	- 패킷을 분할 하는 작업은 송신 호스트/라우터 에서 발생하며
	- 패킷을 병합 하는 작업은 수신 호스트/라우터 에서 발생합니다.
- 데이터 체크섬은 제공하지 않고, 헤더 체크섬만 제공한다.
	- 라우터는 패킷을 전달 받으면 체크섬을 계산해서 헤더의 체크섬 값과 비교합니다.
	- 일치 하지 않으면 해당 패킷은 버립니다.
	- 데이터 (payload)에 대한 오류검증은 더 위 계층에서 이루어 져야 합니다.
		- TCP,UDP 의 체크섬에서 처리
- Best Effort 원칙에 따라 전송 기능을 제공한다. 
	- 전송 패킷이 수신 호스트에게 100% 도착하는 것을 보장하지 않는다.
	- the network dos *not* provide any guarantee that data is delivered or that delivery meets any quality of service.

---

### 3. Public IP, Private IP 그리고 Loopback IP

![[images/ips.png]]

Public IP (왼쪽) 와 Private IP (오른쪽)

`Public IP` vs `Private IP`

|           | 공인 IP (Public IP a.k.a Global IP) | 사설 IP (Private IP)                  |
| --------- | ----------------------------------- | ------------------------------------- |
| 할당 주체 | ISP (Internet Service Provider)     | 라우터 (공유기)                       |
| 할당 대상 | 개인 또는 회사의 서버(라우터)       | 개인 또는 회사의 기기                 |
| 고유성    | 인터넷 (전 세계)에서 유일한 값      | 하나의 네트워크 안에서 유일           |
| 공개 여부 | 내/외부 접근 가능                   | 외부 접근 불가능                      |
| Routing   | Router 가 처리 함                   | Router 가 기본적으로 라우팅 하지 않음 |

`Private IP` 의 주소 대역

| 클래스  | 사설 IP 주소 대역            | Host Id | Network Id | 사용처            |
| ------- | ---------------------------- | ------- | ---------- | ----------------- |
| Class A | 10.0.0.0 ~ 10.255.255.255    | 24bit   | 8bit       | 초 거대 네트워크  |
| Class B | 172.16.0.0 ~ 172.31.255.255  | 16bit   | 16bit      | 대학교 수준       |
| Class C | 192.16.0.0 ~ 192.168.255.255 | 8bit    | 24bit      | 일반 기업, 공유기 |

```
:exclamation: IPv4 에는 A ~ E 다섯 클래스가 있으며 각각에 대해서 공인 IP, 사설 IP 의 범위가 정해져 있다. 보통 A ~ C 클래스가 인터넷 디바이스의 대부분을 차지 하며 D 와 E 클래스는 특별한 이유로 사용된다.
```

`Loopback IP`

- 자기 자신을 가르키는 특별한 IP 주소.
- IPv4 에서는 보통 127.0.0.1 을 주로 사용한다.
    - 원래는 127.0.0.X 에 해당하는 모든 주소가 루프백이다.
- 도착지가 Loopback IP 라면 IP 는 패킷을 생성해서 더 아래 계층 (Data Link 계층, Physical 계층)으로 보내는 것이 아니라 다시 윗 계층으로 올려보낸다.
