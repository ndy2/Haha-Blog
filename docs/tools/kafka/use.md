---
tags: [kafka]
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

#### case 1

```bash title="topic 생성"
./bin/kafka-topics.sh --create \
--topic quickstart-event \
--bootstrap-server \
localhost:9092 \
--partitions 1
```

#### case 2

```bash
./bin/kafka-topics.sh \
--create \ # 1. (1)
--bootstrap-server my-kafka:9092 \ # 2. (2)
--topic hello.kafka # 3. (3)
```

1. --create option 으로 토픽을 생성하는 명령이라는 것을 명시한다.
2. --bootstrap-server 에는 토픽을 생성할 카프카 클러스터를 구성하는 브로커들의 IP 와 port 를 적는다.
   여기서는 1개의 카프커 브로커만 입력한다.
3. --topic 에서 토픽 이름을 작성한다.

```text title="Result"
Created topic hello.kafka
```

#### case 3

```bash
./bin/kafka-topics.sh \
--create \
--bootstrap-server my-kafka:9092 \
--partitions 3 \ # 1. (1)
--replication-factor 1 \ # 2. (2)
--config retention.ms=172800000 \ # 3. (3)
--topic hello.kafka
```

1. `--partition` : 파티션 개수를 지정한다. 옵션을 사용하지 않으면 `config/server.properties` 의 `num.partitions` 옵션 값을 사용한다.
2. --replication-factor : 토픽의 파티션을 복제할 복제 개수를 적는다. 1 은 복제를 하지 않는다는 의미이다. 2 이면 한개의 복제본을 사용한다는 의미이다. 최소 1개 ~ 최대 카프카 클러스터의 브로커 개수 만큼 설정할 수 있다. 옵션을 지정하지 않으면 카프카 브로커 설정의 default.replication.factor 값을 사용한다.
3. --config 을 통해 kafka.topics.sh 명령에 포함되지 않은 추가적인 설정을 할 수 있다. retention 은 토픽 삭제 정책을 의미한다. 172800000ms 는 2일을 ms 단위로 나타낸 것이다. 따라서 2일이 지난 토픽의 데이터는 삭제된다.

```text title="Result"
Created topic hello.kafka
```


---

### 토픽 목록 확인

```bash title="토픽 목록 확인"
./bin/kafka-topics.sh \
--bootstrap-server localhost:9092 \
--list
```

### 토픽 상세 조회

```bash title="토픽 정보 확인"
./bin/kafka-topics.sh --describe \
--topic quickstart-events \
--bootstrap-server localhost:9092
```

### 토픽 삭제

```zsh title="토픽 삭제"
./bin/kafka-topics.sh \
--bootstrap-server localhost:9092 \
--delete --topic topic
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
--bootstrap-server my-kafka:9092 \ # 1. (1)
--topic hello.kafka \ # 2. (2)
--from-beginning # 3. (3)
```
1. `--bootstrap-server` : 카프카 클러스터 정보 (필수)
2. `--topic` : 토픽 이름 (필수)
3. `--from-beginning` : 토픽에 저장된 가장 처음 데이터 부터 출력하는 옵션

```
no1
4
5
```

---

```bash title="메시지 소비"
./bin/kafka-console-consumer.sh \
--bootstrap-server localhost:9092 \
--topic hello.kafka \
--property print.key=true \ # (1)
--property key.separator="-" \ # (2)
--group hello-group \ # (3)
--from-beginning
```

1. `print.key` : 메시지 키를 확인 하는 옵션 (default : false)
2. `key.sparator` :메시지 키/벨류의 구분자 (default : `\t`)
3. `--group` 옵션을 통해 신규 컨슈머 그룹 생성. 컨슈머 그룹을 통해 가져간 토픽의 메시지는 가져간 메시지에 대해 커밋 한다. 커밋이란 컨슈머가 특정 레코드까지 처리를 완료했다고 레코드의 오프셋 번호를 카프카 브로커에 저장하는 것이다. 커밋 정보는 __consumer_offsets 이름의 내부 토픽에 저장된다.

```
key1-no1
null-4
null-5
null-0
null-1
null-2
null-3
null-hello
null-kafka
key2-no2
key3-no3
```


### 컨슈머 그룹 목록 조회

```zsh
./bin/kafka-consumer-groups.sh \
--bootstrap-server localhost:9092 \
--list
```

```
hello-group
```

### 컨슈머 그룹이 어떤 토픽의 데이터를 가져가는지 확인

```zsh
./bin/kafka-consumber-groups.sh \
--bootstrap-server localhost:9092 \
--group hello-group \
--describe
```