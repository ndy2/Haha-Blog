Redis 에는 HA (High Availability) 를 위해 두가지 아키텍처를 제공한다.

1. 모니터링 기반의 {==레디스 센티넬 (Redis Sentinel)==}
2. 클러스터 노드들이 서로 통신하는 {==레디스 클러스터 (Redis Cluster)==} 

가 바로 그 둘이다.

### 1. Redis Sentinel

![redis-sentinel-architecture.excalidraw.png](./excalidraws/redis-sentinel-architecture.excalidraw.png)

- 편의를 위해 레디스와 레디스 센티넬을 같은 노드로 표현하였습니다. 물론 둘을 무리적으로 다른 서버에 두고 관리 할 수도 있습니다.
- Redis Sentinel 은 세가지 기능을 통해 Redis System 의 HA 를 보장합니다.

1. `Monitoring`
- 마스터와 슬레이브 서버의 상태를 주기적으로 모니터링합니다.

1. `Notification`
- 모니터링 결과 문제가 있다면 다른 프로그램이나 시스템 관리자에게 API 를 통해 알림을 전달합니다.

1. `Automatic Failover`
- Master 노드에 문제가 생기면 센티넬 서버는 Slave 노드 중 하나를 선택해 Master 로 승격 시킵니다. 이때 센티넬은 각각 모니터링 결과를 바탕으로 Master 의 상태를 진단하고 이를 바탕으로 일종의 다수결 투표를 실시합니다. 이 작업을 쿼럼(quorum)이라고 합니다. failover 를 실행하는 기준이 되는 quorum 값의 설정은 아주 중요합니다.
- 따라서 최소 3개 이상 홀수개의 sentinel instance 를 가지는 것이 중요합니다.

### 2. Redis Cluster

![redis-cluster-architecture.excalidraw.png](./excalidraws/redis-cluster-architecture.excalidraw.png)

- 레디스 클러스터는 센티넬과 달리 특별한 모니터링용 인스턴스를 가지지 않습니다.
- master, slave 노드는 redis gossip 프로토콜로 서로의 상태를 확인 할 수 있습니다.
- 레디스 클러스의 또 다른 특징은 `sharding` 을 지원 한다는 점입니다.
	- 샤딩은 데이터베이스를 여러 작은 단위 (샤드)로 나는 데이터베이스 다중화 방식입니다.
