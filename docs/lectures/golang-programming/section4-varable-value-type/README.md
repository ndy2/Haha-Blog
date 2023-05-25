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
> * Go 패키지의 함수는  `dot(.)` 을 통해 호출할 수 있다.
> * Go 의 기본 패키지들은 공식 문서를 통해 살펴보자!


### 3. 변수를 선언한느 방법

 
> [!quote] 참고 자료
> * https://go.dev/ref/spec#Variables

1. var 키워드 활용
2. 