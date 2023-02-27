---
tags: [architecture]
title: CAP Theorem
date: 2023-02-09
---
 
> [!quote] 참고 자료
> * Jung-Haeng Lee - [CAP Theorem, 오해와 진실](http://eincs.com/2013/07/misleading-and-truth-of-cap-theorem)
>      * 무조건 읽을 것
> * `『System Design Interview/가상 면접 사례로 배우는 대규모 시스템 설계 기초』` by Alex Xu/ 알렉스 쉬 - [yes24](http://www.yes24.com/Product/Goods/102819435)

### CAP Theorem

> [!quote] CAP theorem on [wikipedia](https://en.wikipedia.org/wiki/CAP_theorem)
> In theoretical computer science, the **CAP theorem** states that any distributed data store can provide only two of the following three quarantees 
> 
> * Consistency - Every read receives the most recent write or an error
> * Availability - Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
> * Partition tolerance - The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.

![[images/the-cap-theorem-diagram.png]]

### CAP

* 데이터 일관성 : 분산 시스템에 접속하는 모든 클라이언트는 어떤 노드에 접속했느냐에 관계 없이 언제나 같은 데이터를 보게 되어야 한다.
* 가용성: 분산 시스템에 접속하는 클라이언트는 일부 노드에 장애가 발생하더라도 항상 응답을 받을 수 있어야 한다.
* 파티션 감내: 파티션은 두 노드 사이에 통신 장애가 발생하였음을 의미한다. 파티션 감내는 네트워크에 파티션이 생기더라도 시스템은 계속 동작하여야 한다는 것을 뜻한다.

### CP, AP, CA 시스템

* CP 시스템 : 일관성과 파티션 감내를 지원한다. 가용성을 희생한다.
* AP 시스템 : 가용성과 파티션 감내를 지원한다. 데이터 일관성을 희생한다.
* CA 시스템: 일관성과 가용성을 지원한다. 파티션 감내는 지원하지 않는다. 그러나 통산 네트워크 장애는 피할 수 없는 일로 여겨지므로, 분산 시스템은 반드시 파티션 문제를 감내할 수 있도록 설계되어야 한다. 그러므로 실세계에 CA 시스템은 존재하지 않는다.
* 온라인 뱅킹 시스템은 데이터 일관성을 포기 할 수 없다. 한 서버에 문제가 생긴다면 다른 서버에 대한 쓰기 연산을 중단시킨다. 즉 가용성을 희생한다.
* 반면 가용성이 중요한 시스템은 멀쩡한 서버를 계속 사용한다. 이때 데이터 일관성이 희생 될 수 있다.
