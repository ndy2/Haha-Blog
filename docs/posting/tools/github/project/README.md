---
tags: [github, github-project]
title: 프로젝트를 이용한 이슈 관리 및 PR 연동 흐름
date: 2023-02-20
---
 

> [!quote] 참고 자료
> * [`Planning and tracking with Projects`](https://docs.github.com/en/issues/planning-and-tracking-with-projects) on Github Docs

### 1. 기본 화면

![[1.png]]

1. 아래의 `+ Add Item` 버튼을 통해 `📋 Backlog` 타입의 아이탬을 생성 할 수 있다.
2. 생성만 하면 `◌ Draft` 표시가 붙어있다.

### 2. Convert `project item` to `Repository Issue`

![[2.png]]

![[images/3.png]]

### 3. Convert Issue to Branch

![[images/4.png]]

![[images/5.png]]

![[images/6.png]]

### 4. Do Work!

![[images/7.png]]

### 5. Merge it

![[images/8.png]]

### 6. Close Issue

* 사진은 수동 `close`
* commit message 혹은 PR comment 로 자동으로 `close`하게 할 수도 있다.

### 7. Project 의 Item 의 상태를 Done 으로 변경

* 사진은 자동 - by github-project-automation `bot`
* 수동도 가능하다.

![[images/9.png]]
