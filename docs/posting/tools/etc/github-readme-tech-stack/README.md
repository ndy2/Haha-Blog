---
tags: [github, readme-tech-stack]
title: 테크 스텍 아이콘 생성 툴
author: ndy2
date: 2023-04-18
description: >-
  
---

### 1. 프로젝트

```preview
https://github.com/0l1v3rr/github-readme-tech-stack
https://0l1v3rr.github.io/github-readme-tech-stack/
```

### 2. 사용법

이 블로그를 만드는데 사용한 Stack인 `Obsidian`, `MkDocs-Material`, `Python` , `GitHub Pages` 를 뱃지 아이콘으로 만들어보자!

#### 1. 아이콘 추가

![[1.png|가이드를 따라 라인별로 원하는 아이콘을 추가]]


#### 2. 생성!

![[2.png|생성된 이미지 링크]]

마크다운 임베드도 잘 된다!

![My Tech Stack](https://github-readme-tech-stack.vercel.app/api/cards?title=My%20Blog%20is%20Made%20With&lineCount=2&line1=Obsidian,Obsidian,483699;&line2=GithubPages,GitHub%20Pages,222222;Python,Python,3776AB;)

아주 흥미롭다.

하지만 이 블로그의 핵심인 MkDocs-Material 의 아이콘은 [simpleicons.org](https://simpleicons.org/) 에서 제공하지 않아 기본적인 활용법으로는 사용할 수 없다. 하지만 해당프로젝트는 무려  Base64 포멧 인코딩으로 SVG 이미지를 URL 전달하는 미친 아이디어를 통해 커스텀 SVG 로고를 추가하는 방법 또한 제공한다.

[가이드](https://github.com/0l1v3rr/github-readme-tech-stack#-adding-custom-svg-logo) 를 따라 MkDocs-Material의 아이콘을 추가해보자!

![My Blog Tech Stack](https://github-readme-tech-stack.vercel.app/api/cards?title=My%20Blog%20is%20Made%20With&lineCount=2&line1=Obsidian,Obsidian,483699;data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4OSA4OSI%2BICA8cGF0aCBkPSJNMy4xMzYsMTcuMzg3bDAsNDIuOTMybDQyLjkzMiwyMS40NjdsLTQyLjkzMiwtNjQuMzk5WiIgLz4gIDxwYXRoIGQ9Ik0yMS45MSw4bDQyLjkzMyw2NC4zOThsLTE4Ljc3NSw5LjM4OGwtNDIuOTMyLC02NC4zOTlsMTguNzc0LC05LjM4N1oiIHN0eWxlPSJmaWxsLW9wYWNpdHk6IDAuNSIgLz4gIDxwYXRoIGQ9Ik02Ny41MzUsMTcuMzg3bC0yNy4yNjIsMTguMTU2bDIxLjg3OCwzMi44MThsNS4zODQsMi42OTFsMCwtNTMuNjY1WiIgLz4gIDxwYXRoIGQ9Ik02Ny41MzUsMTcuMzg3bDAsNTMuNjY2bDE4Ljc3NCwtOS4zODhsMCwtNTMuNjY1bC0xOC43NzQsOS4zODdaIiBzdHlsZT0iZmlsbC1vcGFjaXR5OiAwLjI1IiAvPjwvc3ZnPg%3D%3D,MkDocs_Material,2D79C7;&line2=GithubPages,GitHub%20Pages,222222;Python,Python,3776AB;)

Wow 아주 아름답다. 앞으로 널리 활용해보아야 겠다.