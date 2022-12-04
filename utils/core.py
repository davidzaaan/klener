import os
from tkinter import *
from tkinter.ttk import *
from .custom_exceptions import FolderEmptyError
from .variables import (
    PATH, 
    LIST_OF_FILES,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    FILE_NUM,
    # Main window
    master
)

def delete_files() -> None:
    """
        Function that deletes all the downloaded files when called

        Params
        downloads_folder The path that cointains all the downloaded files

        Return
        None
    """

    if not len(LIST_OF_FILES) > 1:
        raise FolderEmptyError(message="Oops folder is currently empty")

    # Getting all the current downloaded files
    files = (file for file in LIST_OF_FILES)

    for filename in files:
        # .ini files contain information about how Windows display the folder
        if not filename.endswith('.ini'):
            os.remove(path=PATH + filename)

#### Tkinter functionality ####

def display_main_window() -> None:
    """
        Function that will set the Tkinter main window
    """
    master.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{SCREEN_WIDTH}+{SCREEN_HEIGHT}")
    master.title("Klener")
    master.resizable(width=False, height=False)


def display_sec_window() -> Toplevel:
    """
        Function that will create and display a new information window with the status of the files deletion

        Return
            A Tkinter's Toplevel object with the secondary window
    """
    def close_windows() -> None:
        """
            Function that will close recently opened Tkinter windows
        """
        window.destroy()
        master.destroy()

    window = Toplevel(master)
    window.geometry(f"200x170+{SCREEN_WIDTH + 80}+{SCREEN_HEIGHT + 40}")
    window.title("Info")
    window.resizable(width=False, height=False)
    
    close_btn = Button(window, text="Finish", command=close_windows)
    close_btn.pack(side=BOTTOM, pady=40)

    return window


def delete_all() -> None:
    """
        Function that will call the delete_files function and display information about it
    """
    try:
        info_window: Toplevel = display_sec_window()
        delete_files() # Delete all

        # Information about process completion
        info_label = Label(info_window, text=f"{FILE_NUM} files were deleted successfully!")
        info_label.pack(pady=20)

    except FolderEmptyError as err:

        # Information about process completion
        info_label = Label(info_window, text=err)
        info_label.pack(pady=20)


def display_main_label(info_text: str = "You have no files to delete") -> None:
    """
        Function that will create and display the text below on the Tkinter's main window
    """
    label: Label = Label(master, text=info_text)
    label.pack(pady=40)


def display_main_btns() -> None:
    """
        Function that will create and display the buttons for interaction on the Tkinter's main window
    """
    # This will be the button that deletes all the existing files in the Downloads folder
    delete_btn = Button(master, text="Delete all", command=delete_all)
    delete_btn.place(x=80, y=(WINDOW_HEIGHT - 60))


    # This will be the 'No' option
    select_btn = Button(master, text="Select what to delete", state=DISABLED)
    select_btn.place(x=160, y=(WINDOW_HEIGHT - 60))


def set_okclose_btn() -> None:
    """
        Function that creates and display an optional close button in case that there is no files to delete 
        in the user's downloads folder
    """
    okclose_btn = Button(master, text="Ok, close", command=master.destroy)
    okclose_btn.pack(side=BOTTOM, pady=30)