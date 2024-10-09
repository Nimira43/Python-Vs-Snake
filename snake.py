import customtkinter as ctk
from settings import *

class Game(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title('Python vs Snake')
    self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')
    
    self.columnconfigure(list(range(FIELDS[0])), weight = 1, uniform = 'a')
    self.rowconfigure(list(range(FIELDS[1])), weight = 1, uniform = 'a')
    
    self.snake = [START_POS, (START_POS[0] - 1, START_POS[1]), (START_POS[0] - 2, START_POS[1])]


    self.mainloop()

Game()