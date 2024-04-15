import tkinter as tk


window = tk.Tk()
window.title('New Tic Tac Toe')
figures = list()

for i in range(9):
    figures.append(tk.Button(window, text='', width=10, height=5))

for i, button in enumerate(figures):
    button.grid(row= i % 3, column=i // 3)

window.mainloop()
