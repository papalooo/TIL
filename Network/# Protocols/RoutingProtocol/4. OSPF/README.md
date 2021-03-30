# [OSPF](https://ko.wikipedia.org/wiki/%EC%B5%9C%EB%8B%A8_%EA%B2%BD%EB%A1%9C_%EC%9A%B0%EC%84%A0_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C) (Open Shortest Path First)    
## OSPF 는 링크 스테이트 라우팅 프로토콜이다.
SPF 알고리즘이나 Dijkstra 알고리즘을 이용해 최단 경로를 계산한다.
## OSPF Cli 명령어   
en　-　권한 활성화  
conf t　-　설정모드   
router ospf 'Process id'　-　ospf 프로토콜 사용 선언 (번호)   
router-id '루프백주소' - 라우터의 id 를 루프백 주소로 지정  
net '네트워크주소' '와일드마스크' area area-id　-　같은 id 영역으로 구성한 것을 단일 영역 OSPF 라 하고 2개 이상의 id 영역으로 구성한 것을 다중 영역 OSPf 라고한다.   
