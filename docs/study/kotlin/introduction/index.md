@참고 자료)

- 드미트리 제메로프, 스베트라나 이사코바 - Kotlin IN ACTION 1장
- Kotlinlang.org - [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html)
---

### 1. 코틀린 소개

![kotlin_logo.png](images/kotlin_logo.png)

**Kotlin**은 IntelliJ, Pycharm 등의 IDE 로 유명한 *JetBrains* 에서 개발한 프로그래밍 언어입니다.  코틀린은 *Better Language than Java* 를 표방하며 자바에 존재하던 많은 boilerplate 한 코드를 제거할 수 있도록 설계되었습니다.

### 2. 코틀린의 특징

#### 1. 멀티 플랫폼 지원

Kotlin Multiplatform Use cases

-   Android and iOS applications
-   Full-stack web applications
-   Multiplatform libraries

How Kotlin Multiplaform works

![kotlin-multiplatform.png](images/kotlin-multiplatform.png)

코틀린에는 `Kotlin/JVM`, `Kotlin/Native`, `Kotlin/JS`의 세가지 platform-specific 버전이 존재합니다. 

이를 통해 JVM, JS and Native 와 같은 `platform native code` 에 접근 할 수 있게 됩니다.

#### 2. 정적 타입 언어

!!! note "정적 타입 언어"

    모든 프로그램 구성 요소의 타입을 컴파일 시점에 알 수 있고 프로그램 안에서 객체의 필드나 메서드를 사용할 때마다 컴파일러가 타입을 검증하는 언어

!!! TIP "정적 타입 언어의 장점"

    성능 - 실행 시점에 어떤 메서드가 호출될 것인지 결정하는 과정 (Method Dispatch) 가 필요 없으므로 메서드 호출이 빠르다.

    신뢰성 - 컴파일러가 프로그램의 정확성을 검증하기 때문에 프로그램이 오류로 중단될 가능성이 더 적다.

    유지 보수성 - 객체 타입과 호출 메서드가 정적으로 결정되고 (dynamic dispatch 제외) 코드에 드러나기 때문에 처음 보는 코드를 이해하기 쉽다. 개인적으로 이런 기능이 지원되지 않는 python 이나 javascript 코드를 보는 것은 두렵다... 

    도구 지원 - 컴파일러가 객체와 메서드에 대한 정보를 정적으로 획득 할 수 있기 때문에 이를 바탕으로한 IDE 의 리팩토링, 코드 자동완성 기능의 지원이 좋다.

정적 타입언어는 위와같은 장점이 있지만 일반적으로 코드는 길어지고 장황해지는 단점이 있습니다. 코틀린은 컴파일러의 강력한 타입추론을 통해 이러한 문제도 상당부분 해결하였습니다. 

#### 3. 함수형 프로그래밍 + 객체지향 프로그래밍

코틀린은 자바와 달리 처음부터 함수형 프로그래밍을 지원하기 위해 설계 되었습니다. 학술적으로 이야기 하면 함수가 일급 시민 (First-Class Citizen)으로 동작 할 수 있습니다.

!!! note "일급 시민 - First-Class Citizen"

    1. 메서드의 파라미터가 될 수 있다.
    2. 메서드의 반환값이 될 수 있다.
    3. 변수에 저장할 수 있다.

자바에서도 functional interface 와 labmda 를 통해 Java8 이후 부터는 함수형 프로그래밍을 지원하였지만 아쉬운점이 몇가지 있었습니다.

- 함수... 이긴하지만 근본적으로는 일반 인터페이스으로 동작한다.
- 함수를 직접 호출할 수 없다. - method call 방식으로 호출가능

코틀린에서는 `함수 타입`의 도입으로 이런 아쉬운점을 해결하였습니다.

### 3. 코틀린의 철학

#### 1. 실용성

#### 2. 간결성

#### 3. 안정성

#### 4. 상호운용성