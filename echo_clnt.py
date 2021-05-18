import socket

HOST = '127.0.0.1'
PORT = 9090

#소켓 객체 생성
clnt_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#지정한 HOST와 PORT를 사용하여 서버에 접속
clnt_sock.connect((HOST,PORT))

print("채팅방에 입장했습니다! 서버에게 물어보세요!(나가기 : q)")

while 1:
    # 사용자에게 메시지 받기
    clnt_msg = input("\n나 : ")
    #메시지 전송
    if clnt_msg =='q':
        clnt_sock.sendall("q".encode())
        break
    clnt_sock.sendall(clnt_msg.encode())

    #서버로부터 에코 메시지 수신
    data = clnt_sock.recv(1024)
    #수신 메시지 출력
    print('서버 메시지 : ', data.decode())


#소켓 종료
clnt_sock.close()
