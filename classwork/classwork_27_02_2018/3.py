# Реализовать программу с базой учащихся группы. Записи по учащемуся: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.
const_list = ['Name', 'Surname', 'Sex', 'Age']


def add():
    student = {}
    for i in const_list:
        student[i] = input('Input {} : '.format(i))
    return student


def find(fild):
    return student


def print_bd(student_bd):
    for i in range(len(student_bd)):
        print('Student № {}: '.format(i + 1))
        for j in student_bd[i]:
            print('{0}: {1}'.format(j, student_bd[i][j]))
    print('-' * 20)


if __name__ == '__main__':
    bd = {0:{'Name':'Lera', 'Surname':'Scomor', 'Sex':'Female', 'Age':'22'}}
    while True:
        inp = input('Enter "add" - for add student\n"print" - for print group list\n"find" - for find\n'
                    '"q" - for exit program \n')
        if inp == 'q':
            break
        elif inp == 'add':
            bd[len(bd)] = add()
        elif inp == 'find':
            f = input('Enter search fields Name/Surname/Sex/Age: ')

        elif inp == 'print':
            print_bd(bd)
