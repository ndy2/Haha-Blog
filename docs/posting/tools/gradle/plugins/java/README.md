---
tags: [gradle, gradle-plugin, java]
title: gradle java plugin
author: ndy2
date: 2023-03-08
description: >-
  
---
 
> [!quote] 참고 자료
> * https://learn.tomgregory.com/courses/get-going-with-gradle

### Java Project Requirements

* complie Java classes from *`.java`* into *`.classes`* files
* manage resources that live alongside code
* package everything into a *jar* file
* easily run tests
* define dependencies

> [!note]
> All you have to do is add *`Gradle Java Plugin`*

```groovy
plugins {
    id 'java'
}
```

### 1. 컴파일 자바

* adds a tasks `compileJava`
    * `./gradlew compileJava`
* uses Java installation to compile *`.java`* into *`.class`* files
* output *`.class`* files to build directory

### 2. 리소스 처리

* adds a tasks `processResources`
    * ./gradlew processResources
* copies contents of resources directories into build directory

### 3. 패키징

* adds a tasks `jar`
    * ./gradlew jar
* adds compiled classes and resources to jar archive
* jar file 이름 - `<project-name>-<version>.jar`

### 4. 테스트

* adds a tasks `test`
    * ./gradlew test
* compiles test, processes resources, runs tests
* also creates a test report 

### 5. 의존성 관리

* use the dependencies section of `build.gradle`

```groovy title="build.gradle#dependencies"
dependencies {
    implementation 'org.apache.commons:commons-lang3:3.11'
}
```

### Gradle Java Project Layout

| source               | destination               |
| -------------------- | ------------------------- |
| `src/main/java`      | `build/classes/java/main` |
| `src/main/resources` | `build/resources/main` |
| `src/test/java`      | `build/classes/java/test` |
| `src/test/resources` | `build/resources/main` |

### Java Plugin Task Graph

![[1.png]]
