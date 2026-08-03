import cv2

image = cv2.imread("images/sample_converted.jpg")

if image is None:
    print("Image not found!")
    exit()

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()