def zd1():
    words = []
    while (word := str(input())) != "stop":
        words.append(word)
    print(' '.join(words))


def zd2():
    words = []
    while (word := str(input())) != "stop":
        if 'ф' in word or 'Ф' in word:
            print('Ого! Это редкое слово!')
        else:
            print('Эх, это не очень редкое слово...')


def zd3():
    import random
    count = 0
    p = 0
    while p != 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = int(input(f'сколько будет, {a} + {b}'))
        if c == a+b:
            print("ответ правильный")
            count += 1
        else:
            print('ответ неверный!')
            p +=1
    print("игра окончена", '\n Правильных ответов: ', count)




zd1()
zd2()
zd3()
