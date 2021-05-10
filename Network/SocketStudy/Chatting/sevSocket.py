from socket import * 
from threading import *
import time


def send(sock) :
    while True :
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock) :
    while True :
        recvData = sock.recv(1024)
        print('상대방 : ',recvData.decode('utf-8'))


sevSoc = socket(AF_INET, SOCK_STREAM)

# 1번 인자 : AF(Address Family) - 주소체계
# ex) AF_INET : IPv4 프로토콜

# 2번 인자 : Socket Type
# 연결 지향형 소켓이다.
# 소켓과 소켓이 계속 연결되어있는 상태를 유지한다.
# 특징은 소켓과 소켓의 연결은 1 vs 1이다.
# 순차적인 바이트 기반의 연결지향 데이터 전송 방식의 소켓
port = 8088
sevSoc.bind(('',port)) # 서버 운영시 필수 
# bind : 소켓과 AF를 연결하는 과정
# 앞부분 ip, 뒷부분 포트의 형식으로 튜플로 전달해야함
# AF_INET 에서 '' 는 INADDR_ANY 이다 - 모든 인터페이스와 연결

sevSoc.listen(1)
print(str(port),'번 포트로 접속 대기중...')
# listen : 상대방의 접속을 기다리는 단계
# 인자 : 총 몇개의 동시접속을 허용할지

connectionSoc, addr = sevSoc.accept()
# 소켓에 누군가 접속하면 새로운 소켓과 상대방의 AF 를 전달

print(str(addr),'에서 접속이 확인되었습니다.')


sender = Thread(target=send, args=(connectionSoc,))
receiver = Thread(target=receive,args=(connectionSoc,))
# 1번인자 : 스레드가 실행할 함수
# 2번인자 : 함수의 인자(튜플) - 인자가 하나일시 var로 취급되기 때문에 , 를 붙여준다

sender.start()
receiver.start()
# 스레드 시작

while True :
    time.sleep(1) # 과부화 방지
    pass
