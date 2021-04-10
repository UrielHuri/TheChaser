import tkinter as tk
from Utils import WINDOW_WIDTH, WINDOW_HEIGHT

WINDOW_TITLE = 'PhaseOne: FirstCollection'

class PhaseOne:
	def __init__(self,question_num = 1):
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
		title['text'] = f'Question #{question_num}:'
		title['font'] = ("Broadway", 50)
		title.pack(side='left')

		# new game button
		new_game_btn = tk.Button(root)
		new_game_btn['bg'] = 'black'
		new_game_btn['foreground'] = 'white'
		new_game_btn['text'] = 'NEW GAME'
		new_game_btn['font'] = ("Broadway", 30)
		new_game_btn['command'] = newGame
		new_game_btn.place(relx=0.5, rely=0.5, anchor='center')

		root.mainloop()

def newGame():
	print('PRESS')
wind = PhaseOne()
