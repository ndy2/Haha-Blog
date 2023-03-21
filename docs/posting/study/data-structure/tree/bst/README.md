---
tags: [data-structure, tree]
title: 이진 탐색 트리
author: ndy2
date: 2023-03-21
description: >-
  이진 탐색 트리에 대해 알아보자.
---
 
 
> [!quote] 참고 자료
> - [이진탐색트리](https://ko.wikipedia.org/wiki/이진탐색트리) on wikipedia
> - [이진탐색트리(binary search tree)를 설명합니다~ 기본 개념과 트리를 순회하는 여러 방법, 이진탐색트리의 삽입/삭제/검색이 어떻게 동작하는지 예를 통해 설명드려요 :)](https://youtu.be/i57ZGhOVPcI) by 쉬운코드 on Youtube

### 1. 정의와 특징.

> [!note] 이진 탐색 트리의 속성
> 이진 탐색 트리 <sup>Binary Search Tree</sup> 는 다음과 같은 속성이 있는 이진 트리 자료 구조이다.
> - 각 노드에 값이 있다.
> - 값들은 전 순서가 있다.
> - 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을 지닌 노드들로 이루어져 있다.
> - 노드의 오른쪽 서브트리에는 그 노드의 값보다 지닌 노드들로 이루어져 있다.
> - 좌우 하위 트리는 각각이 다시 이진 탐색 트리여야 한다.

> [!note] 이진 탐색 트리의 특징
> * 최솟값은 트리의 가장 왼쪽/ 최댓값은 트리의 가장 오른쪽에 위치한다.
> * 삽입/삭제가 유연하다.
> * Worst Case 에대한 대응이 불가능하다.

> [!note] BST 와 중복 값 처리 - [참고 링크](https://www.geeksforgeeks.org/how-to-handle-duplicates-in-binary-search-tree/)
> - BST 는 기본적으로는 distinct 한 key 를 가진다.
> - 하지만 중복키를 포함하고 싶다면?
>     - 오른쪽에 넣은것 처럼 취급하기 or
>     - 카운트를 보관하기

### 2. 삽입 삭제 검색 연산의 시간복잡도

|        | best | avg     | worst |
| ------ | ---- | ------- | ----- |
| insert | Θ(1) | O(logN) | Θ(N)  |
| delete | Θ(1) | O(logN) | Θ(N)  |
| search | Θ(1) | O(logN) | Θ(N)  |

```kotlin title="공통 코드"
data class Node(
	val value: Int,
){
    var left: Node? = null
    var right: Node? = null
}

fun main() {
    val root = Node(10)
    val left = Node(7)
    val right = Node(13)
    
    root.left = left
    root.right = right
}
```

### 2. 순회

- 중위 순회 (inorder traversal)

```kotlin
fun inorder(n: Node){
    n.left?.let {inorder(it)}
    print("${n.value} ")
    n.right?.let {inorder(it)}
}

fun main() {
    val root = getRoot()
    inorder(root) // "7 10 13 "
}
```

    - BST 에 중위 순회를 적용하면 값이 순서대로 출력된다.

- 전위 순회 (preorder traversal)

```kotlin
fun preorder(n: Node){
    print("${n.value} ")
    n.left?.let {preorder(it)}
    n.right?.let {preorder(it)}
}

fun main() {
    val root = getRoot()
    preorder(root) // "10 7 13 "
}
```

- 후위 순회 (postorder traversal)

```kotlin
fun postorder(n: Node){
    n.left?.let {postorder(it)}
    n.right?.let {postorder(it)}
    print("${n.value} ")
}

fun main() {
    val root = getRoot()
    postorder(root) // "7 13 10 "
}
```


### 2. 검색.

```java
Node search(Node p, int value){
    // 현재 노드의 값과 일치하는 경우 리턴
    if(p.value == value){
        return p;
    }
    // 현재 노드의 값 보다 작은 경우 왼쪽 탐색
    else if(p.value > value){
        if(p.left == null){
            return null;
        }else{
            // 왼쪽 노드에 대해서 재귀적 탐색
            return search(p.left, value);
        }
    }
    // 현재 노드의 값 보다 큰 경우 오른쪽 탐색
    else {
        if(p.right == null){
            return null;
        }else{
            return search(p.right, value);
        }
    }
}
```

### 3. 삽입.

```java
void insert(Node p, int value){
    if(p.value < value){
        if(p.right != null){
            insert(p.right, value);
        }else {
            p.right = new Node(value);
        }
    }else if (p.value > value){
        if(p.left != null){
            insert(p.left, value);
        }else {
            p.left = new Node(value);
        }
    }else {
        // ??
    }
}
```

### 4. 삭제.

- 삭제할 노드의 자녀가 두개인 경우
    - 오른쪽 자녀의 서브 트리 중 제일 값이 작은 노드가 삭제할 노드를 대체하게 한다.
    - 반대도 가능
- 삭제할 노드의 자녀가 하나인 경우
    - 삭제할 노드의 부모가 삭제할 노드를 가르키도록 한다.