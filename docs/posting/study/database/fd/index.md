---
tags: [database]
title: Functional Dependency
author: ndy2
---

> [!quote] 참고 자료
> * 쉬운코드 - [DB에서 functional dependency(FD : 함수 종속)을 설명합니다! 고고씽!!](https://youtu.be/fw8hvolebLw)

### 1. Functional Dependency 란?

- 한 테이블에 있는 두 개의 `attributes set` 사이의 `constraint`
- 집합 X 의 값에 따라 집합 Y 의 값이 유일하게 결정된때
  'X 가 Y 를 함수적으로 결정한다. Y 가 X 에 함수적으로 의존한다' 라고 부르며 두 집합 사이의 이러한 제약 관계를 Functional Dependency (FD) 라고 부른다.

![[excalidraws/fd.excalidraw.png]]

`X = {empl_id}` :material-arrow-right: `Y = {empl_name, birt_date, position, salary}`

empl_id 값에 따라 나머지 모든 필드의 값은 의미적으로 unique 하게 결정된다.

### 2. FD 주의 사항
- 테이블의 특정 순간, 상태가 아니라 **의미적으로 파악**해야 한다.
- player
| ^^id^^ | name  | team_id | backnumber |
| ------ | ----- | ------- | ---------- |
| 1      | messi | 2       | 10         |
| 2      | sonny | 105     | 7          |
| 3       | ronaldo  | null   | null  |

`{name}` :material-arrow-right: `{team_id}` 처럼 보이지만 id 3번과 동명이인인 브라질의 Ronaldo 선수는 team_id 값이 있을 수 있다!


### 3. FD 예시

- `{std_id}` :material-arrow-right:  `{stu_name, birth_date, addr}`
- `{class_id}` :material-arrow-right: `{class_name, year, semester, credit}`
- `{stu_id, class_id}` :material-arrow-right:  `{grde}`
- `{bank_name, bank_account}` :material-arrow-right: `{balance, open_date}`


### 4.  FD 의 종류

#### 0. {} ->Y
항상 Y 의 값이 일정하다면 공집합 즉, 아무 attribute 없이도 Y 값을 결정할 수 있고 이러한 FD 를 `{}` :material-arrow-right: `Y` 처럼 표현 할 수 있다.

#### 1. Trivial FD, Non-trivial FD
Y 가 X 의 subset 이라면 당연히 `X` :material-arrow-right: `Y` 가 성립하고 이런 FD 를 trivial FD 라 부른다.
그렇지 않은 FD 는 non-trivial FD 라 부른다.

### 2. Partial FD, Full FD
X 의 proper subset 으로도 FD 가 성립하면 partial FD 라 부르고 그렇지 않다면 full FD 라 부른다.



