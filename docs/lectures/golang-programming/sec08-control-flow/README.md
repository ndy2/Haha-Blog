---
tags: [lecture, go]
title: 제어문 - 반복문, 분기문
author: ndy2
date: 2023-05-27
description: >-
  
---

### 1. Control flow

> [!note] [`『Control flow』`](https://en.wikipedia.org/wiki/Control_flow) on wikipedia
> 컴퓨터 과학에서 *`control flow`* 란 명령형 프로그램에서 개별 구문, 명령어 혹은 함수 호출의 실행/평가 순서를 의미한다.
> 
> 이런 *`control flow`* 를 명시적으로 강조하는 지의 여부가 `명령형 프로그래밍 언어`와 `선언형 프로그래밍 언어`를 구분하는 기준이 된다.

### 2. 반복문

 
> [!quote] 참고 자료
> * https://go.dev/ref/spec#For_statements

"for" 문은 블락의 반복적인 실행을 담당합니다. for 문은 세가지 종류가 있습니다.

```ebnf
ForStmt = "for" [ [Condition] | [ForClause] | [RangeClause] ] [Block]

Condition = [Expression]
```

위 구문을 풀어보면 
1. `ForStmt` = `for [Condition (=Expression)] [Block]`
2. `ForStmt` = `for [ForClause] [Block]`
3. `ForStmt` = `for [RangeClause] [Block]`

세가지 형태로 포문이 구성될 수 있다는 것을 알 수 있습니다. 또한 for 과 block 사이 `컨디션, for, range 절에` 별도의 괄호 문법이 없다는 점 역시 인상적입니다.

#### 1. while 문 짭퉁 - for + single condition

```go
for a < b {
    a *= b
}

for {
    a *= b
} // 무한 루프!
```

### 2. 전통적인 인덱스를 이용한 for 문

```ebnf
ForClause = [ [InitStmt] ] ";" [ [Condition] ] ";" [ [PostStmt] ] .

InitStmt = [SimpleStmt] .
PostStmt = [SimpleStmt] .
```

`SimpleStmt` 는 간단한 구문으로 `InitStmt` 에서는 short variable declaration 형태로 주어질 수 있다. 반면 `PostStmt` 절대 변수 할당이 이루어 질 수 없다.

`InitStmt` 는 non-empty 인 경우 for 문의 시작전 단 한번만 호출된다.
`PostStmt` 는 매 블락의 호출 이후 호출된다.

```go
for i := 0; i < 10; i++ {
	f(i)
}
```

ForClause 의 모든 요소는 empty 가 될 수 있다. 하지만 이경우 semicolon 을 통해 각 요소의 구분을 해 주어야 한다.

#### 3. Range 루프 - TBD

### 4. 분기문 - if 문

 
> [!quote] 참고 자료
> * https://go.dev/ref/spec#If_statements

```ebnf
IfStmt = "if" [ [SimpleStmt] ";" ] [Expression] [Block] [ "else" ( [IfStmt]| [Block] ) ] .
```

"if" 와 `Expression (판별 식)` 사이에 `SimpleStmt` 가 추가 될 수 있다는 점이 신기하다.

가장 기본적인 형태는 아래와 같다.

```go
if x > max {
	x = max
}
```

반면 가장 복잡한 형태는 아래와 같다. 사이에 추가된 `SimpleStmt` 를 통해 판별식에서 사용할 변수에 이름을 주는 방식으로 사용하여 가독성을 높일 수 있다는 점에서 아주 좋은 구조 같다.

```go
if x := f(); x < y {
	return x
} else if x > z {
	return z
} else {
	return y
}
```

### 5. Switch 문

```ebnf
SwitchStmt = [ExprSwitchStmt] | [TypeSwitchStmt].
```

Switch 문은 `Expression Switch 문`과 `Type Siwth 문` 두가지가 있다.

#### 5.1. Expression Switch 문

예시만 살펴보자.

```go
switch tag {
    default: s3()
    case 0, 1, 2, 3: s1()
    case 4, 5, 6, 7: s2()
}

switch x := f(); {  // missing switch expression means "true"
    case x < 0: return -x
    default: return x
}

switch {
    case x < y: f1()
    case x < z: f2()
    case x == 4: f3()
}
```

`fallthrough` 를 통해 전통적인 switch 문의 fall-through 케이스 처럼 동작할 수 있다. 

#### 5.2. Type 스위치 문

```go
switch i := x.(type) {
    case nil:
    	printString("x is nil")                // type of i is type of x (interface{})
    case int:
    	printInt(i)                            // type of i is int
    case float64:
    	printFloat64(i)                        // type of i is float64
    case func(int) float64:
    	printFunction(i)                       // type of i is func(int) float64
    case bool, string:
    	printString("type is bool or string")  // type of i is type of x (interface{})
    default:
    	printString("don't know the type")     // type of i is type of x (interface{})
}
```