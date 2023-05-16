---
tags: [lecture, redis, data-structure, keys]
title: 레디스 키
author: ndy2
date: 2023-05-16
description: >-
  
---

### 1. Key

> [!note] Redis Key - Definition
> - Keys are the primary way to access data values within Redis.
> - The majority of Redis commands operate a key or keys.

> [!note] Redis Key - Properties
> * Unique
> * Binary safe
>     * "Foo", 42, 3.1415, 0xff
> * Key names can be up to 512MB
> * Trade-off - Length versus Readability

### 2. Key Spaces

- Logical Databases
- Flat key space
- No automatic namespacing
- Naming conventions

### 3. Logical Databases

- identified by a zero-based index.
- default is database 0.
- within a logical database, the key names are unique.
- but the same key name can appear in multiple logical databases.

---
- RDB 의 Schema 와 유사한 개념인듯
- Practical 한 관점에서 하나의 Application 이라도 CACHE 는 0번 DB에 저장하고 SESSION 은 1번 DB에 저장하는 식으로 구분하는것이 좋다.

```bash title="id 가 3번인 DB에 연결하는 redis-cli 옵션 "
> redis-cli -n 3
127.0.0.1:6379[3] > 
```


### 4. Key naming convention

- user:id:followers
    - "user:1000:followers"
    - `object name`
    - `unique identifier`
    - `composed object name`

### 5. Keys, Scan - 모든 키를 조회하는 커맨드

- https://redis.io/commands/keys/
- https://redis.io/commands/scan/

| KEYS                    | SCAN                               |
| ----------------------- | ---------------------------------- |
| Blocks until complete   | Iterates using a cursor            |
| Never use in production | Returns a slot reference           |
| Useful for debugging    | May return 0 or more keys per call |
|                         | safe for production                |

#### 5.1 Keys example

```
> keys customer:1*
1) "customer:1000"
2) "customer:1500"
```

#### 5.2 Scan example

```
> scan 0 MATCH customer:1*
1) "14336"
2) "(empty list or set)"

> scan 14336 MATCH customer:1*
1) "14848"
2) "(empty list or set)"

> scan 14848 MATCH customer:1* COUNT 10000
1) "1229"
2) 1) "customer:1500"
   2) "customer:1000"

> scan 14848 MATCH customer:1* COUNT 10000
1) "0"
2) "(empty list or set)"
```

### 6. DEL, UNLINK - 키를 제거하는 명령어

https://redis.io/commands/del/
https://redis.io/commands/unlink/

| DEL      | UNLINK       |
| -------- | ------------ |
| Blocking | Non-blocking |
