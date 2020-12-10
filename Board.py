import pandas as pd

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
		self.chaser += 1

	def update_player(self):
		self.player += 1

	def check_finish(self):
		if self.chaser == self.player:
			self.winner = 'Chaser'
		elif self.player == len(self.board):
			self.winner = 'Player'
		if self.winner:
			return f'{self.winner} Won!'
		return False

	def chaser_offers(self,amount):
		self.get_board()
		change_amount_by_ratio = 2
		self.board.loc[self.player-1,'Board'] = amount*change_amount_by_ratio
		self.board.loc[self.player, 'Board'] = amount
		self.board.loc[self.player+1,'Board'] = amount//change_amount_by_ratio
		return self.board