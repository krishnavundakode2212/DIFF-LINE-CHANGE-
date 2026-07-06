import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 8080))

message = client.recv(1234)

print(message.decode())

client.close()
