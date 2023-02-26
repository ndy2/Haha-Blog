---
tags: [algorithm, sort]
title: O(n^2) 정렬 알고리즘
---

@ 참고 자료)

- all sample codes from geeksforgeeks

---

### 0. 들어가며

정렬 알고리즘의 성능을 판별하는 잣대!

- `보조 공간 (Auxiliary Space)`
	- 배열을 저장하는 메모리 외의 정렬을 위해 필요한 추가 메모리 
- `시간 복잡도 (Time Complexity)`
	- `comp` 연산의 횟수
	- `swap` 연산의 횟수

### 1. 버블 정렬 Bubble Sort

#### 1. Python Code

```python title="Bubble Sort!" exec="true" source="material-block"
# Python program for implementation of Bubble Sort
def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 1, 4, 2, 8]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
	print("%d" % arr[i], end=" ")
```

#### 2. 실행 흐름

다음 순서로 비교와 스왑을 진행한다.

- arr[0],arr[1] -> arr[1], arr[2] -> ...........-> arr[n-3],arr[n-2] -> arr[n-2], arr[n-1] 
- arr[0],arr[1] -> arr[1], arr[2] -> ............-> arr[n-3],arr[n-2]
- ....
- arr[0],arr[1] -> arr[1], arr[2]
- arr[0],arr[1]

#### 3. 특징

- 버블 정렬은 가장 기초적인 정렬 알고리즘 이다.
- Stable Sort
- 시간 복잡도 - O(n<sup>2</sup>), 보조 메모리 - O(1) (`temp` 저장용 하나)
<br>
- 최선의 경우 - 배열이 모두 정렬 된 경우
	- swap 을 한번도 진행하지 않지만 그경우에도 항상 O(n<sup>2</sup>) 타임의 비교연산이 필요하다.
- 최악의 경우 - 배열이 역순으로 정렬 된 경우
	- swap, comp 연산 모두 O(n<sup>2</sup>) 타임이 필요하다.

---

### 2. 선택 정렬 (Selection Sort)

#### 1. Python Code

```python title="Selection Sort!" exec="true" source="material-block"
# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):
	
	# Find the minimum element in remaining
	# unsorted array
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	# Swap the found minimum element with
	# the first element	
	A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" ")

```

#### 2. 실행 흐름

-      i		`최소 값 찾기` Comp n-i-1 회                   ->        Swap - 무조건 발생
 -      `0`     arr[0], arr[1], .... arr[n-2], arr[n-1]        ->  swap(arr[0], arr[min_idx<sub>0~n-1</sub>])
-       `1`                 arr[1], .... arr[n-2], arr[n-1]       ->  swap(arr[1], arr[min_idx<sub>1~n-1</sub>])
-      `n-2`                               arr[n-2], arr[n-1]      ->  swap(arr[n-2], arr[min_idx<sub>n-2~n-1</sub>])
-      `n-1`                                                  arr[n-1]      ->  swap(arr[n-1], arr[min_idx<sub>n-1~n-1</sub>])  // 생략

#### 3. 특징

- 정렬의 형태에 관계없이 최선의 경우, 최악의 경우 성능이 일정하다.
- Stable Sort
- 시간 복잡도 - comp - `O(n^2)`, swap - O(n), 보조 공간 - `O(1)`

---

### 3. 삽입 정렬 (Insertion sort)

#### 1. Python Code

```python title="Selection Sort!" exec="true" source="material-block"
# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array")
for i in range(len(arr)):
	print ("% d" % arr[i])

# This code is contributed by Mohit Kumra
```

#### 2. 실행 흐름

key 를 고른다 -> *적당한 위치*에 삽입한다.

- i -> key -> comp (i-1 ~ 더 작을 때 까지)/ comp 하는 동시에 뒤로 미는 swap 도 수행
- 1 -> arr[1] -> j = 0 done
- 2 -> arr[2] -> j = 1/ key 와 arr[j] 비교 -> key 가 더 작으면 계속 arr[j+1] 과 [j] 변경

...

- n -> arr[n] -> 이미 정렬된 arr[0-n-1] 에서 앞으로 이동하며 arr[n] 의 위치를 잡아준다

#### 3. 특징

- 개수가 적은 경우, 이미 어느정도 정렬 된 경우 매우 강력하다. 역순으로 정렬된 최악의 경우 성능이 매우 안 좋다.
- key 를 삽입할 위치를 찾는 과정에서 앞 배열이 이미 정렬 되었다는 점을 이용해 비교 연산의 횟수를 O(nlogn) 수준으로 낮추는 `이진 삽입 정렬` 이라는 변형이 존재한다.
- **Time Complexity:** O(N<sup>2</sup>) , **Auxiliary Space:** O(1)
