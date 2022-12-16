```yml
# Project information
site_name: Haha 블로그
site_url: https://ndy2.github.io//Haha-Blog/
edit_uri: blob/main/docs/
site_author: Haha
site_description: >-
  안녕하세요! 좋은 설계와 객체지향 방법론에 관심이 많은 미래의 백엔드 개발자 남득윤입니다.
  잘 부탁드립니다!

# Repository
repo_name: ndy2/Haha-Blog
repo_url: https://github.com/ndy2/Haha-Blog

copyright: Copyright &copy; 2022 - 2022 ndy2

theme:
  name: 'material'
  font:
   text: Roboto
   code: Roboto Mono
  favicon: assets/favicon.ico
  admonition:
   note: octicons/tag-16
   abstract: octicons/checklist-16
   info: octicons/info-16
   tip: octicons/squirrel-16
   success: octicons/check-16
   question: octicons/question-16
   warning: octicons/alert-16
   failure: octicons/x-circle-16
   danger: octicons/zap-16
   bug: octicons/bug-16
   example: octicons/beaker-16
   quote: octicons/quote-16

# Extensions
markdown_extensions:
  - footnotes
  - md_in_html
  - attr_list
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - def_list
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.critic
  - pymdownx.caret
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.tilde
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
  - toc:
      permalink: true

plugins:
  - search
  - glightbox
  - git-revision-date-localized:
      type: date
      timezone: Asia/Seoul
      enable_creation_date: true
  - git-authors
  
# Page tree
nav:
  - Home: index.md
  - 블로그 팁:
      - 들어가기: bloggingtips/getting-started.md
  - 기술 서적 정리/리뷰:
      - 책!: books/index.md
      - 클린 애자일: books/clean-agile/clean-agile.md
      - 스프링 부트로 개발하는 MSA 컴포넌트:
          - 리뷰: books/springboot-msa-component/README.md
          - 1장 마이크로서비스 아키텍처: books/springboot-msa-component/ch01-msa.md
          - 2장 프레임워크와 스프링부트: books/springboot-msa-component/ch02-framework-and-springboot.md
          - 3장 스프링 애플리케이션 기본: books/springboot-msa-component/ch03-springboot-basic.md
          - 4장 스프링 웹 MVC 개요:
              - 들어가기: books/springboot-msa-component/ch04-spring-web-mvc-basic.md
              - 파트 1 HTTP: books/springboot-msa-component/ch04-sec01-http.md
              - 파트 2 서블릿과 MVC: books/springboot-msa-component/ch04-sec02-servlet-and-mvc.md
          - 5장 스프링 MVC를 이용한 REST-API 개발: books/springboot-msa-component/ch05-spring-web-mvc-with-restapi.md
          - 6장 웹 애플리케이션 서버 구축하기:
              - 들어가기: books/springboot-msa-component/ch06-build-web-application-server.md
              - EnableXXX의 동작과 빈 설정 모듈화: books/springboot-msa-component/ch06-sec00-@EnableXXX-and-bean-modulerlize.md
              - 웹 애플리케이션 설정 메커니즘: books/springboot-msa-component/ch06-sec01-webapplication-configure-mechanism.md
              - DispatcherServlet: books/springboot-msa-component/ch06-sec03-dispatcher-servlet.md
          - 7장 스프링 AOP와 테스트, 자동 설정 원리:
              - 들어가기: books/springboot-msa-component/ch07-spring-aop-and-test-and-autoconfiguration.md
              - 스프링 AOP: books/springboot-msa-component/ch07-sec01-spring-aop.md
              - 스프링 부트 자동 설정: books/springboot-msa-component/ch07-sec03-autoconfiguration.md
          - 8장 데이터 영속성:
              - 들어가기: books/springboot-msa-component/ch08-data-persistence.md
              - JPA 장점과 단점: books/springboot-msa-component/ch08-sec01-jpa-pros-and-cons.md
              - 엔티티 매니저와 영속성 컨텍스트: books/springboot-msa-component/ch08-sec08-entitymanager-and-persistence-context.md
              - @Transactional을 사용할 때 주의 사항: books/springboot-msa-component/ch08-sec07-warning-on-@Transactional.md
              - OSIV: books/springboot-msa-component/ch08-sec11-osiv.md
          - 9장 애플리케이션 통합 REST-API :
              - 들어가기: books/springboot-msa-component/ch09-application-integration-restapi.md
              - RestTemplate 클래스 : books/springboot-msa-component/ch09-sec01-resttemplate.md
              - WebClient 클래스 : books/springboot-msa-component/ch09-sec02-webclient.md
  - TIL:
      - 시작하기: til/getting-started.md
```