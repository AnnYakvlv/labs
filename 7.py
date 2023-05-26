# zd1
from PIL import Image, ImageFilter

filename = "turtle.jpg"
with Image.open(filename) as img:
    img.load()

img.show()
width, height = img.size
format = img.format
mode = img.mode

print('ширина: ', width)
print('высота: ', height)
print('формат: ', format)
print('модель: ', mode)


# zd2
new_img = img.resize((img.width // 3, img.height // 3))
new_img.save('turtle_resize.jpg')

conv_img = img.transpose(Image.FLIP_TOP_BOTTOM)
conv_img.save('flipTOP_turtle.jpg')
conv_img = img.transpose(Image.FLIP_LEFT_RIGHT)
conv_img.save('flipLEFT_turtle.jpg')


# zd3
filename2 = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
for file in filename2:
    with Image.open(file) as img:
        img.load()
    new_img2 = img.filter(ImageFilter.SHARPEN)
    new_img2.save('new_' + file)


#zd4
wtmr = 'watermark.png'
with Image.open(wtmr) as img_water:
    img_water.load()

img_water = Image.open(wtmr)
img_water = img_water.resize((img_water.width // 7, img_water.height // 7))

filename3 = 'turtle.jpg'
with Image.open(filename3) as img:
    img.load()

img.paste(img_water, (160, 170), img_water)
img.save('turt_wat.png')
