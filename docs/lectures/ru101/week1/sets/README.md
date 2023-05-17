---
tags: [redis, data-type]
title: Sets
author: ndy2
date: 2023-05-16
description: >-
  
---
 
 
> [!quote] 참고 자료
> * Redis - [`『Redis Sets Explained』`](https://youtu.be/PKdCppSNTGQ) on Youtube
> * Redis - [`『Redis Sets Elaborated』`](https://www.youtube.com/watch?v=aRw5ME_5kMY) on Youtube
> * [commands?group=set](https://redis.io/commands/?group=set) on redis.io

### 1. Set

> [!note] Redis `Sets`
> * are unordered collection of string that conains no duplicates
> * supports standard mathmatical set operations
>     * `SINTER` - 교집합
>     * `SDIFF` - 차집합
>     * `SUNION` - 합집합
> * are not nested

### 2. SADD, SCARD, SMEMBERS, SSCAN

```redis title="SADD - 집합에 추가, SCARD - 카디날리티 조회"
> SADD players:online 42
(integer) 1

> SCARD players:online
(integer) 10000
```

```bash
> SADD venues "Olympic Stadium" "Nippon Budokan" "Tokyo Stadium" # (1) 
(integer) 3 

> SMEMBERS venues # (2)
1) "Olympic Stadium"
2) "Nippon Budokan"
3) "Tokyo Stadium"

> SSCAN venues 0 MATCH * # (3)
1) "0"
2) 1) "Nippon Budokan"
   2) "Oplympic Stadium"
   3) "Tokyou Stadium"
```

1. SADD 는 여러 멤버를 한번에 받을 수 있다. - 레디스에서는 멤버 라는 표현을 주로 사용한다.
2. 키에 대한 모든 멤버를 반환하는 `SMSMBERS`
3. 집합의 멤버를 순회하는 `SSCAN`

### 3. SISMEMBER

```redis title="SISMEMBER - 포함여부 확인"
> SISMEMBER player:online 42
(integer) 1

> SISMEMBER player:online 32
(integer) 0
```

### 4. SREM, SPOP

```bash
> SREM key member [member ...] # (1)
> SPOP Key [count] # (2)
```

1. 멤버를 특정해 제거하는 `SREM`
2. 임의의 멤버를 count (default - 1) 만큼 제거하는 `SPOP`

### 4. `SINTER`, `SDIFF`, `SUNION`, `XXXSTORE`

```redis title="SINTER - 교집합, 32 번 플레이어의 친구중 온라인인 플레이어를 조회"
> SINTER player:32:friends players:online
1) "42"
2) "55"
3) "99"
4) "101"
5) "158"
```

```
> SDIFF player:32:friends players:online
1) "1"
2) "30"
```

```
> SUNION player:32:friends players:40:friends
1) "40"
2) "32"
3) "15"
```

---
- STORE 가 붙는 경우 결과를 destination 에 저장한다.

```
SINTERSTORE destination key [key ...]
SDIFFSTORE destination key [key ...]
SUNIONSTORE destination key [key ...]
```

