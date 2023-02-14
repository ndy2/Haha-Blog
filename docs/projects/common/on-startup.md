---
title: 시작 단계의 체크리스트
date: 2023-02-13
---
### 들어가며

프로젝트를 시작할때 해야하는 작업의 목록을 정리해보자.

### 체크리스트

!!! note "사실상 고정인 항목들"

    * VCS<sup>version control system</sup> - `git` 
    * process - agile
    * dev/framework - spring ~~//아직 나한태는...~~

#### 1. Version Management

- [ ] remote git repository
    - github
    - gitlab

- [ ] git-commit strategy
    - git-flow
    - github-flow
    - custom

- [ ] how to write commit messages

- [ ] Pull/Merge Request strategy
    - github 
        - Create a merge commit
        - Squash and merge
        - Rebase and merge
    - gitlab
        - Merge commit
        - Merge commit with semi-linear history
        - Fast-foward merge
    - Pull/Merge Requset Approval rule

- [ ] Realease strategy

#### 2. Issue tracking

- [ ] Issue tracking system
    - JIRA
    - youtrack
    - gitlab

#### 3. Dev Process

!!! note "참고자료"

    * 로버트 C. 마틴 `『클린 애자일』 [정리 링크](../../../books/clean-agile/clean-agile)

- [ ] waterfall vs agile

- [ ] sprint cycle
    - [ ] 1 week
    - [ ] 2 week
    - [ ] else

#### 4. Communication

!!! note "참고 자료"

    * 비동기적 커뮤니케이션 - [링크](../../../study/dev-general/collaborate/async-communication)

- [ ] tools
    - [ ] kakaotalk
    - [ ] discord
    - [ ] slack
    - [ ] notion
    - [ ] gather

#### 5. Dev (on backend server with spring framework)

##### 1. Architecture (in 하나의 코드베이스)

!!! note "참고 자료"

    * 이동욱님(조졸두) - [계층형 아키텍처](https://jojoldu.tistory.com/603)
    * 톰 홈버그 - `『만들면서 배우는 클린 아키텍쳐』` [정리 링크](https://ndy-dev.notion.site/d737675bbc324c09ae6d1721754b2dcb)
    * 톰 홈버그 - [Let's build components, not layers by Tom Hombergs @ Spring I/O 2022](https://youtu.be/-VmhytwBZVs)

- Layered Architecture
- Hexagonal Architecture
- Component based Architecture

##### 2. Language

!!! note "java LTS<sup>Long Term Support</sup>"

    [참고 링크](https://fftl.tistory.com/m/19)

- 별 다른 이유가 없으면 - Java 11 이 아직은 일반적인 선택
- Record 등 Java 15 이상의 기능을 활용하고 싶으면 - Java 17
- spring 6.0/ spring boot 3.0 이상의 기술을 활용하고 싶으면 - Java 17
- kotlin

##### 3. build system

- maven
- gradle(groovy/kotlin dsl)
    - 별 다른 이유가 없으면 gradle - 점점 더 많이 사용하고 간결하다.

#### 6. Style

##### 1. Linter (a.k.a. static code analysis)
- [ ] sonarl lint
- [ ] checkstyle

#### 7. Test (with Junit5.0~)

!!! note "Test 관련 도구 들"

    * ArchUnit - 아키텍처 (계층별 참조/ 네이밍 룰/ 어노테이션 작성 방식 등)를 단위 테스트로 검증 하는것을 도와주는 라이브러리/프레임워크
    * Fixture Monkey - 픽스쳐를 랜덤하게 생성하는 것을 도와주는 라이브러리
    * assertJ - junit 보다 개선된 방식(자칭,타칭)의 검증 dsl 을 제공하는 라이브러리
    * test container - 테스트 시작/종료시 도커 컨테이너를 제어해서 실제 활경과 테스트 환경의 일치를 도와주는 라이브러리
    * newman - 스크립트를 이용해 postman 을 실행/검증해주는 프로그램/ api 테스트 자동화를 위해 사용함

##### 1. 일반적인 작성 스타일

- [ ] `junit style` vs `assertj style`
    - [ ] 일반 검증 - `assertXXX()` vs `assertThat()`
    - [ ] 예외 검증 - `assertThrows` vs  `assertThatExceptionOfType`

##### 2. Layerwise Test Sterategy

!!! note "참고 링크"

    - 만배클아 - [7장 아키텍쳐 요소 테스트하기](https://www.notion.so/ndy-dev/07-a3803648ad63438a8634eea1fadd3684)

!!! warn "테스트?"

    - 테스트를 어디까지 얼마나 작성해야 하는가는 분명히 정리/합의 해야 하는 부분
    - 모든 계층에 대한 테스트를 작성한다고 생각하고 본인의 경험을 기준으로 일반적인 가이드라인을 작성함
    - Spring Container 의 도움을 받는 테스트를 `(계층별) 통합 테스트`, POJO 와 mocking 만을 이용한 테스트를 `단위 테스트` 라고 지칭함

!!! note "전략 1 - 간단 버전"

    - `Controller Layer` - 통합 테스트
    - `Service(a.k.a. application) Layer` - 단위 테스트
    - `Domain Layer` - 단위 테스트
    - `Persistence(a.k.a. DAO/Repository) Layer` - 통합 테스트

!!! note "전략 2 - 더 빡센 버전"

    * `Integration Test` - 별도의 통합 테스트 구성
        * with gradle - [참고 링크](https://aiden-j.tistory.com/20)
        * with postman & newman - [참고 링크](https://www.postman.com/postman-galaxy/easy-integration-testing-using-postman-and-newman/)
    * `Controller Layer` - 단위 테스트
    * `Service Layer` - 단위 테스트
    * `Domain Entity Layer`- 단위 테스트
    * `Persistence Layer` - 통합 테스트

#### 8. Namings & Ubiquitous Language(a.k.a. Metaphor)

##### 네이밍과 관련된 좋은 글

!!! quote "최범균님 - `『도메인 주도 설계 시작하기』` 발췌"

    -   코드를 작성할 때 도메인에서 사용하는 용어는 매우 중요하다.
    -   정리된 용어를 문서화하고 도메인 모델의 주석으로 남기는 것은 좋은 습관
    -   `Status` or `State`?
    -   `Type` or `Kind`? 심지어 발음 나는 대로 `Gubun` 도 가능

알맞은 영단어를 찾는 것은 쉽지 않은 일이지만 시간을 들여 찾는 노력을 해야한다. 그렇지 않으면 코드는 도메인과 점점 멀어진다. -p.59


##### UL 과 관련된 글들 

- MSA 에서 유비쿼터스 언어(보편 언어)의 중요성 on [Medium/jus0997](https://medium.com/dtevangelist/msa-에서-유비쿼터스-언어-보편-언어-의-중요성-ca22b96aaeea)


#### 9. Documentation

!!! question "어디에?"

    * github/gitlab wiki
    * or 자동화 with asciidoc (or other choices)

!!! question "api specification 어디에?"

    * 개발 전 및 논의 단계 에서 - notion/github/gitlab wiki 등
    * 코드를 통해서 구성하는 방식 - swagger/restdocs


#### 10. What else more?

- CI/CD pipeline/process
- 설정 정보 관리
- Team name/ Project name/ Member roles ...