def zd1_2():
    import json
    print('Добавьте новый товар')
    name = input('Введите название:')
    price = int(input('Введите цену:'))
    weight = int(input('Введите вес:'))
    available = input('Укажите наличие (true/false):')
    available_1: bool
    if available == 'true':
        available_1 = True
    elif available == 'false':
        available_1 = False
    else:
        print('Неверное значение наличия')
    new_data = {
        'название': name,
        'цена': price,
        'наличие': available_1,
        'вес': weight
    }
    with open('C:\\Users\\Acer\\PycharmProjects\\pythonProject\\file2.json', encoding='utf-8') as a:
        data = json.load(a)
        data['products'].append(new_data)
        with open('C:\\Users\\Acer\\PycharmProjects\\pythonProject\\file2.json', 'w', encoding='utf-8') as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
    with open('C:\\Users\\Acer\\PycharmProjects\\pythonProject\\file2.json', 'r', encoding='utf-8') as f:
        mas = json.load(f)
        for p in mas['products']:
            print('Название: ' + str(p["name"]))
            print('Цена: ' + str(p["price"]))
            print('Вес: ' + str(p["weight"]))
            if p['available']:
                print('В наличии')
            else:
                print('Нет в наличии!')
            print('')
    s = input()

def zd3():
    sl = {}
    with open("en-ru.txt", "r", encoding="utf-8") as file:
        while True:
            n = file.readline()
            n = n.rstrip()
            if not n:
                break
            n = n.split("-")
            c = n[len(n)-1].split(",")
            for i in range(len(c)):
                c[i] = c[i].lstrip()
                sl[c[i]] = n[0]
    sl = dict(sorted(sl.items()))
    print(sl)
    f = open('ru-en.txt', 'wt')
    f.write(str(sl))
    f.close()


zd3()