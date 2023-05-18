---
tags: [lecture, redis]
title: 객체 저장과 해시
author: ndy2
date: 2023-05-18
description: >-
  
---

### 1. Simple Object Storage

다음과 같은 Json 객체를 Redis에 저장하는 방법을 알아보자.

```json
{
    'sku' : "123-ABC-723",
    'name' : "Men's 100m Final",
    'disabled_access' : True,
    'medal_event' : True,
    'vanue' : "Olympic Stadium",
    'category' : "Track & Field",
}

{
    'sku' : "737-DEF-911",
    'name' : "Women's 4x100m Heats",
    'disabled_access' : True,
    'medal_event' : False,
    'vanue' : "Olympic Stadium",
    'category' : "Track & Field",
}

{
    'sku' : "320-GHI-921",
    'name' : "Women's Judo Qualifying",
    'disabled_access' : False,
    'medal_event' : False,
    'vanue' : "Nippon Budokan",
    'category' : "Martial Arts",
}
```

### 2. HSET & HGET 시리즈

- `HSET key field value [field value ...]`
```redis
> HSET events:123-ABC-723 name "Men's 100m Final" diabled_access True medal_event True venue "Olympic Stadium" category "Track & Field"
(integer) 5
```

- `HGET key field`
- `HMGET key field [field]`
- `HGETALL key`
    - 해시가 큰 경우 (필드가 100개가 넘어가는 경우) 사용을 자제
- `HSCAN key cursor [Match pattern] [Count count]`
- `HEXISTS key field`


### 3. Complex Object Storage

다음과 같은 JSON 객체를 저장하는 방법을 생각해보자

```json
{
    'sku' : "123-ABC-723",
    'name' : "Men's 100m Final",
    'disabled_access' : True,
    'medal_event' : True,
    'vanue' : "Olympic Stadium",
    'category' : "Track & Field",
    'avaiable' :
       {
           'general' : {
                           'qty' : 20000,
                           'price' : 25.00
                       }
       }
}
```

크게 세가지 접근이 있다.

#### 3.1. Flatten

```
> HSET events:123-ABC-723 name "Men's 100m Final" diabled_access True medal_event True venue "Olympic Stadium" category "Track & Field" available:general:qty 20000 available:general:price 25.00 
(integer) 7
```

- pros
    - Atomic updates/deletes
    - No transaction
    - Encapsuplation
- cons
    - relationship manitenance
    - large objects

#### 3.2 Multiple Hash

```
> HSET events:123-ABC-723 name "Men's 100m Final" diabled_access True medal_event True venue "Olympic Stadium" category "Track & Field"  
(integer) 5

> HSET events:123-ABC-723:available:general qty 20000 price 25.00
(integer) 2
```

### 3. Multiple Hash With Set

```
> SADD events:123-ABC-723:available event:123-ABC-723:general
(integer) 1
```

관계를 표현하기 위한 별도의 집합을 하나 더 가지게 한다.
확장성을 지니지만 조금은 더 복잡하다.