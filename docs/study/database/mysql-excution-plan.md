
@참고 자료)


---

### 0. 들어가며

- `친절한 SQL` 을 읽다보니 oracle 에 기반한 책이라는 점이 아쉬웠습니다.
- 사실 MySQL 을 깊게 학습한 적이 있는 것은 아니라 이 기회에 Oracle DB 로 계속 학습을 이어나가면 어떨까도 생각했지만 여러 대기업에서 MySQL 을 적극적으로 사용하고 있다고 생각되어 M계속 MySQL로 학습하고자 합니다.
![mysql-kakao.png](images/mysql-kakao.png)
![mysql-coupang.png](images/mysql-coupang.png)

- 책에서 나오는 내용을 MySQL 로 따라해보려하니 가장 막히는 부분이 실행 계획을 읽는 부분이었습니다
- 그래서 이 문서에서는 MySQL 의 Execution Plan 을 확인하고 해석하는 법을 간단히 정리해보고자 합니다.

- 예시로 사용한 테이블 구조와 쿼리는 이전에 진행했던 프로젝트 중 하나인 [링크오션](https://github.com/prgrms-web-devcourse/Team-Meoguri-Linkocean-BE) 의 테이블 구조와 쿼리를 사용하겠습니다. 자세한 테이블 구조가 궁금하신 분은 위 링크를 참고해주세요.

- 모든 항목을 정리하지는 않고 프로젝트에서 사용한 쿼리의 실행계획을 찍어보았을때 보이는 특이사항 위주로 정리하겠습니다.
---


