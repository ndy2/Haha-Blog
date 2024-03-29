---
tags: [java, nio]
title: Java 4에 추가된 NIO (New I/O) 에 대해 알아보자
author: ndy2
---
 
> [!quote] 참고 자료
> * sightstudio - https://sightstudio.tistory.com/15
> * Jakob Jenkov - https://jenkov.com/tutorials/java-nio/index.html
> * enics - http://eincs.com/2009/08/java-nio-bytebuffer-channel-file/

**요약**

| 구분 | IO | NIO |
| --- | --- | --- |
| 입출력 방식 | Stream Oriented | Buffer Oriented |
| 버퍼 방식 | Non-Buffer→ BufferedXXX 로 지원 | Buffer |
| 비동기 방식 지원 | X | O |
| Blocking/Non-Blocking 방식 | Blocking Only | Both |
| 사용 케이스 | 연결 클라이언트가 적고, IO 가 큰 경우 (대용량) | 연결 클라이언트가 많고, IO 처리가 작은 경우 (저용량) |
| 커널 버퍼 | 직접 핸들링 할 수 없음 | Direct Buffer 로 커널 버퍼를 직접 핸들링가능 (ByteBuffer) |

---

자바의 NIO (New IO) 는 자바 4 에 추가된 IO API 로 기존 자바 IO 와는 다른 방식으로 동작합니다. NIO 는 Non-blocking IO 의 줄임말 처럼 생각될 수 있지만 NIO 는 실제로 Non-blocking IO 와 Blocking IO 방식 모두 지원합니다. 기존의 Java IO 를 BIO 라고 부르기도 합니다.

자바 7 부터는 NIO2 가 지원되었습니다.

### 1. NIO 는 IO 와 무엇이 다를까요?

* IO 는 Stream 을 통해 동작하고 NIO 는 Channel 과 Buffer 를 통해 동작합니다.
* Channel 은 Stream 과 달리 양방향 통신을 지원합니다.
* NIO 는 Non-Blocking IO 를 지원합니다.
* NIO 는 Selector 라는 개념을 통해 하나의 쓰레드로 여러 Channel 을 관리할 수 있습니다.

### 2. NIO 가 BIO 에 비해서 빠른 이유는 무엇일까요?

* NIO 는 non-blocking IO 를 사용합니다. 따라서 쓰레드의 컨텍스트 스위치 발생 횟수를 줄일 수 있습니다.
* BIO 의 `read()` 과정
	* `JVM -> 커널-> 시스템 콜 -> 디스크 컨트롤러 -> DMA가 커널버퍼로 복사 -> JVM 버퍼에 복사`

![[bio-read.png]]

 이때 발생할 수 있는 문제로는 

 
	1.  JVM으로 내부 버퍼 복사시 CPU가 관여 -> CPU 오버헤드
	
	2. 복사된 Buffer는 활용 후 GC 대상이됨. -> **Stop-the-World**로 인한 성능 저하
	
	3. 복사중인 I/O 요청 스레드는 블로킹 상태 -> 처리속도 저하 
	 

가 있습니다.

* NIO 는 BIO 와 달리 Direct Buffer 를 사용해 커널 버퍼를 직접 핸들링하여 이런 문제를 해결합니다.

### 3. 항상 NIO 를 사용하는 것이 좋을까요?

일반적으로

* 커넥션이 많고, IO 처리가 작은 경우에는 (e.g.) web server, p2p network) NIO 가 좋습니다.
* 커넥션이 적고, IO 처리가 큰 경우에는 Classic IO 즉, BIO 가 좋습니다.

### 4. WAS 와 NIO

톰캣은 ...

* 톰캣은 9.0 버전 이후 부터 NIO 방식의 Connector 를 기본적으로 활용한다.
* 톰캣의 `Connector` 는 Socket Connection 을 통해 HttpServletRequest 객체로 변환하여 Servlet 에 전달 하는 역할을 합니다.
* 하지만 톰캣은 기본적으로 Thread-Per-Request 로 동작한다.
* NIO 의 장점을 못 누리는 중 이라고 생각됨....

네티는 ..

* 네티는 기본적으로 NIO 를 활용한다.
* 네티는 적은수의 Thread 로 많은 요청을 처리한다.
* NIO 의 장점을 누릴 수 있다!
