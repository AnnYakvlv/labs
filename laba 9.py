
from PIL import Image
import os
from pathlib import Path


def zd_1():

    f = os.listdir()
    Path("filter").mkdir(parents=True, exist_ok=True)
    print(f)
    for i in f:
        with Image.open(i) as img:
            img.load()
        im = img.convert('L')
        im.save(Path("filter", i))
    return ''


def zd_2():
    p = os.listdir()
    Path("filter").mkdir(parents=True, exist_ok=True)
    print(p)
    for i in p:
        if Path('filter').suffix == ('.jpg', '.png'):
            with Image.open(i) as img:
                img.load()
                im = img.convert('L')
                im.save(Path('filter', i))
    return ''



def zd_3():
    import csv
    with open('data.csv', 'r') as file:
        r = csv.reader(file, delimiter=',')
        s = 0
        for row in r:
            print(row[0] + ' -', row[1] + ' шт. за', row[2] + ' руб.')
            s = s + int(input())
    print('итоговая сумма: ', s)
    return ''


zd_1()
zd_2()
zd_3()
