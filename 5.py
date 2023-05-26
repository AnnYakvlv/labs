def zd1():
    import random

    s = [1, 2, 3, 4, 5]
    answer = int(input('введите число: '))
    if answer in s:
        print(s, answer, 'вы угадали число!')
    else:
        print(s, answer, 'нет такого числа')

def zd2():
    color = ['white', 'white', 'yellow', 'purple', 'blue']
    s = set([c for c in color if color.count(c) > 1])
    print(*(s if len(s) > 0 else ['Отсутствуют!']))



def zd3():
    week = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
    d = int(input('сколько выходных дней хотите?: '))
    week1 = week[-d:]
    week2 = week[:-d]
    print("ваши выходные дни: ", week1)
    print("ваши вабочие дни: ", week2)



def zd4():
    class1 = ["Иванов", "Сидоров", "Петров", "Швецова"]
    class2 = ["Капустин", "Иванчук", "Андреева", "Ульянова"]
    spot_group1 = tuple(random.sample(class1, 2) + random.sample(class2, 2))
    spot_group2 = tuple(random.sample(class1, 2) + random.sample(class2, 2))
    print(class1)
    print(class2)
    print(spot_group1, "длина команды=", len(spot_group1))
    print(spot_group2, "длина команды=", len(spot_group2))
    group1 = sorted(spot_group1)
    group2 = sorted(spot_group2)
    print(group1, group2)
    if 'Иванов' in (spot_group1 or spot_group2):
        print(spot_group1.count('Иванов')) or print(spot_group2.count('Иванов'))
    else:
        print('no')

zd1()
zd2()
zd3()
zd4()