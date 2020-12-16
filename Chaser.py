from random import random, choice
from Question import Question

class Chaser:
	"""
	A chaser class to manage chaser's actions
	"""
	def __init__(self, rightness_percent = 75):
		"""
		:param rightness_percent (int or float): the probability (in %) the chaser will get the right answers
		"""
		self.rightness_prob = rightness_percent/100

	def __repr__(self):
		return f'Chaser{round(self.rightness_prob)}'

	def __str__(self):
		return f'Chaser{round(self.rightness_prob)}'

	def get_answer(self, question : Question):
		"""
		Get an answer to a given question
		:param question (Question): the given question
		:return: answer sign (A/B/C/D) as str
		"""
		rnd = random()
		if rnd <= self.rightness_prob:
			return question.answer
		else:
			return choice(list(question.wrong_options().keys()))