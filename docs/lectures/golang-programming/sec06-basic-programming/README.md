---
tags: [lecture, go]
title: 프로그래밍 기초 지식
author: ndy2
date: 2023-05-26
description: >-
  
---
 
> [!quote] 참고 자료
> - go.dev - lanaguage spec
>     * [`『Boolean Types』`](https://go.dev/ref/spec#Boolean_types) 
>     * [`『Numeric Types』`](https://go.dev/ref/spec#Numeric_types)

### 1. Boolean 타입
 
> [!quote] 참고 자료
> - [`『Boolean Types』`](https://go.dev/ref/spec#Boolean_types) on  go.dev

> [!note] Boolean
> *`Boolean Type`* 은 predeclared 된 상수인 `true`, `false` 값을 통해 `Boolean truth` 값을 표현한다. 타입 이름은 `bool` 이다.

### 2. Numeric 타입

> [!quote] 참고 자료
> - [`『`Numeric` Types』`](https://go.dev/ref/spec#Numeric_types) on  go.dev

> [!note] Numeric Type
> *`integer`*, *`floating-point`*, 혹은 *`complex`* 타입은 각각 정수, 부동 소수, 복소수 값의 집합을 의미한다. 이들을 모두 *`numeric type`*  이라고 부른다.

```text title="GoLang 의 아키텍쳐와 무관한 숫자 타입"
uint8       the set of all unsigned  8-bit integers (0 to 255)
uint16      the set of all unsigned 16-bit integers (0 to 65535)
uint32      the set of all unsigned 32-bit integers (0 to 4294967295)
uint64      the set of all unsigned 64-bit integers (0 to 18446744073709551615)

int8        the set of all signed  8-bit integers (-128 to 127)
int16       the set of all signed 16-bit integers (-32768 to 32767)
int32       the set of all signed 32-bit integers (-2147483648 to 2147483647)
int64       the set of all signed 64-bit integers (-9223372036854775808 to 9223372036854775807)

float32     the set of all IEEE-754 32-bit floating-point numbers
float64     the set of all IEEE-754 64-bit floating-point numbers

complex64   the set of all complex numbers with float32 real and imaginary parts
complex128  the set of all complex numbers with float64 real and imaginary parts

byte        alias for uint8
rune        alias for int32
```

```text title="아키텍쳐에 의존적인 숫자형 타입"
uint     either 32 or 64 bits
int      same size as uint
uintptr  an unsigned integer large enough to store the uninterpreted bits of a pointer value
```

> [!note] 특이한 점
> * `short`, `long`, `double` 이라는 표현이 아예 존재하지 않는다. `int16`,  `int64`,  `float64` 가 각각 그 의미를 대체하고 있다. 
> * 컴퓨터 아키텍쳐에 의존적인 타입을 가진다.
>     * 32 비트 플랫폼에서 int 는 32 비트를
>     * 64 비트 플랫폼에서 int 는 64 비트를 가진다!
> * 복소수를 위한 complex 타입이 존재한다.
> * `rune` 은 `character`를 의미한다. Go 는 UTF-8를 기본 인코딩 전략으로 사용한다.
> * alias 라고 적힌 아이들 빼고 위 모든 타입은 전부 개별적인 타입이다. 즉 expression, assignment 등에서 두 타입을 혼용해 쓰고 싶다면 명시적인 타입 전환이 필요하다. 이는 int32 와 int 가 모두 같은 32 비트의 정수를 의미한다고 해도 마찬가지 이다.

### 3. `string` 타입

> [!note] 문자열 타입
> - string type 은 문자열 값의 집합을 나타낸다. string 값은 (빈 문자열 일 수도 있음) byte sequence 이다. 바이트의 길이는 문자열의 `length` (길이) 라고 불리며 음수가 될 수 없다.
> - 문자열은 immutable 하다.
> - 문자열의 길이는 built-in 함수 len 을 통해 구할 수 있다.
> - 문자열 s 의 각 바이트는 0 ~ len(s)-1 의 인덱스를 통해 접근할 수 있다.
> - 문자열의 바이트에 대한 주소에 접근할 수 없다.

```go title="바이트 sequence 를 활용하는 go 의 문자열!"
package main

import "fmt"

func main() {
	s := "안녕, 세상!"
	fmt.Printf("len(s) : %v\n", len(s)) // "len(s) : 15"
	fmt.Printf("%#x\n", s[0])  // "0xec"
	fmt.Printf("%#x\n", s[14]) // "0x21"
}
```

![[hello-world-utf8.png]]

아주 특이하다...
분명 각 char 에 대해 접근하는 방법이 있을것이다! 기대된다!

```go title="바이트, rune 배열로 conversion 할 수 있는 go 의 string!"

package main

import "fmt"

func main() {
	s := "안녕, 세상!"
	bs := []byte(s)
	fmt.Println(bs) // [236 149 136/ 235 133 149/ 44/ 32/ 236 132 184/ 236 131 129/ 33]
	fmt.Printf("%T\n", bs) // []uint8

    rs := []rune(s)
	fmt.Println(rs)        // [50504 45397 44 32 49464 49345 33]
	fmt.Printf("%T\n", rs) // []uint32
}
```

아주 특이하다...

```go title="utf-8 에 따른 code point 를 출력하는 formatting"
package main

import "fmt"

func main() {
	s := "안녕, 세상!"
	rs := []rune(s)
	for i := 0; i < 7; i++ {
		fmt.Printf("%#U\n", rs[i])
	}
}
```

```text title="실행 결과"
U+C548 '안'
U+B155 '녕'
U+002C ','
U+0020 ' '
U+C138 '세'
U+C0C1 '상'
U+0021 '!'
```