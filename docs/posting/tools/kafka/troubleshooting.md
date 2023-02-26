---
tags: [kafka, troubleshooting]
title: 문제 해결
date: 2023-02-03
---

### 토픽 생성, 목록 조회 커맨드 실습 시 타임 아웃

`server.properties` 에 아래 라인 추가

 -> `listeners=PLAINTEXT://localhost:9092`

### 카프카 시작 안되는 경우

```
cd /tmp/kafka-logs
rm -rf *
```
