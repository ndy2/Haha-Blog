---
tags: [kotlin,sort]
title: Kotlin의 정렬 API
author: ndy2
date: 2023-04-15
description: >-
  
---

### 0. 들어가며
사실 `Java`의 정렬은 매우 불편하고 헷갈린다. `comparable`, `comparator` 등 비슷하고 다양한 인터페이스, `compareTo`의 결과 값이 음수면 어떻고 양수면 어떻게 정렬될까? 이는 어떻게 동작하는것일까? 등등 Java를 활용하다 보면 정렬 API가 아주 헷갈린다. 

`kotlin`은 `Java`에 비해 훨씬 다양하고 발전된 정렬 API를 제공한다. 이를 잘아는 것은 우아한 코틀린 활용에 매우 중요하다! `IntelliJ`의 도움이 없더라도 능숙하게 다양한 형태의 정렬을 할 수 있도록 정리하고 연습하자. 이를위해 정렬 API의 네이밍 규칙과 동작방식에 대해서도  이해해보자.

또한 알고리즘 문제를 풀다보면 자주 만나는 문제인 정렬에 따른 최댓값/최솟값의 `index` 를 구하는법 에대해서도 정리해보자.

### 1. `Collections.sortedXXX`

기본타입 (정수)의 리스트, 배열의 정렬 API를 알아보자.

```kotlin title="sortedXXX"
fun main() {  
    val list = listOf(1, 10, 5, 3, 2, 7)  
    println("list.sorted() : ${list.sorted()}")  
    println("list.sortedDescending() : ${list.sortedDescending()}")  
    println("list.sortedBy { it } : ${list.sortedBy { it }}")  
    println("list.sortedWith(compareBy { it }) : ${list.sortedWith(compareBy { it })}")  
    println("list.sortedByDescending { it } : ${list.sortedByDescending { it }}")  
}
```

```text title="실행 결과"
list.sorted() : [1, 2, 3, 5, 7, 10]
list.sortedDescending() : [10, 7, 5, 3, 2, 1]
list.sortedBy { it } : [1, 2, 3, 5, 7, 10]
list.sortedWith(compareBy { it }) : [1, 2, 3, 5, 7, 10]
list.sortedByDescending { it } : [10, 7, 5, 3, 2, 1]
```

모두 예상가능한대로 동작하였다. 여기서 눈여겨 보아야 잘 점은 위 함수는 모두 `sortedXXX` 라는 함수 이름을 가지고 있다. 즉 반환값으로 정렬된 리스트를 반환한다는 점이다.

이들의 구현을 하나하나 살펴보자.

#### 1. T가 Comparable 한 경우 활용할 수 있는 `sorted()`, `sortedDescending()`

가장 쉽게 적용할 수 있는 `sorted()` 함수는 다음과 같이 정의되어 있다.
```kotlin
public fun <T : Comparable<T>> Iterable<T>.sorted(): List<T> {  
    if (this is Collection) {  // receiver object이 Collection 이라면 
        if (size <= 1) return this.toList()  
        
        // 배열로 만들어 배열의 `sort()` 를 적용하고 List로 변경
        @Suppress("UNCHECKED_CAST")  
        return (toTypedArray<Comparable<T>>() as Array<T>).apply { sort() }.asList()  
    }  
    // Iterable을 변경 가능하도록 하고 `sort()` 를 적용
    return toMutableList().apply { sort() }  
}
```

`sortedDescending()`의 구현은 다음과 같다. sortedWith의 인자인 comparator에 역순을 의미하는 `reverseOrder()` 를 파라미터로 전달하고 있다.

```kotlin
public fun <T : Comparable<T>> Iterable<T>.sortedDescending(): List<T> {  
    return sortedWith(reverseOrder())  
}
```

#### 2. comparator 를 직접 넘겨주는 `sortedWith` 시리즈

```kotlin title="기본이 되는 sortedWith 함수"
public fun <T> Iterable<T>.sortedWith(comparator: Comparator<in T>): List<T> {  
    if (this is Collection) {  
       if (size <= 1) return this.toList()  
       @Suppress("UNCHECKED_CAST")  
       // sorted 와 거의 유사하다.
       // 타입 파라미터 T 에 Comparable 이라는 upper-bound가 존재하지 않음에 주목하자.
       return (toTypedArray<Any?>() as Array<T>).apply { sortWith(comparator) }.asList()  
    }  
    return toMutableList().apply { sortWith(comparator) }  
}
```

`Comparator<in T>` 를 파라미터로 받는 `sortedWith를` 기본으로 `sortedBy`, `sortedByDescending` 은 모두 주어진 `selector: (T) -> R?` 인자를 바탕으로 적절한 comparator를 생성해 `sortedWith`을 호출하는 방식으로 동작한다.

### 2. compareBy의 명시적 활용

개인적으로 정렬대상 타입이 `Comparable` 하지 않은 경우 `sortedBy(selector)`, `sortedByDescending(selector)` 보다 명시적인 `comparator`를 넘겨주는 `sortedWith` 의 호출을 조금 더 선호한다.

그 이유로는 
1. [이 실험](https://www.github.com/ndy2/sort-memory-test)에서 메모리 이슈로 한번 크게 대인 적이 있기 때문에
    - 사실 이 실험의 결론은 `Comparable` 을 직접 구현하는 것이 가장 좋다는 것이였지만 메모리가 크게 문제 되지 않는다면 `Comparator` 를 전달하는 것으로 충분한 것 같다.
    - 지금 보니 `comparingInt` 시리즈를 사용하면 문제 없을거 같기도 하다.
1. `selector` 는 두개 이상의 요소에 대해 정렬하는 경우를 처리할 수 없다.
2. 그 외에도 `comp` 라는 변수명을 통해 명시적으로 `Comparator`를 작성해주는 편이 코드도 더 이쁜 경우가 많은것 같다.

이 있다.

어떤 Comparable 하지 않은 클래스를 정렬한다는 의미는 일단 정렬 기준이 복잡할 경우가 많다. 단순히 `Pair<Int, Int>` 를 생각했을때 `it.first` 에대해 오름 차순으로 정렬하고 `it.second`에 대해 내림 차순으로 정렬한다는 것 조건은 Selector 로는 표현할 수 없다. 이런 상황과 함께 정렬조건의 변경에 따른 확장성을 생각했을때 `Comparator` 를 직접 생성해서 전달하는 것이 더 깔끔하다는 결론을 내렸다. 물론 `kotlin`은 Comparator 를 생성하는 것에도 또한 `kotlin` 스러운 방식을 제공한다.

first 를 기준으로 오름 차순, second를 기준으로 내림차순으로 `Pair<Int,Int>` 의 목록을 정렬해보자.

![[pair-sort.png|Pair<Int,Int>는 Comparable하지 않다!]]

```kotlin
fun main() {  
    val list = listOf(  
        6 to 1,  
        1 to 3,  
        2 to 7,  
        1 to 10,  
        3 to 4,  
        6 to 7,  
        2 to 5,  
    )  
  
    val comp1 = compareBy<Pair<Int, Int>> { it.first }.thenByDescending { it.second }  
    println("list.sortedWith(comp1) : ${list.sortedWith(comp1)}")  
  
    val comp2 = compareBy<Pair<Int,Int>>({it.first}, {-it.second})  
    println("list.sortedWith(comp2) : ${list.sortedWith(comp2)}")  
}
```

```text title="실행 결과"
list.sortedWith(comp1) : [(1, 10), (1, 3), (2, 7), (2, 5), (3, 4), (6, 7), (6, 1)]
list.sortedWith(comp2) : [(1, 10), (1, 3), (2, 7), (2, 5), (3, 4), (6, 7), (6, 1)]
```

`kotlin`은 복잡한 comparator를 우아하게 생성할 수 있는 방법을 몇가지 제공한다.

첫번째 `comp1` 은 여러 `selector`를 순서에 따라 체이닝 방식으로 전달하였다. `comp2` 에서는 여러 `selector` 를 `varargs` 로 전달한 모습을 볼 수 있다. 둘다 적당히 깔끔해 보이니 취향껏 사용하면 되겠다. 여기서 주의 할 점은 `compareBy` 의 호출에 타입인자를 명시적으로 전달해주어야 한다는 점이다. 이는 `comp` 를 inline 해도 마찬가지 이기 때문에 타입추론이 안되는점이 조금 아쉽지만 이정도면 만족스러운 수준이다.

### 3. 두 방식을 응용해서 Pair<Int,Int> 에서 원하는 정렬기준에 따른 첫번째 원소의 인덱스 구하기

위 `val list = listOf(6 to 1,1 to 3,2 to 7,1 to 10,3 to 4,6 to 7,2 to 5, 1 to 10)` 에서 first가 가장 작고 second가 가장 큰 원소의 인덱스를 구해보자. 이때 같은 값이 있다면 인덱스가 큰 값을 선택하자.  // 정답인 1 to 10을 마지막에 하나 더 추가하였다!

```kotlin
fun main() {  
    val list = listOf(  
        6 to 1,  
        1 to 3,  
        2 to 7,  
        1 to 10,  
        3 to 4,  
        6 to 7,  
        2 to 5,  
        1 to 10  
    )  
  
    val comp =  
        compareBy<IndexedValue<Pair<Int, Int>>>(  
            { it.value.first },  
            { -it.value.second },  
            { -it.index }  
        )  
  
    println(  
        list  
            .withIndex()  
            .sortedWith(comp)  
            .first()  
    )  
}
```

```text title="실행 결과"
IndexedValue(index=7, value=(1, 10))
```

kotlin Collection 의 `withIndex` 확장함수와 `data class IndexedValue`  의 활용을 기억하자.

위 정렬에서 comp는 다음처럼 작성될 수도 있다.
```kotlin
val comp =  
    compareBy<IndexedValue<Pair<Int, Int>>> { it.value.first }  
        // java 의 Comparator 에 정의된 메서드이다.
        .thenComparingInt { -it.value.second }  
        .thenComparingInt { -it.index }  
  
val comp2 =  
    compareBy<IndexedValue<Pair<Int,Int>>> {it.value.first}  
        // kotlin 의 Comparisons.kt 에 정의된 확장 함수이다.
        // 오토박싱으로 인한 메모리 낭비 위험
        .thenByDescending { it.value.second }  
        .thenByDescending { it.index }
```

### 4. `MutableCollection`과 `sortXXX`

지금껏 살펴본 `sotredXXX` 는 모두 Iterable에 대한 확장함수로 원본 리스트는 건드리지 않고 모두 새로운 리스트를 생성해는 API 이다. 그 이유는 물론 `List` 는 Immutable 하기 때문이다.

원본 리스트를 변경하며 정렬하는 `sortXXX` 에 대해 알아보자. 위와 마찬가지로 `Pair<Int,Int>` 에 대한 정렬을 수행하자.

`sort()` 는 Comparable 한 타입에 대해 바로 적용할 수 있는 정렬 API 이다. Comparator 를 직접 전달하는 `sortWith()` 에대해서만 예제를 살펴보자. 물론 `sorted` 에서 처럼 `sortBy(selector)` 와 `sortByDesencding(selector)` 도 존재한다.

```kotlin
fun main() {  
    val list = mutableListOf(  
        6 to 1,  
        1 to 3,  
        2 to 7,  
        1 to 10,  
        3 to 4,  
        6 to 7,  
        2 to 5,  
        1 to 10  
    )  
  
    val comp =  
        compareBy<Pair<Int, Int>> { it.first }  
            .thenComparingInt { -it.second }  
  
    list.sortWith(comp)  
    println("list = $list") // 원본 리스트가 변경되었다!  
}
```

```text title="실행 결과"
list = [(1, 10), (1, 10), (1, 3), (2, 7), (2, 5), (3, 4), (6, 7), (6, 1)]
```

`sortXXX` 는 `MutableList<T>` 에 적용할 수 있는 확장함수로써 원본 리스트를 바꾼다는 사실을 기억하자. 함수의 리턴 타입은 `Unit` 이다.

![[mutablelist-sort.png|mutableList에 대한 정렬 api]]
함수 이름이 전부 `sort` 였다가 명확하게 바뀐 모습을 볼 수 있다. 또한 당연히 `sortedXXX` 시리즈도 사용가능하다.

### 5. 배열의 정렬 API

![[array-sort.png|배열의 정렬 API]]

이제 메서드의 이름만 봐도 슬슬 감이 온다.

배열의 정렬 API중 특이한 것은 배열이 Comparable 하지 않음에도 `sort()` 를 호출할 수 있다는 것이다. `List`, `MutableList` 타입에서는 제네릭의 upper-bound를 통해 Comparable 하지 않은 타입인자를 가지는 경우 파라미터를 가지지 않은 `sort()` , `sorted()` 의 호출을 아예 막았는데 배열의 경우 그냥 호출하고 `ClassCastException` 을 터트려버린다. 아마 자바의 Array.sort 와의 호환성을 위한 선택인것 같다.

또한 특이한 것은 배열에 대해 `sortedXXX` 호출시 기본적으로 List가 응답이되고 배열을 원하는 경우 `sortedArrayWith` 라는 녀석을 사용해야 한다는 것이다.

```kotlin
fun main() {  
    val array = arrayOf(  
        6 to 1,  
        1 to 3,  
        2 to 7,  
        1 to 10,  
        3 to 4,  
        6 to 7,  
        2 to 5,  
        1 to 10  
    )  
  
    val comp =  
        compareBy<Pair<Int, Int>> { it.first }  
            .thenComparingInt { -it.second }  
  
    println(array.sortedArrayWith(comp).contentToString())  
}
```

```text title="실행 결과"
[(1, 10), (1, 10), (1, 3), (2, 7), (2, 5), (3, 4), (6, 7), (6, 1)]
```

### 6. 정리

|  정렬 API                        | 동작                                                  | `List<T>` | `MutableList<T>`           | `Array<T>` |
| ------------------------ | ----------------------------------------------------- | --------- | -------------------------- | ---------- |
| `sort()`                 | 자신을 정렬                                           | X         | O `<T:Comparable<T>>` | O(Comparable 하지 않으면 예외)          |
| `sortDesending()`          | 자신을 내림차순으로 정렬                              | X         | O `<T:Comparable<T>>` |      X     |
| `sortWith(comp)`           | comp 를 이용해 자신을 정렬                            | X         | O                          | O          |
| `sortBy(sel)`              | sel 를 이용해 comp 생성후 이용해 자신을 정렬          | X         | O                          | O          |
| `sortByDesending(sel)`     | sel 를 이용해 내림차순 comp 생성후 이용해 자신을 정렬 | X         | O                          | O          |
| `sorted()`               | 정렬된 List 반환                                      | O         | O                          | O          |
| `sortedDesending()`      | 내림차순으로 정렬된 List 반환                         |  O `<T:Comparable<T>>`      | O `<T:Comparable<T>>` |            |
| `sortedWith(comp)`       | comp 를 이용해 정렬된 List 반환                       | O  `<T:Comparable<T>>`      | O `<T:Comparable<T>>` | O          |
| `sortedBy(sel)`          | sel 를 이용해 comp 생성 후 이용해 정렬된 List 반환    | O         | O                          | O          |
| `sortedByDesending(sel)` | sel 를 이용해 내림차순 comp 생성후 이용해 정렬된 List 반환 | O         | O                          | O          |
| `sortedArrayWith(comp)`  | comp 를 이용해 정렬된 배열 반환                       | X         | X                          | O          |
