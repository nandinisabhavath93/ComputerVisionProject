from PIL import Image
import pillow_avif

img = Image.open("images/sample.jpg")

img.convert("RGB").save("images/sample_converted.jpg")

print("Conversion completed")