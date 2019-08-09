from t3 import *
import tkinter as tk
from tkinter import *


# from t3_gui_functions import *
# TODO: seperate functions later

#-TEST#
def new_project_method():
    project_list_box.insert(END, entry.get())
    print("new project")


def edit_project_method():
    print("edit project")


def delete_project_method():
    print("delete project")


def new_task_method():
    print("new task")


def edit_task_method():
    print("edit task")


def delete_task_method():
    print("delete task")


def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)  # change var name later (to avoid scope confusion)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry


# TEST#

'''
 
# TKinter's Hello World: showcases its use with Classes
# should be used in the feature 
    
class Gt3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
'''

# Geometry constants

# window height
WINDOW_HEIGHT = 800
# window width
WINDOW_WIDTH = 800
# button height
BUTTON_HEIGHT = 1
# button width
BUTTON_WIDTH = 10

# list of projects
#project_list = [] #needed ? #TEST#

# initialize tk (root) as gui and set master to default
gui = tk.Tk()
master = Tk()

# set the title of the window
gui.title("GT3: Graphical Todo-list / Time / Tracker")

#######

project_button_frame = Frame(gui, bg="white")
project_button_frame.pack(side=LEFT, fill=BOTH)

project_list_box_frame = Frame(gui, background="white")
project_list_box_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

task_list_box_frame = Frame(gui, background="white")
task_list_box_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

task_button_frame = Frame(gui, background="white")
task_button_frame.pack(side=LEFT, fill=BOTH)

#########

new_project_button = tk.Button(project_button_frame, text="New Project",
                               borderwidth=2, command=new_project_method,
                               width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

edit_project_button = tk.Button(project_button_frame, text="Edit Project",
                                borderwidth=2, command=edit_project_method,
                                width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

delete_project_button = tk.Button(project_button_frame, text="Delete Project",
                                  borderwidth=2, command=delete_project_method,
                                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

new_project_button.pack(side=TOP)
edit_project_button.pack(side=TOP)
delete_project_button.pack(side=TOP)

project_list_box = Listbox(project_list_box_frame)
project_list_box.pack(side=TOP, fill=BOTH, expand=TRUE)

task_list_box = Listbox(task_list_box_frame)
task_list_box.pack(side=TOP, fill=BOTH, expand=TRUE)

#######

new_task_button = tk.Button(task_button_frame, text="New Task",
                            borderwidth=2, command=new_task_method,
                            width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

edit_task_button = tk.Button(task_button_frame, text="Edit Task",
                             borderwidth=2, command=edit_task_method,
                             width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

delete_task_button = tk.Button(task_button_frame, text="Delete Task",
                               borderwidth=2, command=delete_task_method,
                               width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

new_task_button.pack(side=TOP)
edit_task_button.pack(side=TOP)
delete_task_button.pack(side=TOP)

# Entry Widget & String value: gets user's text input (testing)
entry = Entry(master)
entry.pack()

entry.focus_set()


def callback():
    print(entry.get())

#-TEST#
b = Button(master, text="Add", width=10, command=new_project_method)
b.pack()
#TEST-#


# uncomment to add the button demonstrated in TKinter's hello world above
# app = Gt3(master=gui)

# executes the gui (calls tk's main)
gui.mainloop()

entry = Entry(master, width=100)
entry.pack()

text = entry.get()

##### #########


user = makeentry(gui, "User name:", 10)
password = makeentry(gui, "Password:", 10, show="*")
content = StringVar()
entry = Entry(gui, text="caption", textvariable=content)

text = content.get()
content.set(text)

# Quit button
quit_button = tk.Button(project_button_frame, text="Quit",
                        borderwidth=2, command=quit,
                        width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
quit_button.pack(side=TOP)
