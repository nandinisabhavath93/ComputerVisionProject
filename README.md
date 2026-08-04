# Computer Vision Project using OpenCV

## 📌 Project Overview

This project demonstrates different **Computer Vision techniques** using **Python and OpenCV**.

The project includes image processing applications such as:

* Face Detection
* Edge Detection
* Person Edge Detection
* QR Code Detection
* Image Format Conversion

These implementations help understand basic computer vision concepts and OpenCV operations.

---

# 🚀 Technologies Used

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| Python       | Programming Language    |
| OpenCV       | Computer Vision Library |
| Pillow (PIL) | Image Processing        |
| NumPy        | Numerical Operations    |

---

# 📂 Project Structure

```
ComputerVisionProject
│
├── main.py
├── person.py
├── edge.py
├── edge_person.py
├── create_qr.py
├── convert_image.py
├── convert_person.py
├── requirements.txt
├── README.md
│
├── images
│   ├── person.jpg
│   ├── person_fixed.jpg
│   ├── qr.png
│   └── sample_fixed.jpg
│
└── venv
```

---

# ✨ Features

## 1. Face Detection

### File:

```
person.py
```

### Description:

* Detects human faces from an input image.
* Uses Haar Cascade Classifier.
* Draws a rectangle around detected faces.

### Run:

```bash
python person.py
```

### Output:

* Original image
* Face detected with a green bounding box

---

## 2. Edge Detection

### File:

```
edge.py
```

### Description:

* Converts an image into grayscale.
* Applies Canny Edge Detection algorithm.
* Detects boundaries and edges of objects.

### Run:

```bash
python edge.py
```

### Output:

* Original image
* Edge detected image

---

## 3. Person Edge Detection

### File:

```
edge_person.py
```

### Description:

* Performs edge detection on a person's image.
* Highlights body and object boundaries.

### Run:

```bash
python edge_person.py
```

### Output:

* Person image
* Edge detection result

---

## 4. QR Code Detection

### File:

```
create_qr.py
```

### Description:

* Creates and detects QR codes using OpenCV.
* Reads QR code information.

### Run:

```bash
python create_qr.py
```

### Output:

* Generated QR code
* Decoded QR information

---

## 5. Image Conversion

### Files:

```
convert_image.py
convert_person.py
```

### Description:

* Converts unsupported image formats into JPG format.
* Helps OpenCV read images correctly.

---

# ⚙️ Installation Guide

## Step 1: Clone Repository

```bash
git clone https://github.com/nandinisabhavath93/ComputerVisionProject.git
```

Go into project folder:

```bash
cd ComputerVisionProject
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 3: Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

---

## Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

```
opencv-contrib-python
pillow
```

---

# ▶️ How to Run

### Face Detection

```bash
python person.py
```

### Edge Detection

```bash
python edge.py
```

### Person Edge Detection

```bash
python edge_person.py
```

### QR Code Detection

```bash
python create_qr.py
```

---

# 🔮 Future Enhancements

* Real-time face detection using webcam
* Object detection using YOLO
* Deep Learning based image classification
* Real-time video processing
* Multiple object tracking
* AI-based image analysis

---

# 👩‍💻 Author

**Nandini Sabhavath**

---

# 📜 License

This project is created for educational and learning purposes.
