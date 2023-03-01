---
tags: [spring, boot]
title: 스프링의 외부 설정 추상화
author: ndy2
date: 2023-03-01
description: >-
  
---
 
> [!quote] 참고 자료
> [스프링 부트 - 핵심 원리와 활용 by 김영한 on Inflearn](https://www.inflearn.com/course/스프링부트-핵심원리-활용/)

### 1. Comman line Option Arguments

* `Command line argument` 를 `key=value` 형식으로 활용하기 위한 Spring 만의 표준

```bash
java -jar app.jar --username=sa --password=
```

```java
import org.springframework.boot.ApplicationArguments
import org.springframework.boot.DefaultApplicationArguments

public static void main(String[] args) {

    ApplicationArguments appArgs 
    = new DefaultApplicationArguments(args); 
    // "--key=value" 형식으로 주어진 커맨드라인 인자를 파싱해서 처리 할 수 있게 해주는 스프링의 클래스
}

```

스프링은 초기화시 `DefaultApplicationArguments` 를 빈으로 등록한다.

### 2. 스프링 통합

개발자의 입장에서 모두 `key=value` 형식의 설정일 뿐인데 외부 설정의 종류에 따라 조회하는 방식이 다르다.

스프링은 이 문제를 `Enviroment` 와 `PropertySource` 라는 추상화를 통해 해결한다. `Enviroment` 는 여러 PropertySource 를 포함하는 파사드이다. `Enviroment` 역시 초기화 단계에서 빈으로 등록된다.

![[enviroment.excalidraw.png]]
