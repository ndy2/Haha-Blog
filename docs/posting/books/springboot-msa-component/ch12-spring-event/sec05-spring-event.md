스프링은 애플리케이션을 띄우는 다양한 시점에 이벤트를 발행합니다. 이를 이용하면 스프링이 뜨는 다양한 시점에 원하는 코드를 실행 시킬 수 있습니다.

![springApplicationEvent.png](images/springApplicationEvent.png)

---
- 가장 자주 활용되는 Spring 의 이벤트는 `ApplicationReadyEvent` 입니다. 이 이벤트는 모든 애플리케이션과 커맨드 라인 러너가 실행된 후 발생하는 이벤트입니다. 이 시점에는 애플리케이션이 말 그대로 `준비 완료` 된 상태로 모든 빈을 주입 받아 처리 할 수 있어 테스트 환경 등에서 데이터 셋업 등을 목적으로 활용하기 좋습니다.
- 물론 전통적인 방식인 CommandLineRunner 나 ApplicationRunner 를 사용할 수도 있습니다. 이에 관한 자세한 내용은 토비님의 [요 영상](https://youtu.be/f017PD5BIEc) 을 참고해주세요.
