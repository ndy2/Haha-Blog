@참고 자료)

- 인프런/최태현 - 자바 개발자를 위한 코틀린 입문
- 드미트리 제메로프, 스베트라나 이사코바 - 코틀린 인 액션(에이콘 출판사)

---

### 0. 들어가며

!!! quote "코틀린 인 액션 (p.181)"

    코틀린에서는 object 키워드를 다양한 상황해서 사용하지만. 모든 경우 클래스를 정의하면서 동시에 인스턴스(객체)를 생성한다는 공통점이 있습니다.

코틀린은 세가지 상황에서 `object` 키워드를 사용합니다.

- **객체 선언**^object declaration^ - 싱글턴을 정의 하는 방법 중 하나입니다.
- **동반 객체**^companion object^ - 자바의 static 메서드, 변수와 같은 역할을 합니다.
- **객체 식**^object expression^ - 자바의 익명 클래스와 같은 역할을 합니다.

### 1. 객체 선언 - `object declaration`

싱글턴 패턴^singleton pattern^은 클래스의 인스턴스가 오직 하나만 생성되도록 하는 디자인 패턴입니다. 자바에서는 보통 private 생성자를 통해 단하나의 인스턴스를 private static 필드로 생성 해 두고 이에대한 접근을 public static getInstance 와 같은 메서드를 통해 제어하는 방식으로 싱글턴 패턴을 구현합니다. 

코틀린은 언어에서 기본적으로 싱글턴 패턴을 지원합니다. 객체 선언^object declaration^은 클래스 선언과 그 클래스에 속한 단일 인스턴스의 선언을 합친 선언입니다.

=== "자바"

    ```java
    public class JavaSingleTon {  
      
        private static final JavaSingleTon INSTANCE = new JavaSingleTon();  
        private JavaSingleTon(){} // private 생성자  
        public static JavaSingleTon getInstance() {  
            return INSTANCE;  
        }  
    }
    ```

=== "코틀린"

    ```kotlin
    object SingleTon {} // 끝!








    ```

코틀린 바이트코드를 디컴파일 하여 자바 코드를 확인 하면 **객체 선언**이 **클래스 선언**과 **단일 인스턴스의 선언**이 합친 선언 이라는 말의 의미가 더 와닿습니다.

```java title="객체 object 디컴파일 결과"
public final class SingleTon {  // 1. 클래스 선언
   @NotNull  
   public static final SingleTon INSTANCE;  // 2. 단일 인스턴스 선언
  
   private SingleTon() {  
   }  
  
   static {  
      SingleTon var0 = new SingleTon();  
      INSTANCE = var0;  
   }  
}
```

또한 `INSTANCE` 라는 변수명으로 단일 인스턴스의 변수명이 지정된 것을 확인 할 수 있습니다. 따라서 자바에서 `object` 로 선언된 코틀린의 싱글턴 객체에 접근하고자 한다면 `SingleTon.INSTANCE` 와 같이 사용할 수 있습니다.



### 2. 동반 객체 - `companion object`

자바에서 `static` 키워드는 클래스가 인스턴스화 될 때 새로운 값이 복제 되는것이 아니라 정적으로 인스턴스 끼리 값을 공유 한다는 의미입니다.

코틀린에서 `compnion object` 는 클래스와 동행하는 유일한 오브젝트 라는 의미입니다.

=== "자바"

    ``` java
    public class JavaPerson {

     private static final int MIN_AGE = 1;

    public static JavaPerson newBaby(String name){
        return new JavaPerson(name); 
    }

     private String name;
     private int age;

     private JavaPerson(String name, int age)
        this.name = name;
        this.age = age;
     }

    }
    ```

=== "코틀린"

    ``` kotlin
    class Person private constructor(
       val name: String.
       var age: Int, 
    ) {
        companion object {
           const val MIN_AGE = 1 // const -> 컴파일 시에 변수가 할당 된다.
           fun newBaby(name: String) = Person(name, MIN_AGE) 
        }
    }








    ```






