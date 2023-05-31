---
tags: [lecture, go]
title: 동시성
author: ndy2
date: 2023-05-28
description: >-
  
---

### 1. 동시성 vs 병렬성

### 1.5 go 키워드와 goroutine

```go
package main

import (
	"fmt"
)

func main() {
	foo()
	bar()
}

func foo() {
	for i := 0; i < 10; i++ {
		fmt.Println("foo:", i)
	}
}

func bar() {
	for i := 0; i < 10; i++ {
		fmt.Println("bar:", i)
	}
}
```
```text title="실행결과"
foo: 0
foo: 1
foo: 2
foo: 3
foo: 4
bar: 0
bar: 1
bar: 2
bar: 3
bar: 4
```

위 코드를 병렬적으로 만들어보자!

그전에 go 의 유용한 기능을 사용해보자.

```go
func main() {
	fmt.Println("OS \t : ", runtime.GOOS)
	fmt.Println("ARCH \t : ", runtime.GOARCH)
	fmt.Println("CPUs \t : ", runtime.NumCPU())
	fmt.Println("Goroutines \t : ", runtime.NumGoroutine())
}
```

```text title="실행 결과"
OS 	 :  linux
ARCH 	 :  amd64
CPUs 	 :  8
Goroutines 	 :  1
```

그럼 이제 goroutine 을 이용해 위 코드가 동시성을 가지도록 해보자.

```go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("OS \t\t : ", runtime.GOOS)
	fmt.Println("ARCH \t\t : ", runtime.GOARCH)
	fmt.Println("CPUs \t\t : ", runtime.NumCPU())
	fmt.Println("Goroutines \t : ", runtime.NumGoroutine())

	go foo()
	bar()

	fmt.Println("CPUs \t\t : ", runtime.NumCPU())
	fmt.Println("Goroutines \t : ", runtime.NumGoroutine())
}

func foo() {
	for i := 0; i < 5; i++ {
		fmt.Println("foo:", i)
	}
}

func bar() {
	for i := 0; i < 5; i++ {
		fmt.Println("bar:", i)
	}
}
```
```text title="실행 결과"
OS 		 :  linux
ARCH 		 :  amd64
CPUs 		 :  8
Goroutines 	 :  1
bar: 0
bar: 1
bar: 2
bar: 3
bar: 4
CPUs 		 :  8
Goroutines 	 :  2
```

위 코드는 동시성을 가진다. (goroutine 이 2가됨)
또한 foo 출력이 사라졌다!

왜 와이? 그리고 goroutine 이 뭐지? 쓰레드 같은건가?!

### 2. WaitGroup

```
package main

import (
	"fmt"
	"runtime"
	"sync"
)

var wg sync.WaitGroup

func main() {
	fmt.Println("OS \t\t : ", runtime.GOOS)
	fmt.Println("ARCH \t\t : ", runtime.GOARCH)
	fmt.Println("CPUs \t\t : ", runtime.NumCPU())
	fmt.Println("Goroutines \t : ", runtime.NumGoroutine())

	wg.Add(1)
	go foo()
	bar()

	fmt.Println("CPUs \t\t : ", runtime.NumCPU())
	fmt.Println("Goroutines \t : ", runtime.NumGoroutine())
	wg.Wait()
}

func foo() {
	for i := 0; i < 5; i++ {
		fmt.Println("foo:", i)
	}
	wg.Done()
}

func bar() {
	for i := 0; i < 5; i++ {
		fmt.Println("bar:", i)
	}
}
```

```text title="실행 결과"
OS 		 :  linux
ARCH 		 :  amd64
CPUs 		 :  8
Goroutines 	 :  1
bar: 0
bar: 1
bar: 2
bar: 3
bar: 4
CPUs 		 :  8
Goroutines 	 :  2
foo: 0
foo: 1
foo: 2
foo: 3
foo: 4
```

### 3. 다시보는 WaitGroup

