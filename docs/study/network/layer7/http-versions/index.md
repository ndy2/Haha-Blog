@참고 자료)

- [모질라 - HTTP의 진화 ](https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP#http2_더_나은_성능을_위한_프로토콜)

HTTP 의 버전별 특징을 정리한 문서입니다.

---
### 1. HTTP/0.9 - 원 라인 프로토콜

HTTP 초기 버전에는 버전 번호가 없었습니다. HTTP/0.9는 이후에 차후 버전과 구별하기 위해 0.9로 불리게 됐습니다. HTTP/0.9는 극히 단순합니다. 요청은 단일 라인으로 구성되며 리소스에 대한 (프로토콜, 서버 그리고 포트는 서버가 연결되고 나면 불필요로 하므로 URL은 아닌) 경로로 가능한 메서드는 `GET`이 유일했습니다.
```http
GET /mypage.html
```

응답 또한 극도로 단순합니다. 오로지 파일 내용 자체로 구성됩니다.
```html
<HTML>
A very simple HTML page
</HTML>
```

헤더도 없고, 응답 코드도 없습니다. 메서드는 `GET` 이 유일했습니다.

---

### 2. HTTP/1.0

HTTP/1.0 부터 조금은 익숙한 형태의 요청과 응답이 이루어 졌습니다.
- HTTP 버전 정보나, 응답 상태 코드 같은 것이 Start-Line 에 추가되었습니다.
- HTTP 헤더 개념이 추가되었습니다.
- HTTP의 Content-Type 헤더 스펙으로 인해 HTML 파일 외 다른 문서를 전송할 수 있게 되었습니다.

```http
GET /mypage.html HTTP/1.0
User-Agent: NCSA_Mosaic/2.0 (Windows 3.1)

200 OK
Date: Tue, 15 Nov 1994 08:12:31 GMT
Server: CERN/3.0 libwww/2.17
Content-Type: text/html
<HTML>
A page with an image
  <IMG SRC="/myimage.gif">
</HTML>
```

---

### 3. HTTP/1.1

- Persistent Connection 스펙 - Connection 을 재사용하는 기능이 추가되었습니다. (keep-alive)
- pipelining 스펙 - 첫 번째 요청에 대한 응답이 완전히 전송되기 이전에 두번째 요청 전송을 가능케 하여, 커뮤니케이션 (네트워크) 레이턴시를 낮췄습니다.
- ETag, Last-Modified 등 - 추가적인 캐시 제어 메커니즘이 도입되었습니다.
- 현재 (2022) 가장 널리 활용되는 HTTP 버전입니다.

---

### 4. HTTP/2 - 더 나은 성능!

- 구글의 자체적인 SPDY (스피디) 프로토콜을 표준으로 채택한 것입니다.
- Binary Framing 계층의 도입으로 다양한 최적화 기술이 추가될 수 있었습니다.
- HTTP/1.1 의 pipelining 은 요청 순서와 응답순서가 동일해야 합니다. 따라서 Application 계층에서의 Head of Line Blocking 문제가 존재하였습니다.
- HTTP/2 는 Multiplexing 을 통해 병렬 요청이 동일한 커넥션 상에서 이루어 질 수 있도록 하였고, 순서를 제거하여 Applicaition 계층의 HOL 문제를 해결하였습니다.
- 허프만 인코딩을 통해 동일한 헤더를 압축 하였습니다.
- Server Push 메커니즘을 추가 하였습니다.

---

### 5. HTTP/3 - HTTP over QUIC

- 구글이 UDP 를 기반으로 만든 새로운 전송계층 프로토콜인 QUIC 를 기반으로 동작합니다.
- SSL 을 기본으로 지원합니다.
- 전송 계층에서의 HOL 문제를 해결하였습니다.
	- QUIC 은 스트림을 전송계층에서 일급시민 (First-class citizen) 으로 도입하여!  
- 클라이언트의 IP 가 변경되는 경우 빠르게 대처 할 수 있도록 고안되었습니다.
	- Connection UUID 라는 개념을 도입하여!
