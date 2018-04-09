# test func add
def test_add(func, test_result = ['test','test','test','test']):
    result = func()
    print("Test passed") if result == test_result else print("Test not passed")


# test func remove
def test_remove(func):
    """For test need add string to bd"""
    with open("student_bd.txt", "r+", encoding='utf-8') as f:
        data = f.readlines()
    n = func("student_bd.txt")
    with open("student_bd.txt", "r+", encoding='utf-8') as f:
        test_data = f.readlines()
    print("Test passed") if data[n-1] != test_data[n-1] else print("Test not passed")


# test func find
def test_find(func, test_result = {1: {'Name': 'lara', 'Surname': 'tara', 'Sex': 'fem', 'Age': '22'}}):
    "For test - add test_result in bd, and for find enter key_word from test_result"
    with open("student_bd.txt", "r", encoding='utf-8') as f:
        data = f.readlines()
    result = func(data)
    print("Test passed") if result == test_result  else print("Test not passed")