---
tags: [redis, capped-lists]
title: Cardinality & Capped Collections
author: ndy2
date: 2023-05-16
description: >-
  
---
 
> [!quote] 참고 자료
> *  [Introduction to Capped Lists at redis.io](https://redis.io/topics/data-types-intro#capped-lists)

### 1. Cardinality of Collection

```
- LLEN key // List
- SCARD key // Set
- ZCARD key // Sorted-Set
```

### 2. Capped Collections

* Retain subset of members

> [!example] Use Cases
> * Leaderboard in a game
> * Recent Activity in Activity Stream

### 3. LTRIM

* specify the range of elements you want to retain.
* trimming can be specified from the left

![[list-ltrim.excalidraw.png]]

![[list-ltrim-2.excalidraw.png]]

```
> rpush list-one a b c d e f 
(integer) 6

> lrange list-one 0 -1 
1) "a" 
2) "b" 
3) "c" 
4) "d" 
5) "e" 
6) "f" 

> ltrim list-one 0 4 
"OK" 

> lrange list-one 0 -1 
1) "a" 
2) "b" 
3) "c" 
4) "d" 
5) "e"
```

### 4. ZREMRANGEBYRANK Key Start Stop - the Equivalent of LTRIM in Sorted Set

```
> ZADD set-one 1 a 2 b 3 c 4 d 5 e 6 f 
(integer) 6

> ZREMRANGEBYRANK set-one 5 -1 
(integer) 1

> zrange set-one 0 -1 
1) "a" 
2) "b" 
3) "c" 
4) "d" 
5) "e"
```
