---
tags: [os]
title: Virtual Memory 1
---

![[images/virtual-memory.png|가상 메모리 구조]]

`가상 메모리`를 통해 프로세스가 물리 메모리의 크기와 상관없이 메모리를 마음대로 사용할 수 있다.

`가상 메모리` = `램 메모리`(1차 메모리) + `스왑 영역`(2차 메모리)

DAT (Dynamic Address Transformation)

- 동적 주소 전환
- 가상 주소를 물리 주소로 변경하는 과정

### 페이징

![[images/paging.png|페이징]]

- DAT : VA=<p,offset> → PA =<f, offset>
- 사실 page table도 사용시에는 메인 메모리의 커널 영역에 있음
- 페이지 테이블도 스왑 인, 아웃의 대상이 됨 (연관 매핑 방식, TLB)
- 프로세스는 PCB에 PTBR(페이지 테이블의 시작 주소 레지스터)을 저장하여 페이지 테이블을 빠르게 찾음

### 세그멘테이션

![[images/segmentation.png|세그멘테이션]]

DAT : VA=<s,offset> → 물리주소

### 세그멘테이션-페이징

![[images/segmented-paging.png|세그멘테이션-페이징]]

The advantages of segmented paging are-

- Segment table contains only one entry corresponding to each segment.
- It reduces memory usage.
- The size of **Page Table** is limited by the segment size.
- It solves the problem of external fragmentation.

The disadvantages of segmented paging are-

- Segmented paging suffers from internal fragmentation.
- The complexity level is much higher as compared to paging.
