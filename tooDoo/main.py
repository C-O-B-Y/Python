# TooDoo
# license: MIT
# Contributors: Coby McKinney

import os

to_do_list = []


def main():
    print("Welcome to the TooDoo App!")
    run_app()


def run_app():
    build_list(to_do_list)
    print_list(to_do_list)
    run_app()


def build_list(val):
    data = input("Input something you need to accomplish or delete: ")
    if data in val:
        print("Already Exists!")
        attempt_delete(data)
    if data not in val:
        val.append(data)
    print("Added 1 task to your list.")


def print_list(val):
    os.system("cls")
    print("My To-Do list:")
    for x in val:
        task_num = val.index(x)
        print(str(task_num + 1) + ") " + str(x))


def attempt_delete(val):
    data = input("Do you wish to delete this task? (Y/N) ")

    if data == "Y" or data == "y":
        delete(val)
    elif data == "N" or data == "n":
        print("Ok")


def delete(val):
    to_do_list.remove(val)
    print_list(to_do_list)
    run_app()


if __name__ == "__main__":
    main()
