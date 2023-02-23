---
tags: [database]
title: Relational DB
author: ndy2
---

> [!quote] 참고 자료
> * 쉬운코드 -  https://www.youtube.com/embed/gjcbqZjlXjM

---
### 1. `Relation` in Mathematics
![[images/relation-in-mathematics.png]]

`relation` - subset of Cartesian product
`tuple` - element of a relation

### 2. Relational Data Model
Student 개념을 Relational Data Model 로 표현해보자.    -> `attribute` : relation 에서 가지는 역할의 이름
- student_ids: 학번 집합, 7자리 integer     						`id`
- human_names: 사람 이름 집합, 문자열						`name`
- university_grades: 대학교 학년 집합 ( {1,2,3,4} )				`grade`	
- major_names: 대학교에서 배우는 전공 이름 집합					`major`
- phone_numbers: 핸드폰 번호 집합							`phone_num`, `emer_phone_num`

-> 홍길동 학생 `tuple` :`(1234567, "홍 길동", 1, "수학", "010-1234-5678", "010-1111-2222")`

### 3. Relational Database
- relational data model 에 기반하여 구조화된 database
- relational database 는 여러 개의 relations 로 구성된다.

### 4. Relation 의 특징 들
- relation 은 중복된 tuple 을 가질 수 없다.
- relation 에서 tuple 의 순서는 중요하지 않다.
- relation 에서 tuple 을 식별하기 위해 attributes 의 부분 집합을 key 로 설정한다.
- attribute 는 atomic 해야 한다.

### 5. NULL 의 의미
- 값이 존재하지 않음 - `STUDENT` 릴레이션의 `toeic_score` 애트리뷰트
- 값이 존재하지만 그 값을 아직 모름 - `STUDENT` 릴레이션의 `gender` 애트리뷰트
- 해당 사항과 관련이 없음

### 6. Relation 의 Key
- Super Key - relation 에서 tuples 를 unique 하게 식별할 수 있는 attribute set
- Candidate Key - 최소한의 애트리뷰트 만을 가진 Super Key
- Primary Key - Candidate Key 중 선택된 것
- Foreign Key - 다른 relation 의 primary key 를 참조하는 애트리뷰트 셋