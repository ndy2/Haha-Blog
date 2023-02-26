---
tags: [java]
title: String
author: ndy2
---
 

> [!quote] 참고 자료
> * baeldung - [java-string-pool](https://www.baeldung.com/java-string-pool)
> * baeldung - [java-9-compact-string](https://www.baeldung.com/java-9-compact-string)
> * Pankay - [What is Java String Pool?](https://www.digitalocean.com/community/tutorials/what-is-java-string-pool)

자바에서 문자열과 관련된 대표적인 클래스에는

* java.lang.String
* java.lang.StringBuffer
* java.lang.StringBuilder

세가지가 있습니다.

이 문서에서는 먼저 가장 핵심이 되는 클래스인 String 에 대해서 자세히 정리하겠습니다.

이후에 다음 문서에서 세 클래스를 간단히 비교해보겠습니다.

---

### 1. String 은 불변 객체!

`java.lang.String` 은 자바에서 문자열을 표현하는 가장 기본적인 객체입니다. String 의 특징에대해 검색해보면 가장 먼저 나오는 것이 열이면 아홉 `String` 은 불변 객체 (Immutable Object) 라는 것입니다.

String 이 Immutable 함으로써 가질 수 있는 이점은 다음과 같습니다.

1. String Pool 을 통해 힙 메모리를 절약하고 캐싱을 활용할 수 있습니다.
2. String 에는 중요한 데이터가 저장될 수 있는데 이 값을 원천적으로 Immutable 로 만듬으로써 보안에 이점을 가집니다.
3. String 은 불변하기 때문에 여러 쓰레드에서 동시에 참조되어도 문제가 되지 않습니다. 즉, Thread Safe 합니다.
4. hashCode 값을 캐싱할 수 있습니다.

### 2. String 은 Thread-Safe 하다!

이미 불변 객체를 이야기 하면서 다루었지만 상당히 중요한 개념이라 굳이 따로 넘버링을 주었습니다.

> String 은 불변객체이며 따라서 Thread-Safe 합니다!

### 3. String Pool (constant pool)

자바의 String Pool 은 String 을 저장하기 위해 마련된 힙 내부에 위치한 특별한 메모리 공간힙니다.

![[images/string-pool.png]]

String 을 생성하는 방식에는 String literal (`""`) 를 활용하는 방식과 생성자 (`new String(..)`) 을 활용하는 방식이 있습니다. `(*)` 이때 항상 literal 을 사용하는 방식을 사용하는것이 좋습니다. 왜냐하면 생성자를 통해 String 을 생성하면 String pool 이 아닌 일반 heap 영역에 메모리가 저장되고 String 이 Immutable 함으로써 가질 수 있는 이점 (thread-safe 등) 을 가질 수 없습니다. 

`(*)` Java 15 에 추가된 text block (""") 을 활용하는 방식도 있긴 합니다.

링크 - [String pool 과 관련된 헷갈리는 면접 문제](https://www.digitalocean.com/community/tutorials/what-is-java-string-pool#how-many-strings-are-getting-created-in-the-string-pool)

### 4. String 의 내부 구현!

Java 8 까지 String 은 내부적으로 UTF-16 으로 인코딩된 `char[]` 문자 배열을 가졌습니다. 즉 한 글자는 항상 2 바이트를 사용합니다. 하지만 영어의 경우 1 바이트 만으로 충분합니다.

Java 9 에는 이를 해결하기 위해 Compact String 이라는 기능이 추가되었으며 이는 기본적으로 활성화 되어 있습니다. 

```java title="java.lang.String 일부"

public final class String  
    implements java.io.Serializable, Comparable<String>, CharSequence,  
               Constable, ConstantDesc {

	@Stable  
	private final byte[] value;  // char 배열이 아닌 바이트 배열로 저장된다!

	...
}
```

동작 확인

```java
@Test  
void 문자_바이트_찍어보기() {  
    String a = "aa";  
    String b = "가가";  
  
    System.out.println("cs = " + Charset.defaultCharset());  
  
    // a : latin 문자 -> ascii code 
    System.out.println(a.getBytes().length);  
    System.out.println(Arrays.toString(a.getBytes()));  
  
    // 가 : utf-8 : \xEA\xB0\x80 : [-22, -80, -128]  
    System.out.println(Arrays.toString(b.getBytes()));  
}
```

```text title="실행 결과"
cs = UTF-8

2
[97, 97]
6
[-22, -80, -128, -22, -80, -128]
```
