from tkinter import Button


class Cell:
    def __init__(self, window) -> None:
        self.live = 0
        self.button = Button(window, text='', height=5, width=10, command=self.self_move)
        self.move = 'x'
        self.in_cell = ''
        self.last_move = False

    def decrease_life(self) -> None:
        self.live -= 1

    def self_move(self):
        if self.live <= 0 and self.in_cell == '':
            self.last_move = True
            self.button.configure(text=self.move)
            self.in_cell = self.move
            self.live = 6

    