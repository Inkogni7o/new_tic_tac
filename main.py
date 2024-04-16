import tkinter as tk

from core.cell import Cell


def move_maid(event):
    success = False
    for btn in figures:
        if btn.last_move:
            btn.last_move = False
            success = True
    if success:
        for btn in figures:
            btn.move = 'o' if btn.move == 'x' else 'x'


window = tk.Tk()
window.title('New Tic Tac Toe')
figures, move, last_move = list(), 'x', -1

for i in range(9):
    figures.append(Cell(window))

for i, button in enumerate(figures):
    button.button.grid(row=i % 3, column=i // 3)

window.bind('<Button-1>', move_maid)


window.mainloop()
