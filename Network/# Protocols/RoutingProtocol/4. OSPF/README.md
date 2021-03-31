# [OSPF](https://ko.wikipedia.org/wiki/%EC%B5%9C%EB%8B%A8_%EA%B2%BD%EB%A1%9C_%EC%9A%B0%EC%84%A0_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C) (Open Shortest Path First)    
## OSPF 는 링크 스테이트 라우팅 프로토콜이다.
- ### SPF 알고리즘이나 Dijkstra 알고리즘을 이용해 최단 경로를 계산한다.   
- ### OSPF 설정시 사용되는 Process-ID 는 인접 라우터 사이에서 서로 일치하거나 불일치하는  경우에도    Neighbor(이웃) 관계를 형성하고 교환하는 것이 가능하다.
- ### Auto Summary(자동 축약)가 없기 때문에 OSPF 설정시에는 반드시 Wildcard Mask 를 써야한다.
- ### Router-ID 는 IPv4 의 형태를 갖지만 실제 IP 주소와 관련이 없다. (구분감을 위해서이기 때문에 다른 IP 주소를 사용해도 상관없다)     하지만 인접 라우터와 동일한 Router-ID를 사용해선 안된다.
## OSPF 패킷 종류
### Hello 패킷
- EIGRP 와 마찬가지로 인접 OSPF 라우터와 Hello 패킷을 교환하여 Neighbor(이웃) 관계를 형성하고, 주기적으로 교환하며 Keepalive를 확인한다.
### DBD (Database Description) 패킷
- EIGRP 와 다른점은 Adjacent Neighbor 관계를 형성한 OSPF 라우터들은 LSDB의 모든 정보를 Update 하는  것이 아니라 요약된 목차 정보들만 먼저 상대방 장비에게 전송하게 된다.   
이때 요약된 LSDB의 정보가 들어있는 패킷이 DBD 패킷이다.
### LSR (Link State Request)   
- 상대방 장비로부터 수신한 DBD 정보와 자신의 LSDB의 정보를 비교한 후 자신의 LSDB에 없는 정보가 상대방 장비에게 있다고 확인되면 해당 정보에 대해서 상세한 내용을 부탁하는 패킷
### LSU (Link State Update)
- 상대방 장비로부터 LSR을 수신할 경우 요청받은 정보의 상세 내용을 Update 할 때 사용되는 패킷
### LSAck
- OSPF 패킷의 수신 여부를 상대방 장비에게 확인시켜주기 위한 목적의 패킷
## OSPF 라우터 종류
- ### ABR (area border router, 영역 경계 라우터)   
- ### ASBR (autonomous system boundary router, 자율 시스템 경계 라우터)   
- ### IR (internal router, 내부 라우터)   
- ### BR (backbone router, 백본 라우터)   
## OSPF Cli 명령어   
en　-　권한 활성화  
conf t　-　설정모드   
router ospf 'Process id'　-　ospf 프로토콜 사용 선언 (번호)   
router-id '루프백주소' - 라우터의 id 를 루프백 주소로 지정  
net '네트워크주소' '와일드마스크' area area-id　-　같은 id 영역으로 구성한 것을 단일 영역 OSPF 라 하고 2개 이상의 id 영역으로 구성한 것을 다중 영역 OSPf 라고한다.   
