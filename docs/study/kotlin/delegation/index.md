---
tags: [kotlin]
title: 위임 (Delegation)
date: 2023-02-19
---

!!! quote "참고 자료"

    * 참고 자료
    * kotlin documentation - [Delegation](https://kotlinlang.org/docs/delegation.html)
    * kotlin examples - [Delegation/DelegationPattern](https://play.kotlinlang.org/byExample/07_Delegation/01_delegationPattern)

---

### 1. 바로 예시를 보자

```kotlin title="위임 예제"
interface Base {
    fun print()
}

class BaseImpl(val x: Int) : Base {
    override fun print() { print(x) }
}

class Derived(b: Base) : Base by b // (1)

fun main() {
    val b = BaseImpl(10)
    Derived(b).print()
}
```

1. by 절을 이용해 b 를 내부에 저장하고 Base 인터페이스의 메서드가 b 에의해 위힘 처리 되도록한다.


```java title="바이트 코드 디컴파일"
public interface Base {  
   void print();  
}

public final class BaseImpl implements Base {  
   private final int x;  
  
   public void print() {  
      int var1 = this.x;  
      System.out.print(var1);  
   }  
  
   public final int getX() {  
      return this.x;  
   }  
  
   public BaseImpl(int x) {  
      this.x = x;  
   }  
}

public final class Derived implements Base {  
   // $FF: synthetic field  
   private final Base $$delegate_0;  // (1)
  
   public Derived(@NotNull Base b) {  
      Intrinsics.checkNotNullParameter(b, "b");  
      super();  
      this.$$delegate_0 = b;  // (1)
   }  
  
   public void print() {  
      this.$$delegate_0.print();  // (2)
   }  
}

public final class MainKt {  
   public static final void main() {  
      BaseImpl b = new BaseImpl(10);  
      (new Derived((Base)b)).print();  
   }  
  
   // $FF: synthetic method  
   public static void main(String[] var0) {  
      main();  
   }  
}
```

1. 생성자에서 b 를 받아 내부에 저장한다.
2. 위임 방식으로 오버라이딩을 처리한다.

---

### 2. 위임 클래스의 일부 메서드만 오버라이딩 할 수도 있다.

```kotlin
interface Base {
    fun printMessage()
    fun printMessageLine()
}

class BaseImpl(val x: Int) : Base {
    override fun printMessage() { print(x) }
    override fun printMessageLine() { println(x) }
}

class Derived(b: Base) : Base by b {
    override fun printMessage() { print("abc") } // (1) 
}

fun main() {
    val b = BaseImpl(10)
    Derived(b).printMessage()
    Derived(b).printMessageLine()
}
```

1. printMessage 는 직접 처리한다.

```java
public final class Derived implements Base {  
   // $FF: synthetic field  
   private final Base $$delegate_0;  
  
   public void printMessage() {  
      String var1 = "abc";  
      System.out.print(var1);  // (1)
   }  
  
   public Derived(@NotNull Base b) {  
      Intrinsics.checkNotNullParameter(b, "b");  
      super();  
      this.$$delegate_0 = b;  
   }  
  
   public void printMessageLine() {  
      this.$$delegate_0.printMessageLine();  // (2)
   }  
}
```

1. printMessage 메서드는 직접 처리한다.
2. printMessageLine 메서드는 delegation 으로 처리한다.