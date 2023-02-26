---
tags: [architecture]
title: Consistent Hash
date: 2023-02-09
---

@참고 자료)

- `『System Design Interview/가상 면접 사례로 배우는 대규모 시스템 설계 기초』` by Alex Xu/ 알렉스 쉬 - [yes24](http://www.yes24.com/Product/Goods/102819435)
    - 5장 안정 해시 설계
---

### 1. Rehash Problem

N 개의 서버에 부하를 균등하게 나누는 보편적인 방법은 해시 함수를 이용하는 것이다.

```text title="해시 값에 modulo 를 이용해 서버 인덱스를 얻을 수 있다."
serverIndex = hash(key) % N
```

이 방법은 server pool 의 크기 (N) 이 고정되어 있고 데이터 분포가 균등하다면 잘 동작한다. 해시가 잘 동작한다는 의미는 결과적으로 데이터가 모든 서버에 균등하게 분포된다는 의미이다.

!!! note ""

    * 서버는 일반적으로 `노드`라고 표현되기도 한다.
    * 데이터 베이스 서버에 대해서는 Shard, 혹은 데이터베이스 schema 에 대해서는 Partition 이라는 표현을 사용하기도 한다.

세상에서 가장 단순한 위와 같은 구현은 N 이 변경되는 경우 결과 `serverIndex` 가 예측할 수 없이 변경되고 이에 따라 보든 데이터의 해시값을 새로 구하여 변경된 `serverIndex` 의 서버가 해당 데이터를 처리할 수 있도록 해주어야 한다.

- 만약 해당 서버가 데이터베이스의 `Shard` 로 동작 하고 있다면 데이터를 모두 재배치 하는 `resharding` 작업이 필요하다.
- 만약 해당 서버가 캐시 서버로 동작하고 있었다면? 답이 없다. 대규모 `cache miss` 가 발생하게 될 것이다.

### 2. 안정 해시

!!! quote "Consistent Hashing on [Wikipedia](https://en.wikipedia.org/wiki/Consistent_hashing)"

    In computer science, consistent hashing is a special kind of hashing technique such that when a hash table is reside, *only `n/m` keys* need to be remapped on average where n is the number of keys and m is the number of slots <br>
    In contrast, in most traditional hash tables, a chage in the number of array slots causes *nearly all keys* to be remapped because the mapping between the keys and the slots is defined by a *modular operation*

### 3. 해시 공간과 해시 링

- `hash space` - `hash function` 의 공역
- `hash ring` - `hash space` 를 환형으로 이해하는 것

![[excalidraws/hash-ring-1.excalidraw.png]]

- Consistent Hash 에서 Key 가 서버를 조회하기 위해서 modulo 연산을 하는 것이 아니라 시계방향으로 탐색을 한다.
- 이 방식 만으로 서버를 추가/제거 했을때 예측할 수 없는 형태로 대부분의 데이터에 대해서 자신의 대상 서버가 변경되는 현상을 피할 수 있다.
    - 물론 해시를 적용한 다음에 hash ring 위에서 예측가능 하므로 이 방식도 모든 데이터에 대해 hash 값을 새로 계산해 보아야 하는 것은 변함없다.
- 하지만 이 기본 구현법만으로는 서버가 추가되거나 삭제되는 상황에 따라 파티션 (인접한 서버 사이의 해시 공간)의 크기를 균등하게 유지하는 것이 불가능 하다. 따라서 데이터의 균등 분포를 보장 할 수 없다.
- 이 문제를 해결 하기 위에 제안된 기법이 가상 노드<sup>virtual node</sup> 또는 레플리카<sup>replica</sup> 라 불리는 기법이다.

#### 가상 노드

- 가상 노드는 실제 노드 또는 서버를 가리키는 노드이다.
- 키가 서버를 시계 방향으로 탐색하다 가상 노드를 만나도 실제 노드를 조회 한 것과 동일하게 취급한다.

![[excalidraws/virtual-node.excalidraw.png]]

- 가상 노드를 많이 사용할 수록 키의 분포를 균등하게 만들 수 있다.
- 그러나 가상 노드 데이터를 저장할 공간은 더 많이 필요해 진다. `tradeoff` 가 필요하다.

![[excalidraws/virtual-node-add.excalidraw.png]]

- 위 그림들에서 가상 노드의 위치를 실제 서버의 해시값을 시작으로 `Hash Table Size / Number of Virtual Nodes` 만큼 시계방향으로 rotate 한 위치로 가정했는데 이 방법이 일반적인지는 잘 모르겠다.
