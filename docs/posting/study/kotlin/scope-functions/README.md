---
tags:[kotlin]
title: scope functions
date: 2023-02-08
---

@ 참고 자료)

- [코틀린 인 액션](http://www.yes24.com/Product/Goods/55148593) by 드미트리 제메로프, 스베트라나 이사코바
- 자바 개발자를 위한 코틀린 입문 [by 최태현 on Inflearn](https://www.inflearn.com/course/java-to-kotlin/)
- kotlin documentation - [scope functions](https://kotlinlang.org/docs/scope-functions.htm)

---

!!! example

    scope function 을 활용하는 다양한 예시는 만날때 마다 [note](../../../notes/cheetsheets/kotlin/scope-functions) 에 업데이트 할 예정입니다. 여기서는 scope function 의 기술적인 동작 방식과 간단한 활용에 대해서만 다루겠습니다.
---

### 1. Scope Function 이란?

!!! note "scope function"

    * 일시적인 영역을 형성하는 함수
    * lambda 를 사용해 일시적인 영역을 만들고 코드를 더 간결하게 만들거나, method chaing 에 활용한다.

- 아래의 메서드에 scope function 을 적용해 보며 리팩토링 해보겠습니다.

```kotlin
fun printPerson(person: Person?){
    if(person != null){
        println(person.name)
        println(person.age)
    }
}
```

### 2. Scope Function 을 알아보기 전에....

#### Standard.kt

scope function 에는 다섯가지 종류 (let, with, run, apply, also) 가 있으며 이들은 모두 kotlin standard 라이브러리의 Standard.kt 에 탑 레벨 메서드로 정의 되 있습니다. 

scope function 을 알아보기 전 이 Standard.kt 파일을 한번 전체적으로 훑고 가보면 좋을 것 같습니다.

```kotlin title="Standard.Kt"
@file:kotlin.jvm.JvmMultifileClass  
@file:kotlin.jvm.JvmName("StandardKt")  
package kotlin  
  
import kotlin.contracts.*

public class NotImplementedError(message: String = "An operation is not implemented.") : Error(message)

// 1. (1)
public inline fun TODO(): Nothing = throw NotImplementedError()

public inline fun TODO(reason: String): Nothing = throw NotImplementedError("An operation is not implemented: $reason")

// 2. (2)
public inline fun <R> run(block: () -> R): R { /* 생략 */ }

public inline fun <T, R> T.run(block: T.() -> R): R { /* 생략 */ }

public inline fun <T, R> with(receiver: T, block: T.() -> R): R { /* 생략 */ }

public inline fun <T> T.apply(block: T.() -> Unit): T { /* 생략 */ }

public inline fun <T> T.also(block: (T) -> Unit): T { /* 생략 */ }

public inline fun <T, R> T.let(block: (T) -> R): R { /* 생략 */ }

// 3. (3)
public inline fun <T> T.takeIf(predicate: (T) -> Boolean): T? { /* 생략 */}

public inline fun <T> T.takeUnless(predicate: (T) -> Boolean): T? { /* 생략 */}

// 4. (4)
public inline fun repeat(times: Int, action: (Int) -> Unit) { /* 생략 */}
```

1. `TODO()` - 개발하다보면 주석으로 앞으로 작성해야 되는 부분을 TODO 로 채워 놓는 경우가 많습니다. `kotlin` 은 이 부분까지 함수로 뽑아서 개발자의 실수를 예방하고 있습니다.
2. 이 글의 주제인 scope function 이 정의되어 있습니다.
3. 객체의 상태를 체크하는 로직을 call chain에 embed 할 수 있도록 해주는 두 메서드 takeIf 와 takeUnless 가 정의 되어 있습니다. 각각 perdicate을 만족/만족x 하는 경우 T 를 반대의 경우는 null 을 리턴합니다.
4. action 을 time 번 반복하는 `repeat` 메서드입니다. action 에서는 반복 index를 zero-based 로 획득 할 수 있습니다.

- 모든 inline 메서드에 포함된 `@kotlin.internal.InlineOnly` 애너테이션 모두 생략하였습니다.
- 전체적으로 한번 훑어 보아도 정의된 함수나 코드 라인이 그리 많지 않아서 모두 이해할 만 합니다! 

#### Contrant

`Standard.kt` 파일에서 눈길이 가는 또 다른 부분은 바로 `contract` 의 활용입니다. `contract` 를 사용하면 코틀린 컴파일러에게 추가적인 정보를 전달하여 타입 추론을 돕고 기타 불필요한 컴파일 에러를 방지할 수 있습니다. `contract` 문법에 관한 내용은 [여기 링크](https://medium.com/harrythegreat/kotlin-contracts-문법-쉽게-배워보기-9ffdc399aa75) 를 참고해주세요. 이 문서의 아래 코드에서는 `contract` 부분을 생략하고 scope function 의 구현과 동작에 대해서 다루겠습니다.

```kotlin title="Standard.kt 에 포함된 contract 의 활용!"
// 2, 3  메서드의 시작 부분에 공통적으로 포함된 라인
public inline fun xxx(yyy) : zzz {
    contract {  
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)  
    }
    // 대충 람다가 한번만 호출되는 계약
    // 각자의 구현
}

public inline fun repeat(times: Int, action: (Int) -> Unit) {  
    contract { callsInPlace(action /*, kind = InvocationKind.UNKNOWN */) }
    // Unknown 인데 이런 계약은 왜 추가 했을까? 
    // repeat 구현 
}
```

### 3. 요약

```kotlin title="kotlin 확장함수 인 scope function 요약"

val value1 : Int = person.let { /* it: Person */ it.age}

val value2 : Int = person.run { /* this: Person */ this.age}

val value3 : Person = person.also { /* it: Person */ it.age}

val value4 : Person = person.apply { /* this: Person */ this.age}

```

### 4. Let

```kotlin
public inline fun <T, R> T.let(block: (T) -> R): R {  
    return block(this)  
}
```

- 전달 받은 block (함수) 에 T 타입의 자기 자신을 전달하여 호출하고 그 block의 반환값인 R 타입의 반환값을 그대로 리턴합니다.
- let 은 *일반 함수* 를 받는다.

### 5. Run

```kotlin
public inline fun <R> run(block: () -> R): R {  
    return block()  
}

public inline fun <T, R> T.run(block: T.() -> R): R {  
    return block()  
}
```

- 그냥 block 을 실행 (run) 하고 반환한다.
- `run` 은 *확장함수*를 받는다. (?)

### 6. Also

```kotlin
public inline fun <T> T.also(block: (T) -> Unit): T {  
    block(this)  
    return this  
}
```

### 7. Apply

```kotlin
public inline fun <T> T.apply(block: T.() -> Unit): T {  
    block()  
    return this  
}
```

### 8. With

```kotlin
public inline fun <T, R> with(receiver: T, block: T.() -> R): R {  
    return receiver.block()  
}
```
