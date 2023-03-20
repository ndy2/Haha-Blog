---
tags: [data-structure]
title: Array vs. ArrayList vs. LinkedList
author: ndy2
date: 2023-03-20
description: >-
  
---
 

### 1. Array
배열의 특징
- 생성당시 크기가 결정된다.
- Heap 에서의 메모리가 선형적으로 저장된다.

배열의 장점
- index 를 통한 단건 조회 (Read) -> `O(1)`
- index 를 통한 단건 작성 (Write) -> `O(1)`

배열의 단점
- 데이터를 중간에 추가/삭제하는 연산에 취약하다.
    - 데이터를 중간에 추가하기 위해서는 데이터를 위한 공간을 생성하기 위해 해당 index 이후의 데이터를 모두 한칸씩 뒤로 밀어주는 연산이 필요하다.
    - 배열의 가장 첫 인덱스 (0) 에 데이터를 추가하고자 하는 경우 연산이 `n` 번 필요하다.
    - 삭제의 경우도 마찬가지.
- 배열의 크기는 생성시에 결정되어야 한다.

Java와 배열
    - ![[1.excalidraw.png]]

### 2. ArrayList
배열리스트 (?) 그냥 ArrayList 라고 하자.

ArrayList의 특징
- List 라고 하는 ADT (추상 자료형)을 Array 라고 하는 구체적인 방식을 통해 구현한 것.
- List 자료형이 지원해야 하는 연산에는 대표적으로
    - `get(i)`, `add(e)`, `remove(i)`, `remove(e)` 등이 있다.

ArrayList의 장점
- 배열과 달리 초기에 크기를 지정해 주지 않아도 된다.

ArrayList의 단점
- 배열을 활용하기 때문에 배열의 단점을 그대로 가져온다.
- 즉 데이터를 중간에 추가/제거하는 연산에 대해 공간을 만들고/제거하기 위해 선형적인 시간이 소요된다.

Java 와 ArrayList

