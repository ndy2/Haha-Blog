---
tags: [os, ipc]
title: IPC Part1
author: ndy2
date: 2023-05-05
description: >-
  
---
 
> [!quote] 참고 자료
> * [운영체제: 05. 프로세스간 통신 (IPC: Inter-Process Communication)](https://youtu.be/Bgdii8FppOU)

### 3.4. Interprocess Communication

- Process 가 동시에(concurrently) 의 실행되는 경우...
    - `독립`적일 수도 있고 서로 `협력`하는 경우 일 수도 있다.

- `independent process` 와 `cooperating process`
    - 핵심은 `데이터 공유(shares data)`
    - 다른 프로세스와 데이터를 공유하면 협력하는 프로세스이고 그렇지 않다면 독립적인 프로세스이다.


> [!note] IPC - Inter-Process Communication
> - 협력하는 process 는 IPC 메커니즘을 필요로 한다.
>     - 즉, 데이터를 공유, 교환하는 정책이 필요하다.
>     - 다시 말해 데이터를 보내고 데이터를 받는 메커니즘이 필요하다.

> [!note] Two fundamental models of IPC
> - shared memory/ 공유 메모리
> - message passing

![[ipc-models.excalidraw.png]]

### 3.5 IPC in Shared-Memory Systems

Shared-Memory 를 살펴보기전에 `Producer-Consumer Problem` 을 살펴보자. `Producer-Consumer Problem` 는 협력하는 두 프로세스 간에 흔히 발생하는 문제이다. `producer` 는 정보/자원을 생산하는 프로세스 `consumer` 는 그 정보/자원을 소비, 활용하는 프로세스이다. 예를 들어 컴파일러는 어셈블리코드를 만들고 어셈블러는 그것을 사용한다. 웹서버는 HTML 을 제공하고 브라우저는 그것을 사용한다.

개인적으로 여기에 `Problem` 이라는 이름을 붙이는것이 조금 어색하게 느껴진다. 책이나 강의 영상에서 Producer-Consumer Problem 그리고 Shared-Memory, Message Queue 의 관계를 Problem과 Solution 처럼 이야기하는데 그보다는 어떤 객체지향에서 이야기하는 추상적인 모델과 구체적인 모델(?) 이런식으로 표현하는 것이 더 적절하게 느껴진다. 그래서 표현을 약간 객체지향 st로 하면 Producer-Consumer 라는 근본적인 모델이 있고 그아래 IPC, 가 있고 그 아래 Shared-Memory, Message Queue 와 같은 솔루션 모델? 이 있다고 느끼면 좋을것 같다.

이런 큰 그림을 바탕으로 이제 `shared-memory` 를 알아보자.

- A Solution using `shared-memory`
    - To allow producer and consumer to run concurrently
    - Let a buffer of item be available
        - 프로듀서는 버퍼를 채우고, 컨슈머는 버퍼를 사용한다.

> [!note] Shared Memory
> A `shared memory` is a region of memory that is shared by the producer and consumer processes

```c title="Shared Buffer 예시"
#define BUFFER_SIZE 10

typedef struct {
  // ...
} item

item buffer[Buffer_SIZE]; // shared buffer

int in = 0;
int out = 0;
```

```c title="producer that using shared memory"
item next_produced;

while(true){
    while(((in + 1) % BUFFER_SIZE) == out);
    // do nothing
    // 버퍼를 채울 공간이 없다면 계속 대기

    /*
      next_produced 를 생성
    */
    buffer[in] = next_produced;
    in = (in + 1) % BUFFER_SIZE;
}
```

```c title="a consumer that uses shared memory"
item next_consuemd;

while(true){
    while(in == out);
    // do nothing
    // 버퍼가 비어있다면 계속 대기

    next_consumed = buffer[out]
    out = (out + 1) % BUFFER_SIZE

    /*
      next_consumed 를 소모
    */
}
```

> [!example] PROS & CONS
> * shared memory 에 접근하는 로직을 애플리케이션 개발자가 직접 작성해야 함
> * 이걸 좀 누가 알아서 보내주면 좋을탠데...
>     * OS : 뜨끔 (난가?)


### 3.6 IPC in Message-Passing Systems

> [!quote] 
>  운영체제 : 나다 싶으면 하자!


바로 코드로 살펴보자!

```c title="producer that send item to message queue"
item next_produced;

while(true){
    /*
      next_produced 를 생성
    */
    send(next_produced);
}
```

```c title="a consumer that receive item from message queue
item next_consuemd;

while(true){
    next_consuemd = receive();
    /*
      next_consumed 를 소모
    */
}
```

boiler-plate 한 코드가 사라졌다! 객체지향을 배우고 운영체제를 살펴보니 또 느낌이 다른것같다... 익숙한 객체지향의 향기가 난다.

이런 message-passing 방식의 IPC 를 구성하는 방식에는 다양한 방법이 있다. direct, indirect 메시지 패싱의 메서드 형태를 살펴보자.

```java title="direct message passing"
void send(Process dest, Message message);
Message recieve(Process src);
```

```java title="indirect message passing"
void send(MessageBox box, Message message);
Message recieve(MessageBox box);

// 메시지 박스를 생성/제거
MessageBox createMessageBox(여러 옵션들...);
void deleteMessageBox(MessageBox box);
```

`MessageBox` 는 `Port` 라고도 불린다!!!