---
tags: [data-structure, algorithm, tree]
title: Segment Tree
author: ndy2
---

@ 참고 자료)

- 개발자 영맨 - [[Range Query] Segment Tree 1/2 - introduction](https://youtu.be/075fcq7oCC8)

### 1. 세그먼트 트리 (Segment Tree)의 정의와 의문점

!!! quote "Segment Tree on [wikipedia](https://en.wikipedia.org/wiki/Segment_tree)"

    세그먼트 트리<sup>segment tree</sup> (a.k.a. statistic tree)는 Interval 이나 Segment 에 대한 정보를 저장하기 위한 트리 자료 구조입니다. 세그먼트 트리에 저장된 세그먼트가 주어진 point 를 포함하고 있는가 질의 할 수 있습니다. 원칙적으로 세그먼트 트리는 static structure 이며 한번 구성되면 수정 될 수 없습니다. 비슷한 자료구조에는 interval tree 가 있습니다.

![[excalidraws/segment-tree.excalidraw.png]]

---

제가 헷갈렸던 부분은 위 Segment Tree 의 정의에 보이는 Interval Tree 와의 의미적인 차이입니다. 특히 용어의 번역에 대한 부분에서 혼란스러운 점이 많았습니다. 

!!! warn "헷갈렸던 번역들"

    [In Mathmatics] <br>
     - (line) segment -> 선분
    - interval -> 구간
    
    [In Computer Science] - 번역이 상당히 헷갈립니다. <br>
    - segment tree 
        - 구간 트리 (?)
        - 근데 사실 선분 트리도 이상함
        - 각 노드에 저장되는 정보는 구간의 통계정보가 맞다
    - interval tree
        -  간격 트리
        -  얘는 뭔지 아직 잘 모름 T.T

앞으로는 헷갈리지 않게 세그먼트 트리 혹은 Segment Tree 라고 영어 이름을 그대로 사용하겠습니다. 그리고 Interval Tree 를 포함해서 Binary Indexed Tree 나 Range Tree 등 Segment Tree 와 유사한 아이디어의 트리 자료구조가 많은데 이들에 대해서도 추후에 학습하고 정리하겠습니다. - [관련 질의 on Stack Overflow](https://stackoverflow.com/questions/17466218/what-are-the-differences-between-segment-trees-interval-trees-binary-indexed-t/)

---

### 2. 세그먼트 트리의 특징과 동작

#### 1. 특징

주어지는 연속된 데이터에 대한 구간 연산 (update, query)을 O(logn) 시간에 할 수 있는 자료구조

- update : 특정 위치 (또는 구간)에 대한 업데이트를 O(logn) 에 가능
- query : 구간에 대한 연산을 O(logn) 에 계산

![[images/segment-tree.png]]

- 세그먼트 트리는 자신의 구간을 반으로 나누어 자식 노드에게 나누어준다.
- :warning: 일반적으로 Complete Binary Tree 아님

```
                           |_0,5_|
                    ______/     \_______
                   |_0,2_|       |_3,5__|
                 _/     |       |       \_
             ____/_    __|       |____     \____
            |_0,1_|  |_2_|      |_3,4_|    |_5_|
           _/__  ___|             |___   \____
         |_0__| |_1_|            |_3_|   |_4_|
```

#### 2. 동작 - Query

!!! note ""

    이미 구성된 트리의 값 중 쿼리의 범위를 포함하는 큰 구간의 값을 계속 찾아 재귀적으로 연산한다.

![[excalidraws/segment-tree-query.excalidraw.png]]

#### 3. 동작 - Update

!!! note ""

    업데이트 하는 구간을 포함하는 범위의 트리의 값을 모두 업데이트 한다.

![[excalidraws/segment-tree-update.excalidraw.png]]

### 4. 세그먼트 트리의 구현과 관련 문제

#### 1. 구현

- 세그먼트 트리는 root 부터 차례대로 1부터 시작하는 번호(segment index) 를 부여한다. 따라서 보통 left 나 right 포인터를 두거나 하지는 않는다.
- 규칙: 왼쪽 자식 : `idx*2` , 오른쪽 자식 : `idx*2+1` 

![[excalidraws/segment-tree-index.excalidraw.png]]

- 보통 Segment Tree 의 배열 크기는 `4 * n` 으로 잡고 시작하는 경우가 많다. 그 이유는 수학적으로 `(최대 segment Index) / n` 의 값이 n 이 무한대로 향함에따라 4 의 아래에서 4로 수렴 함이 증명되었기 때문이다. - [관련 링크와 증명](https://www.quora.com/Why-does-4-*-N-space-have-to-be-allocated-for-a-segment-tree-where-N-is-the-size-of-the-original-array)

#### 2. 관련 문제와 풀이

{{ boj(":g1: 커피숍2", 1275) }} 

- {{ ps("src/자료구조/세그먼트트리/boj/Main_커피숍2_1275.kt") }}
- 구간 합을 저장하는 세그먼트 트리를 구성하고 구간 쿼리와 포인트 업데이트를 수행하는 문제이다.
- 이 문제의 풀이를 통해 Segment Tree 의 구현을 알아보자!

``` kotlin title="구간합 세그먼트 트리"
class Solution_커피숍2(
    val n: Int,         // 데이터의 크기
    val arr: IntArray   // 데이터 배열
) {
    var tree: LongArray = LongArray(4 * n);  // tree 의 크기는 4 * n 으로 초기화

    init {
        initTree(0, n - 1, 1) 
        // 초기화 블럭에서 arr[0] ~ arr[n-1] 위치의 트리 초기화를 segment index 1번 부터 수행
    }

    // op - operation : {x,y,a,b}
    fun proc(op: IntArray) {
        // 1. x ~ y 의 구간합을 출력하고
        println(getRangeSum(0, n - 1, 1, min(op[0], op[1]) -1, max(op[0], op[1]) -1))

        // 2. arr[a-1] 의 값을 b 로 업데이트 
        update(0, n - 1, 1, op[2] - 1, op[3].toLong() - arr[op[2] - 1] )
        
        // 트리업데이트 후 배열도 업데이트, 굳이 안해줘도 되긴함
        arr[op[2] - 1] = op[3] 
    }

    /* 
    @param : start - 데이터 배열의 시작 인덱스 (inclusive)
             end   - 데이터 배열의 끝 인덱스   (inclusive)
             idx   - 현재 업데이트 하고자 하는 segment index 
    */
    private fun initTree(start: Int, end: Int, idx: Int) {
        // start == end -> leaf node 를 의미한다.
        if (start == end) {
            // 배열의 위치 값을 그대로 트리에 대입한다.
            tree[idx] = arr[start].toLong()
        } else {
            val mid = (start + end) / 2

            // 구간을 나누어 왼쪽 자식, 오른쪽 자식의 initTree 를 재귀적으로 호출한다.
            initTree(start, mid, idx * 2)
            initTree(mid+1, end, idx * 2 + 1)

            // 자신의 tree 값을 자식의 tree 값을 통해 초기화함  
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        }
    }

    /*
     @param : start - 데이터 배열의 시작 인덱스 (inclusive)
              end   - 데이터 배열의 끝 인덱스 (inclusive)
              idx   - 현재 탐색 중인 노드의 segment index
              l     - 쿼리 구간의 왼쪽 인덱스 (inclusive)
              r     - 쿼리 구간의 오른쪽 인덱스 (inclusive)
    */
    private fun getRangeSum(start: Int, end: Int, idx: Int, l: Int, r: Int): Long {
        // l 이 end 보다 크거나 start 가 r 보다 작으면
        // 현재 노드가 표현하는 구간은 쿼리 구간과 겹치는 구간이 없다. 바로 0 리턴
        if (l > end || start > r) return 0

        // start 와 end 모두 l 과 r 사이에 있으면
        // 현재 쿼리 구간을 완전히 포함한다. 
        // 현재 노드의 값 바로 리턴. 더이상 자식 노드를 탐색할 필요가 없다.
        else if (l <= start && end <= r) return tree[idx]
        else {
            // 위 두경우가 모두 아니라면
            // 현재 노드가 표현하는 구간은 쿼리 구간을 일부 포함한다.
            // 자식 노드를 탐색하여 두 값을 연산하여 리턴
            val mid = (start + end) / 2
            return getRangeSum(start, mid, idx * 2, l, r) +
                    getRangeSum(mid+1, end, idx * 2 + 1, l, r)
        }
    }

    /*
    @param : start - 데이터 배열의 시작 인덱스 (inclusive)
             end   - 데이터 배열의 끝 인덱스 (inclusive)
             idx   - 현재 탐색 중인 노드의 segment index
             target - 업데이트 하고자 하는 노드의 데이터 배열 인덱스
             amount - 업데이트 하고자 하는 양
    */
    private fun update(start: Int, end: Int, idx: Int, target: Int, amount: Long) {
        // target 이 start 보다 작거나 end 보다 크다면
        // 현재 노드는 업데이트 하고자 하는 target 의 값을 포함 하지 않는다 바로 리턴
        if (target < start || target > end) return

        // 그런지 않으면서 start == end 라면
        // 리프 노트이다. 자신의 값을 amount 만큼 업데이트 한다.
        if (start == end) {
            tree[idx] += amount

        // 타겟을 포함하는 구간이면서 리프노드가 아닌 경우
        // 현재 노드의 구간 어딘가에는 target 이 포함 되어 있다.
        // 자식 노드에 나누어 update 한다.
        // 그 값을 바탕으로 자신의 값도 update 한다.
        } else {
            val mid = (start + end) / 2
            update(start, mid, idx * 2, target, amount)
            update(mid+1, end, idx * 2 + 1, target, amount)
            tree[idx] = tree[idx*2] + tree[idx*2+1]
        }
    }
```

### 5. 더 알아볼 주제 들

#### 1. 비슷한 자료구조 들

맨 위에서 이야기 했듯이

- segment trees, 
- interval trees, 
- binary indexed trees 
- range trees

를 비교하며 학습해보면 좋을 것 같다.

#### 2. 다차원 응용

- 세그먼트 트리는 다차원에 대해서도 일반화할 수 있다.
    - https://youtu.be/kKlZ9B3cS14
    - https://en.wikipedia.org/wiki/Segment_tree#Generalization_for_higher_dimensions

#### 3. Range Query 에 대한 솔루션 정리

- 세그먼트 트리는 업데이트가 가능한 데이터의 구간에 대한 범위 쿼리를 해결하는 자료구조/알고리즘이다.
- 다음 영상에 대부분의 Range Query 에 적용할 수 있는 자료구조/알고리즘을 소개한다. 물론 만능은 없고 상황에 맞게 사용해야한다.
- 이들을 정리/학습 하면 좋을것 같다.
- [링크](https://youtu.be/b_rsXu1pn08)
