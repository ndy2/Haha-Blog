### 0. 들어가며

[이전 글](collections)에서는 `Collections`.*`sort`* 의 동작 방식에 대해 알아보았다. 컬렉션의 정렬 API 는 단순히 배열의 정렬 API - `Arrays`.*`sort`* 를 활용하고있었다. 오늘은 배열의 정렬 API 에 대해서 알아보자.

---

### 1. Arrays.*sort*

전통적이고 대표적이고 가장 널리 활용되는 정렬 API 이다.

```java
package java.util

public class Arrays{

    public static void sort(int[] a) {  
        DualPivotQuicksort.sort(a, 0, 0, a.length);  
    }
    
    public static void sort(int[] a, int fromIndex, int toIndex) {  
        rangeCheck(a.length, fromIndex, toIndex);  
        DualPivotQuicksort.sort(a, 0, fromIndex, toIndex);  
    }

    // 
    // ... 다른 primitive type sort 메서드
    //
    
    public static void sort(Object[] a) {  
        if (LegacyMergeSort.userRequested)  legacyMergeSort(a);  
        else ComparableTimSort.sort(a, 0, a.length, null, 0, 0);  
    }

    public static <T> void sort(T[] a, Comparator<? super T> c) {  
        if (c == null) {  
            sort(a);  
        } else {  
            if (LegacyMergeSort.userRequested)  legacyMergeSort(a, c);  
            else TimSort.sort(a, 0, a.length, c, null, 0, 0);  
        }  
    }
    // ...
}
```

`Arrays`.*`sort`* 는 우선 구간을 지정하는 방식과 구간을 지정하지 않는 방식이 있다. `fromIndex`, `toIndex` 두 인덱스를 전달 받아 범위 체크를 해주고 정렬을 수행한다. 이때 범위 지정 방식에서 주의할 점은 `fromIndex` 는 Inclusive 이고 `toIndex` 는 Exclusive 하다는 점이다. 즉, fromIndex 는 포함하고 toIndex 는 포함하지 않는다. 다른 모든 정렬 api 도 범위를 지정하는 메서드를 제공하지만 구현이 크게 다르지 않기 때문에 위 코드에는 추가하지 않았다.

!!! note "범위 정렬 메서드의 파라미터 Javadoc"

    Params:
    a – the array to be sorted 
    fromIndex – the index of the first element (inclusive) to be sorted 
    toIndex – the index of the last element (exclusive) to be sorted

구현을 살펴보면 드디어 정렬 알고리즘과 관련된 이름들이 보이기 시작한다. 또한 primitive type 과 Object 타입에 대해서 구현 방식이 다른 것을 알 수 있다. 

!!! note ""

    * primitive type -> `DualPivotQuicksort`.*`sort`*
    * 객체 타입 (`Object[]` ) -> `ComparableTimsort`.*`sort`* 
    * 객체 타입 + `Comparator` (`T[] and Comparator<? super T>` )) -> `Timsort`.*`sort`*

객체 타입의 경우 하위호환성을 위해 사용자의 요구에 따라 merge sort 를 사용하도록 지정할 수 있다. 하지만 이후 릴리즈 버전에서는 언제라도 제거 될 수 있고 굳이 사용할 이유가 없기 때문에 사용하면 안된다.  (VM option :  `-Djava.util.Arrays.useLegacyMergeSort=true` )

추후에 알고리즘 쪽에서 정렬에 관해 한번 정리 할때 추가적으로 정리 하는 것이 더 좋을거 같아서 이 글에서 DulPivotQuicksort 나 Timsort 의 구현까지 들어가보지는 않을것이다.

자바가 왜 primitive type 과 객체 타입에 대해서 서로 다른 알고리즘을 적용하였을지 생각해보다가 javadoc 을 보고 힌트를 얻을 수 있었다.

```
<Arrays 클래스의 Javadoc 일부>
sort(Object[])} does not have to be a MergeSort, but it does have to be stable

<모든 객체 타입 정렬 메서드의 Javadoc 일부>
This sort is guaranteed to be stable: equal elements will not be reordered as a result of the sort.
```
 
정렬 메서드가 Stable 하다는 것의 의미는 equal 한 경우 순서가 유지된다는 것을 의미한다. Timsort 의 구현을 이후에 살펴보겠지만 Timsort 는 기본적으로 Stable 한 두가지 정렬 *Merge sort* 와 *Insertion sort* 를 결합하였기 때문에 Stable 하다. 반면 *Quicksort* 의 변형인 *DualPivotQuicksort* 는 Stable 하지 않다. 하지만 생각해보면 primitive 배열이 stable 할 필요가 없다. 왜냐하면 두 값이 equal 하다면 그 값이 표현하는 모든 논리적인 의미가 같다는 것이고 순서를 유지하는것이 의미가 없기 때문이다. 아마 이러한 이유로 자바의 개발자들은 primitive 타입과 객체 타입의 정렬 알고리즘을 별도로 구현한것 같다. (뇌피셜)


---

### 2. `ComparableTimsort` vs `Timsort`

사실 정렬 API 에 관해 정리를 시작하게된 이유도 바로 이 주제에 대해서 알아보기 위해서였다. 이전에 자바의 정렬 API 에 대해서 학습을 했을때에는 아래와 같은 정리를 많은 다른 블로그를 통해 확인하고 결론을 내렸었다.

!!! note ""

    * 컬렉션 -> 팀 소트
    * 배열
        * primitive type 배열 -> Dual Pivot Quicksort
        * Object Type 배열 -> 팀 소트

맞는 말이고 이 까지만 해도 충분한것 같다. 그런데 정렬에 관한 알고리즘 문제를 풀다가 이상한 점을 발견했다. 

---

문제 - {{ boj(":p5: 행성 터널", 2887) }}  는 *최소 스패닝 트리*<sup>Mininum Spanning Tree</sup> 에 관한 문제이다. 이 문제의 특징은 MST 를 판별하는데 필요한 `Edge` 를 단순히 가능한 모든 `Edge` 를 넣게 된다면 메모리 초과를 피할 수 없다는 것이다. 관련 질답 - [링크](https://www.acmicpc.net/board/view/50645)

따라서 정렬을 이용해 `MST` 의 edge 가 될 수 있는 후보군 `Edge` 를 O(n) 으로 (실제는 O(3n)) 하여 Space Complexity 를 선형적으로 가져가는 것이 문제 풀이의 핵심이다. 단순히 `Edge` 를 때려박으면 메모리가 터진 다는 것을 알았지만 해결할 방법이 잘 생각나지 않아 다른 분들의 풀이를 참고했고 (링크) 내 방식의 코드로 옮겼다. (링크) 그런데 암만봐도 두 코드가 똑같은데 여전에 메모리 초과가 발생했다 !! (맞왜틀....)

약 1시간 가량 맞왜틀을 시전한 후에 문제점을 알아냈다. 바로 이장의 주제인 ComparableTimsort 와 Timsort 의 차이이다.

```kotlin "실패한 코드 일부"
private data class Point(val idx: Int, val value: Int)

fun main(){
    val x = mutableListOf<Point>()
    //...
    x.sortBy {it.value}
    //...
}
```

```kotlin "성공한 코드 일부"
private data class Point(val idx: Int, val value: Int) : Comparable<Point> {  
    override fun compareTo(other: Point) = value - other.value  
}

fun main(){
    val x = mutableListOf<Point>()
    //...
    x.sort()
    //...
}
```

실패한 코드에서는 `sortBy { }` 를 활용하였다. `Comparable` 을 구현하지 않고 직접 `Comparator` 를 하나 생성해서 전달하였다. 성공한 코드에서는 `sort()` 를 활용하였고 `Comparable` 을 구현하였다. 

이 장에서 다루지 않은 Kotlin 과 관련된 call stack 이 조금 등장하긴 하지만 둘의 callstack 을 따라가다 보면 다음과 같은 차이가 나온다.

`sortBy` (`Comparator` 제공)

![sortby-callstack.png](images/sortby-callstack.png)


`sort` (`Comparator` 미제공, `Comparable` 구현)

![sort-callstack.png](images/sort-callstack.png)

Timsort 와 ComparableTimsort 의 해당 라인을 살펴보면 그 이름과 콜 스택에서 알 수 있듯이 ComparableTimsort 는 원소를 비교하는 방식에서 `Comparable` 을 이용하는가 혹은 전달받는 `Comparator` 를 이용하는가 에 대한 차이만 있다.

!!! note ""

    - `ComparableTimsort` line 325 - `((Comparable) a[runHi]).compareTo(a[runHi - 1])` 
    - `Timsort` line *296* - `c.compare(pivot, a[mid])`

야심차게 이 문제의 원인이 Timsort 와 ComparableTimsort 의 구현방식에서의 차이라고 생각하고 실험과 정리를 하던 중 진짜 문제점을 찾아내었다. 문제는 자바 쪽이 아니고 코틀린 쪽에 있었다.

내용이 너무 길어지고 자바와는 관련이 없어질 것 같아 이쯤에서 마무리하고 코틀린 쪽에서 이 내용을 추가로 다루어보자!




