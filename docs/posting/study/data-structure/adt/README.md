---
tags: [data-sturcture]
title: ADT
author: ndy2
---

### 1. 추상 자료 구조 (ADT)

나는 이 용어를 컴퓨터 공학을 전공한 첫 학기에 들었다. 하지만 최근 OOP 를 학습하고 ADT 를 강조하는 몇몇 영상을 본 이후에서야 이 단어의 정확한 의미와 중요성을 알게되었다.

`Abstract Data Type (ADT)` 는 OOP 에서의 interface 혹은 abstract class 와 같다. 이들은 구체적인 구현방법을 포함하지 않고 자료에게 수행할 수 있는 연산의 집합으로만 정의된다.

예를 들어 `List` 는 일렬로 나열한 원소의 모임으로 정의된다. 나머지는 없다.

- List 내부의 자료구조가 실제 메모리상에 일렬로 배치되든 (`ArrayList`) 
- 참조를 통한 링크로 연결되어 순서를 가지든 (LinkedList) 

이들은 모두 `List` 이다.

### 2. 목표

요 자료구조 파트에서는 최대한 ADT 와 실제 구현 자료구조가 가지는 특성을 분리해서 생각하고 디테일한 자료구조가 가지는 특징을 자세히 알아보겠다.

!!! note ""

    Special Thanks to 쉬운코드 on https://www.youtube.com/@ez.
