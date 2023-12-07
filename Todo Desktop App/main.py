

# this program contains the todo desktop application

from todo import Todo
import PySimpleGUI as sg
import datetime

# setting theme
sg.theme("BlueMono")

# creating elements
time_label = sg.Text("", key="time_label")
todo_label = sg.Text("Type in a TO-DO")
todo_input = sg.Input(tooltip="Enter todo", key="todo_input")
add_button = sg.Button(button_text="Add", tooltip="Add", mouseover_colors="LightBlue2", size=10, key="Add")
list_box = sg.Listbox(values=Todo.get_todos(),
                      enable_events=True, key="todo_listbox", size=[45, 10])
edit_button = sg.Button(button_text="Edit", key="Edit")
complete_button = sg.Button(key="Complete", button_text="Complete", size=10, mouseover_colors="LightBlue2",
                            tooltip="Complete")
exit_button = sg.Button("Exit", key="Exit")

# creating layout
layout = [
    [time_label],
    [todo_label],
    [todo_input, add_button],
    [list_box, edit_button, complete_button, exit_button]
]

# creating window
window = sg.Window(title="Todo List App",
                   layout=layout)

while True:
    event, values = window.read(timeout=1000)
    planner_time = datetime.datetime.now()
    window['time_label'].update(value=planner_time.strftime("%d %b %Y, %H:%M:%S"))

    # checking if window is closed by the user
    if event == sg.WINDOW_CLOSED:
        break

    # now checking for other events
    if event == "Add":
        new_todo = values['todo_input']
        if new_todo == "" or new_todo in ["Nothing to complete.", "Nothing to edit.",
                                          "Nothing to add.", "Select a task to complete.",
                                          "Select a task to edit."]:
            sg.popup("Nothing to Add", font=('Helvitica', 15))
        else:
            Todo.write_todo(new_todo)
            window['todo_listbox'].update(values=Todo.get_todos())
            window['todo_input'].update(value="")
    elif event == "Edit":
        v = values
        if not values['todo_listbox']:
            sg.popup("Nothing to edit.", font=("Helvitica", 15))
        else:
            todo_to_edit = values['todo_listbox'][0]
            index = Todo.get_todos().index(todo_to_edit)
            Todo.edit_todo(index, values['todo_input'] + "\n")
            window['todo_listbox'].update(values=Todo.get_todos())
            window['todo_input'].update(value="")
    elif event == "todo_listbox":
        window['todo_input'].update(value=values['todo_listbox'][0])
    elif event == "Complete":
        data = Todo.get_todos()
        if not data:
            sg.popup("Nothing to complete.", font=("Helvitica", 15))
        if not values['todo_listbox']:
            sg.popup("Select a task to complete.", font=("Helvitica", 15))
        else:
            complete_to_be = values['todo_listbox'][0]
            index = Todo.get_todos().index(complete_to_be)
            Todo.complete(index)
            window['todo_listbox'].update(values=Todo.get_todos())
            window['todo_input'].update(value="")
    elif event == "Exit":
        break


window.close()
