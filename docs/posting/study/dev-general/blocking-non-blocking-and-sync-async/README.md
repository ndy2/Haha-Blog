---
tags: [blocking-non-blocking, sync-async]
title: 블로킹/논블로킹 그리고 동기/비동기
author: ndy2
date: 2023-04-24
description: >-
  
---

 
> [!quote] 참고 자료
> * haha

### 0. 들어가며

블로킹/ 논블로킹 그리고 동기/ 비동기는 참 미묘하면서 헷갈리는 개념이다. 몇번 정리했고 비교적 최근에 aync/non-blocking 을 지원하는 spring-web-flux에 관한 udemy 강의도 수강했고 예전에 한 블로그의 커피 판매 예제로 잘 정리했었는데도 막상 설명하려고 하면 볼때마다 새롭고 머리가 하얘지는 느낌을 받는다.

실제 사용케이스와 함께 남에게 설명할 수 있을 정도로 정리해보자.

### 1. Blocking 과 Non-Blocking

> [!note]
> `Blocking` 과 `Non-Blocking` 은 ==제어권==

- Blocking
    - caller 가 callee를 호출하고 제어권을 넘긴다.
    - 즉 callee 가 자신의 처리를 마치고 caller 에게 응답과 함께 제어권을 넘길 때 까지 block 된다.
    - 응답과 제어권을 처리하는 방법에는 두가지가 있다.
        - 1. 동기적으로 응답을 넘겨받고 caller 가 이후 처리
        - 2. 비동기 적으로 호출시 넘긴 callback에 따라 처리
- Non-Blocking
    - caller 가 callee 를 호출하고도 자신의 제어권을 유지한다.
    - callee의 응답이 필요하다면 두가지 방법이 있다.
        - 1. 동기적으로 계속해서 callee 에게 응답을 요구
        - 2. 호출시 callback을 넘기는 비동기적 방식 사용.

### 2. Sync 와 Async

> [!note]
> `sync` 와 `async`의 핵심은 ==callback==

-   `호출된 함수`의 수행 결과 및 종료를 `호출한 함수`가(`호출된 함수`뿐 아니라 `호출한 함수`도 함께) 신경 쓰면 Synchronous
-   `호출된 함수`의 수행 결과 및 종료를 `호출된 함수` 혼자 직접 신경 쓰고 처리한다면(as a callback fn.) Asynchronous


### 3. Spring 과 블로킹/논블로킹, 동기/비동기

역시 개발자는 코드로 이야기하는것이 편하다. 심지어 순수 자바를 이용하는것에 비해 요즘은 세상이 좋아서 훨씬 적은 배경지식으로 오늘의 주제 같은 복잡한 내용도 직접 작성해 볼 수 있으니 좋은 세상이다.
