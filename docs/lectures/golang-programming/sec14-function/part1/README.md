---
tags: [lecture, go]
title: 함수 - Part1
author: ndy2
date: 2023-05-28
description: >-
  
---

 
> [!quote] 참고 자료 on go.dev
> * [`『함수 타입』`](https://go.dev/ref/spec#Function_types )
> * [`『함수 선언』`](https://go.dev/ref/spec#Function_declarations)
> * [`『메서드 선언』`](https://go.dev/ref/spec#Method_declarations)

### 1. 함수 선언 Syntax

```ebnf
FunctionDecl = "func" FunctionName [ TypeParameters ] Signature [ FunctionBody ] .

FunctionName = identifier .
FunctionBody = Block .
```

- `[TypeParameters]` 는 제네릭 함수/메서드에 관련된 문법이라 이번에는 다루지 않겠습니다.
- `[FunctionBody]` 가 `optional` 로 표기 된것은 assembly routine 등을 통해서 외부에 구현이 이루어진 함수인 경우를 이야기 한 다는데 역시 무슨 소린지 모르겠습니다.

쳐낼거 다 쳐내면 go 의 함수 선언 문법은 아래와 같이 정리 할 수 있습니다.

```ebnf
FunctionDecl = "func" identifier Signature Block
Signature = ??
```

함수, 메서드에서 이야기 하는 `Signature` 의 형태는 다음 링크 [`『함수 타입』`](https://go.dev/ref/spec#Function_types ) 에서 확인 할 수 있습니다. 

```ebnf title="go 의 funtion signature"
Signature      = Parameters [ Result ] .
Result         = Parameters | Type .
Parameters     = "(" [ ParameterList [ "," ] ] ")" .
ParameterList  = ParameterDecl { "," ParameterDecl } .
ParameterDecl  = [ IdentifierList ] [ "..." ] Type .
```

자바를 먼저 학습한 사람으로써 메서드/함수의 시그니쳐가 두 언어에서 다르게 정의 되는것이 신기합니다.

| 언어 | 메서드/ 함수 시그니처       | 역할        |
| ---- | --------------------------- | ----------- |
| Go   | 파라미터 목록 + 리턴 타입   | ???         |
| Java | 메서드 이름 + 파라미터 목록 | 메서드 식별 | 


### 2. 메서드 선언 Syntax

> [!note]
> 메서드는 *receiver* 를 가지는 함수이다.

```ebnf
MethodDecl = "func" Receiver MethodName Signature [ FunctionBody ] .

Receiver   = Parameters .
```

###  3. 함수 선언 examples

[*go.dev*](https://go.dev/ref/spec#Method_declarations) 에 따르면 go 에서 메서드는 그저 *receiver type* 을 가지는 함수의 일종입니다. 앞으로는 특별히 구분히 필요하지 않은 선에서 함수라는 용어를 사용하겠습니다.

위의 `Syntax` 들을 전부 풀어보면 아래와 같은 초 간단 함수 선언 Syntax 가 추출됩니다.

```ebnf
함수선언 = "func" [Receiver] identifier ([Parameters]) {
    // code block
}
```

이 Syntax 에 따라 다양한 함수 선언의 예시를 살펴보겠습니다.

```go
package main

import "fmt"

// "func" fi () { block }
func main() {
	foo()
	bar("world!")
	fmt.Println(woo("tang!"))
	fmt.Println(join("1234", "6789", "5"))
}

// "func" fi () { block }
func foo() {
	fmt.Println("foo")
}

// "func" fi (pi pt) { block }
func bar(s string) {
	fmt.Println("Hello", s)
}

// "func" fi (pi pt) (rt) { block }
func woo(st string) string {
	return fmt.Sprint("woo !", st)
}

// "func" fi (pi1, pi2 pt1, pi3, pt2) (rt) { block }
func join(a, b string, deleminator string) string {
	return fmt.Sprint(a, deleminator, b)
}
```

```text title="실행결과"
foo
Hello world!
woo !tang!
123456789
```

*join* 함수에서 parameter 선언시 타입이 같은 인자를 연속에서 선언하는 경우 계속해서 parameter type 을 작성하지 않아도 되는 것이 인상적입니다.

### 4. variadic function

> [!quote] 참고 자료
> * [`『Variadic function』`](https://en.wikipedia.org/wiki/Variadic_function) on Wikipedia
> * [`『Passing arguments to ... parameters』`](https://go.dev/ref/spec#Passing_arguments_to_..._parameters) 

go 의 함수에도 `Java` 의 `vararg (가변 인자)` 와 같은 기능이 있다. 그것은 바로바로 *variadic function* 이다.

> [!note] Variadic function in Go
> - 함수 시그니쳐의 마지막 파라미터의 타입 앞에 `...` 이라는 prefix 가 붙어 있는 함수를 *Variadic Function* 이라고 부른다.
> - variadic 함수의 마지막 파라미터에는 임의 개수의 인자를 전달 할 수 있다.

vararg 대신 Go에서는 *variadic* 이라는 표현을 사용하는데 위키를 살펴보니 오히려 *variadic* 이 더 정확한 표현같기도 하다. 하지만 그런것 보다도 각 언어에서 사용하는 정확한 용어를 사용하는것이 가장 좋은거 같다.

하여튼 요 Go 의 *varadic function* 같은 경우는 Java 처럼 마지막 파라미터에만 적용할 수 있다.

vararg 와 항상 세트로 등장하는것이 바로 *spread operator* 이다. 근데 또 용어가 골 때리는 것이 문서를 살펴 보아도 Go 에서는 이 spread 연산에 별도의 네이밍을 주지 않았다. 그냥 ... parameter 에 인자를 전달하기 란다... 뭔가 Go 를 개발하는 분들이 생각했을 때 `spread operator` 라는 이름이 별로 맘에 들지 않았던 이유가 있었을거 같다.

강의에서도 이 부분을 이야기 하며 `unfurling` 이라는 용어를 사용하였는데 개인적으로 그냥 익숙한 `spread operator` 라고 이해해야겠다.

하여튼 Go 에서는 javascript 와 유사하게 `...` 을 통해 slice 를 varadic 파라미터에 인자로 넘겨 줄 수 있다. 

```go
func Greeting(prefix string, to ...string)
Greeting("hello:", "haha", "papa", "james")
```

이 `...` spread 연산자 및 variadic function 을 사용할때 인자를 넘겨주기 위해 새로운 `slice` 타입이 생성되는 지의 여부를 고려하는것이 꽤나 중요해보인다. 

특히 아무 인자도 넘겨주지 않을때 빈 slice 가 아니라 `nil` 을 넘겨준다고 한다. 사용하는 측에서는 이를 적절히 고려하여 코드를 작성해야 될 것 같다.

### 4. `defer`
 
> [!quote] 참고 자료
> * [`『Defer statement』`](https://go.dev/ref/spec#DeferStmt)

defer 된 구문은 surrounding function 이 return 하기 전 까지 실행이 연기 된다. Java 의 try-finally 처럼 리소스를 정리하는 용도 등으로 사용할 수 있다고 한다.