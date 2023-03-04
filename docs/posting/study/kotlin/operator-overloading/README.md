---
tags: [kotlin]
title: 연산자 오버로딩
date: 2023-02-19
---
 
> [!quote] 참고 자료
> * [`『코틀린 인 액션』`](http://www.yes24.com/Product/Goods/55148593) by 드미트리 제메로프, 스베트라나 이사코바
>     * 7장 연산자 오버로딩과 기타 관례
> * kotlin documentation - [operator overloading](https://kotlinlang.org/docs/operator-overloading.html)

### 1. 연산자 오버로딩 <sup>operator overloding</sup>

연산자 오버로딩이란 언어 차원에서 제공되는 연산자의 기능을 재정의 하는 것이다.

코틀린에서 관례 <sup>Convention</sup> 에 의해 미리 정해진 함수의 이름의 함수를 `operator` 변경자와 함께 정의하면 연산자를 오버로딩 할 수 있다.

> [!note] 연산자 오버로딩의 특징
> * 연산자 오버로딩은 [basic types](https://kotlinlang.org/docs/basic-types.html) 에 대해 최적화를 제공한다.
> * 즉, 함수 호출에 따른 오버헤드가 없다!

이차원 평면의 좌표를 나타내는 Point 클래스에 대해 확장함수로 여러 연산자 오버로딩을 정의 해보자!

```kotlin
data class Point(val x : Int, val y : Int)
```

### 2. 단항 연산자 <sup>Unary operations</sup>

#### 1. Unary Prefix Operation

| Expression | Translated to  |
| ---------- | -------------- |
| +a         | a.unaryPlus()  |
| -a         | a.unaryMinus() |
| !a         | a.not()        |

```kotlin
operator fun Point.unaryMinus() = Point(-x,-y)

val point = Point(10,20)
println(-point) // "Point(x=-10, y=-20)"
```

의미적으로 상당히 유용하고 쓸만해보인다. :thumbsup:

#### 2. Increments and Decrements

| Expression | Translated to |
| ---------- | ------------- |
| a++, ++a   | a.inc()       |
| a--, --a   | a.dec()       |

각 좌표의 값에 1 씩 더하는 연산을 정의해보자.

```kotlin
operator fun Point.inc() {
    x +=1
    y +=1 
}

fun main(){
 	val p = Point(10, 20)   
	p++
    
    println(println())
}
```

앗 예외가 발생한다.

> [!warning] 예외 메시지
> 1. 'operator' modifier is inapplicable on this function: receiver must be a supertype of the return type
> 2. Val cannot be reassigned
> 3. Val cannot be reassigned
> 4. Functions inc(), dec() shouldn't return Unit to be used by operators ++, --

이런 식으로 사용할 수 없다. 공식 문서와 예외 메시지를 읽어보니 `inc()`, `dec()` 함수는 항상 리턴 값을 가져야 한다고 한다. 또한 여기서는 애초에 `val` 이라 값은 변경 할 수 없었다.

```kotlin
operator fun Point.inc() = Point(x+1, y+1)

fun main(){
 	var p = Point(10, 20)   
	val q = ++p
    // val q = p++
    
    println(p) // "Point(x=11, y=21)"
    println(q) // 전위 연산자 -> "Point(x=11, y=21)", 후위 연산자 -> "Point(x=10, y=20)"
}
```

* `inc()`, `dec()` 연산자도 일반적으로 예상되는 *prefix* 와 *postfix* 형태를 잘 처리해 준다.
* 또한 특히 사항으로 p 는 val 로 선언할 수 없다. 공식문서의 `inc()`, `dec()` 처리 순서에 잘 설명이 나오는데 `inc()`, `dec()` 동작 과정에서 변수 p 에 대한 재할당이 발생하기 때문이다.

### 3. 이항 연산자 <sup>binary operations</sup>

#### 1. 산술 연산자 *arithmetic operators*

| Expression | Translated to |
| ---------- | ------------- |
| a + b      | a.plus(b)     |
| a - b      | a.minus(b)    |
| a * b      | a.times(b)    |
| a / b      | a.div(b)      |
| a % b      | a.rem(b)      |
| a..b       | a.rangeTo(b)  |

* `times()` 연산자를 통해 point 에 대해서 스칼라 곱을 표현해보자.

```kotlin
operator fun Point.times(a: Int) = Point(x*a, y*a)

fun main(){
 	val p = Point(10, 20)   

    val q = p * 3 // val q = 3 * p 로 쓸 수 없다.
    println(q) // "Point(x=30, y=60)"
}
```

* 한편 Point 를 받는 또다른 times 연산자를 통해 외적 벡터의 z 값을 표현 해보자.

``` kotlin title="두개의 다른 times 연산자를 적용할 수도 있다."
data class Point(var x : Int, var y : Int)

operator fun Point.times(a: Int) = Point(x*a, y*a)
operator fun Point.times(a: Point) = x*a.y - y * a.x

fun main(){
 	val p = Point(10, 20)   
    val q = Point(5, 2)
    
    println(p*3) //Point(x=30, y=60) - 스칼라 곱
    println(p*q) //-80 - 벡터의 외적
}
```

#### 2. In Operator

| Expression | Translated to  |
| ---------- | -------------- |
| a in b     | b.contains(a)  |
| a !in b   | !b.contains(a) |

#### 3. Indexed Access Operator

| Expression            | Translated to          |
| --------------------- | ---------------------- |
| a[i]                  | a.get(i)               |
| a[i, j]               | a.get(i,j)             |
| a[i0, i1, ... in]     | a.get(i0,i1, ... , in) |
| a[i] = b              | a.set(i,b)             |
| a[i, j] = b           | a.set(i,j,b)           |
| a[i0, i1, ... in] = b | a.set(i0,i1,...,in, b) |

대 괄호안에 index를 여러개 작성 할 수있다는 점이 눈에 띈다.

`Point` 클래스에 한개의 index 를 받는 `get`, `set` 오퍼레이터를 재 정의해 `index 0` 이 `x` 의 값 `index 1` 이 `y` 의 값을 의미하도록 해보자

```kotlin
data class Point(var x : Int, var y : Int) // set 을 위해 var 로 변경

operator fun Point.get(i: Int) = when (i) {
    0 -> x
    1 -> y
    else -> throw RuntimeException("index must be in 0~1")
}

operator fun Point.set(i: Int, a: Int) = when (i) {
    0 -> this.x=a
    1 -> this.y=a
    else -> throw RuntimeException("index must be in 0~1")
}

fun main(){
 	val p = Point(10, 20)   
	println("x : ${p[0]}, y : ${p[1]}") // "x : 10, y : 20"
    
    p[0] = 11
    p[1] = 21
    println("x : ${p[0]}, y : ${p[1]}") // "x : 11, y : 21"
}
```

#### 4. Invoke Operator

| Expression   | Translated to      |
| ------------ | ------------------ |
| a()          | a.invoke()         |
| a(i)         | a.invoke(i)        |
| a(i0,...,in) | a.invoke(i0,...in) |

소괄호를 통해 함수를 호출하는 것 처럼 동작하게 할 수도 있다.

인자를 받지 않는 invoke 함수를 정의해 한번 호출 할 때마다 90 도 시계방향으로 로테이션 하는 연산자를 오버로딩 해보자.

```kotlin
operator fun Point.invoke() = Point(y, -x)

fun main(){
 	var p = Point(10, 20)   
    
    for(i in 0..3){
        p = p() // p 자체를 invoke! 
        println(p)
    }
    /*
    "Point(x=20, y=-10)"
    "Point(x=-10, y=-20)" 
    "Point(x=-20, y=10)" 
    "Point(x=10, y=20)"
    */
}
```

#### 5. Augmented Assignments (compound assignment)

| Expression | Translated to    |
| ---------- | ---------------- |
| `a+=b`       | a.plusAssign(b)  |
| `a-=b`       | a.miusAssign(b)  |
| `a*=b`       | a.timesAssign(b) |
| `a/=b`        | a.divAssign(b)   |
| `a%=b`       | a.remAssign(b)   |

이론적으로 `+=` 을 `plus`, `plusAssign` 양쪽으로 컴파일 할 수 있다. 하지만 둘 중 한쪽만 정의 하는 것이 안전한다.

#### 6. Equality and Inequality Operators

| Expression | Translated to    |
| ---------- | ---------------- |
| `a==b`       | `a?.equals(b) ?: (b === null)`  |
| `a!=b`       | `!(a?.equals(b) ?: (b === null)`)  |

`동등성 검사`는 `1. equals 호출`과 `2. 널 검사`로 컴파일 된다.

#### 7. Comparison Operators

| Expression | Translated to       |
| ---------- | ------------------- |
| a>b        | a.compareTo(b) > 0  |
| a<b        | a.compareTo(b) < 0  |
| a>=b       | a.compareTo(b) >= 0 |
| a<=b       | a.compareTo(b) <=0  |

compareTo 메서드 하나만 재정의 하면 위 모든 연산자가 재정의 된다.

```kotlin
fun main(){
    println("aa"<"bb") // true
}
```

#### 8. Property Delegation Operators

`provideDelegate`, `getValue`, `setValue` 연산자 함수는 Delegated properties 에서 다루겠습니다.

> [!success] See Also
> * [kotlin.delegation](delegation/README)
> * [kotlin.delegation-properties](delegation-properties/README)
