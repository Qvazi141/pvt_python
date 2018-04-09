# Реализовать программу с базой учащихся группы. Записи по учащемуся: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.


# функция добавления элементов в базу
def add_student():
    const_list = ['Name', 'Surname', 'Sex', 'Age']
    student = {}
    for i in const_list:
        student[i] = input('Input {} : '.format(i))
    return student


# функция удаления элементов по ключу
def del_student(data, key):
    del data[key - 1]
    return data


# Функция поиска элементов базы по значениям определнных полей, возвращает словарь совпадений
def find(data, key_words, fields):
    student = {}
    for id, i in enumerate(data):
        for j in range(len(fields)):
            if i.get(fields[j]).upper() == key_words[j].upper():
                student[id] = i
    return student


# функция вывода базы
def print_bd(data):
    for id, i in enumerate(data):
        print('Student № {}: '.format(id + 1))
        for j in i:
            print('{0}: {1}'.format(j, data[id][j]))
        print()
    print('-' * 20)


# основная программа
if __name__ == '__main__':
    student_bd = [{'Name': 'Lara', 'Surname': 'Scomor', 'Sex': 'Female', 'Age': '22'}]
    while True:
        inp = input('Enter:\n"add" - for add student\n"del" - for delete student\n"print" - for print group list'
                    '\n"find" - for find\n"q" - for exit program \n')
        if inp == 'q':
            break
        elif inp == 'add':
            student_bd.append(add_student())
        elif inp == 'del':
            student_bd = del_student(student_bd, int(input('input student number: ')))
        elif inp == 'find':
            fields_for_find = input('Enter search fields Name/Surname/Sex/Age: ').split("/")
            search_words = []
            for i in fields_for_find:
                search_words.append(input("Enter {} for search: ".format(i)))
            bd_for_find = find(student_bd, search_words, fields_for_find)
            print(*bd_for_find.items())
        elif inp == 'print':
            print_bd(student_bd)
