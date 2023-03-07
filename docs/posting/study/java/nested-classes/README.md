---
tags: [java, nested-classes]
title: 자바의 여러 중첩 클래스에 대해 알아보자
author: ndy2
date: 2023-03-07
description: >-
  
---
 
> [!quote] 참고 자료
> * [Nested Classes](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html) on Oracle Documentation
> * [자바의 내부 클래스는 스프링 빈이 될 수 있을까?](https://youtu.be/2G41JMLh05U) by Toby Lee on Youtube
> 	  * 중첩 클래스와 스프링에 관한 재미있는 실험 영상입니다.

### 1. Terminologies

> [!quote] [Nested Classes](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html) on Oracle Documentation
>  * Java 프로그래밍 언어는 클래스 안에 클래스를 정의 할 수 있습니다.
>  * 그런 클래스는 중첩 클래스 (Nested Class) 라고 부릅니다.

> [!note] *`static nested classes`* & *`inner (nested) classes`*
> * 중첩 클래스는 non-static 중첩 클래스와 static 중첩 클래스 두가지로 구분됩니다.
> * non-static nested class 는 내부 중첩 클래스 (Inner static class) 라고 부릅니다.
> * 보통 '중첩 (Nested)' 을 생략하고 `Static Class`, `Inner Class` 라고 많이 부릅니다.
> * ```java
>   class OuterClass{
>		...
>		class InnerNestedClass { // (1)!
>			...
>		}
>		
>		static class  StaticNestedClass { // (2)!
>			...
>		}
>	}
>   ```
>   1. 내부 클래스
>   2. static 클래스

### 2. Why Use Nested Classes?

중첩 클래스를 사용하는 이유는 다음과 같습니다.

- 클래스를 논리적으로 그루핑 할 수 있다.
- (`private`, `default` 접근 제어자와 함께 활용해) 캡슐화를 높인다.
- 가독성/유지보수성을 높인다.

### 3. Inner Classes - 내부 클래스

```java
class OuterClass {
    ...
    class InnerClass {
        ...
    }
}
```

OuterClass 의 바깥에서 InnerClass 의 인스턴스를 생성하기 위해서는 OuterClass 인스턴스와 함께 특별한 문법이 필요합니다.

```java
OuterClass outerObject = new OuterClass(); // 1. OuterClass 인스턴스 생성
OuterClass.InnerClass innerObject = outerObject.new InnerClass(); // (해당 인스턴스).생성자 호출 문법!
```
또한 내부 클래스에서는 외부 클래스의 필드를 참조할 수도, 메서드를 호출할 수도 있습니다.


Inner Class 에는 지역 클래스(Local Classes)와 익명 클래스(Anonymous Classes) 라는 특별한 종류가 있습니다.

#### 3.1. Local Classes - 지역 클래스

내부 클래스를 메서드의 바디에 정의한 것을 지역 클래스라고 합니다.

#### 3.2 Anonymous Classes - 익명 클래스

클래스에 이름을 두지 않고 인스턴스화 한 클래스를 익명 클래스 라고 합니다. 익명 클래스의 단점은 실제 관심있는 코드 구현부에 비해 원 인터페이스를 생성하고 메서드를 오버라이딩 하는 문법자체가 너무 verbose 하다는 것입니다. 자바 8부터 도입된 람다표현식을 통해 추상 메서드가 단하나인 인터페이스 (SAM Interface) 에 대해 이 문제를 해결할 수 있습니다.

### 4. Static Nested Classes

static class 는 사실 위치만 내부에 지정되있지 별도의 top-level class 로 취급되어도 문제없는 녀석들입니다. 당연히 외부 클래스의 필드를 참조할 수도, 메서드를 호출할 수도 없습니다.

```java
class OuterClass {
    ...
    static class StaticClass {
        ...
    }
}
```