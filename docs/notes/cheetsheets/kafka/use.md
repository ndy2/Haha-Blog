---
title: 사용
date: 2023-02-03
---

### Zookeeper 및 Kafka 서버 구동

```bash title="zookeeper 서버 구동"
./bin/zookeeper-server-start.sh ./config/zookeeper.properties
```

```bash title="kafka 서버 구동"
./bin/kafka-server-start.sh ./config/server.properties
```

### 토픽 생성

```bash title = "topic 생성"
./bin/kafka-topics.sh --create \
--topic quickstart-event \
--bootstrap-server \
localhost:9092 \
--partitions 1
```

### 토픽 목록 확인

```bash title="토픽 목록 확인"
./bin/kafka-topics.sh \
--bootstrap-server localhost:9092 --list
```

### 토픽 정보 확인

```bash title="토픽 정보 확인"
./bin/kafka-topics.sh --describe \
--topic quickstart-events \
--bootstrap-server localhost:9092
```


### 메시지 생산

```bash title="메시지 생산"
./bin/kafka-console-producer.sh \
--broker-list localhost:9092 \
--topic quickstart-events
```


### 메시지 소비
```bash title="메시지 소비"
./bin/kafka-console-consumer.sh \
--bootstrap-server localhost:9092 \
--topic quickstart-events \
--from-beginning
```