---
tags: [hussein, protocol, network]
title: Section3 - Protocols
author: ndy2
date: 2023-05-01
description: >-
  
---

### 1. Protocol Properties

> [!note] What is a protocol?
> - a system that allows two parties to communicate
> - a protocol is designed with a set of properties
> - depending on the purpose of the protocol
> - TCP, UDP, HTTP, gRPC, FTP

> [!note] Protocol properties
> - Data format
>     - Text based (plain text, JSON, XML)
>     - Binary (protobuf, RESP, h2, h3)
> - Transfer mode
>     - Message based (UDP, HTTP)
>     - Stream based (TCP, WebRTC)
> - Addressing system
>     - DNS name, IP, MAC
> - State
>     - Stateless (TCP, gRPC, apache thirft)
>     - Stateless (UDP, HTTP)
> - Routing
>     - Proxies, Gateways
> - Flow & Congestion control
>     - TCP (Flow & Congestion control)
>     - UDP (No control)
> - Error management
>     - Error code
>     - Reties and timeouts

### 2. OSI Model

#### 0. 들어가며

여러 선배 개발자/ 강사들이 OSI 모델에 대해 자신의 인사이트를 공유하는 영상을 많이 보았었다. 후세인의 인사이트 중 가장 독특한 점은 `TCP/IP 모델`이 아닌 전통적인 `OSI 7 layer 모델`을 선호하고 그 이유가 상당히 그럴듯 하다는 것이다. 대부분의 최근 영상에서 `OSI 7 layer 모델`의 윗 세 계층을 하나의 Application 계층으로 이해하는 `TCP/IP 모델`을 이야기 하는것에 비해 상당히 대조적이다.

#### 1. OSI Model

> [!note] OSI Model - Open System Interconnection Model
> - Layer 7 - Application - HTTP/FTP/gRPC
> - Layer 6 - Presentation - Encoding, Serialization
> - Layer 5 - Session - Connection establishment, TLS
> - Layer 4 - Transport - UDP/TCP
> - Layer 3 - Network - IP
> - Layer 2 - Data Link - ARP, MAC Address, Frames, Ethernet
> - Layer 1 - Physical - Electric signals, fiber or radio waves

> [!note] Communication Model 이 필요한 이유
> - Agnostic Application
> - Network Equipment Management
> - Decoupled Innovation
>   
> - 즉, 모델(medium)에 구애받지 않는 애플리케이션/ 물리적인 장비의 관리 등 모든 계층의 커플링을 낮추어 개별적인 업그래이드가 가능하도록 하기 위해 `Communication Model` - 계층별 모델이 필요하다.

### 2. Internet Protocol

> [!note] IP Address
> - Layer 3 protocol
> - Can be set automatically or statically
> - Network and Host portion
> - 4 byte in IPv4 - 32 bits

> [!note] Network vs Host
> - `a.b.c.d/x`
>     - e.g. `192.168.254.0/24`
> - The first 24 bits are network, the rest 8 are for host

> [!note] Subnet Mask
> - `192.168.254.0/24` is also called a subnet
> - The subnet has a mask `255.255.255.0`
> - Subnet mask is used to determine whether an IP is in the same subnet

#### IP Packet 뿌시기

- IP Packet = Headers + Data Sections
- Header 는 기본적으로 20 bytes (option 을 키면 최대 60 바이트)
- Data Section 은 최대 65536 바이트
    - 하지만 현실에서는 MTU 에 따라 평균적으로 1500 바이트를 가진다.

### 3. ICMP

  

### 4. UDP

> [!note]
> - UDP = User Datagram Protocol
> - Layer 4 Protocol
> - Simple protocol to send and receive data
> - No Handshakes
> - Stateless
> - 8 byte header

> [!example] UDP Use cases
> - Video streaming
> - VPN
> - DNS
> - WebRTC


