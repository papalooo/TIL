# Network
## [AS](https://ko.wikipedia.org/wiki/%EC%9E%90%EC%9C%A8_%EC%8B%9C%EC%8A%A4%ED%85%9C) (Autonomous System)   
한 단체에서 관리되고 제어되며, 동일한 라우팅 정책을 사용하는 네트워크 그룹을 말한다.
## [Collision Domain](https://en.wikipedia.org/wiki/Collision_domain)
둘 이상의 장치가 네트워크 세그먼트에서 동시에 패킷을 보내려고 할 때 네트워크 충돌이 발생한다.   
<br>

# [Ethernet Frame](https://en.wikipedia.org/wiki/Ethernet_frame) - Elements   
## **Preamble**
>### Ethernet v2 표준
>- 송신측과 수신측의 비트 동기화를 위해 사용   
>- 상위 7byte : 비트 동기화를 위한 10101010 비트열 전달   
>- 하위 1byte : 프레임 시작을 알리는 10101011 비트열 전달
>- Preamble 크기는 Frame header 크기 게산 시 제외한다.
>- 크기 8byte   
>### IEEE 802.3 CSMA/CD 표준   
>- 송신측과 수신측의 비트 동기화를 위해 사용   
>- 전체 byte : 10101010 비트열을 전달
>- 크기 7byte   
## **SFD** (Start Frame Delimeter)   
>- 프레임의 시작을 알리는 1byte 로 이루어짐
>- 1byte = 10101011   
>- IEEE 802.3 표준에서는 8byte 의 Preamble 을 7byte 의 Preamble 과 1byte 의 SFD로 분리하였다.   
>- 크기 1byte
## **DA** (Destination Address)   
>- 목적지의 2계층 주소를 나타낸다.   
>- 6byte 주소의 첫번째 비트만 '1' 이면 MultiCast 를 의미한다.   
>- 6byte 주소의 모든 비트가 '1' 이면 BroadCast 를 의미한다.   
>- 크기 6byte   
## **SA** (Source Address)   
>- 출발지의 2계층 주소를 나타낸다.   
>- 크기 6byte   
## **Type**/Length   
>### IEEE 802.3 CSMA/CD 표준   
>- MAC 프레임 정보의 길이를 표시하는 영역 (Length)   
>- 크기 2byte
>### Ethernet v2 표준   
>- Mac 프레임 데이터 부분에 실려있는 상위계층의 프로토콜 종류를 표시하는 영역 (Type)   
>- 크기 2byte   
>
> ### 표준 구분 방법 (수신된 프레임의 해당 영역값)    
>- 0x0600 이상이면 Ethernet v2 의 Type 으로 해석하고   
>- 0x0600 미만이면 IEEE 802.3 의 Length 로 해석한다.    
## **Data** (=Payload)
>- 상위 계층으로부터 받은 데이터 or 상위 계층에 전달할 데이터   
>- 최대크기 : 1500byte , 최소크기 : 46byte
>- 만약 데이터 크기가 최소크기인 46byte 보다 작을 땐, padding 영역을 추가하여 46byte 로 만든다. (padding 영역은 0 으로 채워짐)   
> > ### IEEE 802.3 CSMA/CD   
> > IEEE 802.3 에선 Data 부분에는 아래의 항목이 크기만큼 대체된다.   
> > ### **DSAP** (1byte)   
> > - Destination Service Access Point   
> > - 목적지에서 확인 할 상위 계층 프로토콜 정보   
> > ### **SSAP** (1byte)   
> > - Source Service Access Point   
> > - 출발지에서 확인 할 상위 계층 프로토콜 정보   
> > ### **Ctrl** (1~2byte)   
> > - 네트워크 환경 제어 값   
> > ### **OUI** (3byte)   
> > - MAC 주소의 OUI 만 추출하여 명시 함   
> > ### **Type** (2byte)   
> > - DSAP, SSAP 로 표현할 수 없는 상위 계층의 프로토콜 종류를 정확하게 명시 함   
> > ### **~1500byte = Data**
## **FCS** (Frame Check Sequence)   
>- Preamble 과 FCS 부분을 제외한 유효한 MAC Frame 의 비트열에서 오류를 검사한다.   

## **CRC** (Cyclic Redundancy Check)
>- 송신측의 데이터로부터 다항식에 의해 추출된 결과를 여분의 오류검사필드(FCS)에 덧븉여 보내면 수신측에서는 동일한 방법으로 추출한 결과와의 일치성으로 오류검사를 하는 방식   

- - -
## [SPF](https://networkencyclopedia.com/shortest-path-first-spf/) (Shortest Path First)
SPF 알고리즘은 Dijkstra 알고리즘으로도 불린다.   
이 알고리즘은 목적지까지의 최단 경로 트리를 만드는 알고리즘이다.   
