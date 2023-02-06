---
title: 퀵 소트 (Quicksort)
date: 2023-02-04
---

### 1. 퀵 정렬

!!! note "퀵 정렬!"

    * 퀵 정렬<sup>Quicksort</sup>은 효율적이고, 범용적인 정렬 알고리즘 입니다.
    * 퀵 정렬은 `divide-and-conquer` 알고리즘입니다.


### 2. 퀵 정렬 코드!

```python title="Quick Sort!" exec="true" source="material-block"
# Python3 implementation of QuickSort

# Function to find the partition position
def partition(array, low, high):
	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# e greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# Function to perform quicksort
def quick_sort(array, low, high):
	if low < high:
		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quick_sort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quick_sort(array, pi + 1, high)


# Driver code
array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')
# This code is contributed by Adnan Aliakbar
```

### 3. 퀵 정렬 파티션 동작 흐름

![quicksort.excalidraw.png](excalidraws/quicksort.excalidraw.png)

1. `lo` 가 `hi` 보다 크거나 같다면 정렬할 필요가 없다. `break`!
2. 피봇을 정한다
3. 탐색 구간 전체를 훑으며 피봇을 보다 작은 원소를 찾으면 `swap` 을 통해 위치를 잡아준다. (`i` 는 `swap` 대상이 등장하였을때 위치를 잡아주기 위한 포인터 라고 생각하자)
4. 탐색을 마치면 i 를 기준으로 왼쪽에는 피봇보다 작은 원소가 i 를 포함하여 i의 오른쪽에는 피봇보다 큰 원소만이 위치하게 된다. `swap` 으로 피봇의 위치를 잡아준다. 이때 피봇의 위치는 전체 배열에서 결정되었다고 볼 수 있다.
5. 결정된 `pivot` 의 위치를 기준으로 좌우로 나누어 `1` 을 두번 호출한다.


### 4. 퀵 정렬의 특징

!!! note "퀵 정렬의 성능"

    * Quick 정렬의 성능은 pivot 을 선정하는 방식에 크게 의존적입니다. 매번 devide 시에 pivot 의 위치가 적절히 중간에 잘 설정되어서 비슷한 크기의 덩어리로 분할이 된다면 좋은 성능을 낼 수 있습니다.

    * 반면 매번 pivot 의 최솟값 혹은 최댓값으로 선정된다면 최악의 성능을 보여줍니다. pivot 선택시 이러한 케이스가 잘 등장하지 않도록 pivot 을 선정하는 여러 기법이 개발되었습니다.
        * e.g.) Random Quicksort, median-of-three Quicksort, dual-pivot quicksort ...
        * Java 는 primitive 타입의 배열 정렬에 dual-pivot quicksort 를 사용합니다. 

!!! note "시간 복잡도, 보조 공간"

    * Best Case, Average Case - O(nlogn)
    * Worst Case - O(n^2)
    * Auxiliary Space - O(1) (i.e. in-place algorithm)
        * See Also) is quicksort in-place or not on [stackoverflow](https://stackoverflow.com/questions/22028117/is-quicksort-in-place-or-not)
        * worst-case 의 경우 pivot 이나 i index 를 저장하기 위한 메모리 공간이 call stack 에 계속 누적되면서 O(n) 메모리를 필요로 한다는 주장도 일부 있는 것 같다. 하지만 일반적으로 in-place 로 취급하는 의견이 지배적인 것 같다.

!!! question "stable?"

    * not stable!
    * 즉 비교 순서가 같은 원소간의 정렬 후 순서를 보장하지 않는다.


!!! note "퀵 정렬과 다른 정렬들 비교"

    * 퀵 정렬은 전반적으로 *randomized data*, 특히 *분포가 큰 데이터* 에 대해서 같은 O(nlogn) 시간 복잡도의 merge sort 나 heapsort 에 비해 빠르다고 알려져 있습니다.

    * 퀵 정렬이 머지 정렬에 비해 가지는 장점은 다음과 같습니다.
        * in-place (Merge 정렬은 O(n) 의 보조 저장 공간을 필요로 함)
        * cache-locality Good!. 
            * 즉, 캐시의 지역성을 활용하기가 머지 소트에 비해 수월하다. 
            * 배열의 연속된 원소에 접근하는 경우가 많다.
        * 하지만! 만약 Linked List 를 정렬해야 한다면  Merge Sort 가 더 좋습니다. 
            * 링크드 리스트 자료구조는 머지 소트의 머지 연산을 O(1) 타임에 가능하게 해 줍니다. 
            * 링크드 리스트의 노드는 어짜피 메모리 공간에 순서대로 있지 않기 때문에 퀵 정렬이 자랑하는 cache-locality 도 의미가 없습니다.
            * 퀵 정렬에서 pivot 을 램덤으로 선정해서 해당 위치의 값을 알아내는 연산도 LinkedList 에서는 pivot 의 위치만큼의 탐색이 필요해집니다.

    * 퀵 정렬과 Heapsort 를 비교한 내용은 다음과 같습니다.
        * 일반적으로 quicksort 가 빠르다.
            * 이 내용은 debatable 합니다. 몇몇 논문은 heapsort 가 더 빠르다고 합니다. 
        * introsort 는 quicksort 의 변형으로 worst-case 가 탐지되면 heapsort 를 사용합니다. (c++ GNU 에서 사용)

    * 반면 다음과 같은 단점도 있습니다.
        * 최악의 경우 O(n^2) 의 성능을 내고 이를 피하기 위한 pivot 의 선정은 heuristic 에 의존적입니다.

