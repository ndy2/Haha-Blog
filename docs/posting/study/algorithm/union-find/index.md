---
tags: [algorithm, union-find]
title: 유니온 파인드 (Union-Find)
date: 2023-02-04
---
### 1. Union-Find 알고리즘

***Union-Find 알고리즘***은 *Disjoint-Set* 자료구조를 효율적으로 구현하기 위한 알고리즘 입니다.

Union-Find 알고리즘은 그 이름 처럼 크게 두개의 연산을 가집니다.

- *find(a)* - a 라는 원소가 속한 그룹을 찾는다.
- *union(a,b)* - 원소 a 와 b 를 *union* 즉, 같은 집합으로 합칩니다.

### 2. Naive Implementation

#### 1. union(a,b), find(a) 메서드

다양한 방법이 있겠지만 저는 흔히 아래 방식을 활용합니다.

```kotlin
lateinit var parents : IntArray // 노드의 부모 (대표값)

fun union(a: Int, b: Int) {  
    val pa = find(a)  
    val pb = find(b)  
  
    if (pa != pb) {  // 두 노드의 부모가 다르면 
        parents[pa] = pb  // 둘중 하나의 부모를 바꿔준다.
    }  
}  
  
fun find(a: Int): Int {  
    if (parents[a] == a) {  // 초기상태 (자기 자신을 가르키는 경우) 에는 자기자신 리턴
        return a  
    } else {  
        parents[a] = find(parents[a])  
                // 연쇄적인 find 를 통해 부모를 바꿈
                // this is called path compression!
        return parents[a]  // 업데이트 된 부모 인덱스 반환
    }  
}
```

#### 2. 활용

아래 그래프에 대해 Union-Find 알고리즘을 적용해 보겠습니다.

![[excalidraws/graph.excalidraw.png]]


union-find 알고리즘은 흔히 배열을 이용해 구현됩니다.

1. 최초 각 node 는 자기자신을 가르킵니다. 
```kotlin
var n = 7
parent = IntArray(n+1) {it} // [0,1,2,3,4,5,6,7]
```

2. edge 를 추가하면 양옆 노드에 대해 union 연산을 적용합니다.
```kotlin
var edges = arrayOf(
    Edge(1,2), Edge(2,3)
    Edge(4,5), Edge(5,6), Edge(6,4)
)

for (edge in edges){
   val (a,b) = edge
   union(a,b)
}
```

3. parent 배열을 통해 임의의 노드가 같은 집합에 속해있는지 알 수 있습니다.
```kotlin
fun isInSameSet(a: Int, b: Int){
  return find(a) == find(b)
}
```


### 3. 생각 할 거리

#### 1. `Parents` 배열의 의미

최종적으로 생성된 parents 배열을 출력해보면 다음과 같습니다. 이를 그림으로 나타내면 아래와 같습니다.

`union 적용 전`

![[excalidraws/graph-before.excalidraw.png]]

`union 적용 후`

![[excalidraws/graph-after.excalidraw.png]]

1번 노드를 보면 `parents` 배열은 그 자체가 disjoint-set 의 대표값을 표현하지는 못하지만 `find` 를 연쇄적으로 호출함으로써 결국 자신의 대표값을 찾을 수 있다는 것을 알 수 있습니다.

#### 2. 시간 복잡도

`union` - 두번의 `find` 연산으로 이루어집니다.
`find` - worst case 에 대입 연산(O(1))이 노드의 숫자번 (n 번) 발생합니다. 즉, `O(n)` 입니다.

즉 두 연산 모두 O(n) 시간 복잡도를 가집니다.

### 3. 개선

- Naive Implementation 방식은 O(logN) 시간 복잡도를 가지는 *Union by Rank or Height*,  *Path Compression* 방식으로 개선 될 수 있습니다.
- 또한 만약 node 1 이 속한 집합의 노드를 모두 알고 싶다면 현재 방식에서는 효율적이지 않습니다. 이는 parents 배열이 tree 형태가 아니라 circular-linked-list 형태를 띄도록 구현하여 효율적으로 구할 수 있습니다.
