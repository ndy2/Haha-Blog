---
tags: [kotlin, tips]
title: 꿀팁 모음
date: 2023-02-20
---
 
>[!quote] 참고 자료
>* Kotlin by Jetbrains on Youtube - playlist [`『Kotlin Tips 2023』`](https://www.youtube.com/watch?v=i-kyPp1qFBA&list=PLlFc5cFwUnmyDrc-mwwAL9cYFkSHoHHz7)


### 1. How to Improve Loops in Kotlin | Kotlin Tips 2023

```kotlin
val fruits = listOf("Apple", "Banana", "Cherry", "Durian")
```

=== "Step 0"

```kotlin title="basic loops with .. range"
fun main() {
    for (index in 0 .. fruits.size - 1){
        val fruit = fruits[index]
        println("$index: $fruit")
    }
}
```

=== "Step 1"

```kotlin title="basic loops with until range"
fun main() {
    for (index in 0 until fruits.size){
        val fruit = fruits[index]
        println("$index: $fruit")
    }
}
```

=== "Step 2"

```kotlin title="loops with Collection.lastIndex"
fun main() {
    for (index in 0 .. fruits.lastIndex){
        val fruit = fruits[index]
        println("$index: $fruit")
    }
}
```

=== "Step 3"

```kotlin title="loops with Collection.indices"
fun main() {
    for (index in fruits.indices){
        val fruit = fruits[index]
        println("$index: $fruit")
    }
}
```

=== "Step 4"

```kotlin title="loops with Collection.withIndex()"
fun main() {
    for ((index, fruit) in fruits.withIndex()){
        println("$index: $fruit")
    }
}
```

=== eoc

### 2. How YOU CAN DO MORE with the Elvis operator | Tips from the Kotlin team

=== "Elvis 연산자 기본"

```kotlin title="Elvis 연산자 기본 활용"
fun main() {
    val name :String? = getName()
    val gretting : String = name ?: "undefined"
}
```

=== "Elvis 연산자 with `run { }`"

```kotlin title="Elvis 연산자 는 Expression 만 받으면 된다."
fun main() {
    val name :String? = getName()
    val gretting : String = name ?: run { // (1)
        println("oops no name defined")
        "undefined"
    }
}
```

1. run 을 통해 람다 블럭을 expression 으로 제공할 수 있다.

=== eoc

### 3. These 3 Tips will Change Your Approach to Strings in Kotlin

```kotlin
fun main(){
    //tip1
    println("momo_dancing.jpg".removeSuffix(".jpg")) // momo_dancing
    println("__MEOW__".removeSurrounding("__")) // MEOW

    //tip2
    println("".isEmpty()) // true
    println(" ".isBlank()) // true
    
    //tip3
    println("momo".equals("MomO", ignoreCase = true)) // true
}
```

### 4. Calculate Your Code Performance | Kotlin Tips 2023

```kotlin
import kotlin.time.ExperimentalTime
import kotlin.time.measureTimedValue

@OptIn(ExperimentalTime::class)
fun main() {
    val (value, time) = measureTimedValue { longOperation() }
    println("It took $time to calculate $value")
}
```

### 5. Deduplicating Collection Items | Kotlin Tips 2023

```kotlin title="컬렉션 중복 제거"
val fruitBasket = listOf("Apple", "APPLE", "ApPle", "Banana", "Melon", "Apple")

fun main() {
    println(fruitBasket.distinct()) // (1)
    println(fruitBasket.toSet()) // (2)
    println(fruitBasket.distinctBy { it.toLowerCase() } ) // (3)
}
```

1. `[Apple, APPLE, ApPle, Banana, Melon]` - `List<String>`
2. `[Apple, APPLE, ApPle, Banana, Melon]` - `Set<String>`
3. `[Apple, Banana, Melon]` - `List<String>` - `List<String>`