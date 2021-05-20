import socket
import select
import sys

HOST = '127.0.0.1'
PORT = 9090

#소켓 객체 생성
clnt_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#지정한 HOST와 PORT를 사용하여 서버에 접속
clnt_sock.connect((HOST,PORT))

print("채팅방에 입장했습니다! 서버에게 물어보세요!(나가기 : q)")

while True:
    read, write, fail = select.select((clnt_sock,sys.stdin),(),())

    for desc in read:
        if desc == clnt_sock:
            data = clnt_sock.recv(1024)
            print('서버 메시지 : ', data.decode())
        else:
            clnt_msg = desc.readline()
            clnt_sock.sendall(clnt_msg.encode())


#소켓 종료
clnt_sock.close()
