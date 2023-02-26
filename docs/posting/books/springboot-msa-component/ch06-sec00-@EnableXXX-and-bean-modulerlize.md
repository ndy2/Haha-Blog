이 절에서는 웹 애플리케이션 설정의 핵심이 되는 `@EnableWebMvc` 애너테이션과그 동작 방식을 살펴본다. 그 전에 스프링 프레임워크 여기저기에 보이는 `@EnableXXX` 애너테이션 이 동작하는 방식을 이해하자.

e.g. `@EnableWebMvc`, `@EnableTransactionManagement`, `@EnableWebSecurity`, ... 

이 내용은 토비의 스프링 vol 2 7.8 절을 바탕으로 정리한 내용이다.

Spring 이 애플리케이션의 설정에 @EnableXXX 와 Configurer 등 복잡한 메커니즘을 도입하는 이유는 모두 재사용성, 확장성, 변경가능성을 제공하기 위해서이다.

```java
public class Hello{

	String name;

	public void setName(String name){
		this.name = name;	
	}

	public void sayHello(){
		System.out.println("Hello " + name);
	}
}
```

이 Hello 클래스가 반복적으로 여러 프로젝트에 사용해야 할 복잡한 기능을 가진 인프라 빈이라고 가정해보자.

설정 방식도 복잡하고 매번 직접 @Bean 으로 생성하기도 어렵다면 미리 만들어둔 설정을 재사용할 수 있게 해야한다.

```java
@Configuration
public class HelloConfig{

	@Bean
	public Hello hello(){
		Hello h = new Hello();
		h.setName("Spring");
		return h;
	}
}
```

### 1. @Import 와 @Configuration 상속

가장 일반적인 설정의 재사용 방식이다.

#### @Import 사용

@Import 는 다른 @Configuration 이 있는 클래스에서 @Configuration 클래스 정보를 정말로 **Import** 하듯이 활용할 수 있도록 해준다.

```javadoc
Indicates one or more component classes to import — typically @Configuration classes.

Provides functionality equivalent to the <import/> element in Spring XML. Allows for importing `@Configuration` classes, `ImportSelector` and `ImportBeanDefinitionRegistrar` implementations, as well as `regular component` classes.
```

아래 처럼 활용할 수 있다.

```java
@Configuration
@Import(HelloConfig.class)
class AppConfig {
}
```

하지만 @Import 는 클래스 밖에 전달 받지 못한다. 다양한 정보를 재설정 할 수 없다.

#### @Configuration 상속, 오버라이딩

```java
@Configuration
public class AppConfig extends HelloConfig{
	
	@Override
	public Hello hello(){
		Hello h = supoer.hello();
		h.setName("Haha");
		return h;
	}
}
```

- `@Import` 를 사용할 때와 달리 설정을 자유롭게 변경할 수 있다. 
- 원래 정의되어 있던 `@Bean` 메서드를 통채로 오버라이딩 했기 때문이다.

하지만 단점이 많은 방식이다.

- 상속이라는 큰 결합을 원래 설정클래스와 가지게 됨.
- 여러 설정클래스를 한 클래스로 표현 할 수 없음.

> @Import 의 간결한 활용과 여러 클래스 표현 + 상속의 필요한 설정 수정 가능
> 이 모두를 만족할 수 있는 좋은 방법은 없을까?

### 2. @EnableXXX 와 ImportAware

Spring 의 `@Enable`로 시작하는 애너테이션은 모듈화된 빈 설정정보를 추가하면서 엘리먼트 값을 이용해 옵션 정보를 제공할 수 있게 해 준다.

Spring 은 기본적으로 `@Import` 를 포함한 메타애너테이션을 `@Import` 와 같이 취급한다.

`@EnableXXX` 애너테이션에 엘리먼트 값을 옵션정보로 활용하기 위해서는 `@Configuration` 클래스가 `ImportAware` 인터페이스를 확장해야 한다.

```java
@Import(HelloConfig.class)
public @interface EnableHello {
	String name();
}
```

```java
@Configuration
public class HelloConfig implements ImportAware{

	@Bean
	Hello hello(){
		Hello h = new Hello();
		h.setName("Spring");
		return h;
	}

	@Oberride
	public void setImportMetadata(AnnotationMetadata importMetadata){
		Map<String,Object> elements = importMetadata.getAnnotationAttributes(EnableHello.class.getName());
		String name = (String) elements.get("name");
		hello().setName(name);
	}
}
```

### 3. Bean Configurer

재사용하려는 빈 설정정보의 양이 많거나 확장 방법이 다양하고 복잡할 경우에는 애노테이션의 엘리먼트만으로는 충분하지 않을 수 있다. 이럴 때는 @Enable 애너테이션과 함께 자바 코드를 이용한 설정정보의 확장 포인트가 필요한데 이를 빈 설정자 (Bean Configurer) 라고 한다.

Spring 프레임워크가 제공하는 빈 설정자는 WebMvcConfigurer, ~~WebSecurityConfiguerer~~ 등이 대표적이다. 

빈 설정자를 이용해 Hello 의 name 필드를 자바코드로 세팅하는 방식은 아래와 같다.

```java
public interface HelloConfigurer {
	void configureName(Hello hello);
}
```

```java
@Configuration
@EnableHello
public class AppConfig implements HelloConfigurer {

	@Override
	public void configName(Hello hello){
		hello.name = "haha";
	}
}
```

```java
@Configuration
public class HelloConfig{

	@Autowired
	private HelloConfigurer helloConfiguerer;

	@Bean
	Hello hello(){
		Hello h = new Hello();
		h.setName("Spring");
		helloConfiguerer.configName(h);
		return h;
	}
}
```

### 4. `ImportSelector` 와 `ImportBeanDefinitionRegister`

이정도면 설정 정보를 group 화 하고 모듈화 하는 대부분의 테크닉을 이해했다.

책에서 마지막으로 언급하는 방식은 바로 `ImportSelect` 와 `ImportBeanDefinitionRegister` 이다.

어떤 상황이나 세팅 정보에 따라 빈의 타입이나 구성 정보가 통째로 변경해야 한다면 어떨까? AOP 기반의 Transaction 서비스를 지원해주는 @EnableTransactionManagement 를 구경해보자

```java
package org.springframework.transaction.annotation;

...
@Target(ElementType.TYPE)  
@Retention(RetentionPolicy.RUNTIME)  
@Documented
@Import(TransactionManagementConfigurationSelector.class)
public @interface EnableTransactionManagement {

	...

	AdviceMode mode() default AdviceMode.PROXY;
}
```

이제 TransactionManagementConfigurationSelector 를 살펴보자!

![TrasactionManagementConfigurationSelector.png](images/TrasactionManagementConfigurationSelector.png)

- 추상 클래스와 템플릿 메서드 패턴을 이용해 `selectImports` 메서드의 파라미터를 `AdviceMode` 로 두었다.
- 스프링이 지원하는 두가지 프록시 방식 (JDK 의 다이나믹 프록시 기반, AspectJ AOP 기반) 에 따라 내부에 설정되어야 하는 빈의 정보가 완전히 달라지게 된다.
- 이를 `EnableTransactionManagement` 에서 `AdviceMode` 를 설정하는 것으로 간단히 변경할 수 있도록 한 것이다. 이때 `ImportSelector` 를 구현하여 `@Enable` 애너테이션의 `@Import`에 추가하였다.
- 옵션에 따라 복잡한 빈 설정 조합을 만들어내야 하는 경우라면 `ImportBeanDefinitionRegistrar` 를 이용할 수 있다.

### 더 알면 좋은 것들

이 페이지의 주제는 처음 말했다 싶히 @Enable 애너테이션의 동작방식과 빈 설정 정보의 모듈하 방식이다.

즉, 직접 설정을 하고 그 설정이 동작하는 방식이다. 이와 더불어 SpringBoot 의 핵심 기능중 하나인 자동 설정 (Auto Configuration) 이 어떻게 동작하는가 또 이를 어떻게 제어하는가 역시 좋은 학습 주제이다.
