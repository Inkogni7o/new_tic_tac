def check_move(btns: list, index: int) -> bool:
    success = False
    if btns[index].in_cell == '':
        return True
    return success


def check_win(btns: list) -> bool:
    for i in range(3):
        if ((btns[i * 3].in_cell ==
             btns[i * 3 + 1].in_cell ==
             btns[i * 3 + 2].in_cell) and btns[i * 3].in_cell != ''):
            print(btns[i * 3])
