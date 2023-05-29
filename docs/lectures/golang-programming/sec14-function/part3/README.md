---
tags: [lecture, go]
title: 함수 - Part3
author: ndy2
date: 2023-05-29
description: >-
  
---

### 1. 익명 함수, Function Expression

```go
package main

import "fmt"

func main() {
	foo()
	func() {
		fmt.Println("anonymoust func 1")
	}()

	var fm2 = func() {
		fmt.Println("anonymoust func 2")
	} // Function Expression

	fm2()
	fmt.Printf("type of fm2 : %T\n", fm2) // "type of fm2 : func()"
}

func foo() {
	fmt.Println("foo")
}
```

Go 에서 Function 은 First-Class-Citizen 이다.

> [!note]
> * 변수에 담을 수 있다. - Functional Expression
> * 함수의 리턴값이 될 수 있다. - Return Function
> * 함수의 인자가 될 수 있다. - Function Callback

```go
package main

import "fmt"

func main() {
	s1 := foo()
	fmt.Println(s1) // "Hello world"

	fe := foo
	fmt.Println(fe()) // "Hello world"
}

func foo() string {
	s := "Hello world"
	return s
}
```

### 2. 함수를 리턴하기

```go
package main

import "fmt"

func main() {
	s1 := foo()
	fmt.Println(s1()) // "100"
}

func foo() func() int {

	return func() int {
		return 100
	}
}

```

Go를 학습할 수록 너무 심각하게 유연해서 이걸 어떻게 체계적으로 잘 활용해야 되는건지 궁금하다.

### 3. Callback

```go
import "fmt"

func main() {
	var add = func(a int, b int) int {
		return a + b
	}
	var added = reduce(0, add, 1, 2, 3, 4)
	fmt.Println(added) // "10"

	var mul = func(a int, b int) int {
		return a * b
	}
	var multiplied = reduce(1, mul, 1, 2, 3, 4)
	fmt.Println(multiplied) // "24"
}

func reduce(init int, f func(a, b int) int, vi ...int) int {
	var result = init
	for _, v := range vi {
		result = f(result, v)
	}
	return result
}
```