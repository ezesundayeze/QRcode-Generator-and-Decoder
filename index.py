# Import QR Code library
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Create qr code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# The data that you want to store
data = "hgMy name is Eze Sunday Eze"

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save("image.jpg")

# reading qrcode
dcode = decode(Image.open('image.jpg'))
d = str(dcode[0][0])
lent = len(d)
print((d)[2:lent-1])
