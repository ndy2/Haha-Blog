---
title: 스프링 부트의 자동 설정 동작 원리
date: 2023-02-03
---
![EnableAutoConfiguration.excalidraw.png](excalidraws/EnableAutoConfiguration.excalidraw.png)

`@EnableAutoConfiguration` 은 최종적으로 두개의 `@Import` 애너테이션을 포함합니다.

### 2. `@AutoConfigurationPackage`

`@AutoConfigurationPackage` 는 빈을 직접 등록 한다기 보다는 추후 관리를 위해서 `BeanDefinitionRegistry` 에 `Bean Definition` 을 등록하는 과정이 필요한데 자동 설정 빈에 대해 이러한 작업을 수행해주는 `AutoConfigurationPackages.Registrar` 를 빈으로 등록해주는 역할을 합니다.
<br>
`"AutoConfigurationPackages"` 를 Key 로 하고 `"자동 설정된 패키지의 basePackage 목록"`을 Value 로 하는 요소가 하나 `BeanDefinitionRegistry`에 추가되는 작업이 이루어 집니다.

### 1. `@Import(AutoConfigurationImportSelector.class)`

`ImportSelector` 타입의 클래스를 @Import 에 포함하면 스프링 부트는 ImportSelector 에 정의된 `selectImports` 메서드를 호출해 임포트 대상이되는 설정 클래스의 목록을 동적으로 획들 할 수 있습니다.

`@Import`  `ImposrtSelector` 의 동작에 대한 자세한 내용은 여기 를 참고해주세요

`@Import(AutoConfigurationImportSelector.class)`는 {==**어딘가에**==} 저장된 자동 설정 정보를 읽어  는 자동설정 대상이 되는 빈을 등록하는 역할을 합니다. `AutoConfigurationImportSelector` 의 `selectImports` 메서드를 통해 동적으로 자동 설정 클래스 목록을 획득하는 과정을 따라가 보겠습니다.

---

### 3. Spring 이 외부 파일을 통해 자동 구성 설정 대상 패키지 경로 목록을 획득하는 과정

#### 1.selectImports
```java title="org.springframework.boot.autoconfigure.AutoConfigurationImportSelector#selectImports"
private static final AutoConfigurationEntry EMPTY_ENTRY = new AutoConfigurationEntry();
private static final String[] NO_IMPORTS = {};

@Override  
public String[] selectImports(AnnotationMetadata annotationMetadata) {  
   if (!isEnabled(annotationMetadata)) {  
      return NO_IMPORTS;  
   }  
   AutoConfigurationEntry autoConfigurationEntry = getAutoConfigurationEntry(annotationMetadata);  
   return StringUtils.toStringArray(autoConfigurationEntry.getConfigurations());  
}
```


#### 2. getAutoConfigurationEntry
```java
protected AutoConfigurationEntry getAutoConfigurationEntry(AnnotationMetadata annotationMetadata) {  
   if (!isEnabled(annotationMetadata)) {  
      return EMPTY_ENTRY;  
   }  
   AnnotationAttributes attributes = getAttributes(annotationMetadata);  
   List<String> configurations = getCandidateConfigurations(annotationMetadata, attributes);  
   configurations = removeDuplicates(configurations);  
   Set<String> exclusions = getExclusions(annotationMetadata, attributes);  
   checkExcludedClasses(configurations, exclusions);  
   configurations.removeAll(exclusions);  
   configurations = getConfigurationClassFilter().filter(configurations);  
   fireAutoConfigurationImportEvents(configurations, exclusions);  
   return new AutoConfigurationEntry(configurations, exclusions);  
}
```


#### 3. getCandidateConfigurations
```java
protected List<String> getCandidateConfigurations(AnnotationMetadata metadata, AnnotationAttributes attributes) {  
   List<String> configurations = ImportCandidates.load(AutoConfiguration.class, getBeanClassLoader())  
         .getCandidates();  
   Assert.notEmpty(configurations,  
         "No auto configuration classes found in "  
               + "META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports. If you "  
               + "are using a custom packaging, make sure that file is correct.");  
   return configurations;  
}
```


#### 4. ImportCandidates.*load*
```java title="ImportCandidates"

private static final String LOCATION = "META-INF/spring/%s.imports";

public static ImportCandidates load(Class<?> annotation, ClassLoader classLoader) {  
   Assert.notNull(annotation, "'annotation' must not be null");  
   ClassLoader classLoaderToUse = decideClassloader(classLoader);  
   String location = String.format(LOCATION, annotation.getName());  
   Enumeration<URL> urls = findUrlsInClasspath(classLoaderToUse, location);  
   List<String> importCandidates = new ArrayList<>();  
   while (urls.hasMoreElements()) {  
      URL url = urls.nextElement();  
      importCandidates.addAll(readCandidateConfigurations(url));  
   }  
   return new ImportCandidates(importCandidates);  
}
```


`AutoConfigurationEntry` 생성 과정
1.  spring-boot-autoconfigure 의 jar 파일에 위치한 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` 파일에 선언된 모든 자동 설정 클래스 목록을 로딩합니다.

2. AutoConfigurationImportFilter 에 따라 사용하지 않는 설정 클래스의 목록을 제거합니다.


3. 완성된 적용할 자동 설정 클래스의 이름 목록을 반환합니다.

AutoConfigurationImportFilter 는 Conditional 이라는 prefix 를 가지는 여러 애너테이션에 의해 설정 됩니다. 주로 다음 조건 들이 설정되어 있습니다.

- 특정 JAR 라이브러리가 클래스 패스에 포함되는지
	- `@ConditionalOnClass`, `@ConditionalOnMissingClass`
- 특정 스프링 빈이 있는지 여부
	- `@ConditionalOnBean`, `@ConditionalOnMissingBean`
- 프로퍼티 파일에 특정 변수 값이 있는지
	- `@ConditonalOnProperty`