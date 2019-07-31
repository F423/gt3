from t3 import *

import tkinter as tk
from tkinter import *

from t3_gui_functions import *

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

project_button_frame = Frame(gui, bg="white")
project_button_frame.pack(side=LEFT, fill=BOTH)

project_list_box_frame = Frame(gui, background="white")
project_list_box_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

task_list_box_frame = Frame(gui, background="white")
task_list_box_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

task_button_frame = Frame(gui, background="white")
task_button_frame.pack(side=LEFT, fill=BOTH)







new_project_button = tk.Button(project_button_frame, text="New Project", borderwidth=2, command=new_project_method,
                               width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
edit_project_button = tk.Button(project_button_frame, text="Edit Project", borderwidth=2, command=edit_project_method,
                                width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
delete_project_button = tk.Button(project_button_frame, text="Delete Project", borderwidth=2, command=delete_project_method,
                                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
quit_button = tk.Button(project_button_frame, text="Quit", borderwidth=2, command=quit, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

new_project_button.pack(side=TOP)
edit_project_button.pack(side=TOP)
delete_project_button.pack(side=TOP)
quit_button.pack(side=TOP)

project_list_box = Listbox(project_list_box_frame)
project_list_box.pack(side=TOP, fill=BOTH, expand=TRUE)

task_list_box = Listbox(task_list_box_frame)
task_list_box.pack(side=TOP, fill=BOTH, expand=TRUE)





new_task_button = tk.Button(task_button_frame, text="New Task", borderwidth=2, command=new_task_method,
                               width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
edit_task_button = tk.Button(task_button_frame, text="Edit Task", borderwidth=2, command=edit_task_method,
                                width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
delete_task_button = tk.Button(task_button_frame, text="Delete Task", borderwidth=2, command=delete_task_method,
                                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

new_task_button.pack(side=TOP)
edit_task_button.pack(side=TOP)
delete_task_button.pack(side=TOP)








gui.mainloop()
