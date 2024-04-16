import tkinter as tk

from core.cell import Cell
from core.board import check_move


def move_maid(event):
    abs_coord_x = window.winfo_pointerx() - window.winfo_rootx()
    abs_coord_y = window.winfo_pointery() - window.winfo_rooty()
    x, y = abs_coord_x // 80, abs_coord_y // 80
    index = y * 3 + x
    success = check_move(btns, index)
    if success:
        btns[index].make_move()
        for btn in btns:
            if btn.live <= 0:
                btn.in_cell = ''
                btn.button.configure(text='')
            btn.move = 'o' if btn.move == 'x' else 'x'
            btn.live -= 1


window = tk.Tk()
window.title('New Tic Tac Toe')
btns = [Cell(window) for i in range(9)]

for i, button in enumerate(btns):
    button.button.grid(row=i // 3, column=i % 3)

window.bind('<Button-1>', move_maid)

window.mainloop()
