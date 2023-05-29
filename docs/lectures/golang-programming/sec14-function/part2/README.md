---
tags: [lecture, go]
title: 함수 - Part2
author: ndy2
date: 2023-05-29
description: >-
  
---
 
> [!quote] 참고 자료
> * [`『타입 선언』`](https://go.dev/ref/spec#TypeDef)

> [!note]
> `Go` is all about ==*TYPE*==

### 1. 인터페이스 선언

> [!note]
> - 구조체도 타입 인터페이스도 타입 함수도 타입 메서드도 타입 숫자도 타입 문자열도 타입 Boolean 도 타입 Slice 도 타입
> - `Go` is all about ==*TYPE*==

인터페이스의 선언 = 타입 선언, 인터페이스 = 타입

```ebnf
인터페이스 선언 = "type" identifier InterfaceSpec
인터페이스 명세 = "interface" "{" 인터페이스 요소 "}"
인터페이스 요소 = 메서드 요소 or 타입 요소.
타입 요소 = one or more TypeTerm
...
```

아주... 복잡해보인다. 일단 go.dev 에서 이야기 하는 interface type 의 정의에 대해 살펴보자.

> [!note]
> - 인터페이스 타입은 *type set* 을 정의한다.
> - 인터페이스 타입의 변수는 해당 type set 에 존재하는 어떠한 타입의 변수도 저장 할 수 있다.
> - 그러한 타입은 interface 의 구현 타입 이라고 표현한다.
> - 초기화 되지 않은 인터페이스 타입의 값은 `nil` 이다.

### 2. interface 관련 예시

```go
package main

import "fmt"

type CarnivorousPlant struct {
	species string
}

type Animal struct {
	species string
}

func (cp CarnivorousPlant) eat(insect string) {
	fmt.Printf("%v eats insect %v\n", cp.species, insect)
}

func (a Animal) eat(food string) {
	fmt.Printf("%v eats food %v\n", a.species, food)
}

type Eatable interface {
	eat(target string)
}

func doEat(eatable Eatable, target string) {
	eatable.eat(target)
}

func main() {
	elephant := Animal{"Elephant"}
	dionaea := CarnivorousPlant{"Dionaea"}

	doEat(elephant, "grass")
	doEat(dionaea, "fly")
}
```

인터페이스로 써 동작할 수 있음을 정의하는 것이 전통적인 OOP 에서 처럼 클래스 (~struct) 에 이루어 지는 것이 아니라 `struct` 의 선언과 분리되어 외부에 메서드를 정의하는 것으로 이루어 질 수 있다는 점이 아주 인상적이다.

전통적인 방식 보다 훨씬 유연하게 타입을 구성/설계 할 수 있을 것으로 생각된다.

### 3. Go 는 OOP 를 지원하는 언어인가요?

인터페이스의 더 복잡한 활용과 문법을 살펴보는 것은 미루어 두고 위 주제에 대해서 알아보자.

> Go 는 OOP 를 지원하는 언어인가요?

