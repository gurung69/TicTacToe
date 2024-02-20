from tkinter import *
import numpy as np

size = 400
color_X = "red"
color_O = "blue"
symbol_width = 20

class TicTacToe:
  def __init__(self):
    self.curr_player = "X"
    self.draw = False
    self.score = {"X":0, "O": 0}

    self.win = Tk()
    self.win.title("TicTacToe")
    self.win.geometry("400x400")
    self.canvas = Canvas(self.win, width=size, height=size)
    self.canvas.bind("<Button-1>", self.fill_position)

    self.board = np.full((3,3), None)

    self.score_frame = Frame(self.win, width=size, height=size)
    

  def draw_board(self):
    self.score_frame.pack_forget()
    self.canvas.delete("all")
    self.canvas.pack()
    for i in range(1,3): # create grid
      self.canvas.create_line(i*size/3, 0, i*size/3, size)
      self.canvas.create_line(0, i*size/3, size, i*size/3)

  def display_score(self):
    self.canvas.pack_forget()
    for widget in self.score_frame.winfo_children():
      widget.destroy()
    self.score_frame.pack()
    

    if self.draw:
      Label(self.score_frame, text="It's a tie", font="Fredoka 25 bold", fg="red").grid(row=1, pady=15)
    else:
      Label(self.score_frame, text="Player "+self.curr_player +" win", font="Fredoka 25 bold", fg="green").grid(row=1, pady=20)

    Label(self.score_frame, text="Scores", font="Fredoka 20 bold").grid(row=2, pady=10)
    Label(self.score_frame, text="Player X : \t"+str(self.score["X"]), font="Fredoka 20 bold").grid(row=3,pady=5)
    Label(self.score_frame, text="Player O : \t"+str(self.score["O"]), font="Fredoka 20 bold").grid(row=4, pady=5)

    Button(self.score_frame, text="Play Again", command=self.restart_game).grid(row=5,pady=5)
    Button(self.score_frame, text="Quit", command=self.win.destroy).grid(row=6)

  def restart_game(self):
    self.board = np.full((3,3), None)
    self.curr_player = "X"
    self.draw = False
    self.draw_board()
  
  def fill_position(self, event):
    position = np.array([event.x, event.y])
    position = (position//(size/3)).astype(int)

    if self.board[position[1], position[0]] == None:
      if self.curr_player == "X":
        self.canvas.create_line((size/3)*position[0]+symbol_width, (size/3)*position[1]+symbol_width, (size/3)*position[0]+(size/3)-symbol_width, (size/3)*position[1]+(size/3)-symbol_width, width=symbol_width, fill=color_X)
        self.canvas.create_line((size/3)*position[0]+(size/3)-symbol_width, (size/3)*position[1]+symbol_width, (size/3)*position[0]+symbol_width, (size/3)*position[1]+(size/3)-symbol_width, width=symbol_width, fill=color_X)
      if self.curr_player == "O":
        self.canvas.create_oval((size/3)*position[0]+symbol_width, (size/3)*position[1]+symbol_width, (size/3)*position[0]+(size/3)-symbol_width, (size/3)*position[1]+(size/3)-symbol_width, width=symbol_width, outline=color_O)

      self.board[position[1], position[0]] = self.curr_player;

      if self.check_winner():
        self.score[self.curr_player] += 1
        self.display_score()
      
      self.check_draw()
      if self.draw:
        self.display_score()

      self.switch_player()
      
  
  def switch_player(self):
    if self.curr_player == "X":
      self.curr_player = "O"
    else:
      self.curr_player = "X"

  def check_winner(self):
    for i in range(3):
      if self.board[i, 0] == self.board[i, 1] == self.board[i,2] != None:
        return True
      if self.board[0, i] == self.board[1, i] == self.board[2, i] != None:
        return True
    if self.board[0, 0] == self.board[1,1] == self.board[2, 2] != None:
      return True
    if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] != None:
      return True
    
    return False 
  
  def check_draw(self):
    if None not in self.board:
      self.draw = True
  
  def start(self):
    self.draw_board()
    self.win.mainloop()
    


game = TicTacToe()
game.start()
