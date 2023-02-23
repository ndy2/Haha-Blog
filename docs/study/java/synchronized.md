---
tags: [java]
title: synchronized
author: ndy2
---

> [!quote] 참고 자료
> * haha
>* Jakob Jenkov - https://www.youtube.com/watch?v=eKWjfZ-TUdo
>*  oracle java tutorial - https://docs.oracle.com/javase/tutorial/essential/concurrency/sync.html
>*  쉬운코드 - https://youtu.be/Dms1oBmRAlo?t=1275

자바에는 동시성 처리를 위해 다양한 방식을 제공합니다.

구체적인 이용 방식이나 효과는 모두 다르지만 보통

1. synchronized 키워드
2.  volatile 키워드
3. `java.util.concurrent` 패키지의 Atomic 자료형 클래스들
4. `java.lang.ThreadLocal` 클래스 

가 대표적인 동시성 처리를 위해 자바가 지원하는 키워드와 클래스 들입니다.

이 자료에서는 가장 대표적이고 널리 활용되는 `synchronized` 키워드에 대해서 알아보겠습니다.

---

### 1. synchronized 키워드
`synchronized` 로 선언된 메서드, 블락은 한 시점에 하나의 쓰레드에 의해서만 실행 될 수 있습니다.

```java title="SynchronizedExchanger - 한 시점에 하나의 쓰레드만 접근할 수 있는 객체홀더"
public class SynchronizedExchanger {

    protected Object object = null;

    public synchronized Object getObject() {  // (1)
        return object;
    }

    public synchronized void setObject(Object object) { // (2)
        this.object = object;
    }

    public Object getObj(){ // (3)
        synchronized (this){
            return object;
        }
    }

    public void setObj(Object o) { // (4)
        synchronized (this) {
            this.object = o;
        }
    }
}
```

(1), (2) - `synchronzied method

(3), (4) - `synchronized staement`

synchronized 키워드에는 항상 monitor 가 전달되어야 합니다. 위 예시에서 `synchronized` 블락에는 `this` 로 객체 자신을 `모니터 오브젝트`로 활용 하였습니다. 메서드에 `synchronized` 키워드를 활용한다면 인스턴스 메서드에는 this 가 정적 메서드에는 `Class<?>` 객체가 `모니터 오브젝트`로 활용됩니다.

자바의 `synchronized` 키워드는 항상이 모니터 객체와 함께 동작합니다. 이 객체는 종종 모든 객체가 가지는 내제적인 락 이라는 의미에서 `intrinsic lock` 혹은 `monitor lock` 혹은 그냥 `monitor` 라고도 불립니다. 이 문서에서는 개인적으로 입에 붙은 `모니터 객체`, `모니터 락` 이라는 표현을 주로 사용하겠습니다.

모니터의 자세한 동작방식은 마지막에 알아보겠습니다.

### 2. 그림으로 보는 synchronzied 키워드

#### 1. 같은 객체 공유

![[images/synchronized-1.png]]
Thread 1과 Thread 2가 동일한 SynchronizedExchanger 객체를 공유하는 경우

위 코드에서 모든 메서드는 같은 monitor 객체 (this)를 가지기 때문에 Thread 1 이 setObject를 호출하는 순간 Thread 2는 getObject를 호출 할 수 없습니다. (동기화 블럭으로 선언된 xxxObj 메서드 들도 마찬가지)

#### 2. 서로 다른 객체 활용

![[images/synchronized-2.png]]
Thread 1과 Thread 2가 각자의 SynchronizedExchanger 객체를 가지는 경우

이렇게 활용하게 되면 Thread1 과 Thread2에서는 syncrhonized 를 활용하는 의미가 없습니다. 각 쓰레드가 자신의 SynchronizedExchanger 의 모니터 락을 획득하여 동기화 메서드, 블락에 진입할수 있기 때문입니다. (사실 당연합니다.)

#### 3. Static 메서드와 synchronzied 키워드
```java title="StaticSynchronizedExchanger 클래스 객체를 모니터 락으로 활용한다!"
public class StaticSynchronizedExchanger {

    private static Objectobject= null;

    public static synchronized Object getObject() {
        return object;
    }

    public static synchronized void setObject(Object o) {
		object= o;
    }

    public static Object getObj(){
        synchronized (StaticSynchronizedExchanger.class){
            return object;
        }
    }

    public static void setObj(Object o) {
        synchronized (StaticSynchronizedExchanger.class) {
			object= o;
        }
    }
}
```

![[images/synchronized-3.png]]

전체 쓰레드에서 한 쓰레드만이 synchronized static 메서드를 호출 할 수 있습니다.

### 3. 복잡하게 모니터 객체를 활용하는 예제 코드

#### 1. static, instance 메서드에 모두 synchronized 활용하기

```java title="MixedSynchronizedExchanger"
public class MixedSynchronizedExchanger {

    private static Object staticObject= null;

    public static synchronized Object getStaticObject() {
        return staticObject;
    }

    public static void setStaticObj(Object o) {
        synchronized (MixedSynchronizedExchanger.class) {
						staticObject= o;
        }
    }

    protected Object object = null;

    public synchronized void setObject(Object object) {
        this.object = object;
    }

    public Object getObj(){
        synchronized (this){
            return object;
        }
    }
}
```

위 처럼 활용하면 서로다른 두 쓰레드는 동시에 각각 static 메서드와 instance 메서드에 진입할 수 있습니다. 활용하는 모니터 객체가 다르기 때문입니다. 하지만 물론 동시에 모두 static 메서드 혹은 모두 instance 메서드에 진입할 수 는 없습니다.

#### 2. 한 객체에서 여러 모니터 객체 활용하기
```java title="MultipleMonitorObject"
public class MultipleMonitorObjects {

    private Object monitor1 = new Object();
    private Object monitor2 = new Object();

    private int counter1 = 0;
    private int counter2 = 0;

    public void incCounter1(){
        synchronized (this.monitor1){
            this.counter1++;
        }
    }

    public void incCounter2(){
        synchronized (this.monitor2){
            this.counter2++;
        }
    }
}
```

이경우 intCounterN 메서드는 두개의 카운터 필드는 서로 다른 모니터 객체에 의해 동기화 되므로 서로다른 쓰레드에 의해 동시에 실행 될 수 있습니다.

여기서 처음으로 this 가 아니라 별도로 생성한 더미 객체를 모니터 객체로 활용하는 예시가 나왔습니다. 모니터 객체를 적절하게 활용하면 여러 쓰레드간 공유되는 객체에서 전체 객체에 대한 접근을 block 하지 않고 효과적으로 처리 할 수 있습니다. 물론 synchronized 블락 자체도 메서드에 거는 것보다 최소한의 statement 에 거는것이 더 좋습니다.

`java.util.concurrent.ConcurrentHashMap` 은 이런 전략을 잘 활용한 예시입니다. `ConcurrentHashMap` 과 `@Deprecated` 된 `java.util.Hashtable` 은 모두 동시성 처리를 지원하는 해시맵 자료구조 이지만 그 전략에서 차이가 있습니다. 자세한 내용은 추후 정리해서 업로드 하겠습니다.


#### 3. 서로다른 class instance 에서 모니터 객체를 공유하기

```java title="SharedMonitorObject"
public class SharedMonitorObject {

    private Object monitor = null;

    private int counter = 0;

    public SharedMonitorObject(Object monitor) {
        if(monitor == null){
            throw new IllegalArgumentException(
                    "Monitor object cannot be null."
            );
        }
        this.monitor = monitor;
    }

    public void incCounter(){
        synchronized (this.monitor){
            this.counter++;
        }
    }
}

```

이런식으로 활용되는 경우가 있을진 모르겠지만 이런식으로도 쓸 수 있다고 합니다

매우 멋지고 Advanced 한 기술이고 잘 쓰면 Fancy한 동기화 기술을 사용할 수 있지만 정말 잘 동기화 하고 있는가에 대한 검증은 매우매우 어려워진다고 합니다.




### 4. 모니터 객체를 활용할때 주의 할 점

#### 1. Monitor objects cannot be null
-   모니터 객체는 null이 될 수 없다.
-   모니터 객체가 null일 경우 동기화 메서드/ 블락 진입시 null pointer exception이 발생한다.

#### 2. Don't use String constant objects as monitor objects
- 자바 컴파일러가 마구마구 최적화 해버립니다. 같은 instance 임을 보장 할 수 없음. 마찬가지로 Wrapper 클래스도 사용하면 안됩니다.

#### 3. Java synchronized blocks inside Java Lambda Expressions
- java 람다 표현식에서는 this라는 참조를 사용할 수 없으므로 monitor 객체로 this를 전달 할 수 없습니다.

### 5. 자바 synchronized 블락의 한계
- 한 시점에 오직 하나의 쓰레드만 synchronzied 블락에 진입할 수 있습니다.
	- 두개 이상의 쓰레드의 진입을 허용하기 위해서는 ReenterantLock 과 같은 녀석을 직접활용해야 합니다.
- Waiting 중인 쓰레드 간에 Synchronized 블락에 진입할 쓰레드의 순서를 보장할 수 없습니다.
	- 공정하지 않을 수 있으며 경우에 따라서는 Starvation 현상이 발생 할 수도 있습니다.

- JVM 상의 쓰레드 끼리의 동기화만 보장합니다.
	- 여러 JVM 인스턴스에서 동시성을 보장하기 위해서는 분산락의 활용이 필요합니다. 

### 6. synchronized 블락과 성능 오버헤드

![[images/synchronized-overhead.png]]

- 경쟁이 발생하여 쓰레드가 대기하는 상황이 발생한다면 오버헤드가 큽니다.
- 경쟁이 발생하지 않는다고 해도 Lock을 획득하고 Release 하는 약간의 오버헤드는 발생하게 됩니다.

>[!question]
>싱글 쓰레드 환경이라면 StringBuilder 와 StringBuffer 의 성능은 동일할까요?

### 7. 자바에서 모니터란?

- 자바에서의 모니터를 알기위해서 일단 모니터에 대해서 알아야 합니다.
- 이와 관련해서는 추후에 Spin Lock/ Mutex/ Semaphore/ Monitor 를 키워드로 운영체제를 학습할때 글을 올리겠습니다.
- 오늘은 간단히 정리만 하겠습니다.

```title="모니터의 뼈대가 되는 코드"
acquire(mutexLock)
while(!condition){
	wait(mutexLock, cv); 
}

... 이런 저런 코드 (critical section) ...

signal(cv2); -- OR -- broadcast(cv2);
realease(mutexLock);
```

- 자바의 모든 객체는 내부적으로 모니터를 가집니다.
- 자바의 모니터는 하나의 `뮤텍스 락`과 하나의 `condition variable` 을 가집니다.
- `뮤텍스 락`은 entry (entrance) queue 를 가집니다.
	- synchorzied 키워드를 만난 쓰레드는 모두 entry queue 에 들어갑니다.
	- 현재 mutex lock 이 이용가능하다면 condition 을 확인하러 가고 그렇지 않다면 mutex lock 이 realease 될 때까지 대기합니다.

- `CV` 는 waiting queue 를 가집니다. 
	- wait 
		- 다른 쓰레드에서 notify 혹은 notifyAll 을 통해 깨울 때 까지
		- 쓰레드 자기자신을 waiting queue 에 추가합니다.
	- notify
		- waiting queue 의 가장 앞에 위치한 쓰레드를 깨웁니다.
		- 깨어난 쓰레드는 condition 을 확인하고 다시 wait 하거나 critical section 에 진입합니다.
	- notifyAll
		- waiting queue 의 모든 쓰레드를 깨웁니다.


