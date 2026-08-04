import qrcode
import os

# Text or URL to store in the QR code
data = "https://www.google.com"

# Create QR code
img = qrcode.make(data)

# Create the images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Save the QR code
img.save("images/qr.png")

print("QR code created successfully!")
print("Saved as images/qr.png")