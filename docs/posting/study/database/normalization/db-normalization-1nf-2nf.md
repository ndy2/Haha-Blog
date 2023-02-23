---
tags: [db, db-normalization]
title: 1NF & 2NF
author: ndy2
---
 
> [!quote] 참고 자료
> * 쉬운코드 - [(1부) DB 정규화(normalization)는 DB를 설계하는 공식적인 방법이죠~](https://youtu.be/EdkjkifH-m8)
> * 쉬운코드 - [(2부) DB 정규화(normalization) 2부입니다!!]

### 1. 1NF
> attribute 의 value 는 반드시 나누어 질 수 없는 단일한 값이어야 한다.

![[images/before-1nf.png]]
card_id 에트리뷰트가 두개의 카드번호를 하나의 값으로 표현하고 있습니다. row 를 분리하는 방식으로 1NF 를 만족하도록 변경하면 아래와 같은 테이블이 나옵니다.

![[images/after-1nf.png]]

- 중복 데이터가 생겼습니다.
- ratio 의 개념이 이상해 졌습니다. (한 직원에 대해서 합이 2가되었습니다.)
- PK 에도 변경이 필요해 졌습니다.


### 2. 2NF

> `non-prime attribute set` 은 모든 `candidate key` 에 `fully functional dependent` 해야 한다.


card_id 를 분리해서 테이블에 저장함으로써 기존의 `{account_id}`, `{bank_name, account_num}` 은 candidate key 로 동작할 수 없습니다. 모두 `card_id` 까지 포함되어야 tuple을 유일하게 결정하는 candidate key 가 될 수 있습니다.

따라서 prime attribute set 과 non-prime attribute set 에도 변경이 생겼습니다.

변경된 non-prime attribute set 은 card_id 가 빠진 `{class, ratio, empl_id, empl_name}` 입니다.
그럼 모든 후보 키 `{account_id, card_id}`, `{bank_name, account_num, card_id}` 가 non-prime attribute set  `{class, ratio, empl_id, empl_name}` 를 fully functional determine 하는지 살펴보면 그렇지 않습니다.

FD 를 결정할때는 항상 의미론적으로 접근해야 한다는 사실을 주의해야합니다. 생각해보면 두 후보키에서 모드 card_id 가 없이 기존의 `{account_id}`, `{bank_name, account_num}` 만으로 non-prime attribute 를 determine 할 수 있다는 사실을 알 수 있습니다. 따라서 card_id 가 빠지는 것이 자연스럽습니다. 이를 위해 아래와 같이 테이블을 분리해 보겠습니다.


![[images/after-2nf.png]]
확인해보면 두테이블 모두 2NF 를 만족 한다는 것을 알 수 있습니다.

`ACCOUNT_CARD` 테이블은 후보 키를 {account_id, card_id} 로 가집니다. (계좌 하나가 여러 카드에 연동될 수 있다는 사실을 잊지 말아 주세용) 따라서 non-prime attribute 는 공집합이고 2NF 를 만족한다는 것은 trivial 합니다.
