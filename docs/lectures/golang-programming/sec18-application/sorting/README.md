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

### 2. 정수 Slice - desending, abs 로 정렬

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

### 3. 정수 slice - 절댓값으로 정렬

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

