---
tags: [network, layer7]
title: DNS
author: ndy2
---

### 0. 들어가며

제가 좋아하고 즐겨보는 강사님 중 한분인 [널널한 개발자 최호성](https://www.youtube.com/@user-kw8xd4qi8q)님께서 주로 하시는 말씀으로 `*인터넷*을 이루는 가장 중요한 요소 두가지는 *DNS 와 *라우터* 이다.` 라는 것이 있습니다. 오늘은 그 중요한 ***DNS*** 라는 녀석을 알아보겠습니다. 

### 1. DNS

- 도메인 이름 시스템^Domain^ ^Name^ ^System^ 은 사람이 읽을 수 있는 도메인 이름을 머신이 읽을 수 있는 IP 주소로 변환합니다.

**`DNS 의 특징`**

- UDP 사용
- 계층적 질의

---

### 2. Pre DNS-Query

url 주소를 브라우저에 입력하면 곧 바로 DNS 서버에 DNS 질의가 발생하는 것이 아니라 몇가지 캐시들을 확인 하고 IP 정보가 저장되어 있지 않다면 DNS 쿼리를 실행합니다.

#### 1. host 파일 확인

호스트 파일 이란 호스트 이름에 대응하는 IP 주소가 저장되어 있어서 DNS 에 주소 정보를 제공받지 않고도 IP 주소를 찾게 해주는 파일입니다.

MAC os 에서 호스트 파일을 출력한 결과는 아래와 같습니다.

```shell
$ > cat /etc/hosts
##
# Host Database
# 
# localhost is used to configure the loopback interface
# when the system is booting. Do not change this entry.
##
127.0.0.1             localhost
255.255.255.255       broadcasthost
::1                   localhost
$ >
```
기본적으로 IPv4 와 IPv6 의 루프백 주소와 broadcasthost 주소가 하나 저장되어 있는 것을 확인 할 수 있습니다. 

#### 2. OS 의 dns 캐시 확인

Window 에서 DNS 캐시 확인 한 결과는 아래와 같습니다.

```bash
C:\Users\1>ipconfig /displaydns

Windows IP 구성
...
    katalk.kakao.com
    ----------------------------------------
    데이터 이름 . . . . . : katalk.kakao.com
    데이터 유형 . . . . . : 5
    TTL(Time To Live) . : 16
    데이터 길이 . . . . . : 8
    섹션 . . . . . . . : 응답
    CNAME 레코드  . . . . : katalk-fo6ld96d.kgslb.com

    데이터 이름 . . . . . : katalk-fo6ld96d.kgslb.com
    데이터 유형 . . . . . : 1
    TTL(Time To Live) . : 16
    데이터 길이 . . . . . : 4
    섹션 . . . . . . . : 응답
    (호스트) 레코드 . . . : 211.249.219.27
...
```


#### 3. 브라우저의 dns 캐시 확인
- 크롬과 같은 브라우저에도 DNS 서버와 같이 DNS 캐시를 저장하고 있습니다.
- 크롬 - chrome://net-internals/#dns 이 주소에 접속하면 크롬 브라우저의 DNS ~~캐시를 확인하고~~ 초기화 할 수 있습니다. 
    - dns 캐시 엔트리 목록을 확인하는 화면은 더이상 제공 되지 않는것 같습니다.

![[images/crhome-dns.png]]

### 3. DNS-Query
- 위의 모든 단계를 거쳐도 IP 주소를 확인 할 수 없었다면 DNS 질의 <sup>DNS Query</sup> 가 이루어집니다. 

![[images/how-dns-works.png]]

DNS 질의 응답 메시지는 아래와 같은 구조로 이루어 져 있습니다.

``` title="dns 질의, 응답 요약"
## dns query
dev.taggle.kr A IN
---
Query Name String/ dev.taggle.kr : 질의 하는 도메인의 이름 
Type             / A             : 데이터의 타입(A - 주소, NS - 네임서비스, ..)
Class            / IN             : DNS 통신중인 네트워크 (인터넷 - In) 

## dns response
dev.taggle.kr A IN add

Time to live: 598 (9 minutes, 58 seconds)
Address = 54.254.197.159
---
Time to live  / 598                      : DNS 캐시의 유지 시간
Resource Data / Address = 54.254.197.159 : 질의한 요청에 대한 응답 데이터
```

> DNS 질의, 응답 메시지 캡쳐링 - [영상 링크](https://youtu.be/rw-7LtnDnYU?t=190)

### 4. DNS 서버의 종류

DNS 서버는 자신이 DNS 엔트리를 가지고 응답을 내려줄 수 있는 권한에 대한 여부로 크게 두가지로 구분 됩니다.

- 권한 없는 네임 서버 - non-Authorative Name Server, a.k.a. Local DNS server
    - 보통 ISP 가 담당합니다.
    - 클라이언트의 DNS 질의를 받아 권한 있는 네임 서버에게 Recursive 하게 혹은 Iterative 하게 DNS 질의를 위임 하여 응답을 받아 클라이언트에게 전달합니다.
    - 데이터를 가지지는 않지만 DNS 캐시를 가지고 직접 응답을 할 수는 있습니다.
- 권한 있는 네임 서버 - Authorative Name Server
    - 계층형 구조를 가집니다.
    - 일종의 계층형 DB 라고 볼 수 있습니다.
    - Root DNS server 
        - root url (`.`) 에 대한 name service 제공
        - 전 세계에 단 13 대 존재
    - TLD DNS server
        - Top Level domain (.kr, .com, .org, ...) 에 대한 name service 제공
    - 그 이하는 Second DNS server, Sub-Domain DNS server 등으로 불립니다.

- DNS 쿼리는 Iterative 혹은 Recursive 한 방식으로 처리 됩니다.
![[excalidraws/dns-query.excalidraw.png]]