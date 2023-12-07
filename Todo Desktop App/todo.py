
# this file contains the todo class

# importing libraries
import os

# global variables
FILENAME = "todo.txt"

# checking if file doesn't exist then create it.
if not os.path.exists("todo.txt"):
    with open("todo.txt", 'w') as file:
        pass

class Todo:
    """
        This class creates an object which can be used to perform various todo tasks.
    """

    # private attributes
    filename = FILENAME

    @staticmethod
    # get_todos()
    def get_todos():
        """
        This function fetch all todos from the filename and returns
        list containing all remaining todos.
        :return:
        """

        # opening file
        file = open(Todo.filename, 'r')
        data = []
        while True:
            line = file.readline()
            if line == "":
                break
            data.append(line)
        file.close()

        return data

    @staticmethod
    # write_todo
    def write_todo(todo):
        """
        This function write the todo on the filename.
        :return:
        """

        with open(Todo.filename, 'a') as f:
            f.write(todo + '\n')

    @staticmethod
    # edit todo
    def edit_todo(index_to_edit, string):
        """
        This function edits an already present todo in the file.
        :return:
        """

        # first we open the file and get all todos
        data = Todo.get_todos()
        index_to_edit = index_to_edit
        for index, todo in enumerate(data):
            if index == int(index_to_edit):
                data[index] = string

        # its only edited locally. We need to write changes on file
        # for this we can call the reset method
        Todo.__reset(data)

    # reset()
    @classmethod
    def __reset(cls, data):
        """
        This function re-writes all todos on the file as present in the data.
        :return:
        """
        fd = open(Todo.filename, 'w')
        for todo in data:
            fd.write(todo)
        fd.close()

    @classmethod
    def complete(cls, index):
        """
        This function removes the specified item from the todos on the file.
        :param index:
        :return:
        """

        index = index
        data = Todo.get_todos()
        data.pop(index)
        Todo.__reset(data)

    # overloading stream output
    @ classmethod
    def __str__(cls):
        """
        This function returns the string representation of todos present in the file.
        :return:
        """

        s = ""
        data = Todo.get_todos()
        for index, todo in enumerate(data):
            s = s + str((index + 1)) + " - " + todo

        return s
