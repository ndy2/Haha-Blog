---
tags: [network, layer7, http]
title: HTTPS
author: ndy2
---
 
> [!quote] 참고 자료
> - 생활 코딩 - [HTTPS와 SSL 인증서](https://opentutorials.org/course/228/4894)
> - Alysa Chan - [TCP and TLS handshake](https://medium.com/@alysachan830/tcp-and-tls-handshake-what-happens-from-typing-in-a-url-to-displaying-a-website-part-2-243862438cd9)
> - `RFC 2818` - HTTP Over TLS [링크](https://web.archive.org/web/20050607073343/http://www.ietf.org/rfc/rfc2818.txt)
> - `RFC 5246` - TLS [링크](https://datatracker.ietf.org/doc/html/rfc5246)

> [!note]
> - HTTPS 란 channel-oriented security 를 제공하기 위해 고안된 TLS [RFC 2246] 를 HTTP 위에 얹어서 사용하는 것이다.
> - TLS protocol의 목적은 두 커뮤니케이션하는 애플리케이션의 privacy와 data integrity를 보장하는 것이다.

이 문서에서는 TLS 의 `privacy` 를 위한 하위 프로토콜인 핸드세이크 프로토콜에 대해 자세히 알아보겠습니다.

---

### 1. HTTP Over TLS

개념적으로 HTTP/TLS는 매우 간단합니다. TCP위에 HTTP를 얹듣이 HTTP위에 TLS를 얹으면 된다.

### 2. TLS 의 두가지 핵심 프로토콜

- 레코드 프로토콜
	- `data integrity`
	- 전송될 메시지의 형식을 결정합니다. (압축, 파편화, 암호화)
- 핸드세이크 프로토콜
	- `privacy`
	- 키 교환/ 합의 프로토콜
	- 클라이언트와 서버간의 안전한 대칭키 공유를 목적으로 합니다.

### 3. TLS Handshake Protocol

- Note - TLS handshake 는 TCP handshake 이후에 이루어 집니다.
![[images/tls-handshake.png]]

핸드세이크의 핵심은 암복호화 과정의 코스트가 큰 비대칭키의 사용을 최소한으로 사용하여 안전하게 대칭키를 공유해 일반적인 HTTP 요청시에는 비대칭키가 아닌 대칭키를 활용하는 것입니다.

#### 1. ClientHello

- `클라이언트 측에서 생성한 램덤 데이터`
- 클라이언트가 지원하는 암호화 방식들
- 세션 id - 이미 ssl 핸드 쉐이킹을 했다면 기존의 세션을 활용한다

#### 2. Server Hello

- `서버 측에서 생성한 램덤 데이터`
- 서버가 선택한 클라이언트의 암호화 방식
    - 암호화 방식에 대한 협상 종료
- `인증서` 
	- 서버의 공개키를 포함한다
	- 서버가 생성한 공개키를 CA 의 비밀키로 암호화 한 것이다.

#### 3. Pre-Master Key 교환

클라이언트는 서버의 `인증서` 가 CA 에 의해 발급된 것인지 확인, 브라우저에 내장된 CA 목록을 확인

→ 없다면 경고 메시지

→ 확인하기 위해서 CA 의 공개키를 이용해 복호화한다.

클라이언트는 `서버 측에서 생성한 램덤 데이터` 와 `클라이언트 측에서 생성한 램덤 데이터` 를 조합해서 pre master secret 이라는 키를 생성한다. 이 키는 이후의 세션 단계에서 데이터를 주고 받을 때 암호화 하기 위해서 사용될 것이다. 이 때 사용할 암호화 기법은 대칭키이기 때문에 pre master secret 값은 제 3자에게 절대로 노출 되어서는 안된다.

문제는 pre master secret 을 서버에게 전달하는 것이다.

서버의 공개키로 pre master secret 값을 암호화해서 서버로 전송하면 서버는 자신의 비공개키로 안전하게 복호화 할 수 있다.

#### 4. 서버

서버는 클라이언트가 보내온 공개키로 암호화된 pre master secret 을 자신의 비공개키로 복호화 한다.

이로서 서버와 클라이언트가 모두 pre master secret 값을 공유하게 되었다.

일련의 과정을 통해 mastert secret 을 생성한다.
