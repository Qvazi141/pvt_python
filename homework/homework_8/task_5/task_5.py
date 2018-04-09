# Реализовать программу, позволяющую осуществлять управление файлами:
# копирование, создание, удаление, переименование. Необходимо предусмотреть возможность смен директории.
# Изначально используется текущий каталог запуска скрипта программы.
import os


def command_call(q, commands, command, path):
    """Func for call command, return boolean type and path"""
    try:
        if not command:
            return True, path
        if command[0] == "quit":
            return commands[command[0]](path)
        elif command[0] == "touch":
            path = commands[command[0]](path,command)
        elif command[0] == "help":
            path = commands[command[0]](path)
        elif command[0] == "pwd":
            path = commands[command[0]](path)
        elif command[0] == "ls":
            path = commands[command[0]](path)
        elif command[0] == "cp":
            path = commands[command[0]](path, command)
        elif command[0] == "mv":
            path = commands[command[0]](path, command)
        elif command[0] == "rm":
            path = commands[command[0]](path, command)
        elif command[0] == "cd":
            path = commands[command[0]](path, command)
        return True, path
    except PermissionError:
        print("Permission denied")
        return True, path


def print_help(path):
    """print all available commands"""
    print('call command quit - for quit program')
    print('call command touch [file_name] - for create file')
    print('call command cp [file_name] [file_name2] - for copy !only! file')
    print('call command rm [file_name] - for del !only! file')
    print('call command mv [file_name] [file_name2] - for rename file in the current directory')
    print('call command cd - for change dir')
    print('call command pwd - for print path')
    print('call command ls - for list directory contents ')
    return path


def check_arguments(args, count):
    """Func for check arguments count"""
    if len(args) > count:
        return False
    else:
        return True


def quit_app(path):
    """Func for quit program, return boolean type"""
    return False, path


def ls(path):
    """Функция для вывода списка содержимого текущей директории,
    возвращает path текущей директории"""
    for element in os.listdir(path):
        print(element)
    return path


def touch(path, file_name):
    """Функция для создания файла, возвращает path текущей директории"""
    if not check_arguments(file_name, 2):
        print('Argument mismatch')
        return path
    with open(path+'/'+file_name[1], "w+"):
        print('File created')
    return path


def pwd(path):
    """Функция для вывода текущего path, возвращает текущий path"""
    print(path)
    return path


def cp(path, file_names):
    """Функция для копирования файла, возвращает текущую директорию"""
    if not check_arguments(file_names, 3):
        print('Argument mismatch')
        return path
    try:
        with open(path + '/' + file_names[1], "r") as f:
            copy = f.read()
        with open(path + '/' + file_names[2], "w") as f:
            f.write(copy)
    except FileNotFoundError:
        print('File not found')
    return path


def rm(path, file_name):
    """Функция для удаления файла, возвращает текущую директорию"""
    if not check_arguments(file_name, 2):
        print('Argument mismatch')
        return path
    try:
        os.remove(path + '/' + file_name[1])
    except FileNotFoundError:
        print('File not found')
    return path


def mv(path, file_names):
    """Функция для переименования файла, возвращает текущую директорию"""
    if not check_arguments(file_names, 3):
        print('Argument mismatch')
        return path
    try:
        with open(path + '/' + file_names[1], "r") as f:
            copy = f.read()
        os.remove(path + '/' + file_names[1])
        with open(path + '/' + file_names[2], "w") as f:
            f.write(copy)
    except FileNotFoundError:
        print('File not found')
    return path


def cd(path, path_to_move):
    """Функция для перехода в другой path, возвращает path перехода"""
    if not check_arguments(path_to_move, 2):
        print('Argument mismatch')
        return path
    try:
        os.chdir(path_to_move[1])
        return path_to_move[1]
    except FileNotFoundError:
        print("Path not found")
        return path


if __name__ == "__main__":
    """Точка входа в программу"""
    my_commands = {
        'help': print_help,
        'quit': quit_app,
        'touch': touch,
        'cp': cp,
        'rm': rm,
        'mv': mv,
        'cd': cd,
        'pwd': pwd,
        'ls': ls
    }
    my_path = os.path.abspath(os.curdir)
    print('Enter help - for print command.')
    open_app = True
    while open_app:
        my_command = input('>>> ').split()
        if my_path[-1] == '/' or my_path[-1] == '\\':
            my_path = my_path[:-1]
        open_app, my_path = command_call(open_app, my_commands, my_command, my_path)
