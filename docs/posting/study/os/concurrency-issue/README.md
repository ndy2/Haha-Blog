---
tags: [os, concurrency]
title: 운영체제와 동시성 문제
author: ndy2
date: 2023-04-14
description: >-
  운영체제에서 동시성 문제를 해결하는 방법을 알아보자.
---
 
> [!quote] 참고 자료
> * 쉬운코드 - 운영체제 강의 on Youtube 
>     * [`『스핀락/뮤텍스/세마포』`](https://youtu.be/gTkvX2Awj6g)
>     * `『모니터』`

### 1. 동기화란?

여러 프로세스/스레드를 동시에 실행해도 공유 데이터의 일관성을 유지하는 것

> [!note] Critical Section
> 공유 데이터의 일관성을 보장하기위해 하나의 프로세스/스레드만 진입해서 실행 가능한 영역

### 2. Spin Lock

```c title="test_and_set의 pseudo code"
int test_and_set(int* lockPtr){
    int oldLock = *lockPtr;
    *lockPtr = 1;   // lockPtr의 값을 무조건 1로 변경
    return oldLock; // 기존 값을 리턴
}
```

```c title="critical section with spin lock"
volatile int lock = 0; // global

void critical(){
    while (test_and_set(&lock) == 1); // Lock이 소유가 되었다면 계속 루프를 돌며 락을 확인
    /* 
        critical section
    */
    lock = 0; // 탈출 직전 Lock을 해제 
}
```

사실 위 코드에는 이상한 점이 있다...
`int test_and_set(int* lockPtr)` 함수의 원자성이 보장되지 않는 다면 두 Thread가 동시에 `lock=0` 이라고 판단 할 수 있다.

`test_and_set`은 CPU의 도움을 받는 atomic 명령어 이다!

> [!note] `atomic 명령어`
> 명령어가 atomic 이라는 의미는 쪼개질 수 없다는 의미이다. 즉 실행 도중에 컨텍스트 스위치가 발생하여 다른 쓰레드가 실행되지 않고 항상 독립적인 실행이 보장된다는 의미이다.

Spinlock의 단점

- Lock이 있는지 계속 확인하는 작업 때문에 CPU의 낭비가 심하다.

### 2. mutex

mutex 는 spinlock의 단점을 극복하기 위해 lock이 준비되지 않으면 sleep 하고 lock이 준비 되는 경우 깨어나 queue에서 빠져나와 lock을 획득하는 방식으로 동작한다. 주의 할 점은 mutex 의 구현에 value에 대한 mutual exclusiveness를 보장하기 위해 spinlock이 사용된다.

```c++
class Mutex{
    int value = 1; // 현재 이용 가능한 lock의 숫자
    int guard = 0; // value 에대한 접근의 mutual exclusiveness 를 보장한다.
}

Mutex::lock(){ // lock 획득 과정
    while(test_and_set(&guard)); // guard 취득
    if(value == 0){
        현재 쓰레드를 큐에 넣음;
        guard = 0; & go to sleep;
    }else{
        value = 0;
        guard = 0;
    }
}

Mutext::unlock() {
    while(test_and_set(&guard));
    if(큐에 하나라도 대기 중이면){
        그 중 하나를 깨운다. !!
    }else{
        value = 1;    
    }
    guard = 0;
}

mutex -> lock();
// critical section
mutex -> unlock();

```


### 3. Semaphore

> [!note] Semaphore
> Signal mechanisim을 가진 하나이상의 프로세스/쓰레드가 critical section에 접근 가능하도록 하는 장치

```c++
class Semaphore{
    int value = n; // 현재 이용가능한 lock의 숫자
    int guard = 0; // value 에대한 접근의 mutual exclusiveness 를 보장한다.
}

Semaphore::wait(){ // lock 획득 과정
    while(test_and_set(&guard)); // guard 취득
    if(value == 0){
        현재 쓰레드를 큐에 넣음;
        guard = 0; & go to sleep;
    }else{
        value -= 1;
        guard = 0;
    }
}

Semaphore::signa() {
    while(test_and_set(&guard));
    if(큐에 하나라도 대기 중이면){
        그 중 하나를 깨운다. !!
    }else{
        value += 1;    
    }
    guard = 0;
}

semaphore -> lock();
// critical section
semaphore -> unlock();

```

`value`가 1인 세마포어, 즉 한번에 하나의 프로세스/쓰레드에게만 진입을 허용하는 세마포어를 binary semaphore 라고 한다. value 가 2 이상인 세마포어를 counting semaphore 라고 한다.

세마포어는 `signal` 을 통해 순서를 정해줄 수 있다.

### 4.  Mutex vs Semaphore

- mutex는 락을 가진 자만 락을 해제할 수 있다.
- 세마포어는 그렇지 않다.
- 뮤텍스는 priority inheritance 속성을 가진다.
    - priority 가 높은 프로세스가 priority 가 낮은 프로세스에 의존하는 문제를 해결할 수 있다.
    - 어짜피 lock을 해제하는 주체가 자신으로 정해져 있기 때문에 일시적으로 priority 가 낮은 프로세스의 priority를 높이면 된다.
- 세마포어는 그 속성이 없다.
    - 어떤 process 가 lock을 해제할 지 알수 없기 때문이다.

> [!tip] when to use what?
> 상호 배제만 필요하다면 뮤텍스를, 작업 간의 실행 순서 동기화가 필요하다면 세마포어를 권장한다.

### 5. monitor

TODO