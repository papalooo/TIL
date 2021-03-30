# [EIGRP](https://ko.wikipedia.org/wiki/EIGRP) (Enhanced Interior Gateway Routing Protocol)
거리 벡터 라우팅 프로토콜이다.   
EIGRP 는 Helllo 패킷을 인접 라우터와 서로 교환 한 후 Neighbor(이웃) 관계를 맺고 테이블을 생성한다. 패킷이 일정시간동안 응답이 없으면 장애로 판단하고 해당 라우터와 관계를 끊습니다.    
그 외에는 라우팅 정보를 요청하는 Query 패킷과 라우팅 정보를 전달하는 Update 패킷,   
Query 패킷을 수신한 라우터가 요청받은 라우팅 정보를 전송하는 Reply 패킷,   
각각의 패킷에 대해 응답해주는 Ack 패킷이 있다.   
Update 패킷을 통해 라우팅 정보가 저장된 Topology 테이블이 생성되면 이 테이블의 정보로 최단 경로를 라우팅 테이블에 저장한다.
### + 5개의 메트릭 가중치
EIGRP 는 대역폭(K1, Bandwidth), 부하(K2, Load), 지연(K3, Delay), 신뢰성(K4 K5, Reliability) 5개의 메트릭 가중치가 존재한다.   
K1과 K3 는 디폴트로 1의 값을 갖는다. K2는 부하(Load), K4와 K5는 신뢰성(Reliability)메트릭과 관계되는 가중치로써 디폴트로 0의 값(0~255)을 갖는다.   
메트릭 계산식 = [K1 * 대역폭 + (K2*대역폭) / (256-부하) + K3 * 지연] * [K5 / (신뢰도 + K4)]   
## EIGRP Cli 명령어 
en - 권한 활성화   
conf t - 설정모드   
router eigrp 'Process id' - eigrp 프로토콜을 사용하겠다고 선언 (번호)   
net '인접 네트워크 주소' - 라우팅(루프백 도)   
no auto-summary - 자동 요약 기능 해제   