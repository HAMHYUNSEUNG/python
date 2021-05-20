import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 9090

def recv_msg(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        elif data.decode() == 'q':
            print("클라이언트 : ", addr, clnt_sock, "종료!")
            clnt_sock.close()
            serv_sock.close()
        print("\n상대방 : ",data.decode())


def send_msg(sock):
    while True:
        msg = input("\n나 : ")
        sock.send(msg.encode())

# 소켓 객체 생성 / IPv4, tcp 사용
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind 함수(주소할당)
serv_sock.bind((HOST, PORT))

# 접속허용
serv_sock.listen()

# accept 대기 / 접속 시 연결소켓 리턴
clnt_sock, addr = serv_sock.accept()

# 접속한 클라이언트 주소 출력
print("클라이언트 접속!\n")
print('접속 클라이언트 주소 : ', addr)



recv = threading.Thread(target=recv_msg, args=(clnt_sock,))
send = threading.Thread(target=send_msg, args=(clnt_sock,))

recv.start()
send.start()

# 클라이언트 메시지 수신대기
while True:
    time.sleep(1)
    pass

