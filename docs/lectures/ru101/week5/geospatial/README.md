---
tags: [redis, geospatial]
title: Geospatial - 지리 정보
author: ndy2
date: 2023-05-23
description: >-
  
---
 
> [!quote] 참고 자료
> - [Documentation for Geospatial commands at redis.io](https://redis.io/commands#geo)  
> - [Wikipedia article on the Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula)

### 1. Geohash

> [!quote] 참고 자료
> * [`『Geohash』`](https://en.wikipedia.org/wiki/Geohash) - on wikipedia

레디스는 지리정보 객체를 다루는 일반적인 전략을 사용합니다. 좌표의 위도와 경도 쌍에 대해 `GeoHash` 값을 계산합니다. `GeoHash` 는 레디스에서 52 bit integer 값입니다.

레디스는 `GeoHash` 값을 `Sorted Sets` 에 저장합니다.

### 2. Geo Commands

#### 2.1 GEOADD

https://redis.io/commands/geoadd/

```
GEOADD key longitude latitude member [longitude latidude member ...]
```

` ` 에 `(longitude, latitude, name)` 으로 식별되는 geospatial `item` 을 추가한다.

```
> GEOADD geopoints 139.75 35.693333 "Nippon Budokan"
(integer) 1

> GEOADD geopoints 139.76632 35666754443311 "Olympic Stadium"
(integer) 1

> GEOADD geopoints 139.640072 35.443311 "Yokohama Stadium"
(integer) 1

> ZRANGE geopoins 0 -1 withscore
1) "Yokohama Stadium"
2) "4171216862175648"
3) "Olympic Stadium"
4) "4171232605494985"
5) "Nippon Budokan"
6) "4171232800732117"
```

#### 2.2 GEOHASH & GEOPOS

```
GEOHASH key member [member ...]
GEOPOS key member [member ...]
```

- `GEOHASH` returns the GeoHash for one or more members of the set
- `GEOPOS` returns the logitude and latitude of one or more members

> [!warning] 
>  - GEOHASH 는 11자로 표현된 GeoHash 값을 반환한다.
>  - 이 값에는 precision 의 문제가 있다!
