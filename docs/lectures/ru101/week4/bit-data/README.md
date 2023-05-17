---
tags: [lecture, redis]
title: Bit data
author: ndy2
date: 2023-05-17
description: >-
  
---

### 1. Bit Data

- Bitfields & Bit Arrays
- Compact, Optimized structures
- Commands to manipulate Bits
- No explicit Bit data type
- Commands operate on Strings

### 2. BIT DATA 예시

```bash
> BITFIELD mykey SET u8 0 42 # (1)
1) "0"

> GET mykey # (2)
"*"

> BITFIELD mykey get u8 0 # (2)
1) "42"

> BITFIELD mykey INCRBY u8 0 1 # (3)
1) "43" 

> TYPE mykey # (4)
"string" 

> OBJECT encoding mykey # (5)
"raw"

> GET mykey # (6)
"+"
```

아스키 테이블을 뒤져보면 42 는 `"*"` 43 은 `"+"` 임을 알 수 있다. 이제 BITFIELD 명령을 부셔보자.

### 3. BITFIELD

`BITFIELD` 명령은 다른 Sub Command 들과 함께 구성됩니다.

```
BITFIELD key 
  [GET encoding offset]
  [SET encoding offset value]
  [INCRBY encoding offset increment]
  [OVERFLOW <WRAP | SAT | FAIL>]
```

> [!note] encoding 이란?
> - Signed (i) or Unsigned (u)
> - Size (Number of Bits)
> - 최대 `i64` or `u63`
> - 스키마가 없기 때문에 개발자가 해당 비트의 구성을 명확히 알아야 한다.

```bash
> BITFIELD mykey SET u8 0 42 # (1)

> BITFIELD mykey get u8 0 # (2)

> BITFIELD mykey INCRBY u8 0 1 # (3)
```

1. `mykey` 를 `unsigned 8 bit` 의 인코딩으로 취급해서 `0 번째 offset` 에 `42` 라는 값을 채워 넣어라.
2. `mykey` 를 `unsigned 8 bit` 의 인코딩으로 취급해서 `0 번째 offset` 부터 값을 읽어라
3. `mykey` 를 `unsigned 8 bit` 의 인코딩으로 취급해서 `0 번째 offset` 의 값을 1 올려라

![[bitfield.excalidraw.png]]

`BITFIELD mykey SET u8 2 1` 의 결과는?

```
> BITFIELD mykey SET u8 2 1 
1) "172" 

> GET mykey 
"\x00@"
```

![[bitfield-offset.excalidraw.png]]

### 4. BITCOUNT, BITOP, BITPOS

#### 4.1. BITCOUNT

```
BITCOUNT key [start end [BYTE | BIT]]
```

- default - `BYTE`

```
redis> SET mykey "foobar"
"OK"

redis> BITCOUNT mykey
(integer) 26

redis> BITCOUNT mykey 0 0
(integer) 4

redis> BITCOUNT mykey 1 1
(integer) 6

redis> BITCOUNT mykey 1 1 BYTE
(integer) 6

redis> BITCOUNT mykey 5 30 BIT
(integer) 17

redis>
```

![[bitfield-foobar.excalidraw.png]]

#### 4.2 BITOP

```
BITOP <AND | OR | XOR | NOT> destkey key [key ...]
```

```
> SET key1 aa 
"OK" 

> BITOP NOT notkey1 key1 
(integer) 2 

> GET notkey1 "\x9e\x9e"
```

- `not a` = `10011110b` = `0x9e`

### 4.3 BITPOS

```
BITPOS key bit [start [end [BYTE | BIT]]]
```

```
> SET key1 foobar
"OK"

> BITPOS key1 0
(integer) 0

> BITPOS key1 1
(integer) 1
```
