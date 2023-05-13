---
tags: [review, architecture, ddd, eric-evans]
title: [DDD Europe 2019] 에릭 에반스 - What is DDD
author: ndy2
date: 2023-05-13
description: >-
  
---
 
> [!quote] 참고 자료
> * Domain-Driven-Design Europe - [`『What is DDD - Eric Evans - DDD Europe 2019』`](https://youtu.be/pMuiVlnGqjk) on Youtube

### 0. 들어가며

`도메인 주도 설계`의 최고 권위자 이자 창시자인 에릭 에반스의 발표를 요약, 정리해보자. 

![[ddd-book.png|에릭 에반스 - 도메인 주도 설계 DDD 의 바이블 같은 책이다.]]

발표는 예시와 함께 진행된다. 자신이 해양 운송 회사 (shipping company)에서 컨테이너, 운송, 정박 등을 관리하는 소프트웨어를 작성하는 개발자라고 생각하자.

![[ship-container.png|해양 운송 - 왜인지 도커가 생각난다.]]

### 1. 첫번째 Use-Case

> 고객 : "제 컨테이너 하나를 홍콩에서 텍사스 달라스로 보내고 싶어요."
> 점원 : "오케이 알겠어요. 잠시만 기다려 주세요~" (프로그램 사용)
> 점원 : "넵. 당신의 컨테이너는 `선박 ABC 호`에 실릴것이고 `N월 M일`에 텍사스의 Tx 로 `기차 XYZ호` 를 타고 이동할것입니다~"
> 고객 : "감사합니다~"

아래와 같은 레거시 시스템이 있다고 생각해보자.

![[legacy.excalidraw.png]]

위 구조의 장점은 굉장히 단순하다는것이다. 하지만 너무 단순하고 유연하지않다.

> [!question] What kind of concept we are missing?
> Creative collaboration of software experts and domain experts. - *Eric Evans*

> DDD 에서 중요한 원칙 하나 - *Language is Important*


### 2. 모델에 대해 알아보자

> Generate variation. - 
> Don't dither.
> Don't get finickey. 

> Choosing the model

다양한 논의를 통해 아래와 같은 variation 이 도출되었다. 어떤것이 더 좋은 모델일까?

![[which-model-is-better.excalidraw.png]]

> [!question] What is a *model*
> 에릭에반스의 정의를 듣기전 나만의 정의를 먼저 생각해보자.
> 내 생각에 모델이란 애플리케이션의 구성 요소중에서 어떤 상태가 중요한 녀석들? 이라고 정의할 수 있지 않을까 싶다. 내가 알기로 또 내가 분류하기로 dto, entity, 정도를 묶어서 모델이라고 표현하니 상태가 중요하지 않은 로직만을 가지는 서비스와는 그런 측면에서 비교되는것 같다. - 남득윤
> 
> 

이제 에릭 에반스의 이야기를 들어보자.

지구라는 도메인을 지도라는 모델을 이용해 표현할때 아래와 같은 예시가 있다.

=== "평면 지도"

     ![[worldmap-1.png]]

=== "지구본"

     ![[worldmap-2.png]]

이러한 모델을 구성할때 고려되는 사항을 정리해보자

> - Abstraction 
>     - 지구는 둘글다
> - Data Selection
>     - 관심 사항 (해안선, 강, 항구)
>     - 모든 데이터를 표현할 수는 없다.
> - Established Formalism
>     -  둥근 지도를 평면으로 피는 공식을 정리한다.
> - Assertion
>     - 모델이 만족해야 하는 가정 (Mercator 지도는 두 점간의 방향을 보존한다.)

음... 난해하지만 바로 정리해주는 Definition 을 이해하기 위한 초석이라고 생각한다. 그럼 에릭 에반스의 도메인 그리고 모델에 대한 정의를 알아보자.

> [!note] Definitions
> * *domain* - A sphere of knowledge or activity.
> * *model* - A system of abstractions representing selected aspects of a *domain*.

> model 은 domain 에 대한 지식과 가정에 대한 distill (증류)를 한다. (액기스를 뽑는다 정도로 이해하자.)

에릭 에반스가 이야기의 핵심은 `모델은 도메인에 대해 모든것을 표현하는 것이 아니라 원하는 영역에 추상적으로, 선택적으로 표현하는 것`이다.

> model needs *narrow focus*
> model is not just those objects (Cargo, Itinerary, Leg, ...). It describes the way thoes objects are related each other

### 3. Ubiquotous language

> [!note] ubiquitous language
> A language structured around the domain model and used by all team members to connect all the activities of the team with the software.
> 
> ... within a bounded context.

### 4. 몇가지 결론

- 좋은 모델은 없다. 유용한 모델은 있다.
    - 유용하다는 것은 다양한 시나리오를 잘 설명할 수 있다는 뜻이다.
- 도메인 이란 지식이나 활동의 영역이다.
- 모델이란 도메인의 특정 영역를 추상화하여 표현하는 것
- 통일된 언어/용어 (UL) 사용하는 것은 아주 중요하다.