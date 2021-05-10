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
        print('상대방 : ', recvData.decode('utf-8'))


port = 8088
clientSoc = socket(AF_INET,SOCK_STREAM)
clientSoc.connect(('127.0.0.1', port))

# 클라이언트에선 bind 와 listen, accept 과정이 빠지고 대신
# connect 가 추가 되었다. 
# 클라이언트 -> 서버 의 접속을 위해 connect() 를 실행
# 인자는 AF 

print('클라이언트측에서 서버와 연결에 성공했습니다.')

sender = Thread(target=send, args=(clientSoc,))
receiver = Thread(target=receive, args=(clientSoc,))

sender.start()
receiver.start()

while True :
    time.sleep(1)
    pass