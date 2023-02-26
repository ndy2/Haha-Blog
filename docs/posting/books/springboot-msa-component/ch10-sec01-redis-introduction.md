참고 - [Waht Makes Redis Special? | Redis Internals](https://www.youtube.com/watch?v=h30k7YixrMo&ab_channel=AsliEngineeringbyArpitBhayani)

!!! note

	Redis :  The open source, in-memory data structure store used by millions of developers 
	as a database, cache, streaming engine, and message broker.
     
    레디스의 특징을 대표하기 적합한 키워드 두가지는
    1. '메모리', 2. '싱글 스레드' 이다.

## What Makes Redis Special?

### 1. Every Operation on Redis is **Atomic**

!!! note

    atomic - when command is executing, Redis does not context switch and stant
    executing others command. That is you don't have to worry about concurrency at all

- putting a key
- adding to the list
- set union, intersection
- incrementing the value

### 2. Data is Stored **in-memory**

- hence the most common use of Redis is for "caching"

-> 백업 지원!

Redis 는 메모리 기반의 데이터 저장소다. 메모리 특성상 매우 빠른 속도로 데이터를 저장 및 조회할 수 있다. 하지만 메모리 특정상 저장된 데이터는 사라질 가능성이 있다. 이를 보완 하고자 레디스는 메모리의 데이터를 디스크로 백업하는 두가지 방식을 제공한다. 두 가지 기능은 각각 사용해도 되지만, 함께 설정 하여 상호 보완적으로 사용해도 된다.

1. RDB (Redis DataBase)
- relational database 아니다.
- 특정 시간 마다 전체 메모리 데이터에 대한 스냅샷을 생성한다.
- 데이터 복구는 스냅샷을 그대로 로딩하면 되어 상대적으로 간단하다.
- 하지만 스냅샷이 마지막으로 저장된 시점 이후의 데이터는 유실된다.

 1. AOF (Append Only File)
- 레디스의 데이터 변경 이벤트를 감지해 이를 모두 로그에 저장하는 방식이다.
- 데이터의 변경 이벤트를 초 단위로 취합하여 로그 파일에 작성한다.
- RDB 방식에 비해 데이터 유실량이 적은 장점이 있다.
- 하지만 로그 파일에 대한 관리가 필요하고 복구 시간이 RDB에 비해서 오래 걸린다.

### 3. Redis 가 {==싱글 스레드==}로 클라이언트 커맨드를 처리하는 방식!

은 바로 **이벤트 루프**!

![redis-event-loop.excalidraw.png](./excalidraws/redis-event-loop.excalidraw.png)

!!! note

    
    **이벤트 루프(event loop)** 는 동시성(concurrency)을 제공하기 위한 프로그래밍 모델
     중 하나로, 특정 이벤트가 발생할 때까지 대기하다가 이벤트가 발생하면 디스패치해 처리하
     는 방식으로 작동합니다.  

이벤트 루프를 활용한 다양한 구현체

- Netty, Node.js (libuy), Redis 

Single Thread

 Conccurency 를 위해 mutex, semaphore, waiting 이 필요 없다.

I/O multiplexing

- 다중 TCP 연결을 concurrent 하게 다룰 수 있다.

### 4. Other Key Features

Transactions, Pub/Sub, TTL on keys and LRU eviction
