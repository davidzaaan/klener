import os
from tkinter import *
from tkinter.ttk import *
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
    """
    for filename in LIST_OF_FILES:
        os.remove(path=PATH + filename)

#### Tkinter functionality ####

def display_main_window() -> None:
    """
        Function that will set and display the Tkinter main window
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
    window = Toplevel(master)
    window.geometry(f"200x170+{SCREEN_WIDTH + 80}+{SCREEN_HEIGHT + 40}")
    window.title("Info")
    window.resizable(width=False, height=False)
    
    close_btn = Button(window, text="Finish", command=master.destroy)
    close_btn.pack(side=BOTTOM, pady=40)

    return window


def delete_all() -> None:
    """
        Function that will call the delete_files function and display information about the process
    """
    info_window: Toplevel = display_sec_window()
    delete_files() # Deleting all files...

    # Information about process completion
    info_label = Label(info_window, text=f"{FILE_NUM} files were deleted successfully!")
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
    # Button that deletes all existing downloaded files
    delete_btn = Button(master, text="Delete all", command=delete_all)
    delete_btn.place(x=80, y=(WINDOW_HEIGHT - 60))

    # Button to select certain files to delete
    select_btn = Button(master, text="Select what to delete", command=create_sf_window)
    select_btn.place(x=160, y=(WINDOW_HEIGHT - 60))


def display_okclose_btn() -> None:
    """
        Function that creates and display an optional close button in case that there is no files to delete 
        in the user's downloads folder
    """
    okclose_btn = Button(master, text="Ok, close", command=master.destroy)
    okclose_btn.pack(side=BOTTOM, pady=30)

#### ONLY SELECTED FILES FUNCTIONALITY ####

def display_sf_second_window(sfwindow: Toplevel) -> Toplevel:
    """
        Function that will create and display a new information window with the status of the
        selected files deletion

        Return
            A Tkinter's Toplevel object with the secondary window
    """
    window: Toplevel = Toplevel(sfwindow)
    window.geometry(f"200x170+{SCREEN_WIDTH + 50}+{SCREEN_HEIGHT + 40}")
    window.title("Info")
    window.resizable(width=False, height=False)
    
    # Close information window button
    close_btn = Button(window, text="Finish", command=master.destroy)
    close_btn.pack(side=BOTTOM, pady=40)

    return window


def create_sf_window() -> None:
    """
        Function that creates and displays on Tkinter the interface for the user to delete
        only certain files
    """
    # Main window
    selectfiles_window = Toplevel(master)
    selectfiles_window.geometry(f"{WINDOW_WIDTH + 100}x{WINDOW_HEIGHT + 100}+{SCREEN_WIDTH - 80}+{SCREEN_HEIGHT - 50}")
    selectfiles_window.title("Select what to delete")
    selectfiles_window.resizable(width=False, height=False)

    # Main label setting
    label: Label = Label(selectfiles_window, text="Select what to delete")
    label.pack(side=TOP, pady=10)

    # Scrollbar setting
    scrollbar = Scrollbar(selectfiles_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Create a Listbox
    listbox = Listbox(selectfiles_window, selectmode=MULTIPLE, yscrollcommand=scrollbar.set)
    listbox.pack(side=TOP, expand=YES, fill=BOTH, padx=10, pady=70)

    # Insert items into the Listbox
    for index, item in enumerate(LIST_OF_FILES):
        listbox.insert(index, item)

    # Exit button
    exit_btn = Button(selectfiles_window, text="Close", command=selectfiles_window.destroy)
    exit_btn.place(x=180, y=(WINDOW_HEIGHT + 60))

    def remove_selected_files() -> None:
        """
            Function that deletes the selected files
        """
        # Get the selected elements from the Listbox
        selected_items = listbox.curselection()

        if selected_items:
            # Create a new information window
            info_window = display_sf_second_window(selectfiles_window)

            for index_of_file in selected_items:
                # Selected files deletion
                os.remove(PATH + LIST_OF_FILES[index_of_file])

            info_label = Label(info_window, text="Files deleted")
            info_label.pack(pady=20)
            

    # Delete selected files button
    delete_btn = Button(selectfiles_window, text="Delete", command=remove_selected_files)
    delete_btn.place(x=100, y=(WINDOW_HEIGHT + 60))

    # Delete all files button
    delete_anyway_btn = Button(selectfiles_window, text="Delete all anyway", command=delete_all)
    delete_anyway_btn.place(x=260, y=(WINDOW_HEIGHT + 60))