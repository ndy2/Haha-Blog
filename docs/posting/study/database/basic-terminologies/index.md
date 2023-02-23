---
tags: [database]
title: Basic Terminologies
author: ndy2
---

> [!quote] 참고 자료
> * 쉬운코드 - https://www.youtube.com/embed/aL0XXc1yGPs

### Database
- 전자적(electronically)으로 저장되고 사용되는
  관련있는(related) 데이터들의 조직화된 집합(organized collection)

### DMBS (Database Management Systems)
- 사용자에게 DB를 정의하고 만들고 관리하는 기능을 제공하는 소프트웨어
- e.g.) PostgreSQL, MySQL, Oracle Database

### 메타데이터 (metadata, a.k.a. catalog)
- DB를 정의하거나 기술하는 data
- e.g.) 데이터 유형, 구조, 제약 조건, 보안, 저장, 인덱스, 사용자 그룹

### 데이터베이스 시스템
- database + DBMS + 연관된 애플리케이션
- 줄여서 그냥 database 라고 부르기도 함
![[images/database-system.png]]

### Data Models
- DB의 구조를 기술하는데 사용될 수 있는 개념들이 모인 집합
- DB 구조를 추상화해서 표현할 수 있는 수단을 제공

- DB Model 은 여러 종류가 있으며 추상화 수준과 DB 구조화 방식이 조금식 다르다.
- DB에서 읽고 쓰기 위한 기본적인 동작들도 포함한다.

- Data Model 의 분류
	- conceptual (or high-level) data models
	- logical (or representational) data models
	- physical (or low-level) data models


#### Conceptual Data Models
- 일반 사용자들이 쉽게 이해할 수 있는 개념들로 이루어진 모델
- 추상화 수준이 가장 높다
- 비즈니스 요구사항을 추상화 하여 기술할 때 사용
- e.g.) Entity-Relationship Diagram

#### Logical Data Models
- 이해하기 어렵지 않으면서도 디테일하게 DB를 구조화 할 수 있는 개념을 제공
- 데이터가 컴퓨터에 저장될 때의 구조와 크게 다르지 않게 DB 구조화를 가능하게 함
- 특정 DBMS 나 storage에 종속되지 않는 수준에서 DB를 구조화 할 수 있는 모델
- e.g.) Relational Data Models (테이블), Object Data Models, Object-Relational Data Modles

#### Physical Data Models
- 컴퓨터에 데이터가 어떻게 파일 형태로 저장되는지를 기술할 수 있는 수단을 ㅔ공
- data format, data orderings, access path (index) 등등
- access path : 데이터의 검색을 빠르게 하기위한 구조체

### Database Schema
- data model 을 바탕으로 database의 구조를 기술한 것
- schema는 database를 설계할 때 정해지며 한번 정해진 후 자주 바뀌지 않음

### Database State (a.k.a snapshot)
- 특정 시점에 database에 있는 데이터


### Three-Schema Architecture  (a.k.a. ANSI/SPARC architecture) [참고](https://www.javatpoint.com/dbms-three-schema-architecture)
- database system 을 구축하는 architecture 중의 하나
- user-application 으로 부터 물리적인 database를 분리 시키는 목적
- 세 가지 level이 존재, 각각의 level 마다 schema가 존재한다.

![[images/three-schema-architecture.png]]


### Database Language
-  View Definition Language (VDL)
-  `Data Definition Language (DDL)`
-  Storage Definition Language (SDL)
- `Data Manupulation Language (DML)`