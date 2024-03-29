---
tags: [data-structure, algorithm, tree]
title: Trie
author: ndy2
---

트라이 <sup>Trie</sup> 는 *문자열의 집합*을 표현하는 트리 자료구조이다.

문자열이 다른 데이터 타입에 비해서 가지는 특징은 길이를 가진다는 것이다. 따라서 문자열의 비교는 `int`, `float` 데이터를 비교하는 것과 달리 문자열의 길이에 영향을 받는다. `Trie` 는 이를 극복하기 위한 자료구조이다.

!!! note ""

	`{"haha", "haker", "hakerton", "pin", "pine", "pinterest", "zzz"}`

위와 같은 집합을 여러 자료구조에 담아놓고 검색을 수행해보자.

- n = 7 - 문자열의 개수
- m = 9 - 문자열의 최대 길이, 삽입이나 조회 시에는 현재 문자열의 길이인 경우도 있지만 대충 문자열의 길이를 표현하는 변수로 퉁 치겠음

### 1. 배열 (Array)

![[docs/posting/study/data-structure/tree/trie/excalidraws/array.excalidraw.png]]

문자열 검색의 시간 복잡도는 `O(nm)` 이다. 

#### 1. 배열 + 이진 탐색

이진 탐색을 사용하면 문자열 검색을 `O(mlogn)` 시간으로 단축 시킬 수 있지만, 배열을 정렬 하는 초기 과정 자체에 `O(nmlogn)` 시간이 걸린다.

### 2. 해시 집합 (HashSet)

문자열 *집합* 을 저장할때 해시*셋* 을 사용하면 좋지 않을까? 해시 검색에 O(1) 타임을 지원하는 것으로 유명하다.

해시 검색에 O(1) 타임이 필요하단 내용은 항상 해시 함수를 계산하는 시간을 상수타임 이라고 가정하여 이야기 하는 것이다. 하지만 문자열의 길이를 고려한다면 O(m) 타임이 필요하다.

따라서 n 개의 문자열으로 HashSet 자료구조를 구성하는데 `O(nm)` 타임이 필요하다.

!!! note "polynomial rolling hash function"

     typical hash function for string
     자바는 p 를 31 로 설정하여 사용한다. <br>
    ![polynomial-rolling-hash-function.png](images/polynomial-rolling-hash-function.png)
    
    (수식의 m 은 hash table 의 bucket size 임)

해시셋을 이용한 검색은 해시값을 얻기만 하면 바로 bucket 의 참조를 얻을 수 있으므로 해시집합이 잘 분포되었다는 가정 하예 O(m) 이라고 얘기할 수 있다.

### 3. 트라이 (Trie)

![[excalidraws/trie-example.excalidraw.png|400]]

Trie 는 문자열 집합을 위 그림 처럼 저장한다.

트라이는 삽입시 O(m) 타임이 필요하다. 따라서 트라이를 구성하는데 O(nm) 시간 복잡도가 필요하다.

트라이에서 검색을 하기 위해서는 마찬가지로 O(m) 타임이 필요하다.

### 4. 해시 셋 Vs Trie

[참고](https://www.baeldung.com/cs/hash-table-vs-trie-prefix-tree)

해시셋과 트라이를 비교해보면 다음과 같은 차이가 있다.

|                      | Hash Set                                                                             | Trie                                                                                                                                                              | 비고                                                                            |
| -------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 삽입                 | O(m)                                                                                 | O(m)                                                                                                                                                              | m - 삽입 문자열 길이                                                            |
| 단건 검색            | O(m)<br> 해시 값 계산                                                                | O(m) <br> character 비교                                                                                                                                          | m - 검색 문자열 길이 <br> Trie 는 검색 실패시 빠른 판단 가능                    |
| 전체 검색            | O(n)                                                                                 | O(n)                                                                                                                                                              | Trie 는 전체 검색시 개별 데이터를 구성하는데 노드를 순회해야 하는 Overload 있음 |
| 공간 복잡도 (메모리) | 보통 HashCollision 을 피하기 위해 <br> 테이블을 크게 잡아 사용하기 때문에 꽤 많이 씀 | node 별 pointer 나, complete flag 필드 같은 것을 저장하기 위해 추가적인 메모리가 필요함 <br> 하지만 데이터가 많아져 prefix 간의 공유가 많아지면 어느정도 해소가능 |                                                                                 |

Trie 는 Hash Set 과 달리 자동 완성 기능과 같은 다양한 기능을 flexiable 하게 제공 할 수 있다.
