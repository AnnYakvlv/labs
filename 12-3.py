from tkinter import *


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
        # print(flavor)
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

