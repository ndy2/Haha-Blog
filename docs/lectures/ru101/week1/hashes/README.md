---
tags: [lecture, redis, data-structure, keys]
title: Hashes
author: ndy2
date: 2023-05-16
description: >-
  
---

### 1. Hash

- Key with named fields
- Single level
- Provide commands on those fields
	- e.g.) INCR
- Dynamically add and remove fields
- Stored extremply efficiently
- Are not recursive

### 2. HSET - 해시 저장

```redis title="HSET Syntax"
HSET key field value [field value ...]
```

- 해시를 저장한다.

```redis title="HSET example"
HSET evnet:judo capacity 12000 location "Nippo Budokan" ticket_price:gold 100 availability:gold 8000
```

![[hset_gui.png|HSET with REDISINSIGHT]]

### 3. HEXISTS, HDEL, HINCRBY, HINCRBYFLOAT

```redis title="HEXISTS - 필드의 여부를 확인"
> HEXISTS event:judo capacity 
(integer) 1
> HEXISTS event:judo timezone
(nil)
```

```
> HINCRBY event:judo availability:gold -10 
(integer) 7990
```

### 4. HGET, HGETALL, HSCAN, HMGET, HKEYS, HVALS

![[hget_gui.png]]

이런 해시 값에서 HSCAN 을 이용해 모든 `availiablity:*` 패턴의 field 를 순회해보자.

```
> HSCAN event:judo 0 match availability:* 
1) "0" 
2) 1) "availability:gold" 
   2) "7990" 
   3) "availability:silver" 
   4) "2000"
```

### 5. Hash Uses Cases

- Rate Limiting
- Session Cache
