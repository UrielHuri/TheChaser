import tkinter as tk

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1200

# TO DELETE
def getAttr(d):
	for key in d:
		print(f'{key} : {d[key]}')
#################

class MainWindow:
	def __init__(self):
		root = tk.Tk()
		# set window properties
		root.title('The Chaser')
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
main = MainWindow()
