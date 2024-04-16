import tkinter as tk

from core.cell import Cell
from core.board import make_move

window = tk.Tk()
window.title('New Tic Tac Toe')
figures, move = list(), 'x'

for i in range(9):
    figures.append(Cell(window, i))

for i, button in enumerate(figures):
    button.button.grid(row=i % 3, column=i // 3)
    btn_copy = button
    print(button.id, btn_copy.id)
    button.button.configure(text=' ', command=make_move(figures, 'asdasd', btn_copy))


window.mainloop()
