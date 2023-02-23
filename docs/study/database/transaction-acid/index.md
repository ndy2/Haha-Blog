---
tags: [database]
title: Transaction
author: ndy2
---

### 트랜잭션
==트랜잭션==이란 데이터베이스의 상태를 변화하기 위해서 수행하는 작업의 단위

### ACID
트랜잭션은 ACID 로 약칭되는 성질을 만족해야한다.

Atomicity (원자성)
- 트랜잭션은 모두 성공 (commit) 하거나 실패 (rollback) 해야한다.

Consistency (일관성)
- 트랜잭션이 commit 된 이후에 데이터베이스는 consistent 해야한다.
- 즉, 데이터베이스에 존재하는 제약사항(constraint)이 깨지면 안된다.

Isolation (독립성)
- 트랜잭션은 다른 트랜잭션에 독립적으로 자신만 실행되고 있는것 처럼 동작해야한다.
- 성능을 위해 종종 완화되며 표준에서는 4가지 레벨 (Transaction Isolation Level) 을 통해 관리한다.

Durability (지속성)
- 트랜잭션이 커밋되었다면 어떠한 상황에도 어떠한 형태로든 저장되는 것을 보장해야한다.
- 즉, DB 서버의 파워가 꺼지거나 프로세스가 죽는 상황에서도 HDD, SSD 와 같은 이차메모리에 트랜잭션의 결과는 저장되어야 한다.

### Isolation Level

- Isolation level 은 성능을 위해 트랜잭션의 독립성을 레벨을 나누어 관리하는 것이다.
- 표준에서는 4가지 레벨을 가지며 이들은 독립성이 잘 지켜지지 않은경우 발생할 수 있는 이상현상 세가지를 어느 정도까지 허용할 것이냐를 기준으로 구분한다.

- 먼저 세가지 이상현상을 알아보자.

1. Dirty Read
- 롤백된 데이터가 조회되는 현상이다.

2. Non-Repeatable Read
- 같은데이터의 조회 결과가 바뀌는 현상이다.

3. Phantom Ream
- 이상 데이터가 추가/삭제되어 조회되는 현상이다.


- 네가지 레벨을 알아보자.

1. Serializable
	- 이상현상을 전혀 허용하지 않는다.
	- 트랜잭션을 serial 한 스케쥴로 실행하는 것을 의미한다.

2. Repeatable Read (MySQL Default)
	- Phatom Ream 를 허용한다.

3. Read Committed (PostgreSQL Default)
	- Phantom Read 와 Non-Reapeatable Read 를 허용한다.

4. Read Uncommitted
- 세가지 이상현상을 모두 허용한다.


