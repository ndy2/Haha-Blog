---
tags: [spring, spring-data-jpa]
title: Repository Hierarchy
author: ndy2
date: 2023-03-23
description: >-
  
---
 
 
> [!quote] 참고 자료
> * spring-data jpa documentation - [Hierarchy for Packages](https://docs.spring.io/spring-data/jpa/docs/current/api/org/springframework/data/jpa/repository/package-tree.html)org.springframework.data.jpa.repository
> * [CrudRepository, JpaRepository, and PagingAndSortingRepository in Spring Data](https://www.baeldung.com/spring-data-repositories) on baeldung
> * [Announcing ListCrudRepository & Friends for Spring Data 3.0](https://spring.io/blog/2022/02/22/announcing-listcrudrepository-friends-for-spring-data-3-0)

### 1. Repsitory Interface Hierarchy

* Spring Data 3.0 이 되면서 인터페이스의 상속 계층 구조가 크게 업데이트 되었습니다.
* 아래 그림을 통해 이해해봅시다.

![[repository-hierarchy.excalidraw.png]]

### 2. `@NoRepositoryBean` & `@RepositoryDefinition`

위 그림을 보면 익숙하지 않은 애너테이션들이 눈에 띕니다. Spring 5 에 추가된 stereotype annotation 인 @Indexed 에 대해서는 다음에 알아보겠습니다. 이번 시간에는 `org.springframework.data.repository` 패키지의 두가지 애너테이션인 `@NoRepositoryBean` & `@RepositoryDefinition` 에 대해서 알아보겠습니다.

#### `@NoRepositoryBean`

먼저 요 녀석이 등장하는 곳을 살펴보면 Repository 인터페이스를 상속한 인터페이스에서 등장한다는 사실을 알 수 있습니다. 요 녀석이 적용된 인터페이스는 직접적으로 빈이 생성되지 않습니다. 즉 이름 그대로 No-Repository-Bean 입니다.

spring-data, data-jpa 가 메서드 이름을 통해 바이트코드 조작으로 구현체를 생성해야 한다는 사실을 떠올리면 빈이 생성되면 안되는 이유를 알 수 있습니다.

@NoRepositoryBean 을 아래와 같이 직접 활용 할 수도 있습니다.

```java
@NoRepositoryBean
public interface ProductDao extends JpaRepository<Product, Long> {}

public interface ProductDaoChild extends ProductDao {
	Product findByname(String name);
}
```

#### `@RepositoryDefinition`

@RepsotiroyDefinition 는 domainClass 와 idClass 엘리먼트를 통해 인터페이스의 상속 없이 spring 이 리포지토리 구현체의 맥락을 이해할 수 있도록 도와줍니다.

```java
@RepositoryDefinition(domainClass = Comment.class, idClass = Long.class) 
public interface CommentRepository { 
	Comment save(Comment comment); 
	List<Comment> findAll(); 
}
```
