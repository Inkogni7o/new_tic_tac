from tkinter import Button


class Cell:
    def __init__(self, window, id) -> None:
        self.live = 0
        self.button = Button(window, text=' ', height=5, width=10)
        self.id = id
        self.x, self.y = id % 3, id // 3

    def decrease_life(self) -> None:
        self.live -= 1

    