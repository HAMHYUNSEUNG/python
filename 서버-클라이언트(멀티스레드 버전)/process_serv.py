import socket
import multiprocessing as mp


HOST = '127.0.0.1'
PORT = 9090

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

def recv_msg():
    data = clnt_sock.recv(1024)
    print(data)
    print('test 1')

def send_msg():
    msg = input("나 : ")
    clnt_sock.sendall(msg.encode())
    print('test 2')

# 클라이언트 메시지 수신대기
while True:
    p = mp.Process(name="subprocess", target= recv_msg())

    while True:
        send_msg()
        send_msg()



# 소켓닫기
clnt_sock.close()
serv_sock.close()
