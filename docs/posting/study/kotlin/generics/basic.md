---
tags: [kotlin, generics]
title: 제네릭스 (generics) 기초
date: 2023-02-17
---
 
> [!quote] 참고 자료
> * [`『코틀린 인 액션』`](http://www.yes24.com/Product/Goods/55148593) by 드미트리 제메로프, 스베트라나 이사코바
>     * 9 장 제네릭스
> * kotlin documentation - [generics](https://kotlinlang.org/docs/generics.html)

### 1. Generic Type Parameter

> [!note] 타입 파라미터와 타입 인자
> * 제네릭스를 사용하면 타입 파라미터 <sup>type parameter</sup> 를 받는 타입을 정의 할 수 있다.
> * 제네릭 타입의 인스턴스를 만들려면 타입 파라미터를 구체적인 타입 인자 <sup>type argument</sup> 로 치환 해야 한다.

> [!warning] 코틀린과 로 타입
> * 자바와 달리 코틀린에서는 제네릭 타입의 타입 인자를 프로그래머가 명시하거나 컴파일러가 추론할 수 있어야 한다.
> * 코틀린은 자바와 달리 처음부터 제네릭을 도입했기 때문에 로 타입을 지원하지 않고 제네릭 타입의 타입 인자를 항상 정의 해야한다.
>
> ```kotlin
> fun main() {  
>    var list : List  
>}
> ```
>
>    -> `Kotlin: One type argument expected for interface List<out E>`

---

### 2. Generic Function and Properties

#### 1. 제네릭 함수 선언

![[1.excalidraw.png]]

#### 2. 제네릭 함수 호출

![[2.png]]

#### 3. 제네릭 확장 프로퍼티 정의와 활용

![[3.png]]

---

### 3. Generic Class Declaration

```kotlin

interface List<T> {
	operator fun get(index: Int) : T
	// ...
}

class StringList : List<String> {
	override fun get(index: Int) : String
	// ...
}

class ArrayList<T> : List<T> {
	override fun get(index: Int): T = ...
	// ...
}

```

----

### 4. Type Parameter Constraint

#### 1. 타입 파라미터 제약

> [!note] 타입 파라미터 제약 <sup>type parameter constraint</sup>
> * 클래스나 함수에 사용할 수 있는 타입 인자를 제한하는 기능
> * 예를 들어 리스트에 속한 모든 원소의 합을 구하는 `sum` 함수는 `List<Int>`, `List<Double>` 등에는 적용할 수 있지만 `List<String>` 등에는 적용할 수 없다.

![[4.png]]

이런 식으로 동작하는 타입 파라미터 제약을 가진 sum 함수의 선언은 아래와 같을 수 있다.

```kotlin
fun <T: Number> List<T>.sum(): T
```

`:warning: 사실 코틀린 표준 라이브러리의 sum 함수는 타입 파라미터를 이용하지 않는다.`

#### 2. 여러 제약을 가하기

```kotlin title="타입 T 는 CharSequence 와 Appendable 을 모두 상속해야 한다."
fun <T> ensureTrailingPeriod(seq: T) where T : CharSequence, T: Appendable {

	if(!seq.endsWith('.')){
		seq.append('.')
	}
}
```

#### 3. 자주 활용되는 케이스 - 타입 파라미터를 널이 될 수 없는 타입으로 한정

* 타입 파라미터 `T` 가 `Any` 를 상속하도록 제한 해라
