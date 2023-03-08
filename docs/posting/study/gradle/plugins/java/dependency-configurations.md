---
tags: [gradle, gradle-plugin, java]
title: gradle java plugin 이 추가하는 Gradle 의 의존성 설정에 대해 알아보자.
author: ndy2
date: 2023-03-08
description: >-
  
---
 
 
> [!quote] 참고 자료
> * [`『declaring-dependencies#what are dependency-configuration』`](https://docs.gradle.org/current/userguide/declaring_dependencies.html#sec:what-are-dependency-configurations) on gradle documentation
> * [`『Java plugin#configurations』`](https://docs.gradle.org/current/userguide/java_plugin.html#tab:configurations) on gradle documentation

### Gradle 의존성 설정

Gradle 의 모든 의존성은 특정한 scope 에 적용됩니다. 이러한 scope 는 기본적으로 이용하능한 것들도 있고 plugin 에 정의되어 있기도 하며 직접 커스텀할 수도 있습니다.

### Java Plugin 의 의존성 설정

Java plugin 에 정의되어 있는 의존성 설정 중 자주 활용되는 녀석들에 대해서 알아보겠습니다.

#### `implementation`

* Implementation only dependencies.
* This is where you declare dependencies which are purely internal and not meant to be exposed to consumers (they are still exposed to consumers at runtime).

```groovy
dependencies {
	 implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
	 implementation 'org.apache.commons:commons-lang3'
}
```

#### `compileOnly` & `annotationProcessor`

* Compile time only dependencies, not used at runtime.
	* This is where you declare dependencies which are required at compile time, but not at runtime. This typically includes dependencies which are shaded when found at runtime.
* Annotation processors used during compilation.

```groovy
dependencies {
	 compileOnly 'org.projectlombok:lombok'
	 annotationProcessor 'org.projectlombok:lombok'
}
```

#### `runtimeOnly`

* Runtime only dependencies.
	* This is where you declare dependencies which are only required at runtime, and not at compile time.

```groovy
dependencies {
	runtimeOnly 'com.h2database:h2'
}
```

#### `testImplementation`

* Implementation only dependencies for tests.
	* This is where you declare dependencies which are used to compile tests.

```groovy
dependencies {
	testImplementation('org.springframework.boot:spring-boot-starter-test') {
			exclude group: 'junit' // excluding junit 4
	}
	testImplementation 'org.springframework.security:spring-security-test'
	testImplementation 'com.github.gavlyukovskiy:p6spy-spring-boot-starter:1.8.0'
	testImplementation 'com.tngtech.archunit:archunit:0.23.1'
	testImplementation 'com.navercorp.fixturemonkey:fixture-monkey-starter:0.3.5'
}
```

#### `testCompileOnly` & `testAnnotationProcessor`

* Additional dependencies only for compiling tests, not used at runtime.
	* This is where you declare dependencies which are only required at test compile time, but should not leak into the runtime. This typically includes dependencies which are shaded when found at runtime.
* Annotation processors used during compilation on tests

```groovy
dependencies {
	 testCompileOnly 'org.projectlombok:lombok:1.18.12' 
	 testAnnotationProcessor 'org.projectlombok:lombok:1.18.12'
}
```

### Java-Library Plugin

자바 라이브러리 플러그인은 자바 플러그인을 확장한 플러그인으로서 `api` 라고 하는 추가적인 의존성 설정을 가지고 있습니다. 

* `api` - 내부 의존성을 컴파일 타임, 런타임에 모두 노출함
    * This is where you declare dependencies which are transitively exported to consumers, for compile time and runtime.
* `implementation` - 내부 의존성을 런타임에만 노출함함
