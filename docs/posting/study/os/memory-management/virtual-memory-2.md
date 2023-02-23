---
tags: [os]
title: Virtual Memory 2
---
메모리 관리자 MMU 세가지 정책에 따라 메모리를 관리한다.

-   `fetch` 정책
    -   프로세스가 필요로 하는 데이터를 언제 메모리로 가져올지 결정
    -   demand paging, pre-fetch
-   `placement` 정책
    -   데이터를 메모리의 어느 위치에 올려놓을지 결정
    -   paging, segmentation, segmentated-paging
-   `replacement` 정책
    -   메모리가 꽉 찼을 때 메모리 내에 있는 어떤 프로세스를 내보낼지 결정

###  1. fetch 정책 - Demand Paging

#### Demand Paging

-   프로세스가 요청할 때 메모리로 가져오는 일반적인 MMU의 fetch 정책
-   운영체제는 프로세스를 구성하는 모듈을 전부 메모리에 올리지 않는다.
-   필요한 모듈만 메모리에 올려 실행하고 나머지 모듈은 필요하다고 판단될 때 메모리로 불러온다.
-   이를 통해 메모리를 효율적으로 관리하고 응답 속도를 향상 시킬 수 있다.

#### Page Table Entry

![[images/page-table-entry.png|PTE (Page Table Entry)]]
`access bit`

-   메모리에 올라 온 후 사용한 적이 있는지 알려주는 비트
-   a.k.a. referece bit

`modified bit`

-   페이지가 메모리에 올라온 후 데이터의 변경이 있었는지 알려주는 비트
-   a.k.a. dirty bit

`valid bit`

-   페이지가 램에 있는지를 나타내는 비트
-   1 이라면 주소 필드에 스왑 영역 내 페이지의 주소가 저장된다 (2차 메모리) ~ page fault
-   0 이라면 주소 필드에는 프레임 번호가 저장된다.
-   a.k.a. present bit

`write, read, excute bit`

-   페이지에 대한 쓰기, 읽기, 실행 권한을 나타낸다.

#### Page fault

-   프로세스가 요청한 페이지가 메모리에 없고 스왑 영역에 있을때 (valid bit 가 1 일때)
-   MMU 는 replacement policy 에 따라 해당 페이지를 스왑 영역에서 램으로 옮겨야 한다.

![[images/page-fault.png|page fault]]

### 2. replacement 정책(페이지 교체 알고리즘)

-   무작위, FIFO
-   최적
-   LRU - 시간적으로 멀리 떨어진 페이지를 스왑 영역으로 보낸다.
-   LFU - 사용 빈도가 적은 페이지를 스왑 영역으로 보낸다.
-   NUR - 최근에 사용한 적이 없는 페이지를 스왑 영역으로 보낸다.