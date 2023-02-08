---
title: Binary-Indexed-Tree
date: 2023-02-08
---

@ 참고 자료)

- 개발자 영맨 - [[Range Sum] 구간 합 #2 - Binary Indexed Tree (Fenwick Tree)](https://www.youtube.com/@bluedawnstar)

### 1. Range Query - O(logn)

![bit-query.png](images/bit-query.png)

- 끝자리가 겹치지 않는다.
- sum(0,10) = BIT[0] + BIT[8] + BIT[10] + BIT[11]
    - 11 = 01011<sub>2</sub>
    - 10 = 01010<sub>2</sub>
    - 08 = 01000<sub>2</sub>
    - 00 = 00000<sub>2</sub>
- 이런 식으로 동작하도록 구현된 트리!

### 2. Point Update - O(logn)

![bit-update.png](images/bit-update.png)

- update(4, delta)
    - BIT[5] += delta  // 5 = 00101<sub>2</sub> (-> + 1<sub>2</sub>)
    - BIT[6] += delta  // 6 = 00110<sub>2</sub> (-> + 10<sub>2</sub>)
    - BIT[8] += delta  // 8 = 01000<sub>2</sub> 


### 3. Range Update

{==TODO!==}