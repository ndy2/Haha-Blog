---
tags: [os, memory]
title: 메모리 관리 개요
author: ndy2
date: 2023-04-13
description: >-
  
---
 
 
> [!quote] 참고 자료
> * 한국기술교육대학교 - 김덕수교수님 - Lec8 Memory Management
> 	* [`『Background』`](https://youtu.be/es3WGii_7mc)
> * Memory Allocation Techniques on geeksforgeeks
> 	* [`『Mapping Addresses to Physical Address』`](https://www.geeksforgeeks.org/memory-allocation-techniques-mapping-virtual-addresses-to-physical-addresses/)

### 메모리의 종류/ 계층구조 요약

![[memory-hierarchy.excalidraw.png]]

### Address Binding

![[address-binding.excalidraw.png]]

![[source-to-execute.excalidraw.png]]

* 프로그램의 논리 주소를 실제 메모리의 물리 주소로 매핑하는 작업

#### Compile time Binding

* 프로세스가 메모리에 적재될 위치를 컴파일러가 알 수 있는 경우
* 프로그램 전체를 메모리에 올려야함

#### Load time Binding

* 메모리 적재 위치를 컴파일 시점에 모르면, 상대 주소를 생성
* 로드 타임에 시작 주소를 반영하여 사용자 코드 상의 주소를 재설정
* 프로그램 전체가 메모리에 올라가야 함

#### Run time Binding

* Address binding 을 실행 시점까지 연기
* HW (MMU)의 도움이 필요하다
* 대부분의 OS 에서 사용

![[dynamic-relocation.png|Dynamic relocation using a relocation register.]]

1. CPU will generate logical address for eg: 346
2. MMU will generate a relocation register (base register) for eg: 14000
3. In memory, the physical address is located eg:(346+14000= 14346)

![[address-mapping.png|MMU = Limit(boundary) Register + Relocation Register]]
