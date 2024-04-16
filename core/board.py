def check_move(btns: list) -> bool:
    success = False
    for btn in btns:
        if btn.last_move:
            btn.last_move = False
            success = True
    return success


def make_move(btns: list) -> None:
    for btn in btns:
        btn.move = 'o' if btn.move == 'x' else 'x'
        btn.live -= 1
    for btn in btns:
        if btn.live <= 0:
            btn.button.configure(text='')
            btn.in_cell = ''


def check_win(btns: list) -> bool:
    for i in range(3):
        if ((btns[i * 3].in_cell ==
            btns[i * 3 + 1].in_cell ==
            btns[i * 3 + 2].in_cell) and btns[i * 3].in_cell != ''):
            print(btns[i * 3].in_cell)