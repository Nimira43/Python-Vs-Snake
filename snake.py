import customtkinter as ctk
from settings import *


class Game(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title('Python vs Snake')
    self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')
    self.mainloop()

Game()