---
title: Scope Function 활용 예시
date: 2023-02-04
---

Scope Function 활용 예시

### 1. Let

### 2. With

#### 1. 함수에 바로 달아서 사용하기

* 코테에서 자주 활용되는 템플릿
    * IntelliJ 의 implicit receiver hint 를 통해 this 가 BufferedReader 타입이 됨을 확인 할 수 있다.

![scope-functions.png](images/scope-functions.png)

    * 다른 방식으로는 use 를 활용하는 방법이 있다. 이경우 br 을 바로 close 해 주어 더 좋은것 같다.

![scope-functions2.png](images/scope-functions2.png)

#### 2. toEntity/toDto

this 를 생략 할 수 있어 필드가 많아도 코드가 간결해진다.

```kotlin
return with(person){
    PersonDto(
        name = name,
        age = age,
    )
}
```

### 3. Run

### 4. Apply

#### 1. Test Fixture 생성시

생성자에 존재 하지 않는 값을 바로 apply 를 활용한 method chaining 으로 세팅 한다.

```kotlin
fun createPerson(
    name: String,
    age: Int,
    hobby: String,
) : Person {
    return Person(
        name = name,
        age = age,
    ).apply {
        this.hobby = hobby
    }
}
```

### 5. Also

#### 1. 생성자에 달아서 바로 후처리 하기

* 채팅 방 생성 후 바로 리포지 토리에 저장하고 관련 이벤트 발행

```kotlin title="채팅 방 생성"
override fun createChatRoom(name: String): ChatRoom {
    return ChatRoom(name).also {
        chatRoomRepository.save(it)
        eventPublisher.publishEvent(ChatRoomCreatedEvent(it.roomId, it.name))
    }
}
```
