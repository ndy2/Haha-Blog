---
tags: [architecture, load-balancing]
title: Load Balancing
---

### 1. 로드 밸런싱이란?

>[!note] "로드 밸런싱 이란?"
>들어오는 네트워크 트래픽을 백엔드 서버 그룹 내에 효율적으로 분배하는 것

![[images/load-balancing.png|로드 밸런싱]]

로드 밸런서는 다음과 같은 기능을 제공합니다.

- 클라이언트 요청 이나 네트워크 부하를 효율적으로 분배한다.
- 이용가능한 서버에게만 요청을 보냄으로써 고가용성<sup>High Avialiablity</sup> 과 안정성 <sup>Reliability</sup> 을 보장한다.
- 서버를 더하고 빼는것에 유연함을 제공한다.


### 2. 로드 밸런싱 알고리즘

- NginX 에서 지원하는 알고리즘 목록입니다.
    - 더 자세한 내용은 이 [링크](https://www.nginx.com/blog/choosing-nginx-plus-load-balancing-techniques/) 를 참고해주세요.

>[!note] Round Robin
>* 순차적으로 요청을 분배한다.
>* 가장 널리 활용되고 구현도 쉽다.
>* 서버 및 요청의 특징에 따라 한 서버가 과부화 될 가능성이 적다면 좋은 선택이다.

>[!note] Least Connections & Least Time
>`Least Connections`
>* 가장 적은 커넥션을 가진 서버에게 요청을 분배한다.
>* 대부분의 경우 실용적이고 좋은 선택이다.
> 
>  `Least Time`
>* 평균 응답시간과 현재 커넥션 수를 합친 공식에 따라 서버를 선정한다.
>* *the current number of active connection*s + *a weighted average response time for past requests*
>* Least Connection 알고리즘에 추가적으로 응답 시간을 고려한 알고리즘이라고 생각할 수 있다.
>* Upstream Server 간의 평균 응답시간이 크게 차이나는 경우 적절한 선택이다.
>      * 예를 들어 DR의 목적으로 여러 Data Center 를 운영한다면, Least Connection 알고리즘은 응답시간을 고려해 가까운 Local Data Center 를 주로 활용 할 것이다.

>[!note] Hash & IP Hash
>`Hash`
>* 장점
>    * 결과가 일정하기 때문에 (deterministic) 부가적인 장점이 발생한다.
>* 단점
>    * 균등한 분배가 보장되지 않는다
>    * 서버가 추가, 제거되는 경우 Rehashing 이 발생한다. 알고리즘 적으로 rehashing 의 발생 빈도를 낮출 수는 있지만 완벽하지는 않다.
>
>`IP Hash`
>* Client 의 IP 가 세션이 동작하는 동안 변경되는 경우 (e.g. 모바일 유저의 IP가 wifi -> 데이터로 변경) 적절하지 않다.
>* forward proxy를 적용하는 경우 proxy ip 가 모두 사용될 것이므로 사용할 수 없다.


>[!tip]
>서버의 성능이 같지 않다면 서버별 `weight` 를 둘 수 있다.