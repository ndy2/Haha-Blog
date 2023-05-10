---
tags: [db]
title: Join
author: ndy2
---
 
> [!quote] 참고 자료
> * 쉬운 코드 - [join 의 의미와 여러 종류 ...](https://www.youtube.com/watch?v=E-khvKjjVv4)

### Join 의 의미

* 두 개 이상의 table 들에 있는 데이터를 한번에 조회 하는것

---

### Implicit Join

```mysql
SELECT D.name
FROM employee AS E, department AS D
WHERE E.id = 1 and E.dept_id = D.id;
```

* from 절에는 테이블들만 나열 하고 where 절에 join condition 을 작성함
* old-style join syntax
* join 이 명시적이지 않음, join condition 이 selection condition 과 함께 작성됨

---

### Explicit Join

```mysql
SELECT D.name
FROM employee AS E JOIN department AS D
ON E.dept_id = D.id
WHERE E.id = 1;
```

* from 절에 JOIN 키워드와 함께 joined table 들을 명시함
* from 절의 ON 뒤에 join condition 작성

---

* 예시 테이블

![[images/table-ex.png]]

---

### Inner Join

```mysql
SELECT *
FROM employee E (INNER) JOIN department D
ON E.dept_id = D.id;
```

* JOIN 이라고만 쓰면 자연스럽게 inner join 임
* 두 테이블에서 join 컨디션을 만족 (`true`) 하는 tuple 만 선택한다.
	* 3-valued-logic 결과가 `unknown` 혹은 `false` 인 tuple 은 선택하지 않는다.
* join 컨디션에서는 `=` 뿐만이 아니래 `<`, `>`, `!=` 등 여러가지 연산자를 선택할 수 있다.
* 결과

![[inner-join.png]]

### Outer Join

```mysql
SELECT *
FROM employee E LEFT (OUTER) JOIN department D
# FROM employee E RIGHT (OUTER) JOIN department D
# FROM employee E FULL (OUTER) JOIN department D
ON E.dept_id = D.id;
```

* LEFT JOIN, RIGHT JOIN, FULL JOIN 만 작성해도 된다.
* 두 테이블에서 join 컨디션을 만족 (`true`) 하지 않는 tuple 도 선택한다.
* join 컨디션에서는 `=` 뿐만이 아니래 `<`, `>`, `!=` 등 여러가지 연산자를 선택할 수 있다.
* LEFT OUTER JOIN 결과 
	* Left Table 즉, Employee 테이블의 모든 튜플을 포함한다.
	* 다른쪽 테이블 즉, Deplartment 테이블의 에트리뷰트는 null 로 채운다.

![[images/left-outer-join.png]]

> [!note]
> mysql 은 Full Outer Join 을 지원하지 않는다.

---

### Equi Join

* join condition 에 `=` 을 사용한 join

### Using

* 애트리뷰트의 이름이 같으면 그 애트리뷰트의 equal 조건을 join condition 으로 활용하라는 키워드
* Result Table 에도 해당 애트리뷰트는 한번만 표시된다.

```mysql
SELECT * FROM employee E INNER JOIN department D ON E.dept_id = D.dept_id;
SELECT * FROM employee E INNER JOIN department D USING (dept_id)
```

---

### Natural Join

* 두 테이블에서 같은 이름을 가지는 모든 attribute pair 에 대해 equi join 을 수행
* join condition 을 명시하지 않음
* 같은 이름을 가지는 모든 attribute pair 에 대해 USING 키워드를 사용하는 꼴임

> [!example]
> * FROM table1 NATURAL [INNER] JOIN table2;
> * FROM table1 NATURAL LEFT [OUTER] JOIN table2;
> * FROM table1 NATURAL RIGHT [OUTER] JOIN table2;
> * FROM table1 NATURAL FULL [OUTER] JOIN table2;

### Cross Join

* 두 테이블이 가질 수 있는 모든 tuple pair 의 조합 (Cartesian product) 을 result table 로 반환
* join condition 이 없음

### 실습

http://sqlfiddle.com/#!9/328b5c/5
