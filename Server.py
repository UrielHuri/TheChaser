from ChaserGame import *
from Board import Board
from Player import Player
from Chaser import Chaser
from Utils import createSocket

s = createSocket()
conn, addr = s.accept()
board = Board()
chaser = Chaser()

while True:
    if initialization(conn):
        conn.send(b"What's your name?")
        name = conn.recv(1024).decode().title()
        player = Player(name)
        p1 = phaseOne(conn,player)
        if p1:
            phaseTwo(conn, player, chaser, board)


