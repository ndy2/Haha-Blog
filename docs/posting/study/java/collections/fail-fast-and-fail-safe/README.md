---
tags: [java, collections]
title: fail-fast vs fail-safe iterator
author: ndy2
date: 2023-03-23
description: >-
  
---
 
 
> [!quote] 참고 자료
> * [Java interview questions and answers for experienced | Live Mock | coding interview]() by Selenium Express on Youtube
> 	* [00:50:14](https://www.youtube.com/watch?v=yX2w-Sof95s&t=3014s)- Q26. Difference between fail fast/fail safe collections
> 	* [00:52:16](https://www.youtube.com/watch?v=yX2w-Sof95s&t=3136s) - Q27. Which types of collections consume more memory; fail-fast or fail-safe?
> * [Fail-Safe Iterator vs Fail-Fast Iterator](https://www.baeldung.com/java-fail-safe-vs-fail-fast-iterator) - on baeldung

### 1. Fail-fast Iterator.

#### What is It?

* 빠르게 실패하는 Iterator?
* Fail-fast Iterator 를 사용하여 iteration 을 하면 대상 컬렉션의 변경을 허용하지 않는다.
* `ArrayList`, `HashMap` 등의 Iterator 가 바로 fail-fast iterator 이다.

#### How Does it Works

* 모든 Collection 은 *`modCount`* 라고 하는 내부적인 카운터를 가지고 있다. 카운터는 컬렉션의 modification (add, remove) 횟수를 카운팅한다.
* iterator `next()` 호출시 Collection 의 *`modCount`* 를 비교한다.
* 만약 초기값과 다르다면 `ConcurrentModificationException` 을 던진다.

#### Code!

```java title="순회 도중에 컬렉션의 원소 제거"
import java.util.ArrayList;  
import java.util.Iterator;  
import java.util.List;  
  
public class Main {  
  
    public static void main(String[] args) {  
        List<Integer> list = new ArrayList<>();  
        list.add(1);  
        list.add(2);  
        list.add(3);  
        list.add(4);  
  
        Iterator<Integer> it = list.iterator();  
  
        while (it.hasNext()){  
            Integer next = it.next();  
            System.out.println("next = " + next);  
            list.remove((Integer) 3);  
            // list.add((Integer) 5); // - 추가도 마찬가지!
        }  
    }  
}
```

```text title="실행 결과 - ConcurrentModificationException"
next = 1
Exception in thread "main" java.util.ConcurrentModificationException
	at java.base/java.util.ArrayList$Itr.checkForComodification(ArrayList.java:1043)
	at java.base/java.util.ArrayList$Itr.next(ArrayList.java:997)
	at Main.main(Main.java:17)
```

> [!note] iterator 와 forEach 문
> 위 코드를 흔히 이야기 하는 forEach 구문으로 작성해도 똑같은 예외가 발생한다.
> byte code 관점에서 둘은 완전히 일치한다.
>
> ```java
> for (Integer next : list) {  
>    System.out.println("next = " + next);
>    list.add((Integer) 5);  
> }
> ```
>

반면 컬렉션의 `remove(E e)` 메서드가 아니라 iterator 의 `remove()` 메서드를 호출하는 것은 문제 없다.

```java
import java.util.ArrayList;  
import java.util.Iterator;  
import java.util.List;  
  
public class Main {  
  
    public static void main(String[] args) {  
        List<Integer> list = new ArrayList<>();  
        list.add(1);  
        list.add(2);  
        list.add(3);  
        list.add(4);  
  
        Iterator<Integer> it = list.iterator();  
  
        while (it.hasNext()){  
            Integer next = it.next();  
            it.remove();  
            System.out.println("next = " + next);  
        }  
        System.out.println("list.size() = " + list.size());  
    }  
}
```

```text title="실행 결과"
next = 1
next = 2
next = 3
next = 4
list.size() = 0
```

#### ArrayList Iterator Implementation

![[arraylist-iterator.png]]

```java title="ArrayList#Iter.checkForComodification"
final void checkForComodification() {  
    if (modCount != expectedModCount)  
        throw new ConcurrentModificationException();  
}
```

---

### 2. Fail-safe Iterators

#### 1. What is It?

* Fail-Safe iterators 는 iteration 을 하는 도중 컬렉션 자체를 변경하는 것을 허용합니다.
* `java.util.concurrent` 패키지의 `ConcurrentHashMap`, `CopyOnWriteArrayList` 의 반복자가 fail-safe iterator 입니다.

#### 2. How Does it Works?

* 요 iterator 들은 실제 Collection 의 clone 을 만들어 그 카피 컬렉션을 순회합니다.
* 순회 하는 도중 변경이 일어 났더라도 복사본은 여전히 변경이 일어나지 않았습니다.
* 따라서 요 iterator 들은 변경이 있더라도 순회할 수 있습니다.

> [!warning]
> * Fail-Safe iterator 는 완벽하지 않습니다.
> 	* `fail-safe` 의 정확한 명칭은 *`weakly consistent`* 입니다.
> * 컬렉션의 순회도중 변경이 발생하여도 그것을 완벽하게 해당 iterator 가 반영하지 못할 수 있습니다.
> * 대상 Collection 의 Javadoc 을 꼼꼼하게 확인해야 합니다.

#### 3. Code!

```java title="CopyOnWriteArrayList 사용!"
import java.util.Iterator;  
import java.util.concurrent.CopyOnWriteArrayList;  
  
public class Main {  
  
    public static void main(String[] args) {  
        CopyOnWriteArrayList<Integer> list = new CopyOnWriteArrayList<>();  
        list.add(1);  
        list.add(2);  
        list.add(3);  
        list.add(4);  
  
        Iterator<Integer> it = list.iterator();  
  
        while (it.hasNext()){  
            Integer next = it.next();  
            System.out.println("next = " + next);  
            list.remove((Integer) 3);  
        }  // iterator 하는 순간에는 copy 를 활용하기 때문에 삭제한 원소 `3` 까지 순회된다.
  
        System.out.println("list = " + list); 
        // 물론 순회가 종료된 이후에는 원본에도 반영이 된다.
    }  
}
```

```text title="실행 결과!"
next = 1
next = 2
next = 3
next = 4
list = [1, 2, 4]
```

### 3. 메모리

* 당연히 fail-safe 한 Collection 이 메모리를 더 많이 사용한다.
* CopyOnWriteArrayList 의 이름에서도 알 수 있듯이 fail-safe 한 속성을 만족하기 위해 iterator 뿐만 아니라 모든 쓰기 연산 (`add`, `set`, `remove`, ...) 에 대해서도 사용시에 전체 내부 배열을 메모리에 카피하는 과정이 필요하다.
* 이는 메모리 관점에서 큰 낭비라고 볼 수 있다.

![[cow-add.png|Arrays.copyOf 을 통해 배열의 스냅샷을 메모리에 저장한다.]]

![[cow-iterator.png|snapshot 필드를 가지고 있는 CopyOnWriteArrayList 의 반복자]]
