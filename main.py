import tkinter as tk

from core.cell import Cell
from core.board import check_move


def draw_board():
    window.geometry('500x500')
    window.config(bg='black')


def move_maid(event):
    abs_coord_x = window.winfo_pointerx() - window.winfo_rootx()
    abs_coord_y = window.winfo_pointery() - window.winfo_rooty()
    x, y = (abs_coord_x - 100) // 82, (abs_coord_y - 100) // 86
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

draw_board()

for i, button in enumerate(btns):
    button.button.place(x=(100 + i % 3 * 82), y=(100 + i // 3 * 86))

window.bind('<Button-1>', move_maid)

window.mainloop()
