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


# test push
def test_push(test_stack=[1, 2, 3, 4], test_number=5, result=[1, 2, 3, 4, 5]):
    test = push(test_stack, test_number)
    if result == test:
        print('test func_push passed')


def pop(stack):
    """Удалить из стека последний элемент.
    Программа должна вывести его значение."""
    return stack[-1], stack[:-1]


# test pop
def test_pop(test_stack=[1,2,3,4], result=[1,2,3], result_last_element = 4):
    test_element, test = pop(test_stack)
    if result == test and result_last_element == test_element:
        print('test func_pop passed')


def back(stack):
    """Программа должна вывести значение последнего элемента,
    не удаляя его из стека. """
    return stack[-1]


# test back
def test_back(test_stack=(1, 2, 3, 4), result=4):
    test = back(test_stack)
    if result == test:
        print('test func_back passed')


def size(stack):
    """Программа должна вывести количество элементов в стеке."""
    count = 0
    for i in stack:
        count += 1
    return count


# test size
def test_size(test_stack=(1, 2, 3, 4), result=4):
    test = size(test_stack)
    if result == test:
        print('test func_size passed')


def clear():
    """Программа должна очистить стек и вывести ok."""
    return []


# test clear
def test_clear(result=[]):
    test = clear()
    if result == test:
        print('test func_clear passed')


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
    test_push()
    test_pop()
    test_back()
    test_size()
    test_clear()
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
                pop_element, main_stack = menu_actions[choice[0]](main_stack)
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

