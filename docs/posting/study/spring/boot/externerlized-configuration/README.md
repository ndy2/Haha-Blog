---
tags: [spring, spring-boot]
title: 외부 설정값 관리
author: ndy2
date: 2023-03-01
description: >-
  스프링부트의 외부 설정값 관리 방법에 대해 알아보자.
---
 
 
> [!quote] 참고 자료
> * [스프링 부트 - 핵심 원리와 활용 by 김영한 on Inflearn](https://www.inflearn.com/course/스프링부트-핵심원리-활용/)
> * [[Server] 로컬서버, 개발서버, 스테이징서버, 운영서버 란? by ryucherry](https://velog.io/@ryucherry/Server-로컬서버-개발서버-스테이징서버-운영서버-란)

### 개요

애플리케이션을 여러 환경에서 사용해야 할 때가 있다. 대표적으로 아래와 같은 경우가 있습니다.

> [!example] 여러가지 서버 환경
> * 로컬 서버
> * 개발 서버
> * 스테이징 서버
> * 운영 서버

위 처럼 다양한 환경의 서버를 띄우기 위해서는 여러가지를 고려해야 합니다.

> [!success] DB 설정을 위해 고민해야 하는 것 예시
> 1. datasource.url 값
>     * local 환경 - `jdbc:mysql://localhost:3306/mydb`
>     * dev 환경 - `jdbc:mysql://myapp-dev:3306/mydb`
> 2. database 종류 자체
>     * local 환경 - 간단하게 `h2` db 를 사용
>     * dev 환경 - `mysql` 활용

단순히 DB 설정 하나만 하더라도 환경에 따라 여러 설정값이 변경 되어야 합니다.

이 문제를 해결하는 방법은 대부분의 문제상황에서 그러하듯이 변하는것과 변하지 않는것을 구분하는 것입니다.

* 변하는 것 - 설정
* 변하지 않는것 - 그런 설정 값들로 구성된 컴포넌트를 통해 처리하는 애플리케이션의 로직들

> [!note] 스프링 부트 외부 설정의 핵심
> ==*외부 설정*==을 통해 변하지 않는 *`빌드결과물`* 로 변하는 *`설정`* 을 제어 할 수 있도록하자.

전통적인 자바진영에서 외부 설정을 활용하던 네가지 방식과 스프링 부트가 어떻게 이들을 통합했는지에 대해서 알아보겠습니다.