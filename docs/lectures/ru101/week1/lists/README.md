---
tags: [redis, data-types]
title: Lists
author: ndy2
date: 2023-05-16
description: >-
  
---

### 1. Lists

- Ordered collection of Strings
- Duplicated are allowed
- Elements can be adde and removed at Left or Right
- Elements can be inserted relative to another
- Used to implement Stacks and Queues
- Are no nested
- Implemented as a linked list 

![[redis-list.excalidraw.png]]

### 2. LPUSH, LLEN, LRANGE

```
> LPUSH orders:4x100m-womens-final jane:4 bill:8 charlie:6 
(integer) 3

> LLEN orders:4x100m-womens-final
(integer) 3

> LRANGE orders:4x100m-womens-final 0 -1
1) "charlie:6"
2) "bill:8"
3) "jane:4"
```

![[redis-list-2.excalidraw.png]]

### 3. Push, Pop Works with Queue & Stack Internally

### 4. LINDEX, LINSERT, LSET, LREM

```
LINDEX key index
LINSERT key BEFORE|AFTER pivot value
LSET key index value
LREM key count value
```

### 5. Lists Use Cases

- Activity Stream
- IPC - Producuer-Consumer Queue
