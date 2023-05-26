def div_3(number: int):
    return True if number % 3 == 0 else False


def div_100(number):
    result = None
    try:
        result = 100 /float(number)
    except ValueError:
        print('нужно написать число!')
    except ZeroDivisionError:
        print('ошибка деления на ноль!')
    except Exception as a:
        print('ошибка: ', a)
    return result


def magic_date(date):
    try:
        date = date.split('.')
        if int(date[0]) * int(date[1]) == int(date[2]) % 100:
            return True
        else:
            return False
    except:
        print("string in format dd.mm.yyyy")


def lu_un_ticket(ticket: str):
    sum1 = sum([int(i) for i in ticket[:int(len(ticket) / 2)]])
    sum2 = sum([int(i) for i in ticket[int(len(ticket) / 2):]])
    if sum1 == sum2:
        return True
    else:
        return False


if __name__ == "__main__":

    print('\nДеление на 3')
    print(div_3(21))
    print(div_3(412))

    print('\nДеление на 100')
    print(div_100(200))
    print(div_100(0))
    print(div_100("ahnirh"))

    print('\nМагическая дата')
    print(magic_date("22.01.2022"))
    print(magic_date("24.01.2042"))

    print('\nБилетик')
    print(lu_un_ticket("385916"))
    print(lu_un_ticket("231002"))