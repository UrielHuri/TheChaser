from random import randrange as rint

class Question:
	def __init__(self,question : str, options : dict, answer : str):
		"""
		creates an instance of Question
		:param question: string of question
		:param options: dict of questions with keys [A,B,C,D]
		:param answer: right option as upper letter [A/B/C/D]
		"""
		self.question = question
		self.options = options
		self.answer = answer

	@classmethod
	def from_dict(cls,q_dict):
		"""
		transforms dictionary to question
		:param q_dict: {keys: question, A,B,C,D, answer}
		:return: Question
		"""
		q_dict_copy = q_dict.copy()
		question = q_dict_copy.pop('question')
		answer = q_dict_copy.pop('answer')
		options = q_dict_copy
		return cls(question,options,answer)

	def __str__(self):
		string = self.question + '\n'
		for key in self.options:
			string += f'{key}: {self.options[key]}\n'
		return string

	def __repr__(self):
		string = self.question + '\n'
		for key in self.options:
			string += f'{key}: {self.options[key]}\n'
		return string

	def to_dict(self):
		"""
		transforms Question to dict with keys [question, A, B, C, D, answer]
		:return: dictionary
		"""
		q_dict = self.options.copy()
		q_dict['question'] = self.question
		q_dict['answer'] = self.answer
		return q_dict

	def wrong_options(self):
		"""
		Get only the wrong answers of the quetion
		:return: dict of answers
		"""
		q_dict = self.options.copy()
		q_dict.pop(self.answer)
		return q_dict

	def is_right(self,answer):
		"""
		Check if given answer is right
		:param answer: A/B/C/D (str)
		:return: bool
		"""
		if self.answer == answer:
			return True
		return False

	def use_lifebuoy(self):
		"""
		Returns the question with only the right answer and ont wrong answer
		:return: str of question with 2 answers
		"""
		wrong_opts = list(self.wrong_options().keys())
		option_index = rint(0,len(wrong_opts))
		options = sorted([self.options[self.answer],self.options[wrong_opts[option_index]]])
		string = self.question
		for opt in options:
			string += '\n'
			string += opt
		return string

def createDBFromJson(q_file = 'QDB.json'):
	"""
	Transforms questions file (as json) to list of Question objects
	:param q_file: name of file with extension (str)
	:return: db (list of Question)
	"""
	with open(q_file) as file:
		q_dicts_list = eval(file.read())
	db = list()
	for q_dict in q_dicts_list:
		q = Question.from_dict(q_dict)
		db.append(q)
	return db

def getQuestionNum(db):
	"""
	Returns random index of a Question from a DB
	:param db: List
	:return: int
	"""
	q_index = rint(0,len(db))
	return q_index


