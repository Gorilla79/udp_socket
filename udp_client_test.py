# Jetson TX2: udp_client_check.py

import socket
import time

# 서버 IP 주소와 포트 설정 (Windows 10의 IP 주소)
server_ip = '192.168.0.130'
server_port = 5000

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 확인 메시지 전송
message = "ping".encode()
sock.sendto(message, (server_ip, server_port))
print("Message sent to server:", message)

# 응답 대기
sock.settimeout(5)  # 5초 동안 응답 대기
try:
    data, addr = sock.recvfrom(1024)
    print("Received response from server:", data.decode())
except socket.timeout:
    print("No response from server. Check connection or server code.")
finally:
    sock.close()
