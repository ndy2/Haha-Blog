
### 스프링 부트 소개

- {==스프링 부트==} <sup>Spring Boot</sup> 는 스프링을 기반으로 실무 환경에 사용 가능한 수준의 독립실행형 애플리케이션 Containerless 을 복잡한 고민 없이 빠르게 작성할 수 있게 도와주는 여러가지 도구의 모음이다.

!!! note

    스프링 != 스프링 부트!!

---

### 스프링 부트의 핵심 목표

- 빠르고 광범위한 영역의 스프링 개발
- 설정보다 관례 <sup>Convention over Configuration</sup> 패러다임
- 다양한 비기능적인 기술 (내장형 서버, 보안, 메트릭, 상태 체크, 외부 설정 방식) 등 제공
	- ~ Spring Cloud 와도 관련이 많지만 그 중심에는 Spring Boot 가 있다!
- 코드 생성이나 XML 설정을 필요로 하지 않음
	- 순수 Java Code 와 간단한 yaml 설정으로 복잡한 기능을 모두 제어 할 수 있다.

---

### 스프링의 시작과 스프링 부트의 시작

#### 스프링의 시작 : by Rod Jhnson @ 2003/06 ~

만든 이유, 핵심 컨셉 


=== "🟢"

    * **좋은 객체 지향 애플리케이션**을 개발할 수 있게 도와준다.
    * EJB → EJB 종속적인 코드가 됨/ POJO 등장
    * 스프링의 IOC 컨테이너에 그 핵심이 있다. → OPC, DIP를 가능하게 지원

=== "❌"

    * 웹 앱, DB 접근 편하게?
    * 웹 서버 자동 띄워주기?
    * 클라우드, 마이크로서비스?


#### 스프링 부트의 시작 : @ 2013 ~

Improved support for **'containerless'** web application architectures [SPR-9888] #14521 - [링크](https://github.com/spring-projects/spring-framework/issues/14521) 

- 한 개발자 스프링 커뮤니티에 스프링은 정말 좋은 프로젝트 이지만 시작하기 위해 진입장벽이 높고 특히 서버를 처음으로 띄우기 까지 필요한 사전 작업이 너무 복잡하다고 문제를 제기하였다.
- 또한 스프링 부트의 핵심이 되는 내장 서블릿 컨테이너에 대한 아이디어도 제기하였다.
- 약 1년 뒤 Spring Boot 프로젝트가 탄생하였다.
- 스프링 부트는 계속해서 업데이트 가장 최근에는 Spring Boot 3.0 의 GA 버전이 공개되었습니다. - [링크](https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga)

---

### Containerless (~Serverless)

- 스프링 부트는 Containerless web application architecture 를 지원해 달라는 한 개발자의 요청에 의해 시작되었습니다.


!!! note "여기서 컨테이너란?"

    도커? IOC 컨테이너? 댓츠 노우노우 <br>
    It is Web Container!

    여기서 Web Container 란? <br> 
    Web Component 를 통해 동적 컨텐츠를 생성하고 Web Component 의 라이프 사이클 (생성, 소멸 ,...)을 관리한다. <br>
    또한 요청에 따라 처리할 알맞은 Web Component 를 선택한다 (라우팅 or 매핑)


위 정의를 자바 진영에 옮겨보면 Web Component 는 서블릿, Web Container 는 서블릿 컨테이너에 라는 것을 알 수 있습니다. 즉 자바 진영에서 Containerless 란 서블릿 컨테이너와 관련된 것입니다. 하지만 말 그대로 서블릿 컨테이너를 제거하는 것은 또 아닙니다. 이와 관련된 자세한 내용은 [강의](https://www.inflearn.com/course/토비-스프링부트-이해와원리) 를 참고해주세요.

---
### Opinionated

 스프링 부트는 Opininated 합니다. 반면 스프링은 Not-Opinionated 합니다. <br>
스프링은 극단적인 유연함을 추구하지만 프레임워크로서의 역할만 딱 한다라고 이해하면 좋을것 같습니다. 즉 자기 주장이 없습니다. 반면 스프링 부트는 대부분의 설정 및 관계에 대해 기본값을 가지고 있으며 당연히 프레임워크로서의 역할도 함께 합니다. 즉, 스프링 부트는  Best-Practice 를 통해 결정된 서버를 띄우기 위한 최소한의 설정과 버전 정보도 함께 제공합니다. 개발자는 중요한 도메인 로직작성에 집중할 수 있습니다.