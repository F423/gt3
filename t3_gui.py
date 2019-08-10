from t3 import *
import os
import tkinter as tk
from tkinter import *
import json


# from t3_gui_functions import *
# TODO: seperate functions later

#-TEST#

def read_projects_method():
    inputFile = 'tasks/tasks.json'
    jsonData = open(inputFile).read()
    jsonToPython = json.loads(jsonData)

    t3json = jsonToPython['t3']  # pld
    dumpprojects(t3json)

    for pname in t3json:
        tasklist = t3json[pname]
        print("Project " + pname)
        project_list_box.insert(END, pname)




def new_project_method():
    project_list_box.insert(END, entry.get())
    print("new project")

    os.system("t3.py --add" + entry.get() + " task1 task2")


def edit_project_method():
    print("edit project")


def delete_project_method():
    project_list_box.delete(0, END)
    print("delete project")

#TODO:
"""
def del_all_projects_method():
    project_list_box_frame.delete(0, END)
    print("delete project")
"""

def new_task_method():
    task_list_box.insert(END, entry.get())
    print("new task")


def edit_task_method():

    print("edit task")


def delete_task_method():
    task_list_box.delete(0, END)
    print("delete task")
"""
def del_all_tasks_method():
    task_list_box.delete(0, END)
    print("delete task")
"""

#credits to http://effbot.org/tkinterbook

def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)  # change var name later (to avoid scope confusion)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry


# Geometric constants

# window height
WINDOW_HEIGHT = 800
# window width
WINDOW_WIDTH = 800
# button height
BUTTON_HEIGHT = 1
# button width
BUTTON_WIDTH = 10

# list of projects
#project_list = [] #DEL# needed?

# initialize tk (root) as gui and set master to default
gui = tk.Tk()
master = Tk()

# set the title of the window
gui.title("GT3: Graphical Todo-list / Time / Tracker")


project_button_frame = Frame(gui, bg="white")
project_button_frame.pack(side=LEFT, fill=BOTH)

project_list_box_frame = Frame(gui, background="white")
project_list_box_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

task_list_box_frame = Frame(gui, background="white")
task_list_box_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

task_button_frame = Frame(gui, background="white")
task_button_frame.pack(side=LEFT, fill=BOTH)


new_project_button = tk.Button(project_button_frame, text="New Project",
                               borderwidth=2, command=new_project_method,
                               width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

edit_project_button = tk.Button(project_button_frame, text="Edit Project",
                                borderwidth=2, command=edit_project_method,
                                width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

delete_project_button = tk.Button(project_button_frame, text="Delete Project",
                                  borderwidth=2, command=delete_project_method,
                                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
#TODO:
"""
del_all_projects_button = tk.Button(project_button_frame, text="Del. All Projects",
                                  borderwidth=2, command=del_all_projects_method(),
                                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
"""

new_project_button.pack(side=TOP)
edit_project_button.pack(side=TOP)
delete_project_button.pack(side=TOP)
#del_all_projects_button.pack(side=TOP)


project_list_box: Listbox = Listbox(project_list_box_frame)
project_list_box.pack(side=TOP, fill=BOTH, expand=TRUE)

task_list_box = Listbox(task_list_box_frame)
task_list_box.pack(side=TOP, fill=BOTH, expand=TRUE)



new_task_button = tk.Button(task_button_frame, text="New Task",
                            borderwidth=2, command=new_task_method,
                            width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

edit_task_button = tk.Button(task_button_frame, text="Edit Task",
                             borderwidth=2, command=edit_task_method,
                             width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

delete_task_button = tk.Button(task_button_frame, text="Delete Task",
                               borderwidth=2, command=delete_task_method,
                               width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
#TODO:
"""
del_all_tasks_button = tk.Button(task_button_frame, text="Del. All Tasks",
                               borderwidth=2, command=del_all_tasks_method(),
                               width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
"""

new_task_button.pack(side=TOP)
edit_task_button.pack(side=TOP)
delete_task_button.pack(side=TOP)
#TODO: del_all_tasks_button.pack(side=TOP)


read_projects_method()

# Entry Widget & String value: gets user's text input (testing)
entry = Entry(master)
entry.pack()

entry.focus_set()

"""
def callback():
    print(entry.get())
"""
# Entry Widget buttons (pb: project button, tb: task button)
pb = Button(master, text="Projects++", width=10, command=new_project_method)
pb.pack()

tb = Button(master, text="Tasks++", width=10, command=new_task_method)
tb.pack()
# executes the gui (calls tk's main)
gui.mainloop()

# Entry variables (includes same)
entry = Entry(master, width=100)
entry.pack()

text = entry.get()


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
