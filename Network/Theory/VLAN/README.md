# VLAN (Virtual Local Area Network) 
가상의 LAN 을 구성하는 기능이다.   
추가로 스위치가 필요한 작업을 vlan 을 통해 절약할 수 있다.   
예시적으로 같은 대역내에서 vlan 을 통해 서로 다른 대역처럼 취급할 수 있다.   
![vlan](./vlan.PNG)   
위 사진처럼 설정했을 때 각각 다른 vlan 으로 나눠줬기 때문에 모두 같은 대역임에도 통신이 안된다.
### VLAN Trunk 설정   
vlan 을 access 가 아닌 trunk 로 설정해주게 되면 두 스위치를 하나의 스위치처럼 취급할 수 있다.   
이 작업을 하지않으면 VLAN ID 가 같아도 물리적 위치가 다른 VLAN 이면 다르게 취급되기 때문에 이같은 상황에 사용된다.   
![vlantrunk](./trunk.png)   
┌─ *Cli* ──────────┐   
int '설정할 포트'   
switchport mode trunk
 
## VLAN Cli 명령어 
en - 권한 활성화   
vlan database - vlan 설정창   
vlan 'vlan번호' name 'vlan이름' - vlan 생성   
exit - vlan 설정창 벗어나기   
conf t - 설정 모드   
int '설정할 포트'   
switchport mode access - 태그 설정   
switchport access vlan 'vlan이름' - vlan 적용   