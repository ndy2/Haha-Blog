---
tags: [os]
title: Context Switch vs Swap In/Out
author: ndy2
date: 2023-04-13
description: >-
  
---

> [!quote] 참고 자료
> * [Difference between Swapping and Context Switching](https://www.geeksforgeeks.org/difference-between-swapping-and-context-switching/) on geeks-for-geeks
> * [Difference between Swapping and Context Switching](https://www.javatpoint.com/swapping-vs-context-switching) on javaTpoint

### 0. 들어가며

운영체제에 대한 지식을 정리하다보니 둘다 잘 들어본 용어이고 각각 어느정도 설명할 수 있지만 둘다 자세히 설명하거나 둘을 비교해보았을따 명확하게 설명할 수 없는것 같다.

관련 내용을 조사해보자!

### 1. context switch

![[context-switch.png]]

- 실행(executing/running) 상태의 프로세스의 문맥을 저장하고 대기(Idle/Ready) 상태의 프로세스의 문맥을 로딩하는 일
- 프로세스의 문맥이란 PCB를 의미한다.
- 이러한 Context Switch를 유발하는 요소로는 OS의 인터럽트 혹은 System Call (Dispatch/ Timeout)이 있다.

### 2. Swap In/Out
![[swap-in-out.png]]

- Swap In/Out 은 기본적으로 Main Memory와 저 너머 이차메모리 사이의 데이터 교환을 의미하는 용어이다. 

### 3. 프로세스의 상태도

프로세스의 상태 다이어그램을 통해 이 내용을 정리해보자.

