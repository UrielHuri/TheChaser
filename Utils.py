import socket

HOST = '127.0.0.1'
PORT = 11111

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1200

# TO DELETE
def getAttr(d):
	for key in d:
		print(f'{key} : {d[key]}')
#################

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