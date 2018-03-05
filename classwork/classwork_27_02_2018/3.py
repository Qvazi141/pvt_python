# Реализовать программу с базой учащихся группы. Записи по учащемуся: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.


def add_student():
    const_list = ['Name', 'Surname', 'Sex', 'Age']
    student = {}
    for i in const_list:
        student[i] = input('Input {} : '.format(i))
    return student


def del_student(student_bd, i):
    del student_bd[i]
    return student_bd


#def find(fild):
#    return student


def print_bd(student_bd):
    for i in range(len(student_bd)):
        print('Student № {}: '.format(i + 1))
        for j in student_bd[i]:
            print('{0}: {1}'.format(j, student_bd[i][j]))
    print('-' * 20)


if __name__ == '__main__':
    bd = {0:{'Name':'Lera', 'Surname':'Scomor', 'Sex':'Female', 'Age':'22'}}
    while True:
        inp = input('Enter "add" - for add student\n"del" - for delete student\n"print" - for print group list'
                    '\n"find" - for find\n"q" - for exit program \n')
        if inp == 'q':
            break
        elif inp == 'add':
            bd[len(bd)] = add_student()
        elif inp == 'del':
            bd = del_student(bd, int(input('input student number: ')))
        elif inp == 'find':
            f = input('Enter search fields Name/Surname/Sex/Age: ')
        elif inp == 'print':
            print_bd(bd)
