---
tags: [lecture, go]
title: 함수 - Part4
author: ndy2
date: 2023-05-29
description: >-
  
---

### 1. Closure

```go
package main

import "fmt"

func main() {
	var x int
	fmt.Println(x) // "0"

	{
		y := 42
		fmt.Println(y) // "42"
		fmt.Println(x) // "0"
	}
	// fmt.Println(y) // not defined y
}

```

```go
package main

import "fmt"

func main() {
	a := incrementor()
	b := incrementor()

	fmt.Println(a()) // "1"
	fmt.Println(a()) // "2"
	fmt.Println(a()) // "3"
	fmt.Println(b()) // "1"
	fmt.Println(b()) // "2"
}

func incrementor() func() int {
	var x int
	return func() int {
		x++
		return x
	}
}
```

### 2. 재귀

```go title="전통적인 2d 길찾기 문제 with recursive func in go!"
package main

import "fmt"

var n = 4
var m = 5

var board = [4][5]int{
	[5]int{0, 0, 0, 0, 0},
	[5]int{1, 1, 1, 1, 0},
	[5]int{1, 1, 0, 1, 0},
	[5]int{1, 1, 0, 0, 0},
}
var visited = [4][5]bool{}

func main() {
	dfs(0, 0)
}

var dy = [4]int{0, 0, 1, -1}
var dx = [4]int{1, -1, 0, 0}

func dfs(r int, c int) {
	visited[r][c] = true
	fmt.Printf("r : %v, c : %v \n", r, c)
	for d := 0; d < 4; d++ {
		ty, tx := r+dy[d], c+dx[d]
		if isValid(ty, tx) && !visited[ty][tx] {
			visited[ty][tx] = true
			dfs(ty, tx)
		}
	}
}

func isValid(r int, c int) bool {
	return r >= 0 && r < n && c >= 0 && c < m
}

```

```text title="실행 결과"
r : 0, c : 0 
r : 1, c : 0 
r : 1, c : 1 
r : 1, c : 2 
r : 1, c : 3 
r : 2, c : 3 
r : 2, c : 1 
r : 2, c : 0 
r : 3, c : 0 
r : 3, c : 1
```
