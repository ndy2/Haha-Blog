---
tags: [redis, pubsub]
title: Publish/Subscribe
author: ndy2
date: 2023-05-23
description: >-
  
---

 
> [!quote] 참고 자료
> Articles at redis.io
>-    [Overview of Publish / Subscribe](https://redis.io/topics/pubsub)
>-    [Documentation for Publish / Subscribe commands](https://redis.io/commands#pubsub)


### 1. Pub/Sub

- Publish/Subscribe does not guarantee delivery!

### 2. Pub/Sub Commands

> [!example] Simple Syndication
> * `PUBLISH channel message`
> * `SUBSCRIBE channel [channel ... ]`
> * `UNPUBLISH [channel [channel ... ]]`

#### 2.1. `PUBLISH`

- `PUBLISH` 명령은 단일 채널에 message 를 발행한다.
- message 는 임의의 바이너리 문자열이 될 수 있다.
    - text, numbers or binary data, serialized json blob

#### 2.2 `SUBSCRIBE`

- 단일 채널을 구독한다.
- wildcard 는 허용되지 않는다.

> [!example] Patterned Syndication
> * `PSUBSCRIBE pattern [pattern ... ]`
> * `PUNPUBLISH [pattern [pattern ... ]]`

> [!example] Admin
> * `PUBSUB subcommand [argument [argument ... ]]`

#### 2.5 `PUBSUB`

```redis title="PUBSUB 의 subcommand 목록"
- PUBSUB
    - CHANNELS [pattern]
    - NUMSUB [channel-1 ... channel-N]
    - NUMPAT
```

