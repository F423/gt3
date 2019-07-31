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

# set the background color of the window
# gui.configure(background="black")

left_frame = Frame(gui)
left_frame.pack(side=LEFT)

center_frame = Frame(gui)
center_frame.pack()

right_frame = Frame(gui)
right_frame.pack(side=RIGHT)


canvas = tk.Canvas(gui, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
canvas.pack()


def new_project_method():
    print("new project")

def edit_project_method():
    print("edit project")

def delete_project_method():
    print("delete project")


new_project_button = tk.Button(left_frame, text="New Project", borderwidth=2,command=new_project_method,width=BUTTON_WIDTH,height=BUTTON_HEIGHT)



edit_project_button = tk.Button(left_frame, text="Edit Project",borderwidth=2,command=edit_project_method,width=BUTTON_WIDTH,height=BUTTON_HEIGHT)
delete_project_button = tk.Button(left_frame, text="Delete Project",borderwidth=2,command=delete_project_method,width=BUTTON_WIDTH,height=BUTTON_HEIGHT)
quit_button = tk.Button(left_frame, text="Quit",borderwidth=2,command=quit,width=BUTTON_WIDTH,height=BUTTON_HEIGHT)

new_project_button.pack(side=TOP)
edit_project_button.pack(side=TOP)
delete_project_button.pack(side=TOP)
quit_button.pack(side=TOP)



gui.mainloop()




