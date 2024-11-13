# Windows 10: video_receiver.py

import cv2
import socket
import numpy as np

# 수신할 포트 설정
local_ip = '0.0.0.0'  # 모든 IP에서 수신
local_port = 5000

# UDP 소켓 생성 및 바인딩
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((local_ip, local_port))

print("Listening for incoming video stream...")

buffer = b''  # 수신 데이터 버퍼

while True:
    # 데이터 수신 (버퍼 크기는 UDP 패킷의 최대 크기에 맞춰 설정)
    packet, _ = sock.recvfrom(65507)
    buffer += packet
    
    # 버퍼가 충분히 쌓였을 때 프레임 복원
    if len(buffer) > 10000:  # 프레임의 예상 크기에 따라 임의의 임계값을 설정 (예: 10,000 바이트 이상)
        # JPEG 이미지 디코딩
        frame_data = np.frombuffer(buffer, dtype=np.uint8)
        frame = cv2.imdecode(frame_data, cv2.IMREAD_COLOR)
        
        # 프레임을 화면에 표시
        if frame is not None:
            cv2.imshow("Video Stream", frame)
        
        buffer = b''  # 버퍼 초기화

    if cv2.waitKey(1) == 27:  # ESC 키로 종료
        break

sock.close()
cv2.destroyAllWindows()
