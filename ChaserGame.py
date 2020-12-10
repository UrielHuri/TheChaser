from Question import *

INVALID_INPUT = 'INVALID INPUT'
MSG_SIZE = 1024

def getPlayerAnswer(conn,quetion, is_chase = False):
	msg = str(quetion)
	if is_chase:
		msg += '\n(Enter L to use 50/50 lifebuoy)'
	conn.send(msg.encode())
	return conn.recv(1024).decode()

def initialization(conn):
	conn.send(b'Welcome to The Chaser!\n')
	conn.send(b"Do you want to play? (Y/N)")
	wanna_play = conn.recv(MSG_SIZE).decode().upper()
	if wanna_play == 'Y':
		return True
	elif wanna_play == 'N':
		return False
	else:
		conn.send(INVALID_INPUT.encode())
		return False

def phaseOne(conn,player):
	conn.send(b"Welcome to phase #1 of The Chaser!\nLet's start:\n")
	REQUESTED_QUESTIONS = 3
	RIGHT_ANSWER_REWARD = 5000
	RIGHT_ANSWER_ANNOUNCE = 'Nice one! your answer is right and you get {}$.\nYour current accunt status is {}.'
	WRONG_ANSWER_ANNOUNCE = 'Bummer! your answer is wrong. Well, maybe next time.\nYour current accunt status is {}.'
	for i in range(REQUESTED_QUESTIONS):
		num = getQuestionNum(player.availble_questions)
		question = player.availble_questions[num]
		player.use_question(num)
		answer = getPlayerAnswer(conn,question)
		if question.is_right(answer):
			player.deposite(RIGHT_ANSWER_REWARD)
			conn.send(RIGHT_ANSWER_ANNOUNCE.format(RIGHT_ANSWER_REWARD,player.get_account()).encode())
		else:
			conn.send(WRONG_ANSWER_ANNOUNCE.format(player.get_account()).encode())
	if player.account > 0:
		return True
	else:
		conn.send(b"You haven't got any right answer...\nYOU LOST and you are a loser.\n\n")
		return False

def handlingPlayerChoice(conn, player_choice,player,board):
	if player_choice not in ['0','1','2']:
		print(INVALID_INPUT)
		return phaseTwo(conn, player,board)
	if player_choice == '1':
		player.deposite(-player.account/2)
		board.player += 1
	elif player_choice == '2':
		player.deposite(player.account)
		board.player -= 1


def theChase(conn, player, chaser, board):
	while not board.check_finish():
		q_num = getQuestionNum(player.availble_questions)
		q = player.use_question(q_num)
		player_input = getPlayerAnswer(conn,q)
		if player_input == 'L':
			player.use_lifebuoy(q)
			player_input = getPlayerAnswer(conn,q.use_lifebuoy())
		player_ans = q.is_right(player_input)
		chaser_ans = q.is_right(chaser.get_answer(q))
		if player_ans:
			conn.send(b'Player was Right!\n')
			board.update_player()
		else:
			conn.send(b'Player was Wrong...\n')
		if chaser_ans:
			conn.send(b'Chaser was Right!\n')
			board.update_chaser()
		else:
			conn.send(b'Chaser was Wrong...\n')
		conn.send(str(board.get_board()).encode())

def phaseTwo(conn, player, chaser, board):
	conn.send(b"Nice! you made it to phase #2!\n")
	RATIO_OF_AMOUNT_CHANGE = 2
	conn.send("You can start 2 steps away from the chaser with your current amount: {}.\n".format(player.get_account()).encode())
	conn.send(b"However, the chaser is willing to offer you two alternatives:\n")
	conn.send("(1) You can go one step DOWN and play for HALF of the amount you have now, which is {}$\n".format(
		RATIO_OF_AMOUNT_CHANGE // player.account).encode())
	conn.send("(2) You can go one step UP and play for TWICE the amount you have now, which is {}$\n".format(
		RATIO_OF_AMOUNT_CHANGE * player.account).encode())
	conn.send(str(board.chaser_offers(player.account)).encode())
	conn.send(b"SO what will you choose?\n(enter 0 to continue with your current amount)\n")
	player_choice = conn.recv(1024).decode()
	handlingPlayerChoice(conn, player_choice, player, board)
	conn.send(str(board.get_board()).encode())
	theChase(conn, player, chaser, board)
