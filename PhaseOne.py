import tkinter as tk
from Utils import WINDOW_WIDTH, WINDOW_HEIGHT
from Question import Question

WINDOW_TITLE = 'PhaseOne: FirstCollection'

class PhaseOne:
	def __init__(self,question : Question, question_num = 1):
		root = tk.Tk()
		# set window properties
		root.title(WINDOW_TITLE)
		root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
		root.configure(background='black')
		root.iconbitmap('running-256.ico')

		# main title
		title = tk.Label(root)
		title['background'] = 'black'
		title['foreground'] = 'white'
		title['text'] = f'PHASE ONE:'
		title['font'] = ("Broadway", 50)
		title.pack(side='top')

		# question title
		question_title = tk.Label(root)
		question_title['background'] = 'black'
		question_title['foreground'] = 'white'
		question_title['text'] = f'Question #{question_num}:'
		question_title['font'] = ("Broadway", 30)
		question_title.pack(side='left')

		# question text field
		question_field = tk.Text(root)
		question_field.place(x=300, y=400, anchor='w')
		question_field.insert(tk.INSERT,question.question)
		question_field['height'] = 3
		question_field['width'] = 30
		question_field['font'] = ("Broadway", 25)

		x, y = 400, 600
		i = 0
		for ans in question.options:
			ans_field = tk.Button(root)
			ans_field['text'] = f'{ans}. {question.options[ans]}'
			if i % 2 == 1:
				x+=200
			else:
				x = 400
			if i > 1:
				y = 700
			ans_field.place(x=x,y=y,anchor='center')
			i+=1

		root.mainloop()

def newGame():
	print('PRESS')

q = Question('What is the answer?',{'A': '1', 'B': '2', 'C': '3', 'D': '4'},'B')

wind = PhaseOne(q)
