---
tags: [blogging, mkdocs, obsidian]
title: 들어가기
date: 2022-12-14
---


이 블로그를 이루는 큰 툴 두가지는 ==obsidian== + ==mkdocs-material== 로 동작합니다.

조금 사용해보니 두가지 모두 매력적인 도구이지만 아직 한국에서는 잘 활용되지 않는 것 같습니다.

obsidian 으로 문서를 관리하고 mkdocs 를 사용해서 블로그 사이트를 구성한 방법과 간단한 팁들에 대해서 공유하면 좋겠다는 생각이 들었습니다.


---

### what is Obsidian - [obsidian.md](https://obsidian.md/)
- obsidian 은 마크다운파일을 관리하는 애플리케이션입니다.
- git 과의 연동, excalidraw 등 다양한 플러그인을 제공하고 입맛에 맞추어 사용가능합니다.
- obsidian 은 `vault` 라는 단위를 IDE 에서의 project 처럼 활용합니다.
- `vault` 의 root directory 에는 `.obsidian` 이라고 하는 숨김폴더가 하나 생기는데 여기에
	- plugin
	- hotkeys
- 등 vault 에 대한 다양한 정보가 관리됩니다.
- obsidian 은 공식적으로 [여기](https://help.obsidian.md/Advanced+topics/Accepted+file+formats) 표기 되어있는 파일만 지원합니다.

```
obsidian 의 장점은 강력한 plugin 들 입니다. 추후에 하나씩 소개하겠습니다.
```

### what is mkdocs - [mkdocs.org](https://www.mkdocs.org/)

- mkdocs 는 마크다운파일을 읽어 정적인 웹 사이트를 구성해 주는 오픈소스 프로젝트입니다.
- mkdocs 는 mkdocs.yml 파일을 이용해 테마, 마크다운 확장, 플러그인 등 다양한 기능을 제공합니다.
- mkdocs 가 만들어 내는 화면의 기본 틀을 테마 (thema) 라고 합니다. 
	- mkdocs 의 다양한 테마는 [여기](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes) 에서 확인 할 수 있습니다.

### [obsidian-publish-mkdocs](https://github.com/jobindjohn/obsidian-publish-mkdocs)

- mkdocs 는 파이썬 기반의 프로젝트로 pip install 을 통해 설치할 수 있습니다. 하지만 이것을 직접하는 것은 쉽지 않을 수 있습니다.
- obsidian-publish-mkdocs 는 자신의 githubio 에  `mkdocs` 를 publish 하는 ci 를 포함하고 있는 `template` 입니다. 위 링크의 README 를 읽으시면 그림에 나오는 것처럼 생긴 자신만의 githubio 사이트가 뚝딱 publish 됩니다!
- 이 템플릿 프로젝트는 기본적으로  [`Material` 테마](https://github.com/squidfunk/mkdocs-material)를 선택했습니다.

이제 mkdocs.yml 을 수정해 보며 만지작 거리며 자신의 블로그의 설정을 변경해봅시다.

[Material 테마의 웹사이트](https://squidfunk.github.io/mkdocs-material)와 이를 구축한 [깃헙 사이트](https://github.com/squidfunk/mkdocs-material)를 비교해보면 빠르게 그 동작 방식을 익힐 수 있습니다.

![[../../assets/my-profile.jpeg|렛츠 고!]]