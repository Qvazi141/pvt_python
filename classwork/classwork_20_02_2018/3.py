# Полученный список из задачи 2 вывести столбиком в отсортированном порядке.
s1 = 'Hello!Anthony!Have!A!Good!Day!'
s1 = s1.split('!')
if s1[-1] == '':
    s1 = s1[:-1]
s1.sort()
for i in s1:
    print(i)
