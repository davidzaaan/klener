from tkinter import *
import os


master = Tk()

# Tkinter's window dimensions
WINDOW_WIDTH = 350
WINDOW_HEIGHT = 200

# User screen dimensions
SCREEN_HEIGHT = int(master.winfo_screenheight() / 2) - int(WINDOW_HEIGHT / 2)
SCREEN_WIDTH = int(master.winfo_screenwidth() / 2) - int(WINDOW_WIDTH / 2)


USER_USERNAME: str = os.environ.get('USERNAME')

PATH: str = f"C:/Users/{USER_USERNAME}/Downloads/"

LIST_OF_FILES: list = os.listdir(PATH)

# Quantity of files in the Downloads folder
FILE_NUM: int = len(LIST_OF_FILES) - 1 # I substract 1 because of the .ini file