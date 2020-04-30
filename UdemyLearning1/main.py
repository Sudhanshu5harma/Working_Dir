import requests
from io import BytesIO
from PIL import Image



r = requests.get("https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_1280.jpg")
print("status: ", r.status_code)

image = Image.open(BytesIO(r.content))



print(image.size, image.format, image.mode)
path = "./image."+image.format

try:
    image.save(path,image.format)
except IOError:
    print("can't save the image")