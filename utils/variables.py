from tkinter import *
import os


master = Tk()

# Tkinter main window dimensions
WINDOW_WIDTH = 350
WINDOW_HEIGHT = 200

# Tkinter main window dimensions
SCREEN_HEIGHT = int(master.winfo_screenheight() / 2) - int(WINDOW_HEIGHT / 2)
SCREEN_WIDTH = int(master.winfo_screenwidth() / 2) - int(WINDOW_WIDTH / 2)

USER_USERNAME: str = os.environ.get('USERNAME')

PATH: str = f"C:/Users/{USER_USERNAME}/Downloads/"

# .ini files contain information about how Windows display the folder
LIST_OF_FILES: list = list(filter(lambda filename: filename != "desktop.ini", os.listdir(PATH)))

# Quantity of files in the Downloads folder
FILE_NUM: int = len(LIST_OF_FILES)