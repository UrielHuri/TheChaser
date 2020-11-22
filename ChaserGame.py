import pandas as pd
from Question import *

def setChaserDiff(level):
	return 100-(4-level)*10

class Player:
	def __init__(self,name,account=0):
		self.name = name
		self.account = account
		self.availble_questions = createDBFromJson()

	def deposite(self,amount):
		self.account += amount

	def use_question(self,q_index):
		self.availble_questions.pop(q_index)

	def get_account(self):
		return f'{self.account}$'

class Board:
	def __init__(self,levels = 8,player = 3,chaser = 0):
		self.levels = levels
		self.chaser = chaser
		self.player = player

	board = pd.DataFrame()

	winner = None

	def get_board(self):
		levels_list = ['']*self.levels
		levels_list[self.chaser] = "Chaser"
		levels_list[self.player] = "Player"
		self.board = pd.DataFrame.from_dict({'Board' : levels_list})
		self.board = self.board.reindex(index=self.board.index[::-1])
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
			print(f'{self.winner} Won!')
			return True
		return False

def getPlayerAnswer(quetion):
	print(quetion)
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
		print('UNVALID INPUT')
		return initialization()

def phaseOne(player):
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












def gameplay(board):
	q = getQuestion()
	showQuestion(q)
	player_ans = checkAnswer(q,getPlayerAnswer())
	chaser_ans = checkAnswer(q,getChaserAnswer(q))
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
