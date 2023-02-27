---
tags: [blog, obsidian]
title: Custom Callout
author: ndy2
date: 2023-02-27
description: >-
  Obsidian에서 Custom Callout 을 만들어보자.
---
 
> [!quote] 참고 자료
> * Obsidian Documentation - [Callouts#Customize-callouts](https://help.obsidian.md/Editing+and+formatting/Callouts#Customize+callouts)
> * [How to customize Obsidian Callouts with your very own SVG icon created in Excalidraw](https://youtu.be/tSSc42tCVto)

### 1. [lucide.dev](https://lucide.dev/) 에 원하는 Icon 이 있는 경우

```css
.callout[data-callout="tweet"] {
    --callout-color: 26, 140, 216;
    --callout-icon: lucide-twitter;
}
```

> [!tweet]
> tweet ~

### 2. fontawesome.com 등 에서 원하는 Icon 의 Svg 찾기

>[!tweet] hi

> [!q] Question
> Q icon

> [!answer]
> A icon

```css
.callout[data-callout="q"] {
    --callout-color: 94, 43, 224;
    --callout-icon: 'copy svg from fontawesome.com';
}

.callout[data-callout="answer"] {
    --callout-color: 231, 225, 247;
    --callout-icon: 'copy svg from fontawesome.com';
}
```

### 3. Custom Svg with Excalidraw

좀 많이 귀찮다... 영상을 참고하자

> [!q-bubble]
> my bubble!
