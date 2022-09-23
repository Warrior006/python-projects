import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# coding
data = 'https://www.google.com/'

img = qrcode.make(data)

img.save('/Users/admin/Desktop/test/myqrcode.png')    # you can add your own path file

# decoding
img = Image.open('/Users/admin/Desktop/test/myqrcode.png')

result = decode(img)

print(result)
