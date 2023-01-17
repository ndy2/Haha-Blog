
### 0. 들어가며

ICMP 는 네트워크 계층의 다른 주제들 (IP/IP 주소, 라우터)에 비해서는 중요도가 떨어지는 것 같습니다. 하지만 관련 글들을 읽으면 한번씩 등장하는 빈도가 다른 프로토콜에 비해서는 있어보입니다. 오늘은 이 ICMP 에 대해서 알아보겠습니다.

### 1. ICMP - 인터넷 제어 메시지 프로토콜

- Internet Protocol Sute 즉, TCP/IP 모델을 서포팅 하는 프로토콜 입니다.
- 라우터와 같은 네트워크 장비에서 에러 메시지나, 부가적인 정보를 다른 네트워크 장비와 주고 받기 위해서 사용합니다.
- 예를들어 네트워크 장애로 패킷이 목적지까지 도달하지 못한 경우 라우터는 ICMP 를 통해 출발지에 에러 메시지를 전송합니다.
- ICMP는 시스템 간의 데이터를 주고받기 위해 사용되는 전송계층의 TCP/UDP 와 같은 프로토콜과는 차이가 있습니다.
    - ICMP는 TCP/UDP 헤더를 필요치 않으며 IP 헤더와 IP 데이터 부분에 ICMP 메시지를 포함하여 패킷을 전송합니다.
- 따라서 `ping`, `traceroute` 와 같은 진단 툴을 제외 하면 개발자가 아니라 보통 시스템에 의해 실행됩니다.

!!! note "ICMP (Internet Control Message Protocol)"

    말 그대로 `인터넷 제어 메시지 프로토콜`!

    인터넷 상의 노드간에 에러 사항이나 통신 제어를 위한 메시지를 주고받을 못적으로 만들어진 프로토콜이다!
    
    *recovery X*, *notify O*

### 2. Control Messages

`A general header for ICMPv4`

```kroki-packetdiag
packetdiag {
  fontsize = 20
  colwidth = 32;
  node_height = 20;

  0-7: Type;
  8-15: Code;
  16-31: Checksum;
  32-63: Content [colheight = 3];
}
```

`ICMP 패킷`은 *IPv4 패킷 내에 캡슐화* 됩니다. 즉, ICMP 헤더는 IPv4 헤더 뒤에 작성됩니다. `ICMP 패킷`은 헤더와 데이터 두 파트로 구분됩니다.

- ICMP 의 데이터 파트에는 다양한 정보가 담길 수 있습니다. 에러에 따른 ICMP 메시지에는 에러를 발생시킨 요청의 IP 헤더를 그대로 담습니다.

- 헤더는 8bit `Type` 필드와 8 bit `Code` 필드 둘에대한 `checksum` 필드로 구성됩니다.
    - `type` - 요청의 큰 타입 (송신 불가, 메시지 리디렉션, 시간 초과 에러 등...)
    - `code` - type 별 구체적인 맥락
    - `checksum` - ICMP 헤더 에러를 검증하기 위한 체크섬

