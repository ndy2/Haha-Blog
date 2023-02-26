---
tags: [db]
title: Anomaly
author: ndy2
---
 
> [!quote] 참고 자료
> * 쉬운코드
>     * DB 테이블 설계 잘못하면 어떤 문제가 생길 수 있을까요?
>     * DB 에서 functional dependency(FD : 함수 종속) 을 설명합니다! 고고씽!! 

### 1. 이상현상 (Anomalies)

#### 1. Insertion Anomaly

![[images/insertion-anomaly.png]]

**문제점**

* 저장 공간 낭비
* 실수로 인한 데이터 불일치 가능성 존재
* null 값을 많이 쓰게 됨

**발생 이유**

* 별개의 관심사가 한 테이블에 있음 - `EMPLOYEE`, `DEPARTMENT`

### 2. Deletion Anomaly

![[images/deletion-anomaly.png]]

**문제점**

* QA 부서 최후의 1 인인 YUJIN 을 삭제하려면?
* QA 문서 자체가 사라진다, 자연스럽지도 않다.

**발생이유** 

* 별개의 관심사가 한 테이블에 있음 - `EMPLOYEE`, `DEPARTMENT`

### Update Anomaly

개발팀의 부서이름이 DEV -> DEV1 로 업데이트 된다면?

**문제점**

* 일부만 업데이트 되어 데이터의 불일치가 발생 할 수 있다.

**발생이유** 

* 별개의 관심사가 한 테이블에 있음 - `EMPLOYEE`, `DEPARTMENT`

### 2. Spurious Tuple

* 두 테이블의 Join 을 잘못 된 방식으로 해서 발생한 이상한 튜플

![[images/spurious-tuple.png]]

### 3. Null 값이 많아짐으로 인한 문제

* null 값이 있는 column 으로 join 하는 경우 상황에 따라 예상과 다른 결과 발생
* null 값이 있는 column 에 aggregate function 을 사용할 때 주의 필요
* 불필요한 storage 낭비
