---
tags: [algorithm, union-find]
title: union by rank
date: 2023-02-04
---

@) 참고 자료

- **Union By Rank and Path Compression in Union-Find Algorithm** - on [geeksforgeeks](https://www.geeksforgeeks.org/union-by-rank-and-path-compression-in-union-find-algorithm/)

---

### 1. Worst Case

이전 시간에 다루었던 Naive Implementation 방식은 최악의 경우 find 연산에 *O(n)* 시간이 소요됩니다. 그 이유는 node 의 대표값을 찾기위한 depth 가 전체 노드의 크기와 일치 할 수 있기 때문입니다.

![[excalidraws/worst-case.excalidraw.png]]

네개의 노드를 일렬로 연결한 그래프에 대해 union-find 알고리즘을 적용하는 경우 발생할 수 있는 worst-case 를 그림으로 나타낸 것입니다. `naive implementation` 에서 `union` 연산을 적용하고자 하는 두 노드에 대해 `find` 연산을 적용 하여 같은 집합에 속해있지 않은 경우 `union` 연산을 수행합니다. 이 때 두 노드를 연결하는 연산을 `link` 로 정의 하여 Union-Find 알고리즘의 pseudo-code 를 작성해보면 아래와 같습니다.

```pseudo-code
UNION(a,b)
    sa = FIND(a)
    sb = FIND(b)
    if  sa != sb
        LINK(sa, sb)

FIND(a)
    if a == a.p
        return a
    else
        a.p = FIND(a.p)
        return a.p

LINK(pa,pb)
    pa.p = pb // or, pb.p = pa
```

여기서 문제가 되고 개선의 여지가 있는 곳은 바로 LINK 연산입니다.

생각해보면 기존의 `link` 연산에는 특별한 방향성을 적용하지 않았습니다. a 를 b 에 연결해주어도 되고 b 를 a 에 연결해 주어도 됩니다. 그렇기 때문에 구현이 간단하지만 최종적으로 생성되는 `parents` 즉, 트리구조의 모양을 제어하지 못합니다. 따라서 최악의 경우 위 그림 처럼 일자로 길죽한 트리가 생성이 되어서 `find` 연산에 `O(n)` 시간을 요구하게 됩니다.

### 2. Union By Rank

이 문제는 union by rank 최적화를 통해 해결할 수 있습니다. tree (subset, 집합) 별로 `rank` 라는 추가적인 개념을 도입하여 union 과정에서 발생할 수 있는 부당한 경우를 제거하는 것이 아이디어 입니다.

pseudo-code 는 아래와 같습니다.

```
UNION(a,b)
    sa = FIND(a)
    sb = FIND(b)
    if  sa != sb
        LINK(sa, sb)

FIND(a)
    if a == a.p
        return a
    else
        a.p = FIND(a.p)
        return a.p

LINK(pa,pb)
    if pa.r > pb.r
        pb.p = pa
    else if pb.r > pa.r
        pa.p = pb
    else 
        pa.p = pb
        pb.r ++
```

`Link` 부분만 변경되었습니다.

node 에 r 이라고 하는 추가적인 property 가 생겼습니다. 이 값은 각 tree 의 높이를 의미합니다. `Link` 를 살펴보면 rank 가 낮은 트리의 루트를 rank 가 높은 트리에 붙인 다는 것을 알 수 있습니다. 두 노드의 랭크가 같을 때는 임의의 방향으로 붙이고 붙여 진 쪽의 rank 를 1 추가해줍니다. 그림으로 살펴보면 아래와 같습니다.

![[excalidraws/union-by-rank.excalidraw.png]]

rank 를 통해 트리의 방향성을 제어 하여 최대한 tree 의 높이가 낮아져 낮은 횟수의 탐색으로 root 를 찾을 수 있도록 하는것이 union-by-rank 방식의 핵심입니다.

### 시간복잡도

union-by-rank 를 적용하면 `find`, `union` 연산의 시간복잡도는 `O(log n)` 라고 합니다. 이를 이해하기 위해서는 *amortized time complexity* 라는 개념을 이해 해야 한다고 하는데 이는 나중에 알아보겠습니다.
