# Import libraries
from PIL import Image, ImageFilter

# Image before filter
original = Image.open("algo_team.png")

# Image after filter
blur = original.filter(ImageFilter.BoxBlur(20))
black_and_white = original.convert("L")

# Show filtered images
black_and_white.show()
blur.show()