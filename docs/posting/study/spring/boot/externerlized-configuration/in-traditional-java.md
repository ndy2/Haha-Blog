---
tags: []
title: 전통적인 자바의 외부 설정 처리 방식
author: ndy2
date: 2023-03-01
description: >-
  
---
 
> [!quote] 참고 자료
> [스프링 부트 - 핵심 원리와 활용 by 김영한 on Inflearn](https://www.inflearn.com/course/스프링부트-핵심원리-활용/)

### 1. 외부 설정을 읽는 네가지 방법

> [!quote] 
> 외부 설정은 일반적으로 다음 4가지 방법이 있다.
> * OS 환경 변수 - OS 의 모든 프로세스에서 사용
> * 자바 시스템 속성 - 해당 JVM 안에서 사용 
> * 자바 커맨드 라인 아규먼트 - main(args) 를 통해 전달
> * 외부 파일 - 직접 읽어 서 사용

### 2. OS 환경 변수

**모든 환경변수 출력**

=== "Window"

    ```bash
    C:\Users\1>set
    ALLUSERSPROFILE=C:\ProgramData
    APPDATA=C:\Users\1\AppData\Roaming
    CommonProgramFiles=C:\Program Files\Common Files
    ...
    ```

=== "Mac"

    ```
    printenv
    ...
    ```

**자바에서 조회**

```java
Map<String,String> envMap = System.getEnv(); // (1)!
String dbUrl = Syste.getenv("db_url") // (2)!
```

1. 전체 환경변수 조회
2. db_url 값 조회

### 3. 자바 시스템 속성

자바 시스템 속성<sup>Java System Properties</sup> 은 실행가능한 JVM 안에서 접근 가능한 외부 설정이다.

```bash
java -Ddb_url=jdbc:mysql://localhost:3306 -jar app.jar
```

* `-D` VM 옵션을 통해 key=value 형식을 주면 된다.
* `-D` 는 -jar 보다 앞에 와야한다.

`자바에서 조회`

```java
import java.util.Properties

Properties properties = System.getProperties(); // (1)!
String dbUrl = System.getProperties("db_url")
```

1. `Properties` 는 `HashMap<Object,Object>` 의 하위 타입이다.

### 4. Command line Arguments

```bash
java -jar app.jar args1 args2
```

```java
public static void main(String[] args){

    System.out.println(args[0]); // "args1"
    System.out.println(args[1]); // "args2"
}
```


