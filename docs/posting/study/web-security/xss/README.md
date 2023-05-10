---
tags: [web, security]
title: 크로스 사이트 스크립팅, XSS
author: ndy2
date: 2023-05-10
description: >-
  
---
 
> [!quote] 참고 자료
>  - [`『[10분 테코톡] 🔧알트의 XSS』`](https://youtu.be/bSGqBoZd8WM)

### 1. XSS 란?

- 가장 널리 알려진 웹 보안 취약점 중 하나.
- 악의적인 사용자가 공격하려는 사이트에 악성 스크립트를 삽입할 수 있는 보안 취약점

### 2. Stored XSS

1. 악의적인 스크립트가 포함된 내용이 데이터베이스에 저장됨
2. 피해자가 해당 스크립트가 출력되는 페이지에 접속하면 스크립트가 실행된다.

### 3. Reflected XSS

1. 해커가 악의적인 스크립트를 URL 에 담아 공유
2. 피해자가 해당 URL 을 클릭하면 스크립트가 실행된다.

### 4. DOM Based XSS

### 2. XSS 보호

- input 이 무조건 plain text 로 읽히도록 한다.
- 모던 웹 브라우저 및 프레임워크 에서는 기본적으로 적용됨
