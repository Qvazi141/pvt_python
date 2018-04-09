from packet_for_test_hw_7 import test


def menu():
    print("-"*40)
    print("Main menu:")
    print("\tpush n\t - for add n;")
    print("\tpop\t\t - for del last element;")
    print("\tback\t - for print last element;")
    print("\tsize\t - for stack size;")
    print("\tclear\t - for clear stack;")
    print("\texit\t - for exit program.")
    print("-"*40)


def push(stack, number):
    """Добавить в стек число n (значение n задается после команды).
    Программа должна вывести ok."""
    tmp = [number]
    return stack + tmp


def pop(stack):
    """Удалить из стека последний элемент.
    Программа должна вывести его значение."""
    return stack[-1]


def back(stack):
    """Программа должна вывести значение последнего элемента,
    не удаляя его из стека. """
    return stack[-1]


def size(stack):
    """Программа должна вывести количество элементов в стеке."""
    count = 0
    for i in stack:
        count += 1
    return count


def clear():
    """Программа должна очистить стек и вывести ok."""
    return []


if __name__ == "__main__":
    main_stack = []
    menu_actions = {
        "menu": menu,
        "push": push,
        "pop": pop,
        "back": back,
        "size": size,
        "clear": clear,
    }
    q = True
    test.test_push(push)
    test.test_pop(pop)
    test.test_back(back)
    test.test_size(size)
    test.test_clear(clear)
    menu()
    while q:
        choice = input('>>> ').lower().split()
        if not choice:
            menu_actions['menu']()
        elif choice[0] == 'push':
            try:
                main_stack = menu_actions[choice[0]](main_stack, choice[1])
                print(">>> ok")
            except KeyError:
                print('Is there something wrong')
                menu_actions['menu']()
        elif choice[0] == 'pop':
            try:
                pop_element,  = menu_actions[choice[0]](main_stack)
                main_stack = main_stack[:-1]
                print(">>> {}".format(pop_element))
            except KeyError:
                print('Is there something wrong')
                menu_actions['menu']()
        elif choice[0] == 'back':
            try:
                last_element = menu_actions[choice[0]](main_stack)
                print(">>> {}".format(last_element))
            except KeyError:
                print('Is there something wrong')
                menu_actions['menu']()
        elif choice[0] == 'size':
            try:
                stack_size = menu_actions[choice[0]](main_stack)
                print(">>> {}".format(stack_size))
            except KeyError:
                print('Is there something wrong')
                menu_actions['menu']()
        elif choice[0] == 'clear':
            try:
                main_stack = menu_actions[choice[0]]()
                print(">>> ok")
            except KeyError:
                print('Is there something wrong')
                menu_actions['menu']()
        elif choice[0] == 'exit':
                print(">>> bye")
                q = False

