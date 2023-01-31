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

추후에 알고리즘 쪽에서 정렬에 관해 한번 정리 할때 추가적으로 정리 하는 것이 더 좋을거 같아서 이 글에서 `DulPivotQuicksort` 나 `Timsort` 의 구현까지 들어가보지는 않을것이다. 객체 타입의 경우 `Comparator` 를 지정해주면 그냥 `Timsort` 를 사용하고 그렇지 않고 `Comparable` 을 상속한 경우에는 `ComparableTimsort` 를 사용한다. 둘의 차이는 두 객체의 비교 연산에 `Comparable` 을 사용하가, `Comparable` 을 사용하는가 이다. 메서드 호출에 따른 성능차이가 있을 수 있긴 하지만 optimized 된 VM 을 사용한다면 큰 의미는 없다고 한다.

---

### 2. 왜 서로 다른 알고리즘을 사용했을까? (뇌피셜)

자바가 왜 primitive type 과 객체 타입에 대해서 서로 다른 알고리즘을 적용하였을지 생각해보다가 javadoc 을 보고 힌트를 얻을 수 있었다.

!!! quote "Arrays 클래스와 정렬 메서드의 Javadoc 일부"
    sort(Object[])} does not have to be a MergeSort, but it does have to be stable

    This sort is guaranteed to be stable: 
    equal elements will not be reordered as a result of the sort.


정렬 메서드가 Stable 하다는 것의 의미는 equal 한 경우 순서가 유지된다는 것을 의미한다. Timsort 의 구현을 이후에 살펴보겠지만 Timsort 는 기본적으로 Stable 한 두가지 정렬 *Merge sort* 와 *Insertion sort* 를 결합하였기 때문에 Stable 하다. 

반면 *Quicksort* 의 변형인 *DualPivotQuicksort* 는 Stable 하지 않다. 하지만 생각해보면 primitive 배열이 stable 할 필요가 없다. 왜냐하면 두 값이 equal 하다면 그 값이 표현하는 모든 논리적인 의미가 같다는 것이고 순서를 유지하는것이 의미가 없기 때문이다. 아마 이러한 이유로 자바의 개발자들은 primitive 타입과 객체 타입의 정렬 알고리즘을 별도로 구현한것 같다.

---

### 3. Arrays.*parallelSort*

`java.util.Arrays` 에는 sort 외에 *parallelSort* 라고하는 정렬 API 가 하나 더 있다. 그 이름에서도 알수 있듯이 여러 쓰레드를 통해 병렬적으로 정렬을 수행하는 API 이다.

```java
package java.util

public class Arrays{

    public static void parallelSort(int[] a) {  
        DualPivotQuicksort.sort(a, ForkJoinPool.getCommonPoolParallelism(), 0, a.length);  
    }

    // sort() 시리즈와 마찬가지로 범위를 지정할 수 있다. 
    public static void parallelSort(int[] a, int fromIndex, int toIndex) {  
        rangeCheck(a.length, fromIndex, toIndex);  
        DualPivotQuicksort.sort(a, ForkJoinPool.getCommonPoolParallelism(), fromIndex, toIndex);  
    }

    // 몇몇 primitive 타입은 parallelSort 를 내부적으로 지원하지 않는다?! 왜 와이?
    public static void sort(byte[] a) {  
        DualPivotQuicksort.sort(a, 0, a.length);  
    }

    public static void parallelSort(short[] a) {  
        DualPivotQuicksort.sort(a, 0, a.length);  
    }

    /* The minimum array length below which a parallel sorting
     * algorithm will not further partition the sorting task. Using 
     * smaller sizes typically results in memory contention across 
     * tasks that makes parallel speedups unlikely. */
     private static final int MIN_ARRAY_SORT_GRAN = 1 << 13;

    // 객체타입의 parallelSort API
    public static <T extends Comparable<? super T>> void parallelSort(T[] a) {  
        int n = a.length, p, g;  
        
        if (n <= MIN_ARRAY_SORT_GRAN ||  
            (p = ForkJoinPool.getCommonPoolParallelism()) == 1)  {
            TimSort.sort(a, 0, n, NaturalOrder.INSTANCE, null, 0, 0);  
        }
        else { 
            new ArraysParallelSortHelpers.FJObject.Sorter<>  (
                 null, a,  
                 (T[])Array.newInstance(a.getClass().getComponentType(), n),  
                 0, n, 0, 
                 ((g = n / (p << 2)) <= MIN_ARRAY_SORT_GRAN) ?  
                 MIN_ARRAY_SORT_GRAN : g, NaturalOrder.INSTANCE
             )
             .invoke();  
            }
        }
}

```


`Arrays`.*`sort`* 에서 다루지 않았던 정수 배열을 받는 `DualPivotQuicksort`.*`sort`* api 의 두번째 인자의 정체가 드러났다. 두번째 인자는 바로 parallelism 을 받는 인자로 병렬성을 나타내는 인자였다. 그렇기 때문에 그냥 *sort( )* 에서는 항상 0을 제공하였던 것이다. 참고로 병렬성은 0 based 로 사용하는 코어 (쓰레드)의 개수 -1 로 표현된다. - 자바 기본 쓰레드 풀인 `ForkJoinPool` 의 *`getCommonPoolParallelism()`* 을 확인해 보면 알 수 있다. ([참고 링크](https://ssdragon.tistory.com/119))

----

#### 1. 특이사항

또한 byte (1byte), char (2byte), short (2byte) 과 같은 사이즈가 작은 primitive 타입에 대해서는 `Arrays`.*`parallelSort`* API 를 제공하지만 내부적으로는 parallelism 을 제공하지도 않고 내부 구현도 그냥 `Arrays`.*`sort`* 와 같다는 점이 눈에 띈다.

-  `DualPivotQuicksort`.*`sort( )`* 의 오버로드 메서드들
![DualPivotQuicksort.sort.png](images/DualPivotQuicksort.sort.png)

---

### 2.  parallelism 이 적용되는 조건, 적용되는 방식 간단 확인

먼저 primitive 타입 중 parallelism 인자를 가지고 있는 int, long, double, float 의 DualPivoQuicksort.sort( ) 를 확인해보자.

``` java title="DualPivoQuicksort#sort(int[], ...)"
/* Min array size to perform sorting in parallel. */
private static final int MIN_PARALLEL_SORT_SIZE = 4 << 10;

static void sort(int[] a, int parallelism, int low, int high) {  
    int size = high - low;  
  
    if (parallelism > 1 && size > MIN_PARALLEL_SORT_SIZE) {  
        int depth = getDepth(parallelism, size >> 12);  
        int[] b = depth == 0 ? null : new int[size];  
        new Sorter(null, a, b, low, size, low, depth).invoke();  
    } else {  
        sort(null, a, 0, low, high);  
    }  
}
```


parallelism 이 1 보다 크고 정렬을 수행할 데이터의 개수가 2<sup>12</sup> (4096) 보다 많은 경우에만 병렬 정렬이 수행된다. 

정렬은 `Sorter` 라고 하는 클래스로 수행되고 이들의 병합은 `Merger` 라고하는 내부 클래스가 수행한다. 이들은 모두 `ForkJoinTask` 라고 하는 녀석을 상속하고 있으며 정렬과 병합작업을 위해 재귀적으로 호출되어 `ForkJoinPool` 에서 쓰레드를 할당받아 각각 작업을 수행하는 것 같다. (어렵네용..)

객체 타입의 경우에는 2<sup>13</sup> (8192) 개 보다 많은 데이터에 대해서만 병렬성을 지원하는 것을 알 수 있다.

`Arrays`.*`sort`* 와 `Arrays`.*`parallelSort`* 의 성능을 비교한 내용은 [여기](https://www.baeldung.com/java-arrays-sort-vs-parallelsort#comparison) 에서 확인해보자.

---

### 4. 마무리...

알고리즘을 건드리지 않는 선에서 정렬의 동작 방식을 최대한 깊게 파해쳐 본것 같다.

요 내용은 어느정도 알던 내용이지만 시간을 내 글을 통해 정리하면서 좀더 지식이 정제된것 같은 느낌이 든다. 

사실 이 글은 알고리즘 문제를 풀다가 시작된 한 의문점에서 시작되었다. 정렬 문제를 코틀린으로 푸는 도중 자바와 코틀린의 코드가 똑같아 보이는데 메모리 사용량에서 큰 차이가 나는 것을 발견했다. 이에 관해 흥미가 있으신 분은 여기를 참고해주세용  [관련 깃헙 링크](https://github.com/ndy2/sort-memory-test)

