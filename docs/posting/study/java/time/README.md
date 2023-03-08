---
tags: [java, java.time]
title: Date-Time Overview
author: ndy2
date: 2023-03-07
description: >-
  
---
 
 
> [!quote] 참고 자료
> * [Date-Time Overview](https://docs.oracle.com/javase/tutorial/datetime/overview/index.html) on Oracle Tutorials

### 1. Date-Time 패키지

![[docs/posting/study/java/time/images/1.png|400]]

- `java.time`
	- ISO-8601 를 따르는 달력 시스템을 표현하는 클래스들
	- 불변, 쓰레드 안전 하다.
- `java.time.chrono`
	- `chrono` 는 그리스어로 시간(time) 이라고한다.
	- defulat 시스템인 `ISO-8601`를 따르지 않는 달력 시스템을 표현하는 클래스들의 패키지이다.
- `java.time.format`
	- 일/시를 포맷팅 하는데 사용하는 클래스들
- `java.time.temporal`
	- 일/시 클래스 간의 상호운용(interoperations)을 가능하게 해주는 클래스들
	- 보통 framework 나 library 개발자 들이 사용한다.
	- Fields (TemporalField and ChronoField) 와 units (TemporalUnit and ChronoUnit) 가 이 패키지에 속한다.
- `java.time.zone`
	- time zone 을 위해 필요한 클래스들

### 2. DayOfWeek 이넘

```java title="월요일을 출력해보자"
import java.time.DayOfWeek  
import java.time.format.TextStyle  
import java.util.*  
  
fun main() {  
    val locale = Locale.getDefault()  
    println(locale) // "ko_KR"  
  
    val monday = DayOfWeek.MONDAY  
    println(monday.getDisplayName(TextStyle.FULL, locale)) // "월요일" // "Monday"  
    println(monday.getDisplayName(TextStyle.SHORT, locale)) // "월"   // "Mon"  
    println(monday.getDisplayName(TextStyle.NARROW, locale)) // "월"  // "M"  
}
```


### 3. Month 이넘

```java
import java.time.Month  
import java.time.format.TextStyle  
import java.util.*  
  
fun main() {  
    val locale = Locale.getDefault()  
    println(locale) // "ko_KR"  
  
    val april = Month.APRIL  
    println(april.getDisplayName(TextStyle.FULL, locale)) // "월요일" // "April"  
    println(april.getDisplayName(TextStyle.SHORT, locale)) // "월"   // "Apr"  
    println(april.getDisplayName(TextStyle.NARROW, locale)) // "월"  // "A"  
}
```

한글에서는 `TextStyle` 에 따른 차이가 별로 없다.


### 4. 날짜를 다루는 클래스들

`LocalDate`, `YearMonth`, `MonthDay`, and `Year`.

#### 1. LocalDate

LocalDate 클래스는 ISO 표준에 따라 연/월/일 을 표현하는 클래스입니다. `of`/`with` 팩토리 메서드를 통해 LocalDate 인스턴스를 생성할 수 있습니다.

```java
LocalDate date = LocalDate.of(2000, Month.NOVEMBER, 20); // (1)!
LocalDate nextWed = date.with(TemporalAdjusters.next(DayOfWeek.WEDNESDAY)); // (2)!
```

1. 2000년 11월 20일
2. 2000년 11월 20일 이후 첫 수요일인 날짜의 `LocalDate`


#### 2. YearMonth

- 연/월을 표현하는 클래스

```java
import java.time.YearMonth  
  
fun main() {  
    val yearmonth = YearMonth.now()
    print("$yearmonth 은 ${yearmonth.lengthOfMonth()} 일 까지 있습니다.")
    // "2023-03 은 31 일 까지 있습니다."
}
```



#### 3. MonthDay

- 월/일을 표현하는 클래스

```java
import java.time.Month  
import java.time.MonthDay  
  
  
fun main() {  
    val monthDay = MonthDay.of(Month.FEBRUARY, 29) //  
    print(monthDay.isValidYear(2023)) // "false" - 2010 년은 윤년이 아니라 2/29 가 없음  
}
```

```java title="MonthDay.isValidYear"
public boolean isValidYear(int year) {  
    return (day == 29 && month == 2 && Year.isLeap(year) == false) == false;  
}
```

#### 4. Year

- 년도를 표현하는 클래스


