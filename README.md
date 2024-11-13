# udp_socket

해당 코드는 jetson tx2보드에 연결된 카메라를 노트북에서 udp socket으로 실시간 스트리밍하는 코드이다.

udp socket을 구현하기 앞서 와이파이는 동일한 와이파이를 설정해야하며, server(노트북)의 IP를 찾아 client에 반영해야 한다.

server와 client로 구성된 해당 파일을 실행하기 전, udp socket에 대한 이해를 공부하는 것을 요하며 추가 첨부한 udp_server_test.py와 udp_client_test.py 파일을 꼭 실행시켜 보는 것을 추천합니다.
