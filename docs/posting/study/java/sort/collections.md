---
tags: [java, sort]
title: Collections.sort
author: ndy2
---

### 0. 들어가며 

자바는 `java.util` 패키지를 통해 정렬 기능을 제공한다. 이들의 동작 방식과 주의 사항에 대해 알아보자!

---

### 1.  컬렉션 정렬

```java
package java.util

public class Collections {

	public static <T extends Comparable<? super T>> void sort(List<T> list) {  
		list.sort(null);  
    }

	public static <T> void sort(List<T> list, Comparator<? super T> c) {  
	    list.sort(c);  
	}
}
```

컬렉션 정렬 API 는 `Collections.` *`sort( )`* 이다. 정렬하고자 하는 `List` 를 기본적으로 받으며 오버로딩을 통해 `Comparator` 를 명시적으로 받는 것과 그렇지 않은 방식 두가지가 제공된다. 

구현을 살펴보면 배열의 sort 메서드 `List.sort()` 를 그대로 넘겨서 호출한다. 별로 살펴볼게 없다! :thumbsup:

---
### 2. 리스트 정렬

++option+b++ 를 눌러 List 의 구현을 살펴보자 ! 

```java title="java.util.List#sort()"
default void sort(Comparator<? super E> c) {  
    Object[] a = this.toArray();  
    Arrays.sort(a, (Comparator) c);  
    ListIterator<E> i = this.listIterator();  
    for (Object e : a) {  
        i.next();  
        i.set((E) e);  
    }  
}
```

사실 List 는 인터페이스 이기때문에 구현이라는 표현은 애매하지만 java 8 에 추가된 default method 를 통해 sort 의 기능을 간단하게 구현하고 있다. 컬렉션을 배열로 바꾸어 배열의 정렬 api (`Arrays#sort( )`) 를 그대로 활용하고 있다.

특이한점으로는 배열의 값을 바꾸는 과정에 listIterator 를 활용한다는 점이다. 이렇게되면 값을 바꿀때 매번 index 를 찾아가는 것이 아니라 참조 자체를 순회하는 방식이기 때문에 효율적인것 같다.

---

다시  ++shift+option+b++ 를 눌러 이 인터페이스를 구현한 녀석을 살펴보자.

![List.sort.png](images/List.sort.png)

### 3. ArrayList 정렬

`ArrayList` 가 눈에 띈다! 살펴보자!

```java
@Override
@SuppressWarnings("unchecked")
public void sort(Comparator<? super E> c) {  
    final int expectedModCount = modCount;  
    Arrays.sort((E[]) elementData, 0, size, c);  
    if (modCount != expectedModCount)  
        throw new ConcurrentModificationException();  
    modCount++;  
}
```

`ArrayList` 는 말그대로 Array 를 내부에 가지고 있기 때문에 (위 코드의 `elementData` 필드) 이를 그대로 활용하는 방식으로 오버라이딩해서 구현하였다. 또한 `modCount` 라는 필드를 통해 여러 쓰레드가 동시에 리스트를 수정하는 경우를 간단하게 제어하고 있다. 

---

### 4. 나머지 리스트 구현체 정렬

그런데 위 목록을 살펴보니 `LinkedList` 와 `Stack` 이 보이지 않는다. (*deprecated* 된 `Vector` 같은 경우는 `ArrayList` 와 구현 방식이 같다.)

![ListCollection.png](images/ListCollection.png)

=== "Stack Sort"
   
	```java
	import java.util.Comparator;  
	import java.util.Stack;  
	  
	public class Main {  
	  
		public static void main(String[] args) {  
			Stack<Integer> stack = new Stack<>();  
			stack.add(3);  
			stack.add(5);  
			stack.add(1);  
			stack.add(7);  
	  
			stack.sort(Comparator.naturalOrder());  
			while (!stack.isEmpty()){  
				System.out.println(stack.pop());  
			}  
		}  
	}
	// 7 5 3 1
	```

=== "LinkedList Sort"

	```java
	import java.util.Comparator;  
	import java.util.LinkedList;  
	  
	public class Main {  
	  
		public static void main(String[] args) {  
			LinkedList<Integer> linkedList = new LinkedList<>();  
			linkedList.add(3);  
			linkedList.add(5);  
			linkedList.add(1);  
			linkedList.add(7);  
	  
			linkedList.sort(Comparator.naturalOrder());  
			while (!linkedList.isEmpty()){  
				System.out.println(linkedList.pop());  
			}  
		}  
	}
	// 1 3 5 7
	```

이들 모두 잘 동작한다. `Stack` 은 `Vector` 를 상속하기 때문에 내부적으로 배열을 통해 데이터를 저장하고 있다. 따라서 `Stack` 은 `List.sort` 호출시 가장 가까운 부모의 오버라이드 메서드인 `Vector` 의 구현에 따라 정렬을 수행한다. 사실 이는 잘못된 구현이고 자바의 실수입니다. ([관련 링크](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=4475301)) Stack 은 LIFO 구조를 만족하기 위해 인덱스를 이용한 접근이나 정렬 기능을 제공하면 안되지만 Vector 를 상속하기 때문에 배열과 관련된 모든 api 가 노출되어야 합니다.

반면 `LinkedList` 는 위에서 살펴본 `List.sort` 의 `default` 구현을 통해 정렬이 수행되는것을 확인 할 수 있다. `LinkedList` 를 정렬한다는 것은 `Stack` 과는 달리 논리적인 결함이 있지는 않다. 하지만 정말 이 경우 `LinkedList` 자료구조가 적절한지 고민해볼 필요가 있다.


### 5. 결론

컬렉션과 관련된 정렬 API 를 살펴보면 결국 모두 배열의 컬렉션 API - `Arrays.sort` 를 이용한다는 것을 알 수 있다. 다음 시간에는 이녀석을 파해쳐 보자!