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
    self.canvas.bind("<Button-1>", self.fill_position)

    self.board = np.full((3,3), None)

    self.draw_board()
    self.win.mainloop()

  def draw_board(self):
    for i in range(1,3): # create grid
      self.canvas.create_line(i*size/3, 0, i*size/3, size)
      self.canvas.create_line(0, i*size/3, size, i*size/3)
  
  def fill_position(self, event):
    position = np.array([event.x, event.y])
    position = (position//(size/3)).astype(int)

    if self.board[position[1], position[0]] == None:
      if self.curr_player == "X":
        self.canvas.create_line((size/3)*position[0]+symbol_width, (size/3)*position[1]+symbol_width, (size/3)*position[0]+(size/3)-symbol_width, (size/3)*position[1]+(size/3)-symbol_width, width=symbol_width)
        self.canvas.create_line((size/3)*position[0]+(size/3)-symbol_width, (size/3)*position[1]+symbol_width, (size/3)*position[0]+symbol_width, (size/3)*position[1]+(size/3)-symbol_width, width=symbol_width)
      if self.curr_player == "O":
        self.canvas.create_oval((size/3)*position[0]+symbol_width, (size/3)*position[1]+symbol_width, (size/3)*position[0]+(size/3)-symbol_width, (size/3)*position[1]+(size/3)-symbol_width, width=symbol_width)

      self.switch_player()
      self.board[position[1], position[0]] = self.curr_player;
  
  def switch_player(self):
    if self.curr_player == "X":
      self.curr_player = "O"
    else:
      self.curr_player = "X"
    


game = TicTacToe()