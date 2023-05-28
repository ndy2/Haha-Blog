---
tags: [lecture, go]
title: 데이터 묶기
author: ndy2
date: 2023-05-28
description: >-
  
---

 
> [!quote] 참고 자료
> * https://go.dev/ref/spec#Array_types
> * https://go.dev/ref/spec#Slice_types
> * https://go.dev/ref/spec#Map_types

### 1. 배열

> [!note] 배열
> - 배열은 단일 타입 원소의 sequence 입니다.
> 그러한 타입을 `element type` 이라고 부르며 원소의 개수를 배열의 `length` 라고 부릅니다. 배열의 길이는 음수가 될 수 없습니다.

> [!note] 배열의 길이
> - 배열의 길이는 배열 타입의 part 입니다. 길이는 int 타입이고 음수가 될 수 없으며 `int` 타입으로 constant representable 해야 합니다. 배열의 길이는 built-in 함수 `len` 에 의해 구해질 수 있습니다.

```ebnf
ArrayType   = "[" ArrayLength "]" ElementType .
ArrayLength = Expression .
ElementType = Type .
```

```go title="다양한 배열 선언"
[32]byte
[2*N] struct { x, y int32 }
[1000]*float64
[3][5]int
[2][2][2]float64  // same as [2]([2]([2]float64))
```

```go
package main

import "fmt"

func main() {
	var x [5]int
	fmt.Println(x) // "[0, 0, 0, 0, 0]"
	fmt.Printf("%T\n", x) // "[5]int" - 배열의 길이도 타입에 포함된다!!!!
	fmt.Printf("len(x) : %v\n ", len(x)) // "len(x) : 5" - built-in 함수 len
}
```

### 2. slice

> [!note] 슬라이스
> - 슬라이스는 _underlying array_ 의 연속적인 segment 에 대한 descriptor 입니다.
> - 슬라이스는 그 underlying array 의 원소 sequence 에 대한 접근을 제공합니다.
> - 슬라이스의 원소의 개수는 슬라이스의 길이 (`length`) 라고 부르고 음수가 될 수 없습니다.
> - 초기화 되지 않은 슬라이스는 `nil` 값을 가집니다.

```ebnf
SliceType = "[" "]" ElementType .
```

#### 2.1. Slice 를 생성하는 방법

##### Composite LITERAL

```go
package main

import "fmt"

func main() {
	x := []int{4, 5, 7, 8, 42}
	fmt.Println(x) // "[4 5 7 8 42]"
	fmt.Printf("%T\n", x) // "[]int" - 슬라이스의 길이는 포함되지 않는다!
	fmt.Printf("len(x) : %v\n ", len(x)) // "len(x) : 5"
}
```

##### `make`

capacity 를 전달 할 수 있다!

```go
package main

import "fmt"

func main() {
	x := make([]int, 10, 100)
	fmt.Println(x) //"[0 0 0 0 0 0 0 0 0 0]"
	fmt.Println(len(x))
	fmt.Println(cap(x))

	x[0] = 42
	fmt.Println(x) //"[42 0 0 0 0 0 0 0 0 0]"
	fmt.Println(len(x))
	fmt.Println(cap(x))
}

```

#### 2.2. Range For-Loop 를 이용한 Slice 순회

```go
package main

import "fmt"

func main() {
	x := []int{4, 5, 7, 8, 42}
	for i, v := range x {
		fmt.Println(i, v)
	}
}
```

```text
0 4
1 5
2 7
3 8
4 42
```

#### 2.3. Slicing a slice!

> [!note]
> - colon operator 를 이용해 slice 를 짜르자!
> - 음수 index 는 사용할 수 없다.

```go
package main

import "fmt"

func main() {
	x := []int{4, 5, 7, 8, 42}
	y := x[1:]
	// z := x[1:-2] // index -x (constant of type int) must not be negative
	fmt.Println(x) // "[4 5 7 8 42]"
	fmt.Println(y) // "[5 7 8 42]"
}
```

#### 2.4. `append`

```go
package main

import "fmt"

func main() {
	x := []int{4, 5, 7, 8, 42}
	x = append(x, 4, 5, 6)
	fmt.Println(x) //"[4 5 7 8 42 4 5 6]"

	x = append(x, x...) // "[4 5 7 8 42 4 5 6 4 5 7 8 42 4 5 6]"
	fmt.Println(x)
}

```

#### 2.5. 원소를 제거하기

slicing 과 append 를 조합해 원하는 위치의 원소를 제거하자

```go
package main

import "fmt"

func main() {
	x := []int{4, 5, 7, 8, 42}
	x = append(x, 4, 5, 6)
	fmt.Println(x) //"[4 5 7 8 42 4 5 6]"

	x = append(x, x...) // "[4 5 7 8 42 4 5 6 4 5 7 8 42 4 5 6]"
	fmt.Println(x)

	x = append(x[:2], x[4:]...)
	fmt.Println(x) /// "[4 5 42 4 5 6 4 5 7 8 42 4 5 6]"
}
```

#### 2.6. 다차원 slice!

- spread sheet!

```go
package main

import "fmt"

func main() {
	row1 := []string{"aa", "ab", "ac", "ad"}
	row2 := []string{"ba", "bb", "bc", "bd"}

	sheet := [][]string{row1, row2}
	fmt.Println(sheet) // "[[aa ab ac ad] [ba bb bc bd]]"
}
```

### 3. Map

> [!note] Map
> `Map` 은 unique 한 key 로 식별되는 value 의 순서가 없는 그룹입니다. 초기화 되지 않은 맵은 `nil` 값을 가집니다.


```
MapType     = "map" "[" KeyType "]" ElementType .
KeyType     = Type .
```

KeyType 에 대한 비교 연산자 `(==`, `!=`) 는 무조건 정의 되어야 합니다.

#### 3.1. Map 을 생성하는 방법

##### Compisite LITERAL

```go
package main

import "fmt"

func main() {
	m := map[string]int{
		"hello":  5,
		"world!": 6,
		"haha":   4,
	}
	fmt.Println(m)          //"map[haha:4 hello:5 world!:6]"
	fmt.Println(m["hello"]) //"5"
	fmt.Println(m["haha"])  //"4"
	fmt.Println(m["papa"])  //"0"

	v1, ok1 := m["haha"]
	fmt.Println(v1, ok1) // 4 true

	v2, ok2 := m["papa"]
	fmt.Println(v2, ok2) // 0 false
}
```

##### `make`

```go
make(map[string]int)
make(map[string]int, 100) // optional capacity
```

#### 4.2. 원소 추가, range 순회

```go
package main

import "fmt"

func main() {
	m := map[string]int{
		"hello":  5,
		"world!": 6,
		"haha":   4,
	}
	v1, ok1 := m["papa"]
	fmt.Println(v1, ok1) // 0 false

	m["papa"] = 4
	v2, ok2 := m["papa"]
	fmt.Println(v2, ok2) // 4 true

	for k, v := range m {
		fmt.Println(k, v)
	}
}

```

#### 4.3. 원소 제거하기

```go
package main

import "fmt"

func main() {
	m := map[string]int{
		"hello":  5,
		"world!": 6,
		"haha":   4,
	}
	delete(m, "haha")
	fmt.Println(m)
}

```

