---
tags: [lecture, go]
title: 구조체
author: ndy2
date: 2023-05-28
description: >-
  
---
 
> [!quote] 참고 자료
> * [Struct Types](https://go.dev/ref/spec#Struct_types)

### 1. Struct 타입 - 구조체

> [!note] _Struct_ 
> - `struct` 란 `field` 라고 불리는 이름을 가진 원소들의 나열 (sequence) 입니다.
> - 필드의 이름은 명시적으로 나타내어 질 수도 있고(IdentifierList) 또한 그렇지 않을 수도 (EmbeddedField) 있습니다.
> - `struct` 에서 non-blank 필드 명은 unique 해야 합니다.

```go title="구조체 예시"
// An empty struct.
struct {}

// A struct with 6 fields.
struct {
	x, y int
	u float32
	_ float32  // padding
	A *[]int
	F func()
}
```

```go title="구조체 person 과 다양한 생성 예시"
package main

import "fmt"

type person struct {
	first string
	last  string
	age   int
}

func main() {
	haha := person{
		"n",
		"dy",
		17,
	}
	fmt.Println(haha) // "{n dy 17}"

	papa := person{ //
		first: "James",
		last:  "Bond",
		age:   42,
	}
	fmt.Println(papa) // "{James Bond 42}"

	// baby := person{"b", "aby"} //  too few values in struct literal of type person
	baby := person{first: "b", last: "aby"}
	fmt.Println(baby)     // "{b aby 0}"- it works!
	fmt.Println(person{}) // "{  0}" - it works TOO!

	newPerson := new(person)
	newPerson.first = "hello"
	newPerson.last = "world"
	fmt.Println(newPerson) // "&{hello world 0}"
}
```

### 2. _embedded field_

> [!note] embedded field
> 타입을 가지지만 명시적인 필드 이름을 가지지 않는 필드를 _embedded field_ 라고 부릅니다.
> embedded field 는 꼭
> - 타입 이름 T 로 식별되거나
> - 인터페이스가 아닌 타입 이름 `*T` 로 식별되거나
> - T 자체는 포인터가 타입이 될 수 없어야 합니다. ??

```go title="embedded field 예시"
// A struct with four embedded fields of types T1, *T2, P.T3 and *P.T4
struct {
	T1        // field name is T1
	*T2       // field name is T2
	P.T3      // field name is T3
	*P.T4     // field name is T4
	x, y int  // field names are x and y
}
```

```go title="field name conflict - illegal struct"
struct {
	T     // conflicts with embedded field *T and *P.T
	*T    // conflicts with embedded field T and *P.T
	*P.T  // conflicts with embedded field T and *T
}
```

### 3. Promotion

> [!note] `promoted`
> 구조체 x 의 (필드) 혹은 (embedded 필드의 메서드) f 는 x.f 가 legal selector 인 경우
> `promoted` 됩니다.

```go title="promoted"
package main

import "fmt"

type person struct {
	first string
	last  string
	age   int
}

type secretAgent struct {
	person // embedded field with implicit name
	ltk    bool
}

func main() {
	sa := secretAgent{
		person: person{"James", "Bond", 42},
		ltk:    true,
	}
	fmt.Println(sa) // "{{James Bond 42} true}"

	fmt.Println(sa.first) // "James" - promoted
	fmt.Println(sa.last)  // "Bond" - promoted 
	fmt.Println(sa.age)   // "42" - promoted
	fmt.Println(sa.ltk)   // "true"
}
```

### 4. Anonymous Struct

```go title="바로 위의 비밀요원 구조체를 익명 구조체로 변경"
package main

import "fmt"

type person struct {
	first string
	last  string
	age   int
}

func main() {
	sa := struct {
		person
		ltk bool
	}{
		person: person{"James", "Bond", 42},
		ltk:    true,
	}
	fmt.Println(sa) // "{{James Bond 42} true}"

	fmt.Println(sa.first) // "James" - promoted
	fmt.Println(sa.last)  // "Bond" - promoted
	fmt.Println(sa.age)   // "42" - promoted
	fmt.Println(sa.ltk)   // "true"
}

```
