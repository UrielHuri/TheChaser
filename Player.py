from Question import createDBFromJson

class Player:
	def __init__(self,name,account=0,lifebuoy = True):
		self.name = name
		self.account = account
		self.lifebuoy = lifebuoy
		self.availble_questions = createDBFromJson()

	def __repr__(self):
		return f'Player {self.name}: {self.get_account()} , lifebuoy: {self.lifebuoy}'

	def __str__(self):
		return f'Player {self.name}: {self.get_account()} , lifebuoy: {self.lifebuoy}'

	def deposite(self,amount):
		self.account += amount

	def use_question(self,q_index):
		return self.availble_questions.pop(q_index)

	def get_account(self):
		return f'{self.account}$'

	def use_lifebuoy(self):
		self.lifebuoy = False