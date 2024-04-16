from core.cell import Cell


def make_move(btns: list, move: str, now_btn: Cell) -> None:
    for btn in btns:
        btn.decrease_life()
        if btn.id == now_btn.id:
            now_btn.button.configure(text=move)
            now_btn.live = 6
            break


