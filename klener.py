
from utils.core import (
    display_main_window,
    display_main_label,
    display_main_btns,
    display_okclose_btn
)

from utils.variables import FILE_NUM, master

def start() -> None:
    """
        Function that will start the Tkinter app mainloop
    """
    display_main_window()

    if FILE_NUM > 0:
        display_main_label(f"You have {FILE_NUM} new downloaded files")
        display_main_btns()
    else:
        display_main_label()
        display_okclose_btn()

    master.mainloop()

start()