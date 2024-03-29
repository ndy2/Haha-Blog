---
tags: [architecture, load-balancing]
title: L4 LB vs L7 LB
date: 2023-02-23
---

### 0. 들어가며

로드 밸런싱은 로드 밸런싱의 기준이 되는 요소의 OSI 7 Layer 에서의 위치를 기준으로 *`전송 계층 로드 밸런싱`* 과 *`응용 계층 로드 밸런싱`*으로 구분됩니다. 오늘은 이 둘을 비교하며 알아보겠습니다.

### 1. 전송 계층 로드 밸런싱

- L4 로드 밸런서는 NAT를 수행하고 보통 IP 를 기준으로 로드밸런싱을 수행합니다.
- 흔히 하드웨어 적으로 구현됩니다.
- 컴퓨팅 파워가 좋지 않고 섬세한 로드밸런싱에 대한 수요가 없던 과거에 널리 활용되었습니다.
- 기본적으로 패킷 단위로 로드밸런싱이 이루어 지기 때문에 패킷 단편화 (fragmentation)에 따라 요청의 맥락을 파악하기 어려울 수 있습니다.

### 2. 응용 계층 로드 밸런싱

- OSI 7 계층 중 가장 높은 응용 계층의 정보를 모두 활용하여 로드밸런싱을 수행합니다.
- 요청 url, 헤더, 쿠키 정보등 http 의 헤더를 활용한 로드밸런싱이 가능합니다.
- 패킷 합치기 (defragmentation)이 발생한 이후에 요청 단위로 로드 밸런싱을 수행할 수 있습니다.
- 7 계층 까지 decapsulation 을 수행 한 다음 로드 밸런싱을 하므로 성능상 단점이 있을 수 있지만 현대 컴퓨터의 컴퓨팅 파워와 응용 계층의 정보를 통해 수행할 수 있는 섬세한 로드 밸런싱을 고려할때 크게 문제가 되지 않습니다.
- Layer 7 로드밸런싱을 제공하는 기기를 흔히 ***reverse-proxy server*** 라고 부릅니다.
