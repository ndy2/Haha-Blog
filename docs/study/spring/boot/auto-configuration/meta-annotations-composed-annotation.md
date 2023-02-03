---
title: 자동 구성 기반 애플리케이션
date: 2023-02-03
---

@ 참고 자료)

- 토비의 스프링 부트 - 이해와 원리 on[Inflearn](https://www.inflearn.com/course/토비-스프링부트-이해와원리)

---

### 1. Meta Annotation & Composed Annotation

#### 메타 애너테이션

- 애너테이션이 애너테이션을 포함하여 중첩되는 경우 중첩된 애너테이션을 메타 애너테이션 이라고 한다.
- Java 의 애너테이션을 선언하기 위해 반드시 포함되어야 하는 `@Retention,` `@Target` 은 대표적인 Java 의 메타 애너테이션이다.
<br>
- `@Component`  는 `@Controller`, `@Service`, `@Repository` 가 포함하는 Spring 의 대표적인 메타 애너테이션만이다.
- 이를 통해 개발자는 컨트롤러 클래스가 Spring Component 임과 동시에 web-mvc 의 Handler 로 동작한다는 사실을 알 수 있다.

!!! warn

    * 메타 애노테이션과 상속은 다르다.
    * @Rentention 으로 애너테이션이 지정된 애너테이션만 다른 애너테이션이 포함할 수 있다.
    * 또한 기본 Reflection 만으로 메타애너테이션을 감지하기 위해서는 어떤 재귀적인 탐색이 이루어져야 한다. 
	    * Spring 의 @Component 나 Junit 의 @Test 등의 애너테이션는 프레임워크에서 그러한 탐색을 지원한다.

#### 합성 애노테이션

- 하나 이상의 메타 애너테이션을 적용한 경우 이를 Composed Annotation 이라고 한다.

!!! example

    * 팀 프로젝트에서 사용하였던 컨트롤러 테스트를 위한 합성 애너테이션

	```java title="ControllerTest"
	@Target(ElementType.TYPE)
	@Retention(RetentionPolicy.RUNTIME)
	@Inherited
	@Tag("controller")
	@AutoConfigureMockMvc
	@SpringBootTest
	@Import({P6spyLogMessageFormatConfiguration.class, DatabaseCleanup.class})
	public @interface ControllerTest {
	}
	```


    * 스프링 웹의 @RestController = @Controller + @ResponseBody
     
    ```java title="org.springframework.web.bind.annotation.RestController"
	@Target(ElementType.TYPE)  
	@Retention(RetentionPolicy.RUNTIME)  
	@Documented  
	@Controller  
	@ResponseBody  
	public @interface RestController {  
	  
	@AliasFor(annotation = Controller.class)  
	String value() default "";  
	  
	}
	```

    * 스프링 부트의 `@SpringBootApplication` = `@SpringBootConfiguration`  + `@EnableAutoConfiguration`   + `@ComponentScan`

    ```java title="org.springframework.boot.autoconfigure.SpringBootApplication"
    @Target(ElementType.TYPE)  
	@Retention(RetentionPolicy.RUNTIME)  
	@Documented  
	@Inherited  
	@SpringBootConfiguration  
	@EnableAutoConfiguration  
	@ComponentScan(excludeFilters = { @Filter(type = FilterType.CUSTOM, classes = TypeExcludeFilter.class),  
	      @Filter(type = FilterType.CUSTOM, classes = AutoConfigurationExcludeFilter.class) })  
	public @interface SpringBootApplication {
    //...
    }
    ```




