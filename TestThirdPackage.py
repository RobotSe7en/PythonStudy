from PIL import Image
image = Image.open('Test.jpg')
print(image.format,image.size,image.mode)
image.thumbnail((200,100))
image.save('thumb.jpg','JPEG')