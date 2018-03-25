# Реализовать модуль, содержащий следующие функции декораторы:
# декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
# декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл;
# декоратор, проверяющий типы, переданных декорируемой функции, аргументов.
# декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции.
# декораторы лежат в packet packet_for_hw_11 - корневая директория
from packet_for_hw_11 import task_0
from time import sleep


@task_0.elapsed_time_decorator
def hello_world():
    sleep(0.5)
    print("decorator 1 passed")


@task_0.name_args_time_decorator
def hello_world_2(*args, **kwargs):
    sleep(0.5)
    print("decorator 2 passed")


@task_0.check_type_decorator
def hello_world_3(type_int):
    print("decorator 3 passed")


@task_0.cache_decorator
def fib(n):
    if n < 2: return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    hello_world()
    hello_world_2(1, 2, 3, 4)
    hello_world_3(1)
    fib(4)
    fib(4)
