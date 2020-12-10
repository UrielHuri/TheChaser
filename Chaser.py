from random import random, choice
from Question import Question

class Chaser:
	def __init__(self, rightness_percent = 75):
		self.rightness_prob = rightness_percent/100

	def __repr__(self):
		return f'Chaser{round(self.rightness_prob)}'

	def __str__(self):
		return f'Chaser{round(self.rightness_prob)}'

	def get_answer(self, question : Question):
		rnd = random()
		if rnd <= self.rightness_prob:
			return question.answer
		else:
			return choice(list(question.wrong_options().keys()))