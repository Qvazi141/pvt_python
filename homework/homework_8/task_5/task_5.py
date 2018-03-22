# Реализовать программу, позволяющую осуществлять управление файлами:
# копирование, создание, удаление, переименование. Необходимо предусмотреть возможность смен директории.
# Изначально используется текущий каталог запуска скрипта программы.

from os import chdir


def command_call(q, commands, command, path):
    if command == "quit":
        return commands[command]()
    elif command == "touch":
        path = commands[command](path)
    return True


def help():
    print("call command quit - for quit programm")
    print("call command touch - for create file")
    print("call command cp - for copy file")
    print("call command rm - for del file")
    print("call command mv - for rename file")
    print("call command cd - for change dir")



def quit_app():
    return False


def touch(path):
    name = input("Enter filename:")
    try:
        with open(path+name, "r"):
            print("File already exists")
    except FileNotFoundError:
        with open(path+name, "w"):
            print("File already exists")
    return path

def cp():
    pass


def rm():
    pass


def mv():
    pass


def cd():
    pass

if __name__ == "__main__":
    my_commands = {
        'help': help,
        'quit': quit_app,
        'touch': touch,
        'cp': cp,
        'rm': rm,
        'mv': mv,
        'cd': cd
    }
    my_path = ""
    print("Print help - for print command.")
    open_app = True
    while open_app:
        command = input(">>> ")
        open_app = command_call(open_app, my_commands, command, my_path)
