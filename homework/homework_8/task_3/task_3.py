# Реализовать программу с базой учащихся группы (данные хранятся в файле).
# Записи по учащемуся: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.


def print_menu():
    print("-"*40)
    print("Main menu:")
    print("\tmenu - for print main menu")
    print("\tadd - for add item")
    print("\tdel - for fr del item")
    print("\tfind - for find word")
    print("-" * 40)


def menu_selection(items, path):
    cursor = input(">>> ").lower()
    if cursor == "menu":
        items["menu"]()
    elif cursor == "add":
        with open(path, "a", encoding='utf-8') as f:
            f.write(" ".join(items["add"]())+'\n')
    elif cursor == "del":
        items["del"]()
    elif cursor == "find":
        items["find"]()


def add():
    bd_struct = ("Name", "Surname", "Sex", "Age")
    add_list = []
    for i in bd_struct:
        add_list.append(input("Enter {}: ".format(i)))
    return add_list


def remove():
    n = int(input("Enter element №: "))
    with open(path, "r+", encoding='utf-8') as f:
        temp = f.readlines()
        f.seek(0)
        for line in range(len(temp)):
             if line+1 != n:
                 f.write(temp[line])
        f.truncate()
        

def find():
    pass

if __name__ == "__main__":
    path = "student_bd.txt"
    q = True
    menu_items = {
        "menu": print_menu,
        "add": add,
        "del": remove,
        "find": find
    }
    print_menu()
    while q:
        menu_selection(menu_items, path)
