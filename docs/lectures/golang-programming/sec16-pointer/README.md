---
tags: [lecture, go]
title: 포인터
author: ndy2
date: 2023-05-28
description: >-
  
---
 
### 1. Pointer

```go
package main

import "fmt"

func main() {
	a := 42
	fmt.Println(a)              // "42"
	fmt.Println(&a)             // "0xc00001c030" - address operation `&a`
	fmt.Printf("%T, %T\n", a, &a) // "int, *int" - pointer type `*int`
  fmt.Println(*(&a))          // "42" -  pointer indirection *(&a) (a.k.a. - dereference)
}
```

> [!note] [Address operators](https://go.dev/ref/spec#Address_operators)
> 타입 `T` 의 operand `x` 에 대해 주소 연산 `&x` 는 `x` 를 가르키는 포인터 타입 `*T` 의 포인터를 생성합니다.

> [!note] [Pointer Type](https://go.dev/ref/spec#Pointer_types) on go.dev
> 포인터 타입이란 base type 변수를 가르키는 모든 포인터의 집합을 표현합니다.

```ebnf
PointerType = "*" BaseType .
BaseType = Type.
```
### 2. Pointer Usage?!

```go
package main

import "fmt"

func main() {
	x := 0
	foo(x)         // "0\n43"
	fmt.Println(x) // "0"

	y := 0
	bar(&y)        // "0\n43"
	fmt.Println(y) // "43" - y get updated!!
}

func foo(y int) {
	fmt.Println(y)
	y = 43
	fmt.Println(y)
}

func bar(y *int) {
	fmt.Println(*y)
	*y = 43
	fmt.Println(*y)
}
```
### 3. Method Set

