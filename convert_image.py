from PIL import Image

# Open original image
img = Image.open("images/sample.jpg")

# Convert and save as real JPG
img.convert("RGB").save("images/sample_fixed.jpg")

print("Image converted successfully")