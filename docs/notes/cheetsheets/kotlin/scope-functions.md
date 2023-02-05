---
title: 제목
date: 2023-02-04
---

Scope Function 활용 예시

### 1. let

### 2. with

#### 1. 함수에 바로 달아서 사용하기

!!! example

    * 코테에서 자주 활용되는 템플릿
        * IntelliJ 의 implicit receiver hint 를 통해 this 가 BufferedReader 타입이 됨을 확인 할 수 있다.
    ![scope-functions.png](images/scope-functions.png)

        * 다른 방식으로는 use 를 활용하는 방법이 있다. 이경우 br 을 바로 close 해 주어 더 좋은것 같다.
    ![scope-functions2.png](images/scope-functions2.png)

### 3. run

### 4. apply

### 5. also

#### 1. 생성자에 달아서 바로 후처리 하기

!!! example

    * 채팅 방 생성 후 바로 리포지 토리에 저장하고 관련 이벤트 발행
       
    ```kotlin title="채팅 방 생성"
    override fun createChatRoom(name: String): ChatRoom {
        return ChatRoom(name).also {
            chatRoomRepository.save(it)
            eventPublisher.publishEvent(ChatRoomCreatedEvent(it.roomId, it.name))
        }
    }
    ```

