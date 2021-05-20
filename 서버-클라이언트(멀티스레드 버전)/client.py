import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 9090

def recv_msg(sock):
    while True:
        data = sock.recv(1024)
        print("\n상대방 : ",data.decode())


def send_msg(sock):
    while True:
        msg = input("\n나 : ")
        if msg == 'q':
            clnt_sock.sendall("q".encode())
            print("종료 goodbye~")
            clnt_sock.close()
        sock.send(msg.encode())

#소켓 객체 생성
clnt_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#지정한 HOST와 PORT를 사용하여 서버에 접속
clnt_sock.connect((HOST,PORT))

print("채팅방에 입장했습니다! 서버에게 물어보세요!(나가기 : q)")

recv = threading.Thread(target=recv_msg, args=(clnt_sock,))
send = threading.Thread(target=send_msg, args=(clnt_sock,))

recv.start()
send.start()

# 클라이언트 메시지 수신대기
while True:
    time.sleep(1)
    pass

