import cv2

# Read person image
img = cv2.imread("images/person.jpg")

# Check image
if img is None:
    print("Person image not found!")
    exit()

print("Person image loaded successfully")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 100, 200)

# Show original image
cv2.imshow("Person Original Image", img)

# Show edge detection result
cv2.imshow("Person Edge Detection", edges)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()