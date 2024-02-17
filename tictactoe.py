from tkinter import *
import numpy as np

size = 400
color_X = "#f0190a"
color_O = "#0a19f0"
symbol_width = 20

class TicTacToe:
  def __init__(self):
    self.curr_player = "X"
    self.win = Tk()
    self.canvas = Canvas(self.win, width=size, height=size)
    self.canvas.pack()
    

    self.board = np.zeros((3,3))

    self.draw_board()
    self.win.mainloop()

  def draw_board(self):
    for i in range(1,3): # create grid
      self.canvas.create_line(i*size/3, 0, i*size/3, size)
      self.canvas.create_line(0, i*size/3, size, i*size/3)



game = TicTacToe()
    

# def clicked(event):
#   print(event.x, event.y)

# win = Tk()
# canvas = Canvas(win, width=size, height=size)
# canvas.bind("<Button-1>", clicked)



# for i in range(1,3): # create grid
#   canvas.create_line(i*size/3, 0, i*size/3, size)
#   canvas.create_line(0, i*size/3, size, i*size/3)
# canvas.pack()
# win.mainloop()