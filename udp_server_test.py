# Windows 10: udp_server_check.py

import socket

# 수신 IP 주소와 포트 설정
local_ip = '0.0.0.0'  # 모든 IP에서 수신
local_port = 5000

# UDP 소켓 생성 및 바인딩
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((local_ip, local_port))

print("Server is listening for incoming messages...")

while True:
    # 메시지 수신
    data, addr = sock.recvfrom(1024)
    print("Received message from client:", data.decode())

    # 응답 전송
    response = "pong".encode()
    sock.sendto(response, addr)
    print("Response sent to client:", response)
