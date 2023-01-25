
참고 자료)

- 토비 스프링 부트 이해와원리 | by 토비 [@인프런](https://www.inflearn.com/course/토비-스프링부트-이해와원리/unit/136916)

---

### 1. 빈 서블릿 컨테이너 띄우기

#### 1. 코드

```java title="Embedded Tomcat 을 직접 띄우는 코드"
package tobyspring.helloboot;  
  
import org.springframework.boot.autoconfigure.SpringBootApplication;  
import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;  
import org.springframework.boot.web.server.WebServer;  
import org.springframework.boot.web.servlet.server.ServletWebServerFactory;  
  
@SpringBootApplication  
public class HellobootApplication {  
  
    public static void main(String[] args) {  
//        SpringApplication.run(HellobootApplication.class, args);  
        ServletWebServerFactory serverFactory = new TomcatServletWebServerFactory();  
        WebServer webServer = serverFactory.getWebServer();  
        webServer.start();  
    }  
}
```

톰캣 글자가 첫 생성시를 제외하고 슬며시 사라진 것을 확인할 수 있다.
스프링이 사랑하는 추상화에 대한 설계철학을 여기서도 엿볼수 있다.

#### 2. 확인
![tomcat-notfound.png](images/tomcat-notfound.png)

톰캣의 기본 에러 페이지를 응답으로 내려준다는 것을 확인했다.

---

### 2. 서블릿 추가!

#### 1. 코드


```java
package tobyspring.helloboot;  
  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import org.springframework.boot.autoconfigure.SpringBootApplication;  
import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;  
import org.springframework.boot.web.server.WebServer;  
import org.springframework.boot.web.servlet.server.ServletWebServerFactory;  
  
import java.io.IOException;  
  
@SpringBootApplication  
public class HellobootApplication {  
  
    public static void main(String[] args) {  
//        SpringApplication.run(HellobootApplication.class, args);  
        ServletWebServerFactory serverFactory = new TomcatServletWebServerFactory();  
        WebServer webServer = serverFactory.getWebServer(context -> context  
                .addServlet("hello-servlet", new HelloHttpServlet())  
                .addMapping("/hello"));  
        webServer.start();  
    }  
}  
  
class HelloHttpServlet extends HttpServlet {  
    @Override  
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws IOException {  
        resp.setStatus(200);  
        resp.setHeader("Content-Type", "text/plain");  
        resp.getWriter().println("I am Hello Servlet!");  
    }  
}
```

#### 2. 결과
![tomcat-hello.png](images/tomcat-hello.png)

---

### 3. 서블릿 컨테이너의 단점!

서블릿은 너무 추상적이다. 공통 처리를 담당하는 앞단의 문지기가 필요! <br> ***Front Controller*** 의 등장!

관련 내용 노션 정리 - [여기](https://www.notion.so/ndy-dev/Servlet-vs-Spring-Web-MVC-67bd245a6a234ed6a1bc5d9a3bbd98dd)

---

### 4. 이어서

위의 초 간단 서블릿 컨테이너를 프론트 컨트롤러 패턴을 적용해 개선시키는 과정은 [강의](https://www.inflearn.com/course/토비-스프링부트-이해와원리) 를 참고해주세요. 