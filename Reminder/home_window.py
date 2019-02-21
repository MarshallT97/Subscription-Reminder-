from tkinter import *
import center_function

class HomeWindow():
    def __init__(self, master):
        self.home = Toplevel(master)
        self.home.title("Home Window")
        center_function.center(500, 500, self.home)
        self.home.resizable(0, 0)
        self.init_ui()

    def init_ui(self):
        ok = 0
