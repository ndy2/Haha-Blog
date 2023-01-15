@ 참고 자료)

- 쉬운코드 - [DBCP (DB connection pool)의 개념부터 설정 방법](https://youtu.be/zowzVqx3MQ4)
- 쓰레드의 커넥션 조회, 반납 시나리오 - [링크](https://jaehun2841.github.io/2020/01/27/2020-01-27-hikaricp-maximum-pool-size-tuning/#Hikari%EB%8B%98-Connection-하나만-주세여)
	- 아주 재미있습니다.
- Naver D2 - [Commons DBCP 이해하기](https://d2.naver.com/helloworld/5102792)


- {==SpringBoot Application==}
- SpringBoot 의 기본 DBCP 로 사용되는 {==HikariCP==}
- {==Mysql==} 

을 사용하여 DBCP 를 설정하는 방식을 알아보겠습니다.

---
### 1. DBCP의 개념과 원리

![dbcp-con.excalidraw](excalidraws/dbcp-con.excalidraw.png)

-  매번 connection 을 열고 닫는 시간적인 비용이 발생합니다.
- 서비스 성능에 좋지 않습니다.

**DBCP** - Database Connection Pool

 => {==미리 커넥션을 만들어두고 Pool 처럼 관리하자! ==}
- 요청의 시작 전에 TCP 연결을 수립하고 해지 하지 않고 Pool 에서 커넥션을 조회하고 반납하자!

### 2. MySql

#### 1. `max_connections`
- client 와 맺을 수 있는 최대 connection 수 (default = 100)
![dbcp-max_connections.png](images/dbcp-max_connections.png)
- mysql 의 max_connections 값이 4로 설정된 경우

- 이런 상황에서 새로운 애플리케이션을 추가하거나 `HikariCP` 의 커넥션 개수를 늘리려고 해도 동작하지 않습니다. 이럴 때는 MySQL의 max_connections 값을 늘려주어야 합니다.

- 초과 분에 대해서는 `Too Many Connections` 에러가 발생합니다.
- 설정 및 확인 방법 - [링크](https://zetawiki.com/wiki/MySQL_max_connections_설정)


#### 2. MySQL - `wait_timeout`
- connection 이 idle (inactive) 할 때 다시 요청이 오기까지 얼마의 시간을 기다린 뒤에 close 할 것인지 결정하는 값 (default - 8 시간 (28800 초))
- 한 쓰레드가 커넥션 풀에서 커넥션을 가져가서 사용하지도 않고 반환하지도 않는 경우 리소스 점유의 문제가 있습니다. 이 문제를 해결하기  MySQL 은 마지막 사용(요청) 시간을 기준으로 wait_timeout 시간이 초과된다면 connection 을 종료합니다.

- 참고 링크
	- [mysql 의 wait_timeout의 의미](https://knight76.tistory.com/entry/30031445050)
		- wait_timeout 이 가장 중요하지만 mysql 의 다른 여러 timeout 과 관련된 설정들,
		- wait_timeout 설정 꿀팁 
	- 에 대한 글입니다.


### 3. HikariCP 설정

#### 1. `minimumIdle`
- Connection Pool 에서 유지하는 최소한의 idle connection 의 개수
- default - `maximumPoolSize` 와 같은 값을 가진다.
- 권장사항
	- 따로 건드리지 말고 maximumPoolSize 와 동일한 값을 써라
	- 이러면 Connection 의 개수가 고정이기 때문에 애플리케이션이 떠 있는 동안 커넥션이 생성되고 종료되지 않는다.

#### 2.  `maximumPoolSize`
- pool 이 가질 수 있는 최대 connection 수
- default - 10
- idle 과 active (in-use) 커넥션의 합

!!! note

    `maximumPoolSize` 가 `minimumIdle` 보다 우선 순위를 가집니다!
    `maximumPoolSize` = 4, `minimumIdle` = 2 인 설정으로 HikraiCP 를 시작하면
    
    minimumIdle 을 만족하기 위해 먼저 두개의 커넥션을 생성합니다.
    이 상태에서 하나의 요청이 와서 커넥션 하나가 `IN-USE` 상태가 된다면 minmumIdle 설정에 따라 Connection 이 하나 추가되고 idle connection 의 최솟값을 2로 유지할 수 있습니다.
    
    하지만 이 상태에서 추가적인 요청이 두개가 더 온다면 minimumIdle을 준수하기 위해 Connection을 두개 더 추가했다가는 maximumPoolSize 가 께지게 됩니다. HikariCP는 이 때 maximumPoolSize 설정이 minimuIdle 설정에 우선해서 동작하도록 합니다.
    
    참고 링크 - 쉬운코드님 영상 14:41

#### 3. `maxLifetime`

- pool 에서 connection의 최대 수명
- maxLifetime 을 넘기면 idle 인 경우 pool 에서 바로 제거 active 인 경우 pool로 반환된 후 제거
- db 의 connection timeout 보다 몇 초 짧게 설정해야한다.

#### 4. `connectionTimeout`

- poll 에서 connection을 받기 위한 대기 시간
- default - 30 초
