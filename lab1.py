# zd2
p = int(input('введите место в плацкартном вагоне: '))
if p % 2 == 0 and p <= 35:
    print("ваше место - в купе наверху")
elif p % 2 != 0 and p <= 35:
    print("ваше место - в купе внизу")
elif p % 2 != 0 and p > 36:
    print("ваше место - боковое внизу")
else:
    print("ваше место - боковое сверху")


# zd3
year = int(input('введите год: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "год - високосный")
else:
    print(year, "год - не високосный")

# zd4
colors = ('красный', 'синий', 'желтый')
col1 = input('цвет 1:')
col2 = input('цвет 2:')
if col1 in colors and col2 in colors:
    if col1 != col2:
        if (col1 in ('красный', 'синий')) and (col2 in ('красный', 'синий')):
            print('фиолетовый')
        if (col1 in ('синий', 'желтый')) and (col2 in ('синий', 'желтый')):
            print('зеленый')
        if (col1 in ('красный', 'желтый')) and (col2 in ('красный', 'желтый')):
            print('оранжевый')
else:
    print('ошибка цветов')


# zd5
N = int(input('введите количество слов: '))
simv = []
for i in range(N):
    simv.append(input())

word = ' '.join(simv)
print(word)


# zd1
def rew_pass(password):
    raw_number = raw_len = raw_up = raw_low = False
    if len(password) > 6:
        raw_len = True
    for symbol in password:
        if symbol.isupper():
            raw_up = True
        elif symbol.islower():
            raw_low = True
        elif symbol.isdigit():
            raw_number = True
    if raw_up and raw_low and raw_len and raw_number:
        return True
    return False


def main():
    password = input('введите пароль: ')
    if rew_pass(password):
        print('паролб надежный')
    else:
        print('пароль ненадежный')

pass


main()
