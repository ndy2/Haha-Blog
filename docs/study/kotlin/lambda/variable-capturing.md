@ 참고 자료)

- Kotlin In Action - 5장 람다로 프로그래밍 하기

---
### 1. 코틀린의 람다 변수(var) 캡쳐링

자바에서는 `final` 변수만 람다에 전달 할 수 있습니다. 람다에 전달되는 모든 변수는 `final` 혹은 `effectively final` 입니다. 하지만 코틀린 에서는 `var` 변수를 람다식에 전달하고 값을 변경 까지 할 수 있습니다.

```kotlin
fun main() {  
  
    var result = 0  
    val lambdaAdder = { input:Int -> result+=input }  
  
    lambdaAdder(10)  
    println(result)  
}
```

```text title="실행 결과"
10
```

자바와 다르게 아무 오류없이 기대한 값을 받아볼 수 있습니다. 바이트 코드를 디컴파일 해서 코틀린 컴파일러가 이를 어떻게 처리 하는지 확인해보겠습니다.

```java title ="코틀린 바이트코드 디컴파일 결과 (약간 정리)"
import kotlin.Unit;  
import kotlin.jvm.functions.Function1;  
import kotlin.jvm.internal.Ref;

public final class LambdaTesKt {  

 public static void main(String[] var0) {  
      final Ref.IntRef result = new Ref.IntRef();  // (1) 
      result.element = 0;  
      Function1 lambdaAdder = (Function1)(new Function1() {  

        public Object invoke(Object var1) {  
            this.invoke(((Number)var1).intValue());  
            return Unit.INSTANCE;  
         }  
  
         public final void invoke(int input) {  
            Ref.IntRef var10000 = result;  
            var10000.element += input;  
         }  
      });  
      lambdaAdder.invoke(10);  // (2)
      System.out.println(result.element);   
   }  
}

```

1. 변경 가능한 변수 포획 - result 를 Ref 클래스로 감싸서 람다에 넘긴다.
2. 인자를 하나 받는 람다가 Function1 클래스로 컴파일 되었다. 코틀린 1.0에서 인라인 되지 않은 모든 람다 식은 익명 클래스로 컴파일 됩니다. 람다가 변수를 캡쳐링 하면 그 변수를 저장하는 필드가 생깁니다.

본적없는 두개의 임포트가 추가 되었습니다. 

Function1 은 하나의 인자를 받는 인터페이스 입니다.

```kotlin
/** A function that takes 1 argument. */  
public interface Function1<in P1, out R> : Function<R> {  
    /** Invokes the function with the specified argument. */  
    public operator fun invoke(p1: P1): R  
}
```


Ref 는 람다식 내부에서 변경되는 외부 참조를 감싸는 래퍼클래스입니다.

신기하게 여기는 자바로 코딩되어 있는데 자세한 이유는 모르겠습니다.

```kotlin
public class Ref{

    // ObjectRef, ByteRef, ShortRef, LongRef, ... 모든 타입의 Ref 존재

    public static final class IntRef implements Serializable {  
        public int element;  // (1)
      
        @Override  
        public String toString() {  
            return String.valueOf(element);  
        }  
    }
}
```

1. 래핑한 값을 저장하는 필드, 퍼블릭 이다.

---
### 2 :warning: 람다와 비동기 실행

```kotlin
fun main() {  
  
    var result = 0  
    AdderThread  { input:Int -> result+=input }.start()  
  
    println("[${Thread.currentThread().name}] $result")  
  
    Thread.sleep(1000)  
    println("[${Thread.currentThread().name}] $result")  
}  
  
class AdderThread(private val lambdaAdder: (Int) -> Unit) : Thread(){  
  
    override fun run() {  
        println("[${name}] run!")  
        lambdaAdder.invoke(1)  
    }  
}
```

```text title="실행 결과"
[main] 0
[Thread-0] run!
[main] 1
```

main 쓰레드는 `Thread-0` 가 실행한 1 을 추가하는 결과가 적용되기 전 (사실은 실행도 하기 전) 에 첫번째 출력을 하러 갑니다. 따라서 위와 같은 순서로 출력됩니다.

---
### :warning: 람다 캡쳐링과 쓰레드 안전

```kotlin
import java.util.concurrent.CountDownLatch  
import java.util.concurrent.Executors  
  
class Counter{  
    var count = 0  
}  
  
fun main() {  
  
    var result = 0  
    val counter = Counter()  
  
    val numberOfThreads = 10000  
    val service = Executors.newFixedThreadPool(10000)  
    val latch = CountDownLatch(10000)  
    for (i in 0 until numberOfThreads) {  
        service.execute {  
            Thread.sleep(100)  
            result++  
            counter.count++  
            latch.countDown()  
        }  
    }  
    latch.await()  
  
    println(result)  
    println(counter.count)  
}
```

```text title="실행 결과"
9985
9989
```

코틀린애서 멀티쓰레드를 테스트 하는 적절한 방법을 몰라서 일단 익숙한 방식으로 테스트 해보았습니다.

코틀린이 지원하는 변수 캡쳐링을 통해 boilerplate 한 참조를 래핑하는 클래스를 제거할 수는 있지만 이는 쓰레드 안전^Thread^ ^Safe^ 과는 별개입니다.

자바가 람다식에 final, effectively final 변수만을 이용가능 하도록 한 이유 역시 쓰레드 안전을 준수하기 위해서인데 단순히 변수를 래핑하는 방식만으로는 Race Condition 의 발생을 막을 수 없습니다.
