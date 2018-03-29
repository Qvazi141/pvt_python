def test_add(add, test_result=["test", "test", "test", "test"]):
    print("Test passed") if test_result == add() else print("Not passed")


def test_del(func_del, path_to_bd="/home/eugene/PycharmProjects/pvt_python/homework/homework_8/task_3/student_bd.txt"):
    test_data = [
        "Eugene Bulakhau man 23\n",
        "lara tara fem 22\n",
        "Angel Vor fem 21\n",
    ]
    func_del(path_to_bd)
    with open(path_to_bd, "r", encoding='utf-8') as f:
        data = f.readlines()
    print("Test passed") if test_data == data else print("Not passed")
