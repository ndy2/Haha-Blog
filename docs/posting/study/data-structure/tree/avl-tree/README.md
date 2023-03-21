---
tags: [data-structure, tree]
title: AVL 트리
author: ndy2
date: 2023-03-21
description: >-
  
---
 
 
> [!quote] 참고 자료
> * [균형을 빡세게 유지하는 AVL 트리는 이진탐색트리의 단점을 어떻게 극복했을까요? 이진탐색트리면서도 균형을 유지하는 AVL 트리의 동작방식과 장단점을 살펴봅니다 :)](https://youtu.be/syGPNOhsnI4) - by 쉬운코드 on Youtube


### AVL 트리의 개념과 특징

- 이진 탐색 트리(BST) 의 한 종류
- 스스로 균형을 잡는 트리
    - Balance Factor 를 이용해 균형을 유지한다.

> [!note] Balance Factor
> `BF(x) = h(x.left) - h(x.right)`

> [!note] AVL 트리의 특징
> - 트리의 모든 노드들은 아래의 특징을 가진다.
>     - `BF(x) ∈ {-1,0,1}`

- 단점
    - 삽입 삭제시 루트노드까지 올라가며 BF 를 확인하고 rotate 연산을 통해 제조정 해주는 과정에 시간이 꽤 소요된다.

|        | best | avg     | ==worst== |
| ------ | ---- | ------- | ----- |
| insert | Θ(1) | O(logN) | O(logN)  |
| delete | Θ(1) | O(logN) | O(logN)  |
| search | Θ(1) | O(logN) | O(logN)  |


### 그림으로 살펴보는 AVL 트리의 균형잡기

#### 1. 오른쪽-오른쪽 편향

- `rotateLeft`

=== "step 0"

    ![[rr-0.excalidraw.png]]

=== "step 1"

    ![[rr-1.excalidraw.png]]

#### 2. 오른쪽 왼쪽 편향

- `rotateRight`
- `rotateLeft`

=== "step 0"

    ![[rl-0.excalidraw.png]]

=== "step 1"

    ![[rl-1.excalidraw.png]]

=== "step 2"

    ![[rl-2.excalidraw.png]]

