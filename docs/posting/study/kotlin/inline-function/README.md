---
tags: [kotlin]
title: inline 함수
date: 2023-02-16
---

@ 참고 자료)

- [`『코틀린 인 액션』`](http://www.yes24.com/Product/Goods/55148593) by 드미트리 제메로프, 스베트라나 이사코바 
    - 8장 고차 함수: 파라미터와 반환 값으로 람다 사용
- kotlin documentation - [Inline Functions](https://kotlinlang.org/docs/inline-functions.html)

---

### 1. Inline 함수 들어가기

[고차 함수 <sup>higher-order functions</sup>](../hof-and-function-type) 을 활용 하면 각 함수는 객체가 되고 각각 closuer 를 포획 합니다. 이를 위해 함수 객체/ 무명 클래스 를 위한 추가적인 메모리 할당이 필요하고 이런것들은 모두 runtime overhead 라고 볼 수 있습니다.

고차 함수를 변수에 담아 여러번 재 활용하는 경우라면 이런 오버헤드는 필수적이지만 그렇지 않다면 람다 식을 inline 함으로써 그런 오버헤드를 없앨 수 있습니다. `lock()` 함수는 이런 상황의 좋은 예시입니다.

- 호출 시점의 코드

```kotlin
lock(l) { foo() }
```

- 컴파일된 코드

```kotlin
l.lock()
try { foo() }
finally { l.unlock() }
```

- 컴파일러가 이렇게 동작하게 하기 위해서 `lock()` 함수에 `inline` 변경자를 넣으면 됩니다.

```kotlin
inline fun <T> lock(lock: Lock, body: () -> T): T { ... }
```

> [!note]
> - `inline` 변경자는 함수 자기 자신과 인자로 받는 람다식 모두에게 영향을 끼칩니다.
> - 컴파일러에 의해 둘 모두 호출 시점에 inline 처리가 됩니다.

### 2. `noinline` 변경자

```kotlin
inline fun foo(inlined: () -> Unit, noinline notInlined: () -> Unit) { ... }
```

`inline` 함수의 모든 람다식이 `inline` 되기 원하지 않는다면 해당 함수 파라미터 앞에 `noinline` 변경자를 추가하면 됩니다.

### 3. Non-local Returns

람다에서는 원 함수에 리턴 할 수 없습니다. 하지만 람다식이 inlined 되었다면 가능합니다.

이런 리턴을 *`non-local`* return 이라고 합니다.

=== "bare `return` is forbidden inside a labmda"

    ``` kotlin
	fun ordinaryFunction(block: () -> Unit) {
	    println("hi!")
	}
	fun foo() {
	    ordinaryFunction {
	        return // ERROR: cannot make `foo` return here
	    }
	}
	fun main() {
	    foo() // 결과 : 'return' is not allowed here 
	}
    ```

=== "label return"

    ``` kotlin
	fun ordinaryFunction(block: () -> Unit) {
	    println("hi!")
	}
	fun foo() {
	    ordinaryFunction {
	        return@ordinaryFunction // label return
	    }
	}
	fun main() {
	    foo() // 결과 : hi!
	}
    ```

=== "bare return with inlined lambda return = non-local return"

    ``` kotlin
	inline fun inlined(block: () -> Unit) {
	    println("hi!")
	}
	fun foo() {
	    inlined {
	        return // OK: the lambda is inlined - non local return
	    }
	}
	fun main() {
	    foo() // 결과 : hi!
	}
    ```
