---
tags: [db]
title: OLAP
author: ndy2
---
 
> [!quote] 참고 자료
> * 우아한형제들 기술블로그 - [정지원,# Aurora MySQL vs Aurora PostgreSQL](https://techblog.woowahan.com/6550/)
> * microsoft - [# OLAP(온라인 분석 처리)](https://learn.microsoft.com/ko-kr/azure/architecture/data-guide/relational-data/online-analytical-processing)

면접에서 아래와 같은 꼬리질문을 받았다.

> [!question]
> MSA 에서 데이터베이스의 독립적인 구성이 중요하다고 해주셨는데 왜 그런지 말씀해 주실 수 있나요?

A. 물리적으로 데이터베이스를 분리하는것은 여러 관점에서 중요합니다. 첫째로는 MSA 의 독립성을 위해서입니다. MSA 의 가장큰 장점은 Micro-Service 컴포넌트간의 의존성을 낮추어 독립성을 바탕으로 확장성, Business Agility 같은 여러 장점을 얻을 수 있습니다. 애플리케이션 레벨에서 아무리 열심히 메시지 큐와 같은 미들웨어로 독립성을 갖추었다고 할지라도 데이터베이스에서 서로 join 을 통해 모든 영역의 데이터를 한번에 조회한다면 이는 아무 의미가 없을 것입니다. 그래서 최소한 MSA 를 활용한다면 데이터베이스를 논리적인 관점에서라도 분리하는 것이 필수입니다.

두번째는 장애 대응입니다. MSA 에서 또한 가장 중요한 것은 Micro-Service 컴포넌트의 장애가 다른 컴포넌트로 전파되지 않도록 관리하는 것입니다. 데이터베이스를 분리하지 않는다면 데이터베이스가 단일 장애 지점이 되어 큰 문제가 될 수 있습니다.

`물론 위와 같이 정리해서 답변 하지는 못했다...`

> [!question]
> 그럼 그런 분리된 데이터베이스 구조에서 통계성 쿼리를 처리하는 방법이 있을까요?

A. 에... 그게... 효과적으로 잘 모아서 Read 만 발생할 수 있는 서버에다가 어쩌구 저쩌구....

`물론 위 처럼 횡설수설 하면서 대답했다...`

추후에 찾아보니 OLTP (Online Transaction Processing) 와 OLAP (Online Analytical Processing) 이라는 키워드가 있다. 여기서는 통계성 쿼리 처리, 즉 OLAP 를 효과적으로 처리하기 위한 일반적인 접근방식을 찾아보자!

---

### OLAP 이란?

> [!quote] miscrosoft - olap
> OLAP(온라인 분석 처리) 는 대규모 비즈니스 데이터베이스를 구성하고 복잡한 분석을 지원하는 기술입니다. 트랜잭션 시스템에 부정적인 영향을 주지 않고 복잡한 분석 쿼리를 수행하는 데 사용할 수 있습니다.
> 
> 기업에서 모든 트랜잭션 및 레코드를 저장하는 데 사용하는 데이터베이스를 [OLTP(온라인 트랜잭션 처리)](https://learn.microsoft.com/ko-kr/azure/architecture/data-guide/relational-data/online-transaction-processing) 데이터베이스라고 합니다. 일반적으로 이러한 데이터베이스의 레코드는 한 번에 하나씩 입력됩니다. 종종 이러한 데이터베이스는 조직에 귀중한 정보를 풍부하게 포함합니다. 그러나 OLTP 에 사용되는 데이터베이스는 분석용으로 디자인되지 않았습니다. 따라서 이러한 데이터베이스에서 답변을 검색할 때는 시간과 노력이 많이 듭니다. OLAP 시스템은 고효율적 방식으로 데이터에서 이러한 비즈니스 인텔리전스 정보를 추출하는 데 도움이 되도록 디자인되었습니다. OLAP 데이터베이스가 과도한 읽기, 낮은 쓰기 워크로드에 최적화되어 있기 때문입니다.

### 데이터베이스 레벨

찾아보니 대용량 통계성 쿼리를 위해 별도의 테이블을 관리하고 이를 OLAP 방식으로 처리하는 것이 일반적인것 같다.

이런 OLAP 를 위해서는 어떤 데이터베이스를 사용하는 가는 데이터의 특성이나 인덱스를 적용하는 방식에 따라 달라 너무 많은 의견있는것 같습니다. 보통 MySQL 과 PostgreSQL 을 두고 고민하는데 직접 데이터를 추가해 쿼리를 날려보고 튜닝하며 성능을 측정하는것이 이런 선택에서는 필수로 보입니다.

혹은 OLAP 를 위해 특별히 설계된 데이터 웨어하우스 툴 (Amazon Redshit, Azure data lake) 을 고려하기도 합니다.

### 애플리케이션 레벨

애플리케이션 레벨에서는 복잡한 쿼리는 JPA 가 아니라 네이티브 쿼리를 쉽게 다룰 수 있는 

Data JDBC 나 MyBatis 같은 툴을 활용하는것이 더욱 좋습니다.

* [김영한님 -복잡한 쿼리 처리하는 방법](https://www.inflearn.com/questions/40192/qdsl%EB%A1%9C-%EB%B3%B5%EC%9E%A1%ED%95%9C-%EC%BF%BC%EB%A6%AC%EB%A5%BC-%EC%96%B4%EB%8A%90%EC%A0%95%EB%8F%84-%EC%BB%A4%EB%B2%84-%EA%B0%80%EB%8A%A5%ED%95%9C%EA%B0%80%EC%9A%94) 
* 스프링 부트로 개발하는 MSA 컴포넌트 - 7 장 1 절 JPA 장점과 잔점
