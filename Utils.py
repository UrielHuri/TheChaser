import socket

HOST = '127.0.0.1'
PORT = 11111

def createSocket(host = HOST, port = PORT, is_server = True):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if is_server:
		sock.bind((host, port))
		sock.listen()
		print('listening on', (host, port))
	else:
		sock.connect((host, port))
		print('connected to', (host,port))

	return sock