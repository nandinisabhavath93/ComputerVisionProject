import cv2
import os

# Image path
image_path = "images/sample_fixed.jpg"

# Check image path
if not os.path.exists(image_path):
    print("Image file not found:", image_path)
    exit()

# Read image
img = cv2.imread(image_path)

# Check image loading
if img is None:
    print("Unable to read image")
    exit()

print("Image loaded successfully")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection using Canny
edges = cv2.Canny(gray, 100, 200)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Edge Detection", edges)

# Wait for key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()