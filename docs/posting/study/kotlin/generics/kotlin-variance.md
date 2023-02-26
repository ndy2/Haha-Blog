---
tags: [kotlin, generics]
title: 변성 in Kotlin
date: 2023-02-18
---

!!! quote " 참고 자료 "

    * kotlin documentation - [generics#Variance](https://kotlinlang.org/docs/generics.html#variance)
    * [`『코틀린 인 액션』`](http://www.yes24.com/Product/Goods/55148593) by 드미트리 제메로프, 스베트라나 이사코바 
        * 9장 제네릭스

---

### 0. 들어가며

[이전 글](../java-variance) 에서

1. 변성의 세가지 종류와 적용 조건 (PECS)
2. 자바에서 extends, super 키워드를 이용해 convariance, contravariance 를 적용 하는 법

을 알아보았다. 

이제,

1. 코틀린에서 변성을 다루기 위해 사용하는 두가지 `variance annotation` 인 `in`, `out` 변경자
2. 코틀린의 `declaration-site variance` 와 `type-projection (call-site variance)`

두가지에 대해서 알아보자!

---

### 1. Declaration-site variance

선언 지점 변성은 자바에는 존재하지 않던 코틀린의 새로운 개념이다. 그 이름과 공식문서의 예제에서 그 모티프를 알 수 있다. 공식문서의 예제를 살펴보자.

`interface Source<T> { T nextT(); }`

java 에서 위 generic interface 를 살펴보자. 선언 지점 변성을 이해하기 위해 필요한 이 인터페이스의 중요한 특징은 타입 파라미터 `T` 를 메서드의 반환 값에서만 사용하고 메서드의 파라미터에는 포함되지 않는 다는 것이다.

```java
void demo(Source<String> strs) {
  Source<Object> objects = strs; // !!! Not allowed in Java // ...
}
```

당연히 위 코드는 컴파일러에러가 발생한다.

하지만 지난 시간 정리한 *PECS* 와 함께 개념을 다시 생각해보면 `Source<T>` 인터페이스는 `T` 타입의 Producer 이다. 또한 위 코드에서 실제로 String 을 생성 할지라도 사용하는 측 입장에서 Object 를 생성한다고 이해해도 아무 문제가 없다. 

선언 지점 변성 <sup>declaration-site variance</sup> 은 이러한 모티프에서 도입되었다. 선언 지점 변성을 통해 컴파일러에게 `Source<T>` 는 `T` 타입을 생성만 하고 따라서 `Source<T>` 대신 `Source<Object>` 를 사용해도 문제가 없다는 것을 알려 줄 수 있다. kotlin 에서는 두가지 `variance annotation` - `in`, `out` 변경자를 통해 이를 나타낼 수 있다. 

```kotlin title="out 변경자의 활용으로 공변성 획득"
interface Source<out T> { fun nextT(): T } 

fun demo(strs: Source<String>) { 
    val objects: Source<Any> = strs 
    // This is OK, since T is an out-parameter 
    // Source<String> 이 Source<Any> 의 하위 타입처럼 동작한다. 
}
```

in 변경자는 반대로 타입 T 를 사용하기만 하는 경우 도입하여 반공변성을 추가 할 수 있습니다.

```kotlin title="in 변경자의 활용으로 반공변성 획득"
interface Comparable<in T> { operator fun compareTo(other: T): Int } 

fun demo(x: Comparable<Number>) { 
    x.compareTo(1.0) 
    // 1.0 has type Double, which is a subtype of Number // Thus, you can assign x to a variable of type Comparable<Double> 
    
    val y: Comparable<Double> = x // OK! - 반공변성
}
```

`in`/`out` 변경자의 이름을 통해 그 역할을 쉽게 유추할 수 있습니다!

### 2. Use-site Variance: Type Projections

클래스/ 인터페이스 전체가 타입 파라미터 T 에 대해서 in/out 한 성질을 가지는 경우 선언 지점 변성을 적용할 수 있습니다. 그렇지 않은 경우에는 Use-site varinace 를 적용 할 수 있습니다. `Array<T>` 는 그런 클래스 중 하나입니다.

```kotlin
class Array<T>(val size: Int) { 
    operator fun get(index: Int): T { ... } // T 를 생산 (out)
    operator fun set(index: Int, value: T) { ... } // T 를 사용 (in)
}
```

`Use-site Variance` 는 그 이름 처럼 사용하는 시점에 `T` 를 produce 하기만 하는 메서드만 혹은 `T` 타입을 consume 하는 메서드만 사용 하는 경우라면 사용 시점에 변성을 정의해 주는 방식입니다. 

배열 클래스에 use-site variance 를 적용한 두 예시 를 살펴보고 글을 마치겠습니다.

```kotlin title="copy 에서는 from 메열을 통해 배열의 타입을 생산 하기만 한다"
fun copy(from: Array<out Any>, to: Array<Any>) { ... }
```

```kotlin title="fill 메서드 에서는 dest 배열의 String 타입을 소비하는 메서드만 활용한다."
fun fill(dest: Array<in String>, value: String) { ... }
```
