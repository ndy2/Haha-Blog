---
tags: [data-structure, tree]
title: Red-Black Tree
author: ndy2
date: 2023-03-22
description: >-
  
---
 
 
> [!quote] 참고 자료
> * [Red/Black Tree visualization](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html) @ usfca
> * 쉬운코드 on Youtube - 레드블랙트리(red-black tree)
>     - [1부 - 개념, 특징, 삽입](https://youtu.be/2MdsebfJOyM)
>     - [2부 - 삭제, 시간복잡도, AVL 트리와의 비교](https://youtu.be/6drLl777k-E)

### 1. 개념.

> [!note] Red-Black 트리
> - 이진 탐색 트리 (BST)의 한 종류
> - 스스포 균형 잡는 트리
> - BST 의 worst case 의 단점을 개선한다.
>     - 트리의 편향을 막는다.

> [!note] NIL 노드
> - 존재하지 않음을 의미하는 노드
> - 자녀가 없을 때 자녀를 NIL 노드로 표기
> - 값이 있는 노드와 동등하게 취급
> - RB 트리에서 leaf 노드는 NIL 노드

> [!success] Red-Black 트리가 만족하는 속성
> 1. 모든 노드는 red 혹은 black
> 2. 루트 노드는 black
> 3. 모든 NIL(leaf) 노드는 black
> 4. red의 자녀들은 black `or` red가 연속적으로 존재할 수 없다.
> 5. 임의의 노드에서 NIL 노드 까지 가는 경로의 Black 수는 같다. (자기 자신은 제외) - `Black Height`

> RB 트리는 삽입/삭제 시 주로 #4, #5를 위반하며 이들을 해결하려 구조를 바꾸다 보면 자연스럽게 트리의 균형이 잡히게 된다.

### 2. 삽입

- 일반적인 BST 의 삽입 과정과 동일하다.
- 삽입하는 노드의 색깔은 red
- 속성의 위반이 발생하면 재조정 

 #### 1. `insert(50)` -> `insert(20)` -> `insert(10)` 에서 마지막 `insert(10)` 을 처리 하는 과정

=== "step 1"

    ![[rb-tree-insert-1.excalidraw.png]]

=== "step 2"

    ![[rb-tree-insert-2.excalidraw.png]]

=== "step 3"

    ![[rb-tree-insert-3.excalidraw.png]]


#### 2. `insert(50)` -> `insert(20)` -> `insert(40)` 에서 마지막 `insert(40)` 을 처리 하는 과정

=== "step 1 - basic insert"

    ![[1.png]]
    Found null tree (or phantom leaf), inserting element
    Node and parent are both red.
    Node is right childe, parent is left chide -> rotate

=== "step 2 - single rotate left"

    ![[2.png]]
    Node and parent are both red.
    Node is left childe, parent is left chide
    -> Can fix extra redness with a single rotation

=== "step 3 - single rotate right"

    ![[3.png]]

=== "step 4 - update colors"

    ![[4.png]]

#### 3. 위 상태에서 `insert(30)` 을 처리하는 과정

=== "step 1"

    ![[a.png]]
    
    Node and parent are both red. Uncle of node is red
    -- push blackness down from grandparent

=== "step 2"

    ![[b.png]]
    Root of the tree is red. Color it black

=== "step 3"

    ![[c.png]]

### 3. 삭제.

1. 일반적인 BST 처럼 삭제
2. 삭제 후 속성 위반 여부를 확인하고 재조정

- Step 1. 삭제되는 노드의 색 확인
    - 삭제되는 노드의 색
        - 자녀가 두개 라면 successor 의 색
        - 그렇지 않다면 자신의 색
    - 삭제되는 색이 red 라면 어떠한 속성도 위반하지 않는다.
- Step 2. 삭제 후 재조정

### 4. 시간 복잡도

|        | best | avg     | ==worst== |
| ------ | ---- | ------- | ----- |
| insert | Θ(1) | O(logN) | O(logN)  |
| delete | Θ(1) | O(logN) | O(logN)  |
| search | Θ(1) | O(logN) | O(logN)  |

### 5. AVL 트리와의 비교

 
> [!quote] 참고 자료
> * ebongzzang - [RB Tree](https://ebongzzang.github.io/algorithm/Red-Black-tree-그리고-AVL-tree와의-비교/#avl-tree와-비교)

|                 | RB tree                                                   | AVL tree                            |
| --------------- | --------------------------------------------------------- | ----------------------------------- |
| BST             | Yes                                                       | Yes                                 |
| time complexity | O(logN)                                                   | O(logN)                             |
| 삽입/삭제       | AVL 보다 빠름                                             | RB 보다 느림                        |
| 검색            | AVL 보다 느림                                             | RB 보다 빠름                        |
| self-balancing  | r/b 속성을 만족                                           | balance factor 를 통해              |
| 활용            | linkx kernel 내부 <br> Java TreeMap <br> c++ std::map ... | dictionary<br> 검색이 대부분인 경우 |

