---
tags: [lecture, go]
title: 정렬
author: ndy2
date: 2023-05-30
description: >-
  
---
 
> [!quote] 참고 자료
> * [`『sort』`](https://pkg.go.dev/sort) @`pkg.go.dev`

### 1. 정수 Slice 정렬

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	a := []int{4, 10, 8, 3, -3, 5, -1}
	sort.Ints(a)
	
	fmt.Println(a) // "[-3 -1 3 4 5 8 10]"
}
```

### 2. 정수 Slice - Desending, Abs 로 정렬

#### 2.1. `sort.Sort`, `sort.Reverse` 이용

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	a := []int{4, 10, 8, 3, -3, 5, -1}
	sort.Sort(sort.Reverse(sort.IntSlice(a)))

	fmt.Println(a) // "[10 8 5 4 3 -1 -3]"
}

```

#### 2.2. `sort.Slice` 이용

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	a := []int{4, 10, 8, 3, -3, 5, -1}
	sort.Slice(a, func(x, y int) bool {
		return a[y] < a[x]
	})

	fmt.Println(a) // "[10 8 5 4 3 -1 -3]"
}
```

### 3. 정수 Slice - 절댓값으로 정렬

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	a := []int{4, 10, 8, 3, -3, 5, -1}
	sort.Slice(a, func(x, y int) bool {
		return abs(int64(a[x])) < abs(int64(a[y]))
	})

	fmt.Println(a) // "[-1 3 -3 4 5 8 10]"
}

func abs(n int64) int64 {
	y := n >> 63
	return (n ^ y) - y
} // http://cavaliercoder.com/blog/optimized-abs-for-int64-in-go.html
```

음... 람다식 없나?!

### 4. `fun Sort`

Sort 함수를 이용해 커스텀 타입의 정렬을 수행해보자.

```go title="sort/sort.go #Sort"
// Sort sorts data in ascending order as determined by the Less method.
// It makes one call to data.Len to determine n and O(n*log(n)) calls to
// data.Less and data.Swap. The sort is not guaranteed to be stable.
func Sort(data Interface) {
	n := data.Len()
	if n <= 1 {
		return
	}
	limit := bits.Len(uint(n))
	pdqsort(data, 0, n, limit)
}
```

`Sort` 함수는 `Interface` 타입 `interface` 인자를 하나 전달 받고 이를 이용해 `pattern-defeating quicksort(pdqsort)` 함수에 내부적으로 정렬을 위임한다.

그럼 가장 중요한 것이 바로 `Interface` 타입이다.

```go
type Interface interface {
	Len() int
	Less(i, j int) bool
	Swap(i, j int)
}
```

인터페이스에 정의된 세가지 함수를 모두 리시버로 가지는 타입 T 는 Interface 로 동작 할 수 있으며 Sort 에 사용될 수 있다. 위에서 사용한 `sort.Ints` 함수의 구현을 살펴보자.

```go
// Ints sorts a slice of ints in increasing order.
func Ints(x []int) { Sort(IntSlice(x)) }
```

이녀석도 사실은 `Sort` 를 내부적으로 호출하고 IntSlice 라는 타입의 Interface 를 사용했던 것이다!

```go
// IntSlice attaches the methods of Interface to []int, sorting in increasing order.
type IntSlice []int  
  
func (x IntSlice) Len() int { return len(x) }  
func (x IntSlice) Less(i, j int) bool { return x[i] < x[j] }  
func (x IntSlice) Swap(i, j int) { x[i], x[j] = x[j], x[i] }
```

이제 sort.Ints, sort.Sort 의 비밀인 Interface 타입에 대해 알게 되었으므로 조금더 복잡한 기준의 정렬을 수행해보자. 목표는 [이 문제](https://www.acmicpc.net/problem/1181) 이다.

> 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
>  1. 길이가 짧은 것부터
>  2. 길이가 같으면 사전 순으로

```go
package main

import (
	"fmt"
	"sort"
)

type StringSorter []string

func (x StringSorter) Len() int { return len(x) }
func (x StringSorter) Less(i, j int) bool {
	if len(x[i]) != len(x[j]) {
		return len(x[i]) < len(x[j])
	} else {
		return x[i] < x[j]
	}
}
func (x StringSorter) Swap(i, j int) { x[i], x[j] = x[j], x[i] }

func main() {
	var n int
	fmt.Scan(&n)

	var arr []string
	for i := 0; i < n; i++ {
		var v string
		fmt.Scan(&v)
		arr = append(arr, v)
	}

	sort.Sort(StringSorter(arr))
	fmt.Println(arr)
}
```

Slice 만을 사용하는 경우 sort.Slice 를 활용해 익명함수를 넘기는 방식으로 작성하는것이 더 일반적인 것 같다.
