# Реализовать программу с базой учащихся группы (данные хранятся в файле).
# Записи по учащемуся: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.
from packet_for_test_hw_8 import test_task_3

def print_menu():
    """Функция вывода основного меню."""
    print("-"*40)
    print("Main menu:")
    print("\tmenu - for print main menu")
    print("\tadd - for add item")
    print("\tdel - for fr del item")
    print("\tfind - for find word")
    print("\tq - for quit program")
    print("-" * 40)


def menu_selection(items, path):
    """Функция выбора меню. Осуществляет вызов других функций."""
    cursor = input(">>> ").lower()
    if cursor == "menu":
        items["menu"]()
    elif cursor == "add":
        with open(path, "a", encoding='utf-8') as f:
            f.write(" ".join(items["add"]())+'\n')
    elif cursor == "del":
        items["del"](path)
    elif cursor == "find":
        with open(path, "r", encoding='utf-8') as f:
            bd_for_search = f.readlines()
        print(items["find"](bd_for_search))
    elif cursor == "q":
        return items["quit"]()
    return True


def add():
    """Функция добавления элемента. Возвращает список для добавления."""
    bd_structure = ("Name", "Surname", "Sex", "Age")
    add_list = []
    for i in bd_structure:
        add_list.append(input("Enter {}: ".format(i)))
    return add_list


def remove(path):
    """Функция удаления элементов. Удаляет по номеру, возвращает номер удаленного элемента"""
    n = int(input("Enter element №: "))
    with open(path, "r+", encoding='utf-8') as f:
        temp = f.readlines()
        f.seek(0)
        for line in range(len(temp)):
            if not line + 1 == n:
                f.write(temp[line])
        f.truncate()
    return n
        

def find(bd_in_list):
    """Функция поиска. Возвращает словарь совпадений"""
    # подготовка структуры для поиска
    bd_structure = ("Name", "Surname", "Sex", "Age")
    bd_in_dict = {}
    try:
        for element_id, element in enumerate(bd_in_list):
                temp = element.split()
                bd_in_dict[element_id] = {bd_structure[i]: temp[i].lower() for i in range(len(bd_structure))}
        bd_in_list.clear()
        temp.clear()
    except:
        return "Database is empty" if bd_in_list == [] else "Database structure error"
    # ввод данных для поиска
    fields = input('Enter search fields Name/Surname/Sex/Age: ').split("/")
    key_words = {field: input("{}: ".format(field)).lower() for field in fields}
    result = {}
    # поиск
    for element_id, element in enumerate(bd_in_dict):
        for field in fields:
            if bd_in_dict[element].get(field) == key_words.get(field):
                result[element_id] = bd_in_dict[element]
    return result


def exit_application():
    """Функция закрытия программы. Возвращает значение False"""
    return False


if __name__ == "__main__":
    # test_task_3.test_add(add)
    # test_task_3.test_remove(remove)
    # test_task_3.test_find(find)
    path = "student_bd.txt"
    quit_program = True
    menu_items = {
        "menu": print_menu,
        "add": add,
        "del": remove,
        "find": find,
        "quit": exit_application
    }
    print_menu()
    while quit_program:
        quit_program = menu_selection(menu_items, path)
