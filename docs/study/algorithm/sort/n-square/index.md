---
title: O(n^2) 정렬 알고리즘
---

### 0. 들어가며

정렬 알고리즘의 성능을 판별하는 잣대!

- `보조 공간 (Auxiliary Space)`
	- 배열을 저장하는 메모리 외의 정렬을 위해 필요한 추가 메모리 
- `시간 복잡도 (Time Complexity)`
	- `comp` 연산의 횟수
	- `swap` 연산의 횟수


```c title="아래의 코드에서 사용할 comp, swap 함수"
#include <stdbool.h>
bool comp(int x, int y){
	return x>y
}

void swap(int* xp, int * yp){
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}
```

### 1. 버블 정렬 Bubble Sort

arr[0] 과 arr[1]  -> 

```c
void bubbleSort(int arr[], int len) {
  int i, j, tmp;
  for (i = 0; i < len - 1; ++i) {
    for (j = 0; j < len - i - 1; ++j) {
      if (arr[j] > arr[j + 1]) {
        swap(&arr[j], &arr[j+1])
      }
    }
  }
}
```

