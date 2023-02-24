---
tags: [blog, obsidian]
title: File hide with snippet
author: ndy2
date: 2023-02-24
---
 
> [!tip]
> 평소에 보기 싫은 파일을 File Explore View 에서 숨겨보자!

### 1. plugin file-hider

<div class="rich-link-card-container"><a class="rich-link-card" href="https://github.com/Oliver-Akins/file-hider" target="_blank">
	<div class="rich-link-image-container">
		<div class="rich-link-image" style="background-image: url('https://opengraph.githubassets.com/d7fe57145d5a29a16c989ce70e807ca4ac6dbf351af78dd1a9e25f743a053d88/Oliver-Akins/file-hider')">
	</div>
	</div>
	<div class="rich-link-card-text">
		<h1 class="rich-link-card-title">GitHub - Oliver-Akins/file-hider: A plugin for https://obsidian.md that allows hiding specific files and folders from the file explorer.</h1>
		<p class="rich-link-card-description">
		A plugin for https://obsidian.md that allows hiding specific files and folders from the file explorer. - GitHub - Oliver-Akins/file-hider: A plugin for https://obsidian.md that allows hiding specif...
		</p>
		<p class="rich-link-href">
		https://github.com/Oliver-Akins/file-hider
		</p>
	</div>
</a></div>

관련 `plugin` 이 존재한다. 하지만 설치하고 적용해 보니 파일이 많아지는 경우 `file explore` 화면이 깨지는 문제가 있었다.

### 2. `.obsidian/snippets` 활용

<div class="rich-link-card-container"><a class="rich-link-card" href="https://www.reddit.com/r/ObsidianMD/comments/wlltgh/hide_folders_in_my_vault/" target="_blank">
	<div class="rich-link-image-container">
		<div class="rich-link-image" style="background-image: url('')">
	</div>
	</div>
	<div class="rich-link-card-text">
		<h1 class="rich-link-card-title">r/ObsidianMD - Hide folders in my vault</h1>
		<p class="rich-link-card-description">
		4 votes and 10 comments so far on Reddit
		</p>
		<p class="rich-link-href">
		https://www.reddit.com/r/ObsidianMD/comments/wlltgh/hide_folders_in_my_vault/
		</p>
	</div>
</a></div>

![[file-hide.png|Settings -> Appearance -> CSS Snippets]]

CSS snippets 를 직접 넣어주어 원하는 폴더/파일을 숨길 수 있다.

```css
div[data-path='resources'], div[data-path='resources'] + div.nav-folder-children {display: none;}
div[data-path='docs/archive'], div[data-path='docs/archive'] + div.nav-folder-children {display: none;}
div[data-path='docs/assets'], div[data-path='docs/assets'] + div.nav-folder-children {display: none;}
div[data-path='LICENSE'] {display: none;}
```

평소에는 잘 보지 않는 폴더 세가지와 라이센스 파일 하나를 기본 화면에서 제거하였다.

![[images/after.png|깔끔한 file explorer 화면!]]
