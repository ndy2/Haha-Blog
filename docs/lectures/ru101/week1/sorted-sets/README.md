---
tags: [redis, data-type]
title: Sorted Sets
author: ndy2
date: 2023-05-16
description: >-
  
---
 
 
> [!quote] 참고 자료
> * Redis - [`『Redis Sorted Sets Explained』`](https://youtu.be/MUKlxdBQZ7g) - on Youtube
> * [Commands?groupd=sorted_set](https://redis.io/commands#sorted_set) - on redis.io

### 1. Sorted Sets

> [!note] Sorted Sets
> * Ordered collection of unique strings
> * Floating point score
> * manipulation by value, position, score or lexigraphically
> * Set commands can be applied to `Sorted Sets`
>     * Union
>     * Intersiontion
> * are not nested, hierarchies

- score 는 floating point 로 표현된다.
- 오름차순으로 정렬된다.
- score 가 같은 원소는 `lexicographical` 하게 정렬된다.

### 2. ZADD, ZRANGE

- ZADD
    - Adds one or more members to a sorted set
    - or update their scores
    - create the key if it does not exists

```
ZADD key [NX | XX] [GT | LT] [CH] [INCR] score member [score member
  ...]
```

- ZRANGE
    - returns members in a sorted set within a range of indexes
    - 범위를 나타낼때 `(` 를 붙이면 exclusive 한 인덱스를 의미한다.
    - `BYSCORE`, `BYLEX`, `REV` 옵션들은 커맨드 자체로 대체될 수 있다.

```
ZRANGE key start stop [BYSCORE | BYLEX] [REV] [LIMIT offset count] [WITHSCORES]
```

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 1 "uno"
(integer) 1
redis> ZADD myzset 2 "two" 3 "three"
(integer) 2
redis> ZRANGE myzset 0 -1 WITHSCORES
1) "one"
2) "1"
3) "uno"
4) "1"
5) "two"
6) "2"
```


### 3. ZSCORE, ZRANK

- zscore
    - 점수를 확인

```
redis> ZSCORE myzset "one"
(integer) 1
```

- zrank
    - 인덱스 (순위)를 확인

```
redis> ZSCORE myzset "one"
(integer) 0
```

### 4. set based 연산 - `ZINTER`, `ZUNION`, `ZDIFF`

```
ZINTER numkeys key [key ...] [WEIGHTS weight [weight ...]]
  [AGGREGATE <SUM | MIN | MAX>] [WITHSCORES]

ZUNION numkeys key [key ...] [WEIGHTS weight [weight ...]]
  [AGGREGATE <SUM | MIN | MAX>] [WITHSCORES]

ZDIFF numkeys key [key ...] [WITHSCORES]
```

score 에 대한 가중치를 조절하는 wight 와 aggragate 방식을 조절 할 수 있다.