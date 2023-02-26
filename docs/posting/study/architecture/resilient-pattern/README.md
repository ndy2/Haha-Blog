---
tags: [architecture]
title: Resilient Pattern
date: 2023-02-23
---

@참고 자료)

- UWE FRIEDRICHSEN
	- https://www.ufried.com/blog/resilience/
	- https://www.ufried.com/blog/resilience_vs_fault_tolerance/
	- https://ufried.com/blog/why_resilient_software_design_1/
- vinsguru 
	- [Timeout Pattern](https://www.vinsguru.com/timeout-pattern/)
	- [Retry Pattern](https://www.vinsguru.com/retry-pattern/)
	- [Circuit Breaker Pattern](https://www.vinsguru.com/circuit-breaker-pattern/)
	- [Bulkhead Pattern](https://www.vinsguru.com/bulkhead-pattern/)
	- [Rate Limiter Pattern](https://www.vinsguru.com/rate-limiter-pattern/)
- ms
	- https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
	- https://learn.microsoft.com/ko-kr/azure/architecture/patterns/bulkhead

---

### 0. 들어가며

Resilient Pattern 의 종류를 정리하기 전에 Resilient 와 Resilient Pattern 의 의미를 먼저 정리하겠습니다.

- Resilient 는 탄력성있는, 회복성있는 등으로 단어입니다. 
- 한 시스템이 Resilient 하다는 것은 외부의 부적절한 영향에 휘둘리지 않으며 혹은 이를 빠르게 회복할 수 있다는 것입니다.
- MSA 패턴에서 Resilient Pattern 이란 마이크로 서비스 컴포넌트가 정상적으로 동작하지 않을때도 요청에 대해 정상적인 (의도한 대로의) 응답을 할 수 있도록 하는 패턴입니다.

Resilient 라는 특성은 IT 분야 뿐만 아니라 많은 영역에서 중요한 특성입니다. 한국은 화물차의 주행에 꼭 필요한 요소수의 생산에 필요한 요소의 수입량의 97퍼센트를 중국에 의존하고 있었습니다. 한국은 요소의 공급 시스템에 Resilient 특성을 가지고 있지 않았습니다. 중국 정부의 수출 통제라는 부적절한 영향에 일시적으로 요소, 요소수의 품귀 현상이 발생하였습니다. - [나무위키 링크](https://namu.wiki/w/2021년%20요소수%20대란)

시스템을 설계할때는 항상 효율성 (Efficiency)과 탄력성 (Resilience) 간의 트레이드 오프를 고민해야 합니다. 

이렇게 정리하고 나니 흔히 이야기 하는 Fail Tolerant 와 Resilient 의 차이가 궁금해졌습니다. 검색해 보니 이 [링크](https://www.ufried.com/blog/resilience_vs_fault_tolerance/) 에서 이와 관련된 내용을 잘 정리해 두었습니다. 요약하면 Resilient 를 단순히 Fail Tolerant 와 동일시 하는 사람들도 있지만 필자(Uwe Friedrichsen)는 Resilient는 조금더 확장된 개념 (특히 회복성 측면에서)이라고 이야기합니다. 저도 생각해보니 그런 뉘앙스의 차이만 살짝 있고 둘이 크게 다른 개념처럼 보이지는 않습니다.

이제 MSA 에서 Resilient 특성을 갖추기 위해 활용되는 Resilient Pattern 을 알아보겠습니다.

---

### 1. Timeout Pattern

![[images/timeout-1.png]]

Timeout 패턴은 매 요청시 타임아웃을 걸고 타임아웃 내에 응답이 오지 않는다면 더이상 기다리지 않고 쓰레드를 진행시키는 패턴입니다. 이 때 응답값이 별로 중요하지 않다면 기본값을 채울 수도 있고 응답값이 중요한 값이라면 예외를 발생 시킬 수도 있습니다.

타임아웃 방식은 요청 쓰레드가 타임아웃 시간동안 계속 요청을 물고 있어야 하기 때문에 동시 요청이 많은 시스템에서는 문제가 될 수 있습니다.

### 2. Retry Pattern

![[images/retry-1.png]]

Retry 패턴은 요청이 실패하면 재요청을 보내는 패턴입니다. 이때 재요청의 횟수를 제한하거나 요청 시 간격을 둘 수도 있습니다. 또한 첫번째 요청과 두번째 이상의 요청 (재 요청) 메서드 (fallback)를 다르게 가져갈 수도 있습니다.

### 3. Circuit Breaker Pattern

![[images/circuit-breaker-1.png]]

서킷 브레이커 패턴은 요청 클라이언트와 응답 서버 사이에 Circuit Breker (회로 차단기) 를 추가로 두어 서킷 브레이커가 서버의 상태를 나름의 기준으로 판단하여 서버의 상태가 좋지 않은 경우 이를 차단하는 패턴입니다. 한번씩 요청을 보내서 서버의 상태를 판단해보고 괜찮다고 판단되면 다시 회복합니다. 서킷 브레이커는 서버의 상태를 OPEN (장애) CLOSED(정상) HALF-OPEN(반 장애) 로 구분합니다.

이 패턴은 Retry 패턴이 회복되지도 않을 서버에 계속해서 재시도 요청을 하여 발생할 수 있는 리소스 낭비의 문제를 어느정도 해결합니다. 프록시 패턴의 일종입니다.

### 4. Bulkhead Pattern

![[images/bulkhead-1.png]]

Bulkhead Pattern (격벽 패턴) 은 애플리케이션의 요소를 격리하여 관리함으로써 한 요소의 실패가 다른 요소로 전파되지 않도록합니다. 

Worlkload 1 와 Workload2 의 커넥션 풀을 나누어 Workload 1 의 문제가 Workload 2 로 전파되지 않도록할 수 있습니다.

요청 흐름에 따라 리소스를 나누어 놓았기 때문에 리소스 사용 효율성이 떨어 질 수도 있습니다.

### 5. Rate Limiter Pattern

![[images/rate-limmiter-1.png]]

Rate Limiter 패턴은 일정 시간 (윈도우) 동안 보낼 수 있는 요청의 횟수를 제한하여 서버의 리소스를 보호하는 패턴입니다.
