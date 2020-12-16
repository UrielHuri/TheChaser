import pandas as pd

class Board:
	"""
	Class of the chasing board, which represents the chase phase in the game
	"""
	def __init__(self,levels = 8,player = 3,chaser = 0):
		"""
		creates a chasing board by the inputed parameters
		:param levels (int): number of levels in board
		:param player (int): player's position on board
		:param chaser (int): chaser's position on board
		"""
		self.levels = levels
		self.chaser = chaser
		self.player = player

		# board is kept as dataframe to easily update and display
		self.board = pd.DataFrame()

		# winner is used to indicate the chase has ended
		self.winner = None

	def get_board(self):
		"""
		:return: board's display as DataFrame
		"""
		levels_list = ['']*self.levels
		levels_list[self.player] = "Player"
		levels_list[self.chaser] = "Chaser"
		self.board = pd.DataFrame.from_dict({'Board' : levels_list})
		return self.board

	def __repr__(self):
		return f'Board({self.levels},{self.player},{self.chaser})'

	def update_chaser(self):
		"""
		Promotes the chaser
		"""
		self.chaser += 1

	def update_player(self):
		"""
		Promotes the player
		"""
		self.player += 1

	def check_finish(self):
		"""
		Checks if the chaser got the player, or the player had gotten to the bottom
		:return: winner announcement (str) if True, otherwise False
		"""
		if self.chaser == self.player:
			self.winner = 'Chaser'
		elif self.player == len(self.board):
			self.winner = 'Player'
		if self.winner:
			return f'{self.winner} Won!'
		return False

	def chaser_offers(self,amount):
		"""
		Displays chaser's offers before the beginning of the chase
		:param amount: Player's account
		:return: the board with the offers (DataFrame)
		"""
		self.get_board()
		change_amount_by_ratio = 2
		self.board.loc[self.player-1,'Board'] = amount*change_amount_by_ratio
		self.board.loc[self.player, 'Board'] = amount
		self.board.loc[self.player+1,'Board'] = amount//change_amount_by_ratio
		return self.board