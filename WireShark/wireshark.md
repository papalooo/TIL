# 패킷 필터
## 1. 캡처 필터
> 동작 죽인 네트워크 트래픽 수집 과정에서 필터링한다.   
> 이미 수집한 추적 파일에는 적용할 수 없다.   

[Capture] -> [Options]
![capturefilter](./imgs/capturefilter.png)   
필터 입력 왼쪽에 있는 녹색 아이콘을 클릭하여 설정돼있는 필터들을 선택할 수 있다.   

   
## 2. 디스플레이 필터
> 이미 캡처된 패킷들을 핕터링한다.   
   
[Analyze] -> [Display filters]   
![displayfilter](./imgs/displayfilter.png)   
마찬가지로 필터 입력 왼쪽에 있는 파란 아이콘을 클릭하여 설정돼있는 필터들을 선택할 수 있다.   

## ※ 필터 명령 모음  
### 캡처 필터 
> dst : 목적지   
> src : 출발지    
> (위 두 명령이 없다면 모두 포함)   
> portrange : 포트의 범위를 지정 
> not : 특정 패킷을 제외한 모든 패킷
> and, or : 필터를 and, or 할 수 있음
### 디스플레이 필터
> ip.addr/src/dst : ip 주소 / 출발지의 ip 주소 / 목적지의 ip 주소   
> .port : 포트   
> .dstport : 목적지의 포트
> .flags : 특정 플래그를 가지고있는 패킷 지정
> .flags.syn : 0x02 [] syn 플래그를 가지고있는 패킷 지정