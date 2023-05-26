def zd1():
    class Restaurant:

        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'название ресторана:{self.restaurant_name}, кухня:{self.cuisine_type}итальянская')

        def open_restaurant(self):
            print("ресторан открыт!")

    one_Restaurant = Restaurant("Пряный щербет", " ")
    one_Restaurant.describe_restaurant()
    one_Restaurant.open_restaurant()


    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def icecream_menu(self):
            for flavor in self.flavors:
                flavor = ['шоколад', 'бабл-гам', 'ваниль']
                flavor.append(input('добавь вкусы: '))
                print('вкусы: ', flavor)

                n = input('что убрать из меню?: ')
                if n in flavor:
                    flavor.remove(n)
                    print('вкусы: ', flavor)

                a = input('введите сорт мороженого: ')
                if a in flavor:
                    print('такой сорт есть', flavor)
                else:
                    print('такого сорта нет, выберите из меню', flavor)


    class IceCreamSort(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type, flavors)

        def IceCreamVariant(self):

            k = input('какой тип мороженого?')
            if k == 'мягкое':
                print('вы выбрали мягкое мороженое')

            elif k == 'эскимо':
                print('вы выбрали эскимо')

            elif k == 'рожок':
                print('вы выбрали рожок')


    IceCreamStand.location = input('введите адрес: ')
    IceCreamStand.time = input('время работы: ')

    Ice_Cream_Stand = IceCreamStand('Пряный щербет', 'итальянская', [""])
    Ice_Cream_Stand.icecream_menu()

    Ice_Cream_Sort = IceCreamSort('Пряный щербет', 'итальянская', [""])
    Ice_Cream_Sort.IceCreamVariant()


from tkinter import *
def zd2():


    class Restaurant:

        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'название ресторана:{self.restaurant_name}, кухня:{self.cuisine_type}итальянская')

        def open_restaurant(self):
            print("ресторан открыт!")

    one_Restaurant = Restaurant("Пряный щербет", " ")
    one_Restaurant.describe_restaurant()
    one_Restaurant.open_restaurant()

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)

            flavor = ['шоколад', 'бабл-гам', 'ваниль']
            self.flavors = flavor

        def tk_ice(self):
            flavor = self.flavors
            print(flavor)
            w = Tk()
            w.geometry('200x200')
            w.title("Вкусы мороженого")
            for a in range(len(flavor)):
                ic = Label(w, text=flavor[a])
                ic.pack()
            w.mainloop()
            return ''

    Ice_Cream_Stand = IceCreamStand('Пряный щербет', 'итальянская', [""])
    Ice_Cream_Stand.tk_ice()


zd1()
zd2()