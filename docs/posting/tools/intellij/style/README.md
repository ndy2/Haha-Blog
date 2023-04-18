---
tags: [intellij]
title: 인텔리제이 코드 스타일/포멧팅
date: 2023-02-17
---

### 1. Formatter 적용

![[1.png]]

### 2. 파일의 마지막 줄 항상 New line 추가 하기

![[2.png]]

### 3. Check Style 추가

`rootDir/checkstyle` 에 `naver-checkstyle-rules.xml` 추가

=== "gradle.groovy"

	```groovy
	plugins {
		id 'org.springframework.boot' version '2.7.1'
		id 'java'
		id 'checkstyle' // 추가
	}
	
	  
	checkstyle {
		maxWarnings = 0 // 규칙이 어긋나는 코드가 하나라도 있을 경우 빌드 fail
		configFile = file("${rootDir}/checkstyle/naver-checkstyle-rules.xml")
		toolVersion = "10.2" 
	}
	
	configure(List.of(tasks.checkstyleMain, tasks.checkstyleTest)) {
		group = 'checkstyle'
	}
	```

#### Checkstyle Plugin 설치

![[4.png]]

### 4. Editorconfig

``` title=".editorconfig 예시"
root = true  
  
[*]  
charset = utf-8  
end_of_line = lf  
indent_size = 4  
indent_style = space  
insert_final_newline = true  
max_line_length = 120  
tab_width = 4  
  
[*.java]  
indent_style = tab  
  
[{*.yaml,*.yml}]  
indent_size = 2  
  
[*.adoc]  
indent_style = space  
indent_size = 4  
tab_width = 4  
trim_trailing_whitespace = true
```

![[images/3.png]]

### 5. Intellij Commit Option 설정

![[5.png]]