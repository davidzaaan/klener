from utils.core import display_main_window
from utils.variables import FILE_NUM, master

def start() -> None:
    """
        Function that will start the Tkinter app mainloop
    """
    display_main_window(FILE_NUM)
    master.mainloop()

start()