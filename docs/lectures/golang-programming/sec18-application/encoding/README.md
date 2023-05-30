---
tags: [lecture, go]
title: Json Marshal/Unmarshal
author: ndy2
date: 2023-05-28
description: >-
  
---
 
> [!quote] 참고 자료
> * [`『encoding/json』`](https://pkg.go.dev/encoding/json@go1.20.4) @`pkg.go.dev`

### 0. 들어가며

go 에서는 json 타입에 대해 `Serialize/Deserialize`가 아니라 `Marshal/Unmarshal` 를 제공한다. 둘의 미묘한 차이에 대해서 이해해보자.

![[byte-object.excalidraw.png]]

![[byte-object-2.excalidraw.png]]
 
> [!quote] 참고 자료
> * [`『직렬화와 마샬링』`](https://donghyeon.dev/2020/11/07/직렬화와-마샬링) by 민동현
> * [`『What is the difference between Serialization and Marshaling?』`](https://stackoverflow.com/questions/770474/what-is-the-difference-between-serialization-and-marshaling) - on stackoverflow

> [!note] [`『Marshalling』`](https://en.wikipedia.org/wiki/Marshalling_(computer_science)) on wikipedia
> 컴퓨터 과학에서 `marshlling`/marshaling 은 객체의 메모리 표현을 저장/데이터 전송 등에 적절한 데이터 포멧으로 변환하는 과정이다.

> **So Serialization is a part of Marshalling.** - 대충 요약

마샬링은 remote object 를 다룰 수 있고 데이터 전송의 의도를 더 크게 드러내는 표현인것 같다. 반면 직렬화/역직렬화는 데이터 상태의 전환 만을 의미하는 조금 더 좁은 개념으로 활용되는 것 같다.

이후 내용에서는 remote 니 code-base 니 하는 내용은 다루지 않고 일반적인 serialization 처럼 데이터 포맷 변환의 기능 만을 이야기 하겠다. (사실 go 에서 그 외의 기능을 제공하는지 잘 모르겠다.)

### 1. `func Marshall(v any) ([]byte, error)`

```go
func Marshal(v any) ([]byte, error)
```

`Marshal` 은 v 의 JSON 인코딩을 반환합니다.

```go title="Marshall 예시"
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	type ColorGroup struct {
		ID     int
		Name   string
		Colors []string
	}
	group := ColorGroup{
		ID:     1,
		Name:   "Reds",
		Colors: []string{"Crimson", "Red", "Ruby", "Maroon"},
	}
	b, err := json.Marshal(group)
	if err != nil {
		fmt.Println("error:", err)
	}
	os.Stdout.Write(b)
	// {"ID":1,"Name":"Reds","Colors":["Crimson","Red","Ruby","Maroon"]}
}

```

### 2. `func Unmarshal(data []byte, v any) (error)`

```go
func Unmarshal(data []byte, v any) error
```

Unmarshal 는 JSON-encoded 된 데이터를 파싱하고 결과를 포인터 v 가 가르키는 주소에 저장합니다. 만약 v 가 nil 이거나 pointer 가 아니라면 InvalidUnmarshalError 를 응답합니다.

```go title="Unmarshal 예시"
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	var jsonBlob = []byte(`[
	{"Name": "Platypus", "Order": "Monotremata"},
	{"Name": "Quoll",    "Order": "Dasyuromorphia"}
]`)
	type Animal struct {
		Name  string
		Order string
	}
	var animals []Animal
	err := json.Unmarshal(jsonBlob, &animals)
	if err != nil {
		fmt.Println("error:", err)
	}
	fmt.Printf("%+v", animals)
	// [{Name:Platypus Order:Monotremata} {Name:Quoll Order:Dasyuromorphia}]
}

```