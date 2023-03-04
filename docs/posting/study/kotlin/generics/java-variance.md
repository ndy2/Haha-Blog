---
tags: [kotlin, generics]
title: 변성 with Java
date: 2023-02-18
---
  
> [!quote] 참고 자료
> * [`『코틀린 인 액션』`](http://www.yes24.com/Product/Goods/55148593) by 드미트리 제메로프, 스베트라나 이사코바
>     * 9 장 제네릭스
> * kotlin documentation - [genericss#Variance](https://kotlinlang.org/docs/generics.htmls#variance)

### 1. 변성 <sup>Variance</sup>

* 자바의 가장 어려운 문법 중 하나는 `wildcard types (Foo<*>)` 입니다.
* kotlin 그 대신 다음 두가지를 가집니다.

1. 선언 지점 변성 <sup>declaration-site variance</sup>
2. 타입 프로젝션 <sup>type projections</sup>

이 모든것들은 변성 <sup>Variance</sup> 이라는 개념을 해결하기 위한 도구입니다.

> [!note] 변성 <sup>Variance</sup>
> * 변성 이란 **제네릭 타입의 계층 관계**를 나타내는 개념
> * Variance 에는 다음 세 가지 종류가 있다.
> * `Type A` 가 `Type B` 의 하위 타입 일때, `Foo` 는 타입 파라미터를 한개 가지는 제네릭 클래스 일때 (`Type A` 에 `Integer`, `Type B` 에 `Number`, `Foo` 에 `List` 를 대입해 생각하자)
>     * invariance - `Foo<A>` 와 `Foo<B>` 는 상속 관계가 없다.
>     * covariance - `Foo<A>` 는 `Foo<B>` 의 하위 타입
>     * contravariance - `Foo<A>` 는 `Foo<B>` 의 상위 타입

### 2. Invarinace

코틀린 의 변성에 대해 알아보기 전 자바의 변성에 대한 복습을 간단히 해보겠습니다. 자바와 코틀린 에서 기본적으로 제네릭 타입은 `invariant` 합니다. 즉 `List<Int>` 와 `List<Object>` 에는 상속 관계가 없습니다.

이런 기본적인 방식으로 전달 받은 컬렉션의 모든 요소를 출력 하는 메서드의 시그니처를 아래와 같이 작성 할 수 있습니다.

```java title="invariant!"
public static void printAll(Collection<Object> collection){  
    for (Object o : collection) {  
        System.out.println(o);  
    }  
}
```

```java title="컴파일 에러!"
public static void main(String[] args) {  
    List<Long> longs = List.of(1L, 2L);  
    printAll(longs);  
    // java: incompatible types: java.util.List<java.lang.Long> cannot be converted to java.util.Collection<java.lang.Object>
}
```

`List<Long>` 은 `Collection<Object>` 과 상속 관계가 없으므로 printAll 메서드의 아규먼트로 사용 될 수 없습니다.

### 3. Covariance

이 메서드는 전달 받는 컬렉션의 타입 파라미터에 관계 없이 동작 할 수 있습니다. 따라서 이 메서드에서는 `Object` 의 하위 타입 `T` (모든 자바의 클래스) 에 대해 `Collection<T>` 가 `Collection<Object>` 의 하위 타입이라고 정할 수 있습니다. 이를 공변 <sup>convariance</sup> 이라고 합니다. 자바에서는 `wildcard type argument` 를 이용해 이런 성질을 나타낼 수 있습니다.

```java title="wildcard type argument 를 이용해 공변성을 추가한 메서드"
public static void printAll(Collection<? extends Object> collection){  
    for (Object o : collection) {  
        System.out.println(o);  
    }  
}
// note! - wildcard type arguemtn 의 extends Object 는 생략 될 수 있다.
```

*extends*-bound (upper bound) 는 타입을 *convariant* 하게 만듭니다.

### 4. Contravaraiance

이번에는 컬렉션에 대해서 전달 받은 Consumer 를 모두 실행해주는 forEach 메서드를 생각해 보겠습니다. 이번엔 조금 더 현실성 있게 제네릭 타입 파라미터도 고려해 보겠습니다.

```java title="invariant consumer"
public static <E> void forEach(Collection<E> collection, Consumer<E> action){
    collection.forEach(action); // 사실 이미 구현 된 것에 넘겨주기만 함
}
```

이 forEach 메서드를 사용하는 코드를 작성해 봅시다!

```java
public static void main(String[] args) throws IOException {  
    List<Integer> integers = List.of(1, 2);  
  
    AtomicReference<Integer> sum = new AtomicReference<>(0);  

    // 같은 Integer 타입의 컨슈머 문제 없음
    Consumer<Integer> adder = a -> sum.updateAndGet(v -> v + a);  
    forEach(integers, adder);  

    // 상위 타입인 Object 를 이용한 컨슈머
    Consumer<Object> printer = System.out::println;  
    forEach(integers, printer); // 컴파일 에러
}
/*
java: method forEach in class Main cannot be applied to given types;
  required: java.util.Collection<E>,java.util.function.Consumer<E>
  found:    java.util.List<java.lang.Integer>,java.util.function.Consumer<java.lang.Object>
  reason: inference variable E has incompatible equality constraints java.lang.Object,java.lang.Integer
*/
```

컬렉션의 목록을 사용해 실행만 해주는데 `Consumer<E>` 타입이지만 `Consumer<Object>` 타입 의 컨슈머를 실행 해주어도 논리상 문제 되지 않습니다. 오히려 더 자연 스럽다고 할 수 있습니다. 이런 성질을 반공변성 <sup>contravarian</sup> 라고 합니다.

```java title="contravariant forEach! - Consumer<Object> 도 사용 가능"
public static <E> void forEach(Collection<E> collection, Consumer<? super E> action){  
    collection.forEach(action);  
}
```

### 5. PECS

이 성질을 간단히 요약 하면 *PECS* 라고 나타낼 수 있습니다. 이는 *Producer-Extends, Consumer-Super.* 를 의미합니다.
