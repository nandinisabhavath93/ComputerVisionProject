from PIL import Image
import os

input_file = "images/person.jpg"
output_file = "images/person_fixed.jpg"

# Check input file
if not os.path.exists(input_file):
    print("person.jpg not found!")
    exit()

try:
    img = Image.open(input_file)

    print("Original format:", img.format)

    img.convert("RGB").save(output_file, "JPEG")

    print("person_fixed.jpg created successfully")

except Exception as e:
    print("Error:", e)