import pandas as pd
from Question import *

INVALID_INPUT = 'INVALID INPUT'

def setChaserDiff(level):
	return 100-(4-level)*10

class Player:
	def __init__(self,name,account=0,lifebuoy = True):
		self.name = name
		self.account = account
		self.lifebuoy = lifebuoy
		self.availble_questions = createDBFromJson()

	def deposite(self,amount):
		self.account += amount

	def use_question(self,q_index):
		return self.availble_questions.pop(q_index)

	def get_account(self):
		return f'{self.account}$'

	def use_lifebuoy(self):
		self.lifebuoy = False


class Board:
	def __init__(self,levels = 8,player = 3,chaser = 0):
		self.levels = levels
		self.chaser = chaser
		self.player = player

	board = pd.DataFrame()

	winner = None

	def get_board(self):
		levels_list = ['']*self.levels
		levels_list[self.player] = "Player"
		levels_list[self.chaser] = "Chaser"
		self.board = pd.DataFrame.from_dict({'Board' : levels_list})
		return self.board

	def __repr__(self):
		return f'Board({self.levels},{self.player},{self.chaser})'

	def update_chaser(self):
		self.chaser -= 1

	def update_player(self):
		self.player -= 1

	def check_finish(self):
		if self.chaser == self.player:
			self.winner = 'Chaser'
		elif self.player == -1:
			self.winner = 'Player'
		if self.winner:
			return f'{self.winner} Won!'
		return False

	def chaser_offers(self,amount):
		self.get_board()
		change_amount_by_ratio = 2
		self.board.loc[self.player-1,'Board'] = amount*change_amount_by_ratio
		self.board.loc[self.player+1,'Board'] = amount//change_amount_by_ratio
		return self.board

def getPlayerAnswer(quetion):
	print(quetion)
	print('(Enter L to use 50/50 lifebuoy)')
	return input('Answer: ').upper()

def getChaserAnswer(question, rightness_per = 75):
	chance = rint(1,100)
	if chance <= rightness_per:
		return question.answer
	else:
		options = question.options.keys()
		options.pop(question.answer)
		i = rint(0,len(options)-1)
		return options[i]

def initialization():
	print('Welcome to The Chaser!')
	wanna_play = input("Do you want to play? (Y/N)").upper()
	if wanna_play == 'Y':
		return True
	elif wanna_play == 'N':
		return False
	else:
		print(INVALID_INPUT)
		return initialization()

def phaseOne(player):
	print("Welcome to phase #1 of The Chaser!\nLet's start:\n")
	REQUESTED_QUESTIONS = 3
	RIGHT_ANSWER_REWARD = 5000
	RIGHT_ANSWER_ANNOUNCE = 'Nice one! your answer is right and you get {}$.\nYour current accunt status is {}.'
	WRONG_ANSWER_ANNOUNCE = 'Bummer! your answer is wrong. Well, maybe next time.\nYour current accunt status is {}.'
	for i in range(REQUESTED_QUESTIONS):
		num = getQuestionNum(player.availble_questions)
		question = player.availble_questions[num]
		player.use_question(num)
		answer = getPlayerAnswer(question)
		if question.is_right(answer):
			player.deposite(RIGHT_ANSWER_REWARD)
			print(RIGHT_ANSWER_ANNOUNCE.format(RIGHT_ANSWER_REWARD,player.get_account()))
		else:
			print(WRONG_ANSWER_ANNOUNCE.format(player.get_account()))
	if player.account > 0:
		return True
	else:
		print("You haven't got any right answer...\nYOU LOST and you are a loser.")
		return initialization()

def handlingPlayerChoise(choise,player,board):
	if choise not in ['0','1','2']:
		print(INVALID_INPUT)
		return phaseTwo(player,board)
	if choise == '1':
		player.deposite(-player.account/2)
		board.player += 1
	elif choise == '2':
		player.deposite(player.account)
		board.player -= 1


def theChase(player,board):
	while not board.check_finish():
		q_num = getQuestionNum(player.availble_questions)
		q = player.use_question(q_num)
		player_input = getPlayerAnswer(q)
		if player_input == 'L':
			player.use_lifebuoy(q)
			player_input = getPlayerAnswer(q.use_lifebuoy())
		player_ans = q.is_right(player_input)
		chaser_ans = q.is_right(q, getChaserAnswer(q))
		if player_ans:
			print('Player was Right!')
			board.update_player()
		else:
			print('Player was Wrong...')
		if chaser_ans:
			print('Chaser was Right!')
			board.update_chaser()
		else:
			print('Chaser was Wrong...')
		print(board.get_board())

def phaseTwo(player, board):
	print("Nice! you made it to phase #2!")
	RATIO_OF_AMOUNT_CHANGE = 2
	print("You can start 2 steps away from the chaser with your current amount: {}.".format(player.get_account()))
	print("However, the chaser is willing to offer you two alternatives:")
	print("(1) You can go one step DOWN and play for HALF of the amount you have now, which is {}$".format(
		RATIO_OF_AMOUNT_CHANGE // player.account))
	print("(2) You can go one step UP and play on TWICE the amount you have now, which is {}$".format(
		RATIO_OF_AMOUNT_CHANGE * player.account))
	print(board.chaser_offers(player.account))
	choise = input("SO what will you choose?\n(enter 0 to continue with your current amount)\n")
	handlingPlayerChoise(choise,player,board)
	print(board.get_board())
	theChase(player,board)
