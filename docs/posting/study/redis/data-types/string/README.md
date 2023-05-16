---
tags: [redis, data-type]
title: Redis Strings
author: ndy2
date: 2023-05-15
description: >-
  
---
 
> [!quote] 참고 자료
> * redis.io
> 	* [`『Docs > Data Types > Redis Strings』`](https://redis.io/docs/data-types/strings/)
> 	* [`『Commands > group=string』`](https://redis.io/commands/?group=string)

### 1. Redis Strings

* String 은 바이트 배열, 텍스트, 직렬화된 객체, 바이너리 배열 등 을 저장합니다. 
* String 은 레디스의 가장 기본적인 데이터 타입입니다.
* 캐싱에 사용됩니다.
* counter 혹은 bitwise 연산에 대한 기능역시 추가적으로 제공합니다.

### 2. SET, GET

 
> [!quote] 참고 자료
> * https://redis.io/commands/set/
> * https://redis.io/commands/get/

```redis title="SET, GET 커맨드 실행시 자동 완성되는 커맨드 신텍스"
// SET 커맨드
127.0.0.1:6379> SET key value [NX|XX] [GET] [EX seconds|PX milliseconds|EXAT unix-time-seconds|PXAT unix-time-milliseconds|KEEPTTL]

// GET 커맨드
127.0.0.1:6379> GET key
```

```redis title="String 저장 및 조회"
127.0.0.1:6379> SET hello redis
OK
127.0.0.1:6379> GET hello
"redis"
127.0.0.1:6379>
```

* 레디스의 가장 기본적인 데이터 타입인 문자열에 수행하는 가장 기본적인 커맨드 `SET`, `GET` 이다.
* SET 커맨드의 EX, PX, Exact, ... 는 데이터의 유지시간을 의미하는 옵션이다.

```redis title="10 초뒤 만료되는 문자열"
127.0.0.1:6379> SET hello redis EX 10
OK
127.0.0.1:6379> GET hello
"redis"
127.0.0.1:6379> GET hello
"redis"
127.0.0.1:6379> GET hello
"redis"
127.0.0.1:6379> GET hello
"redis"
127.0.0.1:6379> GET hello
"redis"
127.0.0.1:6379> GET hello
"redis"
127.0.0.1:6379> GET hello
"redis"
127.0.0.1:6379> GET hello
"redis"
127.0.0.1:6379> GET hello // 10 초 뒤 사라짐
(nil)
```

* SET 커맨드의 NX, XX 옵션은 각각 키에대한 데이터가 존재하지 않는 경우, 존재하는 경우 에만 커맨드를 수행한다.

```
127.0.0.1:6379> GET HELLO
(nil)
127.0.0.1:6379> SET HELLO WORLD XX
(nil)
127.0.0.1:6379> SET HELLO WORLD NX
OK
127.0.0.1:6379> SET HELLO WORLD2 XX
OK
127.0.0.1:6379> SET HELLO WORLD3 NX
(nil)
127.0.0.1:6379> GET HELLO
"WORLD2"
```

* GET 커맨드는 아주 간결하다. `GET KEY` 로만 활용 될 수 있다.

### 3. GET, SET 의 확장 커맨드들

* `GETDEL`, `GETEX`, `GETRANGE`, `GETSET`, `MGET`
* `MSET`, `MSETNX`, `SETRANGE`

### 4. 카운트 관리용 커맨드들

* `DECR`, `DECRBY`
* `INCR`, `INCRBY`, `INCRBYFLOAT`


