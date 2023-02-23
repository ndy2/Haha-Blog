---
tags: [kafka]
title: 설치
date: 2023-02-03
---
### 1. 카프카 설치

1. 압축 파일 다운로드

- [다운로드 링크](https://kafka.apache.org/downloads)

![[images/install.png]]

2. 압축 해제

```zsh
mv kafka_2.13-3.3.2.tgz ~/Desktop/work/kafka-demo
cd ~/Desktop/work/kafka-demo
tar -xvf kafka_2.13-3.3.2.tgz
```


```zsh
╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop/work/kafka-demo
╰─$ cd kafka_2.13-3.3.2
╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop/work/kafka-demo/kafka_2.13-3.3.2
╰─$ ls
LICENSE   NOTICE    bin       config    libs      licenses  site-docs
```


### 2. Kafka Connect 설치 - MacOS

```zsh title="Kafka Connect 설치"
curl -O http://packages.confluent.io/archive/6.1/confluent-community-6.1.0.tar.gz
tar -xvf confluent-community-6.1.0.tar.gz
```
