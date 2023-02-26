---
tags: [intellij, collaborate]
title: 인텔리제이 tasks server 추가 및 활용
date: 2023-02-15
---

### 1. `Preferences -> Tools -> Tasks -> Servers`

![[images/intellij-add-tasks-server-1.png]]

---

### 2. Click X3

![[images/intellij-add-tasks-server-2.png]]

---

### 3. Open Task 실행

이슈를 통해 브랜치를 생성하고 싶은 브랜치 (보통 `dev`) 에서 아래의 방식으로 `open tasks` 를 실행하세요

`window` : ++alt+shift+n++

`mac` : ++option+shift+n++

or

![[images/intellij-add-tasks-server-3.png]]

-> `open tasks 화면`

: 연동된 issue 를 통해 새로운 브랜치 (보통 `feature`) 를 생성하고 개발을 수행하세요.

![[images/intellij-add-tasks-server-4.png]]

---

### 4. Open Task

![[images/intellij-add-tasks-server-5.png]]

branch 이름 생성 rule 을 어딘가에서 설정할 수 있은데 어딘지 모르겠습니다.

대충 `feature/#1` 으로 지어줍니다.

- `feature/#issueId` 로 피쳐 브랜치를 생성하면 좋을 것 같습니다.
- `changelist` 는 IDE 내에서 변경 이력을 모아서 관리 할 수 있도록 해주는 녀석입니다. 사용하지 않을 것이라면 체크리스트를 풀어도 좋습니다.

### 5. 개발 완료 후 커밋 과 푸시

![[images/intellij-add-tasks-server-6.png|300]]

### 6. Amend

앗 ! 초기화 하는 김에 application.properties 를 application.yml 으로 바꾸면 좋을것 같습니다. `amend` 를 해봅시다.

![[images/intellij-add-tasks-server-7.png|300]]

### 7. Git Tab 에서 브랜치와 커밋 히스토리 확인 하고..

![[images/intellij-add-tasks-server-8.png]]

### 8. 진짜 푸시

![[images/intellij-add-tasks-server-9.png]]

- 모든 변경 히스토리와 새로운 브랜치가 생성된다는 정보까지 확인가능

### 9. 이슈와 연동해 피쳐 브랜치를 따고 푸시를 완료했다!

![[images/intellij-add-tasks-server-10.png]]

### 10. PR 생성

![[images/intellij-add-tasks-server-11.png]]

![[images/intellij-add-tasks-server-12.png]]
