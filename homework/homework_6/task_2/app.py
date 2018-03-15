from packet_for_hw_6_task_2 import *

if __name__ == "__main__":
    q = True
    while q:
        inp = input("Введите task[0-4] для выполнения задач из homework_5,\n"
                    "q - для выхода: ")
        if inp == 'task0':
            print(task_0.start.__doc__)
            task_0.start()
            print('-' * 20)
        elif inp == 'task1':
            print(task_1.start.__doc__)
            task_1.start()
            print('-' * 20)
        elif inp == 'task2':
            print(task_2.start.__doc__)
            task_2.start()
            print('-' * 20)
        elif inp == 'task3':
            print(task_3.start.__doc__)
            task_3.start()
            print('-' * 20)
        elif inp == 'task4':
            print(task_4.start.__doc__)
            task_4.start()
            print('-' * 20)
        elif inp == 'q':
            q = False

