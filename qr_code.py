# Import libraries
import os
import qrcode

# Make QR code image
image = qrcode.make("https://facebook.com/clb.it.ngoctao")

# Save QR code image
image.save("qrcode.png", "PNG")

# Open the image
os.system("open qrcode.png")