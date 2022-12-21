@ 참고 자료)

- 쉬운코드 - [(1부) DB 정규화(normalization)는 DB를 설계하는 공식적인 방법이죠~](https://youtu.be/EdkjkifH-m8)
- 쉬운코드 - [(2부) DB 정규화(normalization) 2부입니다!!]()

!!! note

    DB 정규화를 이해하기 위해서는 [이상현상](../db-anomaly)과 [FD](../db-functional-dependency)에 관한 내용을 꼭 알고 있어야 합니다!
---

### 1. 정규화 (normalization 개념)

- 정규화 (normalization) - 데이터 중복과 insertion, update, deletion anomaly를 최소화 하기 위하여 일련의 normal forms (NF) 에 따라 RDB 를 구성하는 과정

- Normal forms (NF) - 정규화 되기 위해 준수해야 하는 몇가지 rule들

### 2. 정규화 과정

![nf.png](images/nf.png)

- 순서대로 진행한다!
- 1NF ~ BCNF 까지가 FD 와 key 만으로 정의되는 normal forms
- 3NF 까지 도달하면 정규화 됐다고 말하기도 함, 5NF 이후는 학술적인 영역
- 실무에서는 3NF, BCNF 까지 정도만 함

### 3. Init Table
![1NF.png](images/1NF.png)
자료형은 대충 넣었습니다. 정규화 중이라 안 맞는 부분이 존재합니다.
직원의 월급 계좌를 관리하는 `EMPLOYEE_ACCOUNT` 테이블을 정규화 해보자!

먼저 key 를 식별하고 그 중 primary key 를 선정해야합니다.
#### 1. 키 식별
- (candidate) key - `{account_id}, {bank_name, account_name}`
	- 요구사항에서 직원이 여러 계좌를 가질 수 있고 또 한 계좌는 여러 카드에 연동 될 수 있기 때문에 {empl_id} 와 {card_id} 는 key 가 될 수 없습니다.

- primary key - `{account_id}`
- prime attribute - `account_id`, `bank_name`, `account_name`
- non-prime attribute - `bank_name`, `class`, `ratio`, `empl_id`, `emple_name`, `card_id`

#### 2. FD 식별
주요 FD 는 아래와 같습니다.
![table-fd.png](images/table-fd.png)


### 