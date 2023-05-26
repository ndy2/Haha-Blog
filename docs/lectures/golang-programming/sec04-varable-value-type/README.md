---
tags: [go]
title: Go - 변수,값,타입
author: ndy2
date: 2023-05-25
description: >-
  
---

### 1. HelloWorld

```go title="Hello World!"
package main

import "fmt"

func main() {
	fmt.Println("Hello world!") // "Hello world!"
}

// control flow;
// (1) sequence
// (2) loop; iterative
// (3) conditional
```

> [!note]
> * Go 프로그램은 package main 의 main 함수 실행으로 시작된다.

```go title="Hello Function!, Loop, Conditonal"
package main

import "fmt"

func main() {
	fmt.Println("Hello world!") // "Hello world!"
    foo() // "I'm in foo"

    for i := 0; i < 100 ; i ++ {
        if i % 2 == 0 {
            fmt.Println(i) // "0", "2", "4", "6" ...
        }
    }
}

func foo(){
    fmt.Println("I'm in foo")
}
```

```go title="위의 코드에 go fmt 를 적용!"
package main

import "fmt"

func main() {
	fmt.Println("Hello world!") // "Hello world!"
	foo()                       // "I'm in foo"

	for i := 0; i < 100; i++ {
		if i%2 == 0 {
			fmt.Println(i) // "0", "2", "4", "6" ...
		}
	}
}

func foo() {
	fmt.Println("I'm in foo")
}
```

```bash title="how to run go code"
go run anything.go
```

### 2. 패키지 소개

> [!quote] 참고 자료 on go.dev
> * [fmt 패키지](https://pkg.go.dev/fmt) 
> * [fmt.Println 함수](https://pkg.go.dev/fmt#Println) 

> [!note]
> * Go 의 패키지는 함수, 타입, 상수 들을 구조화 할 수 있다.
> * Go 패키지의 함수는 `dot(.)` 을 통해 호출할 수 있다.
> * Go 의 기본 패키지들은 공식 문서를 통해 살펴보자!

### 3. 변수를 선언하는방법

 
> [!quote] 참고 자료
> * https://go.dev/ref/spec#Variables
> * https://go.dev/ref/spec#Variable_declarations

1. var declaration

```go
package main  
  
func main() {  
	var a = "hello"  
	println(a)  
}
```

```go title="공식 문서의 다양한 변수 선언 방식"
var i int
var U, V, W float64
var k = 0
var x, y float32 = -1, -2
var (
	i       int
	u, v, s = 2.0, 3.0, "bar"
)
var re, im = complexSqrt(-1)
var _, found = entries[name]  // map lookup; only interested in "found"
```

2. Short variable declarations

```go
package main  
  
func main() {  
	a := "hello"
	println(a)  // builtin println
}
```

```go title="공식 문서의 다양한 short 변수 선언"
i, j := 0, 10
f := func() int { return 7 }
ch := make(chan int)
r, w, _ := os.Pipe()  // os.Pipe() returns a connected pair of Files and an error, if any
_, y, _ := coord(p)   // coord() returns three values; only interested in y coordinate
```

### 4. Zero Value

 
> [!quote] 참고 자료
> * https://go.dev/ref/spec#The_zero_value

`선언` 혹은 `new 호출` 을 통해 `변수` 를 저장할때 명시적으로 값을 주지않는 경우 변수는 기본 값을 가집니다. 이런 기본 값은 변수의 타입에 따라 결정되며 GoLang 에서는 이 값을 `Zero Value` 라고 부릅니다. 

| type                                              | zero value |
| ------------------------------------------------- | ---------- |
| int                                               | 0           |
| float                                               | 0.0          |
| boolean                                           | false      |
| string                                            | ""         |
| pointer, function, interface, slice, channel, map | `nil`      |

### 5. `fmt` 패키지

#### `print`, `printf`, `println`

```go title="PrintF"
package main  
  
import "fmt"  
  
func main() {  
	a := 42  
	fmt.Println(a) // 42  
	fmt.Printf("%T\n", a) // int  
	fmt.Printf("%b\n", a) // 101010  
	fmt.Printf("%x\n", a) //2a  
	fmt.Printf("%X\n", a) //2A  
	fmt.Printf("%#X\n", a) //0x2A  
}
```

### 6. Custom Type & Conversion

```go
package main  
  
import "fmt"  
  
type hotdog int  
  
func main() {  
	var a hotdog = 1  
	var b int = 2  
	fmt.Println(a, b) // "1 2"  
	fmt.Printf("%T\n", a) // "main.hotdog  
	fmt.Printf("%T\n", b) // "int"  
	// a = b // Cannot use 'b' (type int) as the type hotdog  
	b = int(a) // convert hotdog to int  
	a = hotdog(b) // convert int to hotdog  
	fmt.Println(a, b) // "1 1"  
}
```