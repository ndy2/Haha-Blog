## HTTP Protocol

![[HTTP-Request-Response.png]]

### HTTP 프로토콜의 주요 버전별 주요 특징
HTTP/1.1 (RFC 2616/ 1999.06)
- **keep-alive** 기능 (Connection 헤더)
- **pipelining** 기능을 제공
- Chunk 응답 기능을 제공한다.

HTTP/2.0 (RFC 7540/ 2015.05)
- 구글이 만든 SPDY 프로토콜을 정식으로 채용한것
- 요청과 응답에 **Multiplexing** 기능을 제공.
- **Binray Framing** 적용
- Server Push, Header 압축 등의 최적화 적용

HTTP/3.0 (RFC 9114/ 2022.06)
- UDP 를 기반으로 한 새로운 전송 프로토콜인 QUIC 를 사용
-  Zero RTT, 패킷 손실에 대한 빠른 대응, 사용자 IP가 바뀌어도 연결이 유지
- 기본적으로 TLS 사용
> 😎 각 버전의 특징에 대해 숙지하고 있자!

### HTTP 특징
- **비연결성(Connectionless)** 과 **무상태(Stateless)**
- HTTP/1.1의 keep-alive 스펙으로 비연결성의 단점을 극복
- 쿠키나 세션에 대한 스펙으로 무상태의 단점을 극복!
> 😎 각 특성의 단점과 극복 방식에 대해 숙지하고 있자!


