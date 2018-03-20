# Реализовать программу с базой учащихся группы (данные хранятся в файле).
# Записи по учащемуся: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.


def print_menu():
    print("-"*40)
    print("Main menu:")
    print("\tmenu n\t - for print main menu")
    print("\tadd n\t - for add item")
    print("\tdel n\t - for fr del item")
    print("\tfind n\t - for find word")
    print("-" * 40)


def menu_selection(items):
    cursor = input(">>> ").lower()
    if cursor == "menu":
        items["menu"]()
    elif cursor == "add":
        items["add"]()
    elif cursor == "del":
        items["remove"]()
    elif cursor == "find":
        items["find"]()


def add():
    pass

def remove():
    pass

def find():
    pass

if __name__ == "__main__":
    q = True
    menu_items = {
        "menu": print_menu,
        "add": add,
        "del": remove,
        "find": find
    }
    print_menu()
    while q:
        menu_selection(menu_items)
