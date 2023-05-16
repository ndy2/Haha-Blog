---
tags: [lecture, redis, data-structure, keys]
title: 레디스 키 만료
author: ndy2
date: 2023-05-16
description: >-
  
---

### 1. Documentation at redis.io

| Set Expiration | Inspect Expiration | Remove Expiration |
| -------------- | ------------------ | ----------------- |
| [`EXPIRE`](https://redis.io/commands/expire)         | [`PTTL`](https://redis.io/commands/pttl)               | [`PERSIST`](https://redis.io/commands/persist)           |
| [`EXPIREAT`](https://redis.io/commands/expireat)       | [`TTL`](https://redis.io/commands/ttl)                |                   |
| [`PEXPIRE`](https://redis.io/commands/pexpire)        |                    |                   |
| [`PEXPIREAT`](https://redis.io/commands/pexpireat)      |                    |                   |

### 2. Expiration Time, TTL

- can be set in milliseconds, seconds or a UNIX timestamp
- can be change by the user
- can be removed

