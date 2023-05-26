def zd1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"1)Название ресторана {self.restaurant_name}, Кухня:{self.cuisine_type}Индийская" )

        def open_restaurant(self):
            print("Ресторант открыт")

    one_Restaurant = Restaurant("Пряный щербет", " ")
    # print(one_Restaurant.restaurant_name)
    # print(one_Restaurant.cuisine_type)

    one_Restaurant.describe_restaurant()
    one_Restaurant.open_restaurant()


def zd2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"2)Название ресторана {self.restaurant_name}, Кухня:{self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторант открыт")



    one_Restaurant = Restaurant("Пряный щербет", "индийская ")
    two_Restaurant = Restaurant("Матрешка", "русская ")
    tree_Restaurant = Restaurant("Казан", "казахская ")

    one_Restaurant.describe_restaurant()
    one_Restaurant.open_restaurant()

    two_Restaurant.describe_restaurant()
    two_Restaurant.open_restaurant()

    tree_Restaurant.describe_restaurant()
    tree_Restaurant.open_restaurant()
    # two_Restaurant.describe_restaurant()
    # two_Restaurant.open_restaurant()

    # tree_Restaurant.describe_restaurant()
    # tree_Restaurant.open_restaurant()

def zd3():
    class Restaurant:

        rating = 2
        print('3)изначальный рейтинг:', rating)
        def __init__(self, restaurant_name, cuisine_type, restaurant_rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.restaurant_rating = restaurant_rating

        def update_rating(self, rating):
            self.restaurant_rating = rating

        def describe_restaurant(self):
            print(f"3)Название ресторана {self.restaurant_name}, Кухня:{self.cuisine_type}Индийская,"
                  f"Рейтинг:{self.restaurant_rating}")

        def open_restaurant(self):
            print("Ресторант открыт")


    one_Restaurant = Restaurant("Пряный щербет", " ", " ")

    one_Restaurant.update_rating(4)
    one_Restaurant.describe_restaurant()
    one_Restaurant.open_restaurant()

zd1()
zd2()
zd3()