---
tags: [db]
title: Clustering Replication Sharding
author: ndy2
---
 
> [!quote] 참고 자료
> * 테리의 일상 [클러스터링](https://dheldh77.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%A7%81Clustering),  [리플리케이션](https://dheldh77.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EB%A0%88%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98Replication),[샤딩](https://dheldh77.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%83%A4%EB%94%A9Sharding?category=805412)
> * Be A Better Dev - [데이터베이스 샤딩이란?](https://www.youtube.com/watch?v=hdxdhCpgYo8)
> * 망나니 개발자 - [[Database] 리플리케이션(Replication) vs 클러스터링(Clustering)](https://mangkyu.tistory.com/97)
> * 쉬운코드 - [[DB] 파티셔닝? 샤딩? 레플리케이션 (partitioning? sharding? replication?)](https://www.youtube.com/watch?v=P7LqaEO-nGU)

---

>[!tip]
>`클러스터링`, `레플리케이션`, `샤딩/파티셔닝`은 모두 데이터베이스 다중화를 위한 기법입니다.

## 1. 클러스터링 (clustering)
- 여러 개의 DB를 수평적인 구조로 구축하는 방식
- 동기 방식으로 노드들간의 데이터를 동기화 한다.
- Active-Active 방식과 Active-Standby 방식이 있다.
![[images/clustering.png]]

### 장점

-   항상 일관성 있는 데이터를 얻을 수 있다.
-   시스템을 계속 장애없이 운영할 수 있다.

### 단점

-   노드들 간의 데이터를 동기화하는 시간이 필요하므로 Replication에 비해 쓰기 성능이 떨어진다.
-   장애가 전파된 경우 처리가 까다로우며, 데이터 동기화에 의해 스케일링에 한계가 있다.


## 2. 리플리케이션
-   여러 개의 DB를 `수직적인 구조(Master-Slave)`로 구축하는 방식
-   `비동기 방식`으로 노드들 간의 데이터를 동기화 한다.
-   Master 노드는 Create, Update, Delete 연산을 수행하고 Slave 노드는 Read 연산을 수행하여 로드를 분산할 수 있다.
![[images/replication.png]]

### 장점

-   DB 요청의 60~80% 정도가 읽기 작업이기 때문에 Replication만으로도 충분히 성능을 높일 수 있다.
-   비동기 방식으로 운영되어 지연 시간이 거의 없다.

### 단점

-   :warning:  노드들 간의 데이터 동기화가 보장되지 않아 `일관성있는 데이터를 얻지 못할 수 있다`.
-   Master 노드가 다운되면 복구 및 대처가 까다롭다.


## 3. 샤딩

-   테이블을 row 단위로 나누어 저장해 DB 용량을 줄이고 검색 성능을 올리는 기법
-   기존 테이블과 같은 스키마를 가지는 `샤드` 라는 작은 단위로 나누어 저장하는 방식

![[images/sharding.png]]

-   `샤드키` - 나누어진 샤드 중 어떤 샤드를 선택할 지 결정하는 키

### 장점

-   Scalability
-   Availability + Fault Tolerance - 한 샤드내에서 장애가 난 경우 다른 샤드는 정상 동작 가능

### 단점

-   Complexity
    -   Partition Mapping (Shard Key)
    -   Routing Layer 추가
    -   Non-uniformity - 샤드 간의 데이터 균등성을 보장하기 어렵다 → re-sharding
-   Analiytical Query
    -   통계성 쿼리를 날리기 어렵다

### 1) 해시 샤딩

-   해시 함수를 사용해 샤드 키를 나누는 방식

(+) 구현이 간단

(-) 확장성이 좋지 않다 - 샤드가 추가 된 경우 해시 함수를 재 설계 해야함

(-) re-sharding 어렵다

### 2) 다이나믹 샤딩

-   샤드키를 저장하는 테이블을 앞단에 두는 방식

(+) 확장성이 좋다. - 샤드가 추가 되어도 테이블에 샤드키만 추가하면 됨

(-) 복잡도가 올라간다

### 3) 엔티티 그룹

-   관계가 되어있는 엔티티를 같은 샤드내에 구성하는 방식

(+) 단일 샤드 내 쿼리가 효율적

(-) 다른 샤드의 엔티티를 참조해야 하는 경우 비효율적


## 4. 파티셔닝

파티셔닝은 데이터베이스 테이블을 더 작은 테이블로 나누는 것이다.

파티셔닝은 `column`을 기준으로 테이블을 나누는 `vertical partitioning` 과 `row` 를 기준으로 테이블을 나누는 `horizontal partitioning` 이 있다. 

>[!note]
>* 샤딩과 Horizontal 파티셔닝은 동작방식이 동일하다.
>* 샤딩은 분리된 데이터를 `샤드` 라고 부르고 서로 다른 데이터베이스 서버 인스턴스로 관리한다.
>* Horinotal 파티셔닝에서는 분리된 데이터는 `파티션` 이라고 부르고 같은 데이터베이스 서버 내의 다른 테이블 혹은 스키마로 관리한다.

그럼 이제 `vertical partitioning` 에 대해 알아보자!

`Vertical Partitioning` 은 `column을` 기준으로 테이블을 나누는 것이다. VP 를 수행하는 경우는 크게 정규화가 있다. `정규화`란 데이터의 중복을 없에고 CUD 연산의 이상현상을 없애기 위해 테이블을 잘게 나누는 것을 의미한다. 하지만 VP 에는 정규화만있는 것은 아니다.

정규화는 추후에 별도로 알아보도록 하고 오늘은 `성능 개선`을 위해 VP 를 수행할 수 있는 상황에 대해 알아보자.

아래와 같은 게시판의 목록 화면을 띄우기 위해서 Article 테이블에는 어떤 쿼리가 발생해야 할까?
![[images/article-table.png]]

![[images/articles.png]]

예상 쿼리
```sql
SELECT id, title, ... 
FROM article
WHERE ...
```

놀라운 사실은 개발자가 SELECT 절에 필드를 명시했다고 할지라도 article 테이블의 where 절에 해당되는 row의 모든 필드 데이터를 메모리에 올리고 SELECT 절의 필드에 대한 프로젝션을 데이터베이스에서 수행한다는 것이다. 이는 데이터베이스가 일반적으로 데이터를 row 단위로 관리하기 때문이다. (Column-oriented DBMS vs Row-oriented DBMS)

이때 아래와 같이 Column 을 기준으로 테이블을 파티셔닝하면 게시판의 목록 조회에 대해서 content를 IO 해야 한다는 부당함을 덜 수 있다.

![[images/article-table-partitioning.png]]
