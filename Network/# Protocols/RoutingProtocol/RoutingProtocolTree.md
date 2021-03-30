# 1. Static Routing Protocol   
- 장점 : 수동식, 라우터 부하경감, 고속 라우팅 가능   
- 단점 : 관리자의 부담증가, 경로 문제 바랭시 라우팅 불가능   
- - -
# 2. Dynamic Routing Protocol   
- 장점 : 라우터가 스스로 라우팅 경로를 결정
- 단점 : 라우터의 부하가 큼   
## 2-1. IGP (Interior Gateway Protocol)    
- AS 내에서의 라우팅을 담당하는 라우팅 프로토콜   
- 종류 : RIP, IGRP, OSPF, EIGRP   
### 2-1-1. Distance Vector Algorithm   
- 라우팅 Table 에 목적지까지 가는데 필요한 거리와 방향만을 기록한다 
- 종류 : RIP, IGRP
### 2-1-2. Link State Algorithm   
- 라우터가 목적지까지 가는 경로를 SPF 알고리즘을 통해 모든 라우팅 테이블에 기록해 두는 것
## 2-2. EGP (Exterior Gateway Protocol)   
- 서로 다른 AS사이에서 사용되는 라우팅 프로토콜   
- 종류 : BGP