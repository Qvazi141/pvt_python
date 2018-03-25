from datetime import datetime


# Декоратор для вывода времени выполнения функции
def elapsed_time_decorator(function_to_decorate):
    def wrapper():
        start_time = datetime.now()
        function_to_decorate()
        end_time = datetime.now()
        print("Elapsed time: {} sec".format(end_time - start_time))
        return end_time - start_time
    return wrapper


# Декоратор для записи имени, аргументов и времени выполнения функции в файл
def name_args_time_decorator(function_to_decorate):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        function_to_decorate(*args, **kwargs)
        end_time = datetime.now()
        with open("func_attribute.txt", "w", encoding='utf-8') as f:
            f.write("Name: " + function_to_decorate.__name__ + '\n')
            f.write("Args: " + str(args) + str(kwargs) + '\n')
            f.write("Elapsed time: {} sec".format(end_time - start_time))
    return wrapper


# Декоратор для проверки типа аргумента функции
def check_type_decorator(function_to_decorate):
    def wrapper(type_check):
        try:
            assert isinstance(type_check, (int, str, list)), TypeError
            function_to_decorate(type_check)
            return wrapper
        except TypeError:
            print("Attribute mismatch, must be list or int or string")
            return wrapper
    return wrapper


# Декоратор для кеширования функции
def cache_decorator(function_to_decorate):
    memory = {}

    def wrapper(*args):
        if args in memory:
            return memory[args]
        else:
            element = function_to_decorate(*args)
            memory[args] = element
            return element
    return wrapper
