from tkinter import Button


class Cell:
    def __init__(self, window) -> None:
        self.live = -1
        self.button = Button(window, text='', height=5, width=10)
        self.move = 'x'
        self.in_cell = ''

    def make_move(self):
        self.button.configure(text=self.move)
        self.in_cell = self.move
        self.live = 6