---
tags: [kotlin]
title: 고차 함수 (Higher-Order-Function)와 함수 타입 (Function Type)
date: 2023-02-16
---
 
> [!quote] 참고 자료
> * [`『코틀린 인 액션』`](http://www.yes24.com/Product/Goods/55148593) by 드미트리 제메로프, 스베트라나 이사코바 
>      * 8 장 고차 함수: 파라미터와 반환 값으로 람다 사용
> * kotlin documentation - [High-order functions and lambdas](https://kotlinlang.org/docs/lambdas.html)

### 1. 고차 함수

!!! note "고차 함수 <sup>high order function</sup>"

     * 람다를 인자로 받고나 반환하는 함수
     * 고차 함수를 활용하면 코드 중복을 없애고 더 나은 추상화를 구축할 수 있다.

!!! example 

    * `list.filter { x > 0 }` 의 `filter` - [코드 링크](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/filter.html) 

위 filter 함수의 시그니쳐를 코드는 아래와 같다.

```kotlin
public inline fun <T> Iterable<T>.filter(predicate: (T) -> Boolean): List<T> {
    return filterTo(ArrayList<T>(), predicate)
}
```

여기 정리하고자 하는 개념이 모두 포함되어 있다.

1. 함수 타입 <sup>function type</sup>
2. 인라인 <sup>inline</sup> 함수

가 바로 그것들이다. 이 장에서는 함수 타입에 대해서 알아보고 인라인 함수는 별도의 문서를 통해 정리해보자!

---

### 2. 함수 타입

#### A. 코틀린 함수 타입 문법

* `(A, B) -> C`
* `val myFun : (A, B) -> C = ...` 와 같이 활용할 수 있다.
* 이때 `myFun` 함수는 `A`, `B` 타입 두개의 아규먼트를 받아 `C` 타입의 값을 반환한다.

#### B. :warning: Unit 과 함수 타입

* 파라미터의 타입 목록은 빌 수 있다. (e.g. `val aSupplier :  ( ) -> A = ...`)
* 하지만 `Unit` 리턴 타입은 생략 될 수 없다. (e.g. `val aConsummer : A -> = ...`)

#### C. 파라미터 이름과 함수 타입

```kotlin
fun performReq(
    url: String,
    callback: (code: Int, content:String) -> Unit
) {
    // ...
}
```

* 파라미터 이름을 지정해 가독성을 높일 수 있다.
* 컴파일러는 타입 검사시에 파라미터 이름은 무시한다.

#### D. *Receiver Type* 과 함수 타입

```kotlin
fun main() {  
    val my : Int.(Boolean) -> String = {  /* this:Int, it:Boolean */
        val isEvenEqualIt = (this % 2 == 0) == it  
        "i am $this, isEvenEqualIt is $isEvenEqualIt"  
    }  
  
    println(1.my(true))  
    println(1.my(false))  
    println(2.my(true))  
    println(2.my(false))  
}
```

```text title="실행 결과"
i am 1, isEvenEqualIt is false
i am 1, isEvenEqualIt is true
i am 2, isEvenEqualIt is true
i am 2, isEvenEqualIt is false
```

#### E. 이 외 다양한 형태의 함수 타입활용

* 함수 타입 자체가 nullable 한 경우 : `((Int, Int) -> Int)?`
* 인자 혹은 리턴 타입이 nullable 한 경우 : `(Int?, Int) -> Int?`
* 중첩된 함수 타입 구조 : `(Int -> ((Int -> Unit)))`
* typealias 와 함수 타입 : `typealias ClickHandler = (Button, ClickEvent) -> Unit`
* 고차 함수의 파라미터에서 활용시 default 값을 지정할 수 도 있다.
* 물론 다루지는 않았지만 고차 함수의 반환값에도 함수 타입을 사용할 수 있다.

### 3. 함수 타입을 생성하는 방법

!!! quote ""

    ref - [kotlin documentation/#intantiating a function type]( https://kotlinlang.org/docs/lambdas.html#instantiating-a-function-type)

함수 타입 인스턴스를 얻는 방식에는 몇가지가 있습니다.

#### A. 람다 식

```kotlin
val intAdd : (Int, Int) -> Int = { a: Int, b: Int -> a + b }
```

#### B. 익명 (?) 함수

```kotlin
val intAdd2 : (Int, Int) -> Int = fun(a: Int, b: Int) = a + b
```

#### C. Callable Reference 활용

```kotlin
fun main() {  
    val intAdd3: (Int, Int) -> Int = ::intAdd3  
    // 이렇게 직접 타입을 넣어줘도 문제 없다.
    // 타입을 넣어주지 않으면 IDE 가 타입을 보여주는 화면에는 
    // KFunction2<Int,Int,Int> 타입으로 표시된다.
    // val intAdd3: KFunction2<Int, Int, Int> = ::intAdd3
    // 이게 뭘 의미하는 지는 아래에서 알아보자.

    val intAdd4 = Integer::sum // 얘도 마찬가지
}

fun intAdd3(a: Int, b: Int) = a + b
```

#### D. 함수 타입을 구현하는 클래스를 정의하고 생성하기

```kotlin
fun main() {  
    val intAdd5 = IntAdder()  
}

// 앗 함수타입이 뭐길래 인터페이스 마냥 구현을 할 수 있을까?
// 아래에서 알아보자.
class IntAdder : (Int, Int) -> Int {  
    override fun invoke(p1: Int, p2: Int) = p1 + p2  
}
```

### 4. 함수 타입을 사용 (호출) 하는 방법

```kotlin title="위의 모든 함수 타입 인스턴스 생성 방법과 함수 타입 사용 모음"
fun main() {  
    val intAdd = { a: Int, b: Int -> a + b }  
    val intAdd2 = fun(a: Int, b: Int) = a + b  
    val intAdd3 = ::intAdd3  
    val intAdd4 = Integer::sum  
    val intAdd5 = IntAdder()  
  
    intAdd.invoke(1,2)  // 호출 방법 1. invoke
    intAdd5(1,2)        // 호출 방법 2. 함수 처럼 사용하기
}  
  
fun intAdd3(a: Int, b: Int) = a + b  
  
class IntAdder : (Int, Int) -> Int {  
    override fun invoke(p1: Int, p2: Int) = p1 + p2  
}
```

### 5. 함수 타입이 동작하는 원리

!!! quote "`『kotlin in action』` p.352"

    컴파일된 코드 안에서 함수 타입은 일반 인터페이스로 바뀐다. 즉 함수 타입의 변수는 FunctionN 인터페이스를 구현하는 객체를 저장한다. 코틀린 표준 라이브러리는 함수 인자의 개수에 따라 Function0<R>, Function1<P1,R> 등의 인터페이스를 제공한다. 각 인터페이스에는 invoke 메서드 정의가 하나 들어 있다.

![[images/functions.png]]

#### Byte Code Decompiled

```java
// IntAdder.java  
import kotlin.Metadata;  
import kotlin.jvm.functions.Function2;  
import org.jetbrains.annotations.NotNull;  
  
public final class IntAdder implements Function2 {  
   @NotNull  
   public Integer invoke(int p1, int p2) {  
      return p1 + p2;  
   }  
  
   public Object invoke(Object var1, Object var2) {  
      return this.invoke(((Number)var1).intValue(), ((Number)var2).intValue());  
   }  
}  

// MainKt.java  
import kotlin.Metadata;  
import kotlin.jvm.functions.Function2;

public final class MainKt {  
   public static final void main() {  
      Function2 intAdd = (Function2)null.INSTANCE;  
      Function2 intAdd2 = (Function2)null.INSTANCE;  
      Function2 intAdd3 = (Function2)null.INSTANCE;  
      Function2 intAdd4 = (Function2)null.INSTANCE;  
      IntAdder intAdd5 = new IntAdder();  
      intAdd.invoke(1, 2);  
      intAdd3.invoke(1, 2);  
      intAdd5.invoke(1, 2);  
   }  
  
   // $FF: synthetic method  
   public static void main(String[] var0) {  
      main();  
   }  
  
   public static final int intAdd3(int a, int b) {  
      return a + b;  
   }  
}
```

Function2 타입의 익명 클래스 인스턴스 생성은 컴파일 타임에 발생하는지 직접 IntAdder 라고 이름을 붙인 클래스를 정의하고 생성하는 방식이 아니라면 직접 확인할 수는 없었다. 

디 컴파일 결과 람다식을 활용하면 코틀린은 보통 익명 클래스로 컴파일 하지만 람다가 변수를 포획할때 마다 람다가 생성되는 시점에 새로운 익명 클래스 객체가 생긴다는 사실을 알 수 있었다. 다음에는 이를 해결하기 위한 kotlin 의 `inline` 변경자를 알아보자!
