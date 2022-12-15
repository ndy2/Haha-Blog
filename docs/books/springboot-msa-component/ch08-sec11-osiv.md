OSIV 는 영속성 컨텍스트의 생명주기를 트랜잭션 범위를 넘어 스프링 MVC 의 View 까지 확장하여 사용할 수 있는 기능이다. 스프링 부트 프레임워크에서는 기본 설정으로 OSIV 가 활성화되어 있다.

```properties title="osiv 활성화를 끄는 설정"
spring.jpa.open-in-view = false
```

책에서 소개하는 아래 그림이 entityManager, connection, transaction 의 생명주기를 아주 잘 나타내 줍니다.

### OSIV - on
![excalidraws/osiv-on.excalidraw.png](excalidraws/osiv-on.excalidraw.png)

### OSIV - off
![excalidraws/osiv-on.excalidraw.png](excalidraws/osiv-off.excalidraw.png)