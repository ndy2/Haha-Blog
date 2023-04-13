---
tags: [os]
title: Context Switch vs Swap In/Out
author: ndy2
date: 2023-04-13
description: >-
  
---

> [!quote] 참고 자료
> * [`『Difference between Swapping and Context Switching』`](https://www.geeksforgeeks.org/difference-between-swapping-and-context-switching/) on geeks-for-geeks
> * [`『Difference between Swapping and Context Switching』`](https://www.javatpoint.com/swapping-vs-context-switching) on javaTpoint
> * 쉬운코드 - [`『컨텍스트 스위칭 뽀개기』`](https://youtu.be/Xh9Nt7y07FE) on Youtube

### 0. 들어가며

운영체제에 대한 지식을 정리하다보니 둘다 잘 들어본 용어이고 각각 어느정도 설명할 수 있지만 둘다 자세히 설명하거나 둘을 비교해보았을따 명확하게 설명할 수 없는것 같다.

관련 내용을 조사해보자!

### 1. Context Switch

![[context-switch.png]]

* 실행(executing/running) 상태의 프로세스의 문맥을 저장하고 대기(Idle/Ready) 상태의 프로세스의 문맥을 로딩하는 일
* 프로세스의 문맥이란 
	* PCB를 의미한다.
	* 프로세스/스레드의 상태
	* CPU - register (PC, SP...), 메모리 등등
* 이러한 Context Switch를 유발하는 요소로는 
	* 주어진 time slice 를 다 사용
	* IO 작업을 해야 한다
	* 다른 리소스를 기다린다
	* OS의 인터럽트 혹은 System Call (Dispatch/ Timeout)이 있다.
* 컨텍스트 스위칭은 OS 의 커널에 의해 실행 된다. 즉 커널 모드에서 실행 된다.

#### 컨텍스트 스위칭의 영향

* Cache Pollution
* 컨텍스트 스위칭 타임 자체가 오버헤드이다.

#### 컨텍스트 스위치의 종류

* 다른 프로세스끼리 스위칭 인지/ 같은 프로세스의 쓰레드끼리 스위칭인지에 따라 다르다.

##### 공통점

* 커널 모드에서 실행
* CPU의 레지스터 상태를 교체

##### 차이점

* Process Context Switch 는 Thread Context Switch 와 달리 VMS 경계 정보/ TLB 정보를 추가적으로 스위칭 한다.

### 2. Swap In/Out

![[swap-in-out.png]]

* Swap In/Out 은 기본적으로 Main Memory와 저 너머 이차메모리 사이의 데이터 교환을 의미하는 용어이다. 

### 3. 프로세스의 상태도

프로세스의 상태 다이어그램을 통해 이 내용을 정리해보자.

![[process-state-diagram.excalidraw.png]]

#### 빨간 선 ~ SwapIn/Out

* 프로세스가 `Suspend 상태`가 되는 경우 동작한다.
* 프로세스가 `Suspend 상태`가 되는 경우는 다음과 같다.
	* 메모리가 꽉 차서 일부 프로세스를 메모리 밖으로 내보낼때
	* 프로그램에 오류가 있어서 실행을 미루어야 할때
	* 바이러스와 같이 악의적인 공격을 하는 프로세스라고 판단될 때
	* 매우 긴 주기로 반복되는 프로세스라 메모리 밖으로 쫒아내도 큰 문제가 없을 때
	* 입출력을 기다리는 프로세스의 입출력이 계속 지연될 때

#### 파란선 ~ Context Switch

* 프로세스 스케쥴러에 의해 실행 되는 (CPU를 차지하던) 프로세스가 교체되는 것을 의미한다.
* 다음과 같은 경우에 프로세스의 교체가 이루어진다.
	* 한 프로세스가 자신에게 주어진 시간을 다 사용하는 경우 (`timeout(PID)`)
	* 인터럽트가 발생하는 경우
		* e.g.) 자신에게 주어진 메모리 공간을 넘어 가려 한다.
		* -> 인터럽트 관리 프로세스가 실행 상태가 되고 대상 프로세스를 강제종료 한 뒤 자신을 종료한다.
		* -> 이 경우에도 컨텍스트 스위치가 발생한다.
