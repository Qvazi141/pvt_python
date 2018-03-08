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
def del_student(student_bd, i):
    del student_bd[i]
    return student_bd


# Функция поиска элементов базы по значениям определнных полей, возвращает словарь совпадений
def find(student_bd, field, key_word):
    field = field[0].upper() + field[1:].lower()
    key_word = key_word.upper()
    student = {}
    for i in bd:
        if bd[i].get(field).upper() == key_word:
            student[i] = bd[i]
    return student


# функция вывода базы
def print_bd(student_bd):
    for i in range(len(student_bd)):
        print('Student № {}: '.format(i + 1))
        for j in student_bd[i]:
            print('{0}: {1}'.format(j, student_bd[i][j]))
    print('-' * 20)


# основная программа
if __name__ == '__main__':
    bd = {0:{'Name':'Lara', 'Surname':'Scomor', 'Sex':'Female', 'Age':'22'}}
    while True:
        inp = input('Enter "add" - for add student\n"del" - for delete student\n"print" - for print group list'
                    '\n"find" - for find\n"q" - for exit program \n')
        if inp == 'q':
            break
        elif inp == 'add':
            number = int(input('Enter index number'))
            bd[number] = add_student()
        elif inp == 'del':
            bd = del_student(bd, int(input('input student number: ')))
        elif inp == 'find':
            f = input('Enter search fields Name/Surname/Sex/Age: ')
            search_word = input('Input word for search: ')
            bd_for_find = find(bd, f, search_word)
            print(*bd_for_find.items())
        elif inp == 'print':
            print_bd(bd)
