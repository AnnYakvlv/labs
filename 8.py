def zd1()
    from PIL import Image, ImageDraw, ImageFont
    filename = "ng.jpg"
    with Image.open(filename) as img:
        img.load()

    cropped_img = img.crop((200, 1300, 1000, 1780))
    cropped_img.save("cropp_ng.jpg")


def zd2()
    day = {1: "ng.jpg", 2: "dr.jpg", 3: "ms.jpg", 4: "ps.jpg"}
    print("1: ng.jpg", "2: dr.jpg", "3: ms.jpg", "4: ps.jpg")

    qw = int(input('введите номер открытки: '))
    filename2 = day[qw]
    with Image.open(filename2) as img:
        img.load()
    img.show()


def zd3()
    image = Image.open("dr.jpg")

    name = 'Congratilous, Kate!!!!'
    drawer = ImageDraw.Draw(image)
    drawer.text((400, 150), name, fill='black')

    image.save('new_dr.png')
    image.show()


zd1()
zd2()
zd3()

