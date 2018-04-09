# test push
def test_push(func, test_stack=[1, 2, 3, 4], test_number=5, result=[1, 2, 3, 4, 5]):
    test = func(test_stack, test_number)
    if result == test:
        print('test func_push passed')


# test pop
def test_pop(func, test_stack=[1,2,3,4], result_last_element = 4):
    test_element = func(test_stack)
    if result_last_element == test_element:
        print('test func_pop passed')


# test back
def test_back(func, test_stack=(1, 2, 3, 4), result=4):
    test = func(test_stack)
    if result == test:
        print('test func_back passed')


# test size
def test_size(func, test_stack=(1, 2, 3, 4), result=4):
    test = func(test_stack)
    if result == test:
        print('test func_size passed')


# test clear
def test_clear(func, result=[]):
    test = func()
    if result == test:
        print('test func_clear passed')
