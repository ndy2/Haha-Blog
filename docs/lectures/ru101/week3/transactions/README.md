---
tags: [lecture, redis, transaction]
title: 트랜잭션
author: ndy2
date: 2023-05-18
description: >-
  
---

### 1. 레디스의 트랜잭션

- 레디스는 `Optimistic Concurency Controll` 을 지원한다.

### 2. WATCH

```redis title="WATCH"
WATCH key [key ...]
```

- Transaction 의 실행 중 대상 Key 에 변경이 발생하는지 감시한다.
- MULTI 전에 호출된다.
- MULTI 호출 뒤 즉 트랜잭션 내부에서는 호출 할 수 없다.
- 대상 Client 에서 한정적으로 동작한다.
    - Global Scope 을 지니지 않는다.


### 3. MULTI, EXEC

```redis title="MULTI - 트랜잭션을 시작한다."
> MULTI
"OK"
```

```redis title="트랜잭션안의 모든 명령을 실행한다."
> EXEC
1) "first command result"
2) "second command result"

...
> EXEC
(nil)
```

Watch 한 키의 값에 다른 클라이언트에 의해 수정이 발생한 경우 Queued 된 명령 전체를 그냥 실행하지 않는 방식으로 Abort 한다. 