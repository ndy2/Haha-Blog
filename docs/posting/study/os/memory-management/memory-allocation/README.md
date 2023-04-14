---
tags: []
title: 메모리 할당/파티셔닝
author: ndy2
date: 2023-04-13
description: >-
  
---
  
> [!quote] 참고 자료
> * 한국기술교육대학교 - 김덕수교수님 - Lec8 Memory Management 
> 	* [`『Fixed Partition Multiprogramming』`](https://youtu.be/te-GU7NKa5Y)
> * Memory Allocation Techniques on geeksforgeeks
> 	* continuout memory allocation
> 		* [`『Fixed (or static) Partitioning in Operating System』`](https://www.geeksforgeeks.org/fixed-or-static-partitioning-in-operating-system/)
> 		* [`『Variable (or dynamic) Partitioning in Operating System』`](https://www.geeksforgeeks.org/variable-or-dynamic-partitioning-in-operating-system/)
> 	* non-continuous memory allocation

### 1. Continuous Memory Allocation

> [!note] Continuous Memory Allocation
> * 프로세스를 하나의 연속된 메모리 공간에 할당하는 정책

다음과 같은 메모리 구성 정책에 대한 고민이 필요하다.

> [!question]
> * 메모리에 동시에 올라갈 수 있는 프로세스의 수는? 
> 	* Multiprogramming degree
> * 각 프로세스에게 할당되는 메모리 공간 크기는?
> * 메모리 분할 방법은?

`Uni-programming`

* Multi Programming degree가 1인 경우
* 즉 한번에 하나의 프로그램만 실행할 수 있다.

`Multi-programming`

* Fixed partition multi-programming
	* 고정된 크기로 메모리 미리 분할
	* 메모리 관리가 간편하고 오버헤드가 적다. 대신 메모리 낭비가 심하다. 유연함이 떨어짐
	* internal/external fragmentation 모두 존재
* Variable partition multi-programming
	* 초기에는 전체가 하나의 영역
	* 프로세스를 처리하는 과정에서 메모리 공간이 동적으로 분할
	* 내부 단편화는 없다.
	* 외부 단편화를 해결하기 위한 조각 모음 (defragmentation) 작업이 필요함
	* 공간 활용률을 높이기 위해 배치 전략에대한 고민이 필요 (First-fit, Best-fit, Worst-fit, ...)
