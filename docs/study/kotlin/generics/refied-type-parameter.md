---
title: 실체화된 타입 파라미터 (refied-type-parameter)
date: 2023-02-17
---

@참고 자료)

- [`『코틀린 인 액션』`](http://www.yes24.com/Product/Goods/55148593) by 드미트리 제메로프, 스베트라나 이사코바 
    - 9장 제네릭스
- kotlin documentation - [generics#type-ereasure](https://kotlinlang.org/docs/generics.html#type-erasure)

---

### 1. 타입 소거 <sup>Type erasure</sup>

!!! note "타입 소거"

    * 제네릭 선언 (제네릭 함수 선언, 제네릭 클래스 선언)에 대한 타입 안정성 검증은 컴파일 타임에 이루어집니다. 
    * 런타임에 제네릭 타입의 인스턴스에는 실제 어떤 타입 아규먼트가 담겨 있는지에 대한 정보가 사라집니다. 
    * 이것을 타입 소거 라고합니다

#### 1. 제네릭 타입 체크와 캐스팅

타입 소거로 인해, 런타입에 생성된 제네릭 타임 인스턴스의 구체적인 타입 아규먼트의 타입을 체크 할 수 있는 일반적인 방법은 없습니다.  `Foo<Bar>` 과 `Foo<Baz?>` 는 런타임에 모두 그냥 `Foo<*>` 일 뿐입니다.

!!! note 

    * 일반적이지 않은 방법으로 슈퍼 타입 토큰 이라는 것이 있습니다.
    * 참고 영상 링크 - [토비의 봄 TV 2회 - 수퍼 타입 토큰](https://youtu.be/01sdXvZSjcI)


그렇기 때문에 컴파일러는 애초가 그런 종류의 타입 체킹 (제네릭 타입 파라미터를 포함한 타입 체킹 이나 타입 파라미터 자체를 이용한 타입 체킹) 을 허용하지 않습니다. 제네릭 클래스 자체 타입에 대한 검증을 star-projected type 을 이용해 수행 할 수 있습니다.


### 2. 인라인 함수와 Refied Type Parameter

```kotlin
>>> fun <T> isA(value: Any) = value is T
Error: Cannot check for instance of erased type: T

>>> inline fun <refied T> isA(value: Any) value is T
>>> println(isA<String>("abc"))
true
>>> println(isA<String>(123))
false
```

인라인 함수의 타입 파라미터는 실체화 되므로 실행 시점에 타입 인자를 알 수 있다.

intellij 에서 확인 - 너무 똑똑하다.

`그냥 활용`

![images/5.png](images/5.png)

++option+enter++

![images/6.png](images/6.png)

`inline 함수 에서만  refied 를 사용할 수 있고 refied 를 사용하지 않으면 여전히 타입 실체화가 되지 않는다.`

![images/7.png](images/7.png)

---

### 3. Refied Type Parameter 와 클래스 참조 예제

코틀린 타입에 대응하는 `java.lang.Class` 를 얻기 (`::class.java`) 위해서 refied type parameter 를 사용하면 좋다!

```kotlin
abstract class BaseIdEntity<Id : Any>(val id: Id)  
class User(id: Long, val name: String) : BaseIdEntity<Long>(id)  
class Product(id: String, val price: Int) : BaseIdEntity<String>(id)  
```

위와 같은 간단한 엔티티의 추상 구조를 생각해보자.

자바에서 각 엔티티 타입의 NotFountException 을 추상화 해서 발생시키는 코드를 만들어보자.
제네릭을 이용해서는 런타임에 타입 클래스의 정보 (simpleName 등) 을 얻을 수 없다. 따라서 `java.lang.Class` 를 활용한다.

```java
public static void main(){

	if (1 == 1) notFound(User.class, 1L)
	if (1 == 1) notFound(Product.class, "product-1")
}

public void notFound(Class<?> clazz, Object id){
	String entityName = clazz.class.simpleName
	throw new NotFoundException(entityName, id) 
}

public class NotFoundException extends ServiceRuntimeException {
	public NotFoundException(String entityName, Object id) {
		super(entityName + "with id  : " + id + "not found");
	}
}
```


---

코드는 살짝 다르다는 점에 유의해 코틀린에서 이 코드를 어떻게 활용할 수 있는지 살펴보자

java 라면 메서드의 파라 미터에 `Class<?>`  타입을 넘기는 등의 트릭이 필요했겠지만 코틀린에서든 훨씬 간결하게 사용 할 수 있다.

```kotlin title="이 정도면 만족하고 사용할 만한것 같다."
fun main() {  
    if (1 == 1) notFound<User>(1L)  
    if (1 == 1) notFound<Product>("product-1")  
}  
  

inline fun <reified E : BaseIdEntity<Long>> notFound(id: Long): Nothing {  
    val entityName = E::class.java.simpleName  
    throw NotFoundException(entityName, id)  
}  
  
inline fun <reified E : BaseIdEntity<String>> notFound(id: String): Nothing {  
    val entityName = E::class.java.simpleName  
    throw NotFoundException(entityName, id)  
}  
  
class NotFoundException(entityName: String, id: Any) : RuntimeException("$entityName with id : $id not found")
```


개인적으로 코틀린 코드가 훨씬 깔끔하게 보인다. 

또한 자바에서는 각 오버로딩 된 `notFound` 메서드에 옳은 타입의 엔티티 클래스 객체가 전달되었는지 확인 할 수 없다. 즉 `notFound(Product.class, 1L)` 같은 코드도 컴파일 및 실행에 성공한다. 반면 코틀린 에서는 각각 가능한 id 타입 별로 `notFound` 메서드가 추가 되는 단점이 있지만 `notFound<Proudct>(1L)` 과 같은 호출은 컴파일러의 타입체킹에 의해 걸러질 수 있다!

`refied E` 타입이 상속하는 BaseIdEntity 타입의 타입 체킹을 위해서 메서드가 추가되기는 했지만 더 좋은것 같다. 일반적인 방법으로는 E 가 상속하는 BaseIdEntity 의 Id 타입을 획득하는 것은 불가능한 것 같다.