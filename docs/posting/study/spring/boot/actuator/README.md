---
tags: [spring, spring-boot]
title: actuator
author: ndy2
date: 2023-03-02
description: >-
  
---
 
 
> [!quote] 참고 자료
> * [`『Actuator - Production-ready Features』` on docs.spring.io](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html)
> * [스프링 부트 - 핵심 원리와 활용 by 김영한 on Inflearn](https://www.inflearn.com/course/스프링부트-핵심원리-활용/)

Spring Boot 에서는 [`spring-boot-actuator`](https://github.com/spring-projects/spring-boot/tree/v3.0.3/spring-boot-project/spring-boot-actuator) 모듈을 디펜던시에 추가하는것 만으로 애플리케이션의 모니터링/관리를 위해 필요한 다양한 정보를 제공하는 엔드포인트를 이용할 수 있습니다.

자주 사용하는 엔드포인트 목록은 다음과 같습니다.

| id              | description                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| `beans`         | 애플리케이션의 빈 목록                                                                                         |
| `conditions`    | Configuration/Auto-Configuration 단계에서 평가한 조건의 목록과 통과 여부                                       |
| `configprops`   | `@ConfigurationProperties` 목록                                                                                |
| `env`           | `ConfigurableEnvironment` 에서 얻을수 있는 모든 property 목록                                                  |
| `health`        | 애플리케이션의 health 정보                                                                                     |
| `httpexchanges` | Http exchange 정보/ HttpExchangeRepository 빈이 있어야 하고 기본적으로 최근 100개의 요청-응답 exchange 를 제공 |
| `info`          | 임의의 애플리케이션 정보 제공                                                                                                               |
| `loggers`       | 현재 애플리케이션 로거의 레벨을 보여주고 수정 할 수도 있음                                                                                                              |
| `metrics`       | 애플리케이션의 "metric" 제공                                                                                                               |
| `mappings`      | @RequestMapping 경로 보두 제공                                                                                                               |
| `threaddump`    | thread dump 수행                                                                                                               |
| `shutdown`      | graceful shutdown 수행/ 기본적으로 disabled                                                                                                               |

`shutedown` 을 제외한 모든 endpoint 는 기본적으로 ==*enabled*== 상태입니다. 또한 기본적으로는 `health` endpoint 만이 HTTP 와 JMX에 ==*exposed*== 되어있습니다.

> [!success] 엔드포인트 사용
> Endpoint 를 사용하기 위해서는 다음 두가지 과정이 모두 필요합니다.
> 1. Enable endpoint
> 2. Expose endpoint
> 
> enable 은 expose 보다 상위 기능 자체를 on/off 하는 것을 의미합니다. 따라서 endpoint 를 disable 한다는 것은 그 기능과 관련된 빈을 아예 등록하지 않는 다는 것을 의미합니다.
> 
> 이런 내용에 주의해야 엔드포인트를 의도한 대로 사용할 수 있습니다.

### 1. `health`

 
> [!quote] 참고 자료
> * [`『Actuator - Production-ready Features#actuator.endpoints.health』` on docs.spring.io](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.endpoints.health)

`health` endpoint 의 기본 동작

```
GET http://localhost:8080/actuator/health
```

```json
{"status" : "UP"}
```

`management.endpoint.health.show-details` 와 `management.endpoint.health.show-components` 프로퍼티를 통해 더 자세한 정보를 조회할 수 있다.

### 2. `info`

> [!quote] 참고 자료
> * [`『Actuator - Production-ready Features#actuator.endpoints.info』` on docs.spring.io](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.endpoints.info)

애플리케이션의 기본 정보를 노출한다.

기본 기능 - `java`, `os`, `env`, `build`, `git`
