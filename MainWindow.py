import tkinter as tk
from Utils import WINDOW_WIDTH, WINDOW_HEIGHT

WINDOW_TITLE = 'The Chaser'
player_name = 'TEST'

class MainWindow:
	def __init__(self):
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
		title['text'] = 'The Chaser'
		title['font'] = ("Broadway", 50)
		title.pack()

		# name clause
		name_label = tk.Label(root)
		name_label['background'] = 'black'
		name_label['foreground'] = 'white'
		name_label['text'] = 'Enter your Name:'
		name_label['font'] = ("Broadway", 25)
		name_label.place(x=400, y=200, anchor='center')

		global player_name
		player_name = tk.Text(root)
		player_name.place(x=800, y=200, anchor='center')
		player_name['height'] = 1
		player_name['width'] = 15
		player_name['font'] = ("Broadway", 25)

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
	global player_name
	print(player_name.get('1.0',"end-1c"))
	# from PhaseOne import PhaseOne
	# new_game = PhaseOne()


main = MainWindow()