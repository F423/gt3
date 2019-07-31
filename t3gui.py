from t3 import *

import tkinter as tk
from tkinter import *

# window height
WINDOW_HEIGHT = 800
# window width
WINDOW_WIDTH = 800
# button height
BUTTON_HEIGHT = 1
# button width
BUTTON_WIDTH = 10

# list of projects
project_list = []

# initialize tk
gui = tk.Tk()

# set the title of the window
gui.title("T3: Todo-list / Time / Tracker")

left_frame = Frame(gui, bg="white")
left_frame.pack(side=LEFT, fill=BOTH)

center_frame = Frame(gui, background="black")
center_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

right_frame = Frame(gui, background="blue")
right_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)


def new_project_method():
    print("new project")


def edit_project_method():
    print("edit project")


def delete_project_method():
    print("delete project")


new_project_button = tk.Button(left_frame, text="New Project", borderwidth=2, command=new_project_method,
                               width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
edit_project_button = tk.Button(left_frame, text="Edit Project", borderwidth=2, command=edit_project_method,
                                width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
delete_project_button = tk.Button(left_frame, text="Delete Project", borderwidth=2, command=delete_project_method,
                                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
quit_button = tk.Button(left_frame, text="Quit", borderwidth=2, command=quit, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

new_project_button.pack(side=TOP)
edit_project_button.pack(side=TOP)
delete_project_button.pack(side=TOP)
quit_button.pack(side=TOP)

project_list_box = Listbox(center_frame)
project_list_box.pack(side=TOP, fill=BOTH, expand=TRUE)

task_list_box = Listbox(right_frame)
task_list_box.pack(side=TOP, fill=BOTH, expand=TRUE)

gui.mainloop()
