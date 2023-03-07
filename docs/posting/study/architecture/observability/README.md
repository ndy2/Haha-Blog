---
tags: [architecture, observability]
title: Observability
author: ndy2
date: 2023-03-07
description: >-
  
---
 
 
> [!quote] 참고 자료
> * [**Observability** in Distributed Systems](https://www.baeldung.com/distributed-systems-observability) on Baeldung by Kumar Chandrakant

### 1. Observability 란?

> [!quote] [관측 가능성](https://ko.wikipedia.org/wiki/관측_가능성) on Wikipedia
>  제어이론에서 **관측 가능성(observability)**이란 시스템의 **출력 변수(output variable)**를 사용하여 **상태 변수(state variable)**에 대한 정보를 알아낼 수 있는지를 나타내는 용어이다. 시스템의 출력 변수를 사용하여 특정 상태 변수에 대한 정보를 알아낼 수 있을 때 그 상태 변수는 **관측 가능하다(observable)**고 하며, 시스템의 모든 상태 변수가 관측 가능할 때 그 시스템은 관측 가능하다고 한다.

알고 싶은 **Observability** 의 정의는 *제어이론* 이 아니라 소프트웨어 공학/컴퓨터 공학 문야 에서의 Observability 입니다. 다시 검색해보겠습니다.

![[docs/posting/study/architecture/observability/images/1.png|Google Observability 뜻 검색 결과|400]]

구글에 검색하여 포스팅/기사의 요약본을 살펴보면 ==2018년 쯤 등장한 모니터링의 새로운 유행어== 정도되는것 같습니다. 하지만 소프트웨어 분야의 새로운 유행어가 등장할때에는 (e.g. `OOP -> DDD`, `fail tolerant pattern -> resilient pattern` ) 항상 기존의 것을 포함하면서도 확장하며 자기만이 내세우는 어떤 중요한 특징이 있다고 생각합니다. 

### 2. Def @ Baeldung

Observability is **the ability to measure the internal state of a system only by its external outputs**.

![[observability-baeldung.excalidraw.png|What is Observability?]]

`Observability` 를 구성하는 세가지 축

1. Logs - 로그

     * 로그는 애플리케이션이 코드를 실행하며 남기는 텍스트이다. 일반적으로 구조화되있고 severity 를 나누어 관리된다(Trace, Debug, Info, Warnning, Error 등).
     * 보통 만들기 쉽지만 성능의 문제를 야기할 수 있다.
     * 또한 로그를 쉽게 모으고 효율적으로 분석하기 위해 `Logstash` 와 같은 추가적인 툴이 필요할 수도 있다.
     * 관련 표준/툴 - Elastic Stack (a.k.a. Elasticsearch, Logstash, and Kibana; ELK)

2. Metrics - 메트릭

    * Metric 은 일정 시간 단위 동안 수집된 애플리케이션의 지표 (카운트, 게이지)이다.
    * e.g.) 초당 메모리 소모량
    * 관련 표준/툴 - OpenCensus, Prometheus

3. Traces - (분산) 추적

    * 분산 시스템에서 Traces 란 여러 분산 애플리케이션간의 요청/응답 및 이벤트의 처리 흐름을 의미한다. 
    * 이를 통해 시스템의 문제점을 빠르게 진단할 수 있다.
    * 관련 표준/툴 - OpenTracing, Jaeger, Sleuth, Zipkin

### 3. `Observability` Vs. Monitoring

Observability

* 관측 가능성
* 관측 (모니터링) 할 수 있는 능력 (Ability)

Monitering

* 모니터링
* 모니터링 (관측) 하는 행위
