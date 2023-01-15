@ 참고 자료)

- 쉬운코드 - [(1부) DB 정규화(normalization)는 DB를 설계하는 공식적인 방법이죠~](https://youtu.be/EdkjkifH-m8)
- 쉬운코드 - [(2부) DB 정규화(normalization) 2부입니다!!]()


---

### 3. 3NF

> 모든 non-prime attribute 는 어떤 key에 대해서도 Transitive FD 가 존재하면 안된다.
> or non-prime attribute 와 non-prime attribute 사이에는 FD 가 있으면 안된다.
> 
> Transitive FD
> if X -> Y & Y -> Z holds, then X -> Z holds 
> unless either Y or Z is NOT subset of any key

- 2NF 까지 적용한 상태의 테이블 구조
![after-2nf.png](after-2nf.png)

살펴보면 (e1, Sony) 튜플이 중복으로 존재한다는 사실을 알 수 있습니다.

그 이유는 Transitive FD 때문입니다.
이 테이블에 존재하는 Transitive FD 는 아래와 같습니다.

1. `{account_id}` -> `{empl_id}` -> `{empl_name}`
2. `{bank_name, account_name}` -> `{empl_id}` -> `{empl_name}`


Employee 테이블을 분리하여 3NF 를 만족하도록 변경하면 아래와 같습니다.
![after-3nf.png](after-3nf.png)


### 3.5 BCNF
> 모든 유효한 non-trivial FD X -> Y 에 대해서 X 는 super key 여야 한다.

EMPLOYEE_ACCOUNT 테이블의 {class} -> {bank_name} FD 는 위 제약사항을 위반합니다!
class 의 값인 BRONZE, LOYAL 만으로는 tuple 을 식별할 수 없습니다.

테이블을 나누어 BCNF 를 만족하도록 변경해보면 아래와 같습니다.
![after-bcnf.png](after-bcnf.png)

### 4. 역정규화

- 테이블을 너무 잘게 나누면 join 시 성능상 이슈도 있고 관리가 힘들 수 있기 때문에 전략적으로 테이블을 합치는 것