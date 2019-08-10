from t3 import *
import json
import os
import tkinter as tk
from tkinter import *

def poll():
    # loop speed control
    # delete_task_button.after(100,poll)

    # tuple with text of all items in Listbox
    all_project_items = project_list_box.get(0, tk.END)
    # tuple with indexes of selected items
    sel_project_index = project_list_box.curselection()
    # list with text of all selected items
    sel_project_item = [all_project_items[item] for item in sel_project_index]

    # tuple with text of all items in Listbox
    all_task_items = task_list_box.get(0, tk.END)
    # tuple with indexes of selected items
    sel_task_index = task_list_box.curselection()
    # list with text of all selected items
    sel_task_item = [all_task_items[item] for item in sel_task_index]



    task_selection = task_list_box.curselection()

   # print("")
   # print("project selection : ")
   # print(sel_project_index)
   # print(sel_project_item)
   # print("task selection")
   # print(task_selection)
   # print("")


    #z = "".join(sel_project_item)
    # get_project_tasks_method(z)
    print()
    print(sel_project_item)
    print(sel_task_item)
    print()
    get_project_tasks_method("".join(sel_project_item))


def on_project_list_box_select(self):
    print("on_project_list_box_select")

    # tuple with text of all items in Listbox
    all_project_items = project_list_box.get(0, tk.END)
    # tuple with indexes of selected items
    sel_project_index = project_list_box.curselection()
    # list with text of all selected items
    sel_project_item = [all_project_items[item] for item in sel_project_index]
    # update the tasks associated with the project
    get_project_tasks_method("".join(sel_project_item))


def on_task_list_box_select(self):
    print("on_task_list_box_select")

    # tuple with text of all items in Listbox
    all_task_items = task_list_box.get(0, tk.END)
    # tuple with indexes of selected items
    sel_task_index = task_list_box.curselection()
    # list with text of all selected items
    sel_task_item = [all_task_items[item] for item in sel_task_index]


def get_selected_project():
    # tuple with text of all items in Listbox
    all_project_items = project_list_box.get(0, tk.END)
    # tuple with indexes of selected items
    sel_project_index = project_list_box.curselection()
    # list with text of all selected items
    sel_project_item = [all_project_items[item] for item in sel_project_index]
    # return selected project
    return sel_project_item


def get_selected_task():
    # tuple with text of all items in Listbox
    all_task_items = task_list_box.get(0, tk.END)
    # tuple with indexes of selected items
    sel_task_index = task_list_box.curselection()
    # list with text of all selected items
    sel_task_item = [all_task_items[item] for item in sel_task_index]
    # return the selected task
    return sel_task_item



def read_projects_method():

    # initialize jason structure
    inputFile = 'tasks/tasks.json'
    jsonData = open(inputFile).read()
    jsonToPython = json.loads(jsonData)
    t3json = jsonToPython['t3']  # pld

    # clear the project list box
    project_list_box.delete(0,'end')

    # iterate through the projects
    for pname in t3json:
        # adds the name of each project to the project list
        project_list_box.insert(END,pname)


def get_project_tasks_method(in_pname):

    if in_pname is None or in_pname is "":
        return

    # setup json structure
    inputFile = 'tasks/tasks.json'
    jsonData = open(inputFile).read()
    jsonToPython = json.loads(jsonData)
    t3json = jsonToPython['t3']  # pld

    # iterate through the json to find the project name
    for pname in t3json:
        # if the project name matches the name to find
        if pname == in_pname:
            # clear the task list
            task_list_box.delete(0, 'end')
            # iterate through the task associated with that project and add them to teh list box
            for task in t3json[pname]:
                # adds the taskName field as the task in the gui
                task_list_box.insert(END, task['taskName'])

            task_list_box.select_set(0)
            task_list_box.event_generate("<<ListboxSelect>>")



def new_project_method():
    print("new project")
    os.system("t3.py --add test_add_project test_task1 test_task2 test_task3")


def edit_project_method():
    print("edit project")


def delete_project_method():
    print("delete project")


def new_task_method():
    print("new task")

    # Create a new window to enter a new task
    global new_task_window
    new_task_window = tk.Toplevel()
    new_task_window.wm_title("New Task")

    # field to allow user to input the name of the task
    new_task_entry_field = Entry(new_task_window)
    new_task_entry_field.pack(side=TOP)

    # create the cancel button
    new_task_cancel_button = tk.Button(new_task_window, text="Cancel", borderwidth=2, command=lambda: new_task_cancel_button_method(new_task_window),
                                   width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    # pack the cancel button
    new_task_cancel_button.pack(side=RIGHT)


    # create the ok button
    new_task_ok_button = tk.Button(new_task_window, text="Ok", borderwidth=2, command=lambda: new_task_ok_button_method(None,new_task_window,new_task_entry_field),
                                   width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    # pack the ok button
    new_task_ok_button.pack(side=LEFT)




def new_task_cancel_button_method(window):
    # destroy the parent window
    window.destroy()


def new_task_ok_button_method(self,window,entry):

    # get the current selected project
    selected_project = get_selected_project()
    print(selected_project)
    os.system("python t3.py --add " + "".join(selected_project) + " " + entry.get())
    on_project_list_box_select(self)
    # destroy the parent window
    window.destroy()


def edit_task_method():
    print("edit task")


def delete_task_method():
    print("delete task")

    # get the current selected task
    selected_task = get_selected_task()
    print("delete task " + "".join(selected_task) )

    # get the current selected project
    selected_project = get_selected_project()
    print("delete task from Project " + "".join(selected_project) )

    print("python t3.py --delete " + "".join(selected_project) + " " + "".join(selected_task))
    os.system("python t3.py --delete " + "".join(selected_project) + " " + "".join(selected_task))

    # os.system("python t3.py --delete project1 task2")

    get_project_tasks_method(selected_project)


# window height
WINDOW_HEIGHT = 800
# window width
WINDOW_WIDTH = 800
# button height
BUTTON_HEIGHT = 1
# button width
BUTTON_WIDTH = 10

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

project_list_box = Listbox(project_list_box_frame, selectmode=SINGLE, exportselection=False)
project_list_box.bind('<<ListboxSelect>>', on_project_list_box_select)
project_list_box.pack(side=TOP, fill=BOTH, expand=TRUE)


task_list_box = Listbox(task_list_box_frame, selectmode=SINGLE, exportselection=False)
task_list_box.bind('<<ListboxSelect>>', on_task_list_box_select)
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


# read existing projects
read_projects_method()


# poll()
gui.mainloop()