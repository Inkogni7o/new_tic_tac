import tkinter as tk

from core.cell import Cell
from core.board import check_move, make_move


def move_maid(event):
    success = check_move(figures)
    if success:
        make_move(figures)


window = tk.Tk()
window.title('New Tic Tac Toe')
figures, move, last_move = list(), 'x', -1

for i in range(9):
    figures.append(Cell(window))

for i, button in enumerate(figures):
    button.button.grid(row=i % 3, column=i // 3)

window.bind('<Button-1>', move_maid)


window.mainloop()
