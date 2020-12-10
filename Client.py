from Utils import createSocket

s = createSocket(is_server=False)

finish = False
while not finish:
    data = s.recv(1024).decode()
    if len(data) > 0:
        print(data)
    if data.find('?') != -1:
        player_input = input()
        s.send(player_input.encode())