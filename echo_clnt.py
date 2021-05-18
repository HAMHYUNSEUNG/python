import socket

HOST = '127.0.0.1'
PORT = 9090

#소켓 객체 생성
clnt_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#지정한 HOST와 PORT를 사용하여 서버에 접속
clnt_sock.connect((HOST,PORT))

#메시지 전송
clnt_sock.sendall('echo test!'.encode())

#서버로부터 에코 메시지 수신
data = clnt_sock.recv(1024)
#수신 메시지 출력
print('server echo message : ', repr(data.decode()))

#소켓 종료
clnt_sock.close()
