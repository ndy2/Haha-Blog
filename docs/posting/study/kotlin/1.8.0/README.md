---
tags: [kotlin]
title: Kotlin 1.8.0
author: ndy2
date: 2023-02-25
description: >-
  코틀린 1.8.0에 추가된 내용들을 알아보자.
---
 
 
> [!quote] 참고 자료
> * kotlin documentation - [What's new in Kotlin 1.8.0](https://kotlinlang.org/docs/whatsnew18.html)
> * [What's New in Kotlin 1.8.0 - Standard Libray Udates](https://youtu.be/cLyTx5wSPbg) by `『Kotlin by JetBrains』`

### 1. Stable 된 내용들

1. `kotlin.math.cbrt`
   
```kotlin
import kotlin.math.cbrt  
import kotlin.math.pow  
  
fun main() {  
    val num = 27.0  
    val negNum = -num  
  
    println("${num}의 세제곱근은 ${cbrt(num)} 입니다.")  
    println("${negNum}의 세제곱근은 ${cbrt(negNum)} 입니다.")  
  
    println("${num}의 세제곱근은 ${num.pow(1/3)} 입니다.")  
    println("${negNum}의 세제곱근은 ${negNum.pow(1/3)} 입니다.")  
}
```

```text title="실행 결과"
27.0의 세제곱근은 3.0 입니다.
-27.0의 세제곱근은 -3.0 입니다.
27.0의 세제곱근은 1.0 입니다.
-27.0의 세제곱근은 1.0 입니다.
```

>[!warning]
>`pow` 함수는 special case 에 대해서 정확한 값을 기대하기 어렵다.


2. `java <-> kotlin` 간의 시간 단위 전환

java 는 `java.util.concurrent.TimeUnit`을 kotlin 은 `kotlin.time.Duration` 을 주로 활용한다. 이제 확장 함수를 이용해 이들의 전환을 쉽게 할 수 있다.

```kotlin
public fun DurationUnit.toTimeUnit(): TimeUnit
public fun TimeUnit.toDurationUnit(): DurationUnit
```


3. `Optional` 관련 확장함수들

```kotlin
import java.util.Optional
import kotlin.jvm.optionals.getOrDefault
import kotlin.jvm.optionals.getOrElse
import kotlin.jvm.optionals.getOrNull

val o = Optional.of("O")
println(o.getOrNull()) // "O"

val e = Optional.empty<String>()
println(e.getOrNull()) // null
println(e.getOrDefault("default")) // "default"

println(e.getOrElse {
    println("print me if empty")
    "default"
})
// "print me if empty"
// "default"

```


### 2. Experimental APIs

1. TimeMark 확장

>[!info]
> - `TimeMark.elapsedNow` - mark 로 부터 소요된 시간을 반환

```kotlin
@OptIn(ExperimentalTime::class)
fun main() {
    
    val timeSource = TimeSource.Monotonic
    val mark1 = timeSource.markNow()
    Thread.sleep(500) // sleep 0.5 seconds.
    val mark2 = timeSource.markNow()

    // Before 1.8
    repeat(4) {
        val elapsed1 = mark1.elapsedNow()
        val elapsed2 = mark2.elapsedNow()

        println("Mesurement ${it + 1} : elapsed1 = $elapsed1, elapsed2 = $elapsed2, diff = ${elapsed1 - elapsed2}")
    }

    // Since 1.8
    repeat(4) {
        val mark3 = timeSource.markNow()
        val elapsed1 = mark3 - mark1
        val elapsed2 = mark3 - mark2

        println("Mesurement ${it + 1} : elapsed1 = $elapsed1, elapsed2 = $elapsed2, diff = ${elapsed1 - elapsed2}")
    }

    print(mark2 > mark1) // prints true - comparable 하다!
}
```

아래와 같이 바꿀 작성할 수 있게 되면서 아래의 경우 `diff` 값이 `mark2 - mark1` 값으로 항상 일정하다는 것이 보장되었다. 위 코드에서는 각각 elapsed1, elapsed2 를 생성하는 코드 호출 시간이 있으므로 약간의 차이가 발생하고 코드 작성 의도를 생각했을때 오류라고 볼 수도 있다.


2. 파일 재귀적 복사/ 재귀적 삭제 API

```text title="before"
├─from
│  │ index.md
│  └─inside
│        haha.txt
└─to
```

```kotlin
import java.nio.file.Paths  
import kotlin.io.path.copyToRecursively  
  
@OptIn(kotlin.io.path.ExperimentalPathApi::class)  
fun main() {  
    val from = Paths.get("./src/main/resources/from/")  
    val to = Paths.get("./src/main/resources/to")  
  
    from.copyToRecursively(  
        target = to,  
        followLinks = false  
    )  
}
```

```text title="After"
├─from
│  │ index.md
│  └─inside
│        haha.txt
└─to
    │ index.md
    └─inside
          haha.txt
```

`followLinks` 파라미터는 symbolic link 까지 복사하는지 결정하는 flag 이다. symbolic link 는 바로가기 같은 참조를 저장하는 파일을 의미한다.

또한 람다식을 통해 예외가 발생했을시 처리하는 방법을 제공한다던가 덮어쓰기를 허용하는 flag 라던가 다양한 옵션들을 제공한다.

resources 의 모든 파일을 `deleteRecusively` api 를 이용해 제거해보자.

```kotlin
import java.nio.file.Paths  
import kotlin.io.path.deleteRecursively  
  
@OptIn(kotlin.io.path.ExperimentalPathApi::class)  
fun main() {  
    val resources = Paths.get("./src/main/resources/")  
    resources.deleteRecursively()  
}
```

resources 폴더까지 모두 사라졌다. 지정한 root 폴더는 남겨놓는 옵션이 있으면 좋을거 같은데 이 api는 별도의 파라미터를 받지않는 형태로 정의되어있다.
