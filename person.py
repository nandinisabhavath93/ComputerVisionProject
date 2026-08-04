import cv2

# Load Haar Cascade
face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Read image
img = cv2.imread("images/person.jpg")

if img is None:
    print("Error: Could not open images/person.jpg")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

print("Faces detected:", len(faces))

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show image
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()