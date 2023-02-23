---
tags: [git]
title: git clone
date: 2023-02-02
---

### 1. 디렉토리나 file 하나만 Clone 하는 방법

- [참고 링크](https://nurilee.com/2020/05/23/github에서-sub-directory-또는-file-1개만-가져오는-방법/)

#### Script

```bash
mkdir [Directory]
cd [Directory]
git init
git config core.sparseCheckout true
git remote add -f origin [remote-url]
echo [target-path] > .git/info/sparse-checkout
git pull origin master
```

#### Example

```bash
╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop
╰─$ mkdir study-webrtc
╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop
╰─$ cd study-webrtc
╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop/study-webrtc
╰─$ git init
╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop/study-webrtc ‹master›
╰─$ git config core.sparseCheckout true
╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop/study-webrtc ‹master›
╰─$ git remote add -f origin https://github.com/eugenp/tutorials.git

Updating origin
remote: Enumerating objects: 334397, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 334397 (delta 0), reused 0 (delta 0), pack-reused 334396
Receiving objects: 100% (334397/334397), 354.31 MiB | 19.34 MiB/s, done.
Resolving deltas: 100% (95585/95585), done.
From https://github.com/eugenp/tutorials
 * [new branch]            JAVA-12714-eugen -> origin/JAVA-12714-eugen
 * [new branch]            fix_givenOneThreadIsWriting_whenAnotherThreadWritesAtSameKey_thenWaitAndGetCorrectValue -> origin/fix_givenOneThreadIsWriting_whenAnotherThreadWritesAtSameKey_thenWaitAndGetCorrectValue
 * [new branch]            master           -> origin/master

╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop/study-webrtc ‹master›
╰─$ echo "webrtc" > .git/info/sparse-checkout

╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop/study-webrtc ‹master›
╰─$ git pull origin master

From https://github.com/eugenp/tutorials
 * branch                  master     -> FETCH_HEAD
╭─deukyun@namdeug-yun-ui-Macmini ~/Desktop/study-webrtc ‹master›
╰─$ ls
webrtc
```