# Face Recognition Project using OpenCV

---

🎯 *Project Overview*  
This project uses the OpenCV library to perform face recognition. The goal is to recognize and identify faces from images or video streams. The system is built to capture faces, process them, and provide real-time recognition.

---

## 🛠 *Technologies Used*  
- Python 3.x
- OpenCV
- Numpy
  
---

## 🚀 *Features*
- Real-time face detection using the webcam.
- Recognizes faces from a pre-trained dataset.
- Displays the name of the detected person (if available).

  ---
  
## 📝 *Installation*  
Follow these steps to run the project:

1. *Clone the repository*  
   ```bash
   git clone https://github.com/your-username/face-recognition.git
   ```
2. *Set up the environment If you’re using Anaconda, create a new environment:*
      ```bash
   conda create --name face_recognition_env python=3.13.5
      ```

3. *Activate the environment*
      ```bash
   conda activate face_recognition_env
      ```

4. *Install dependencies Install the required libraries using:*
      ```bash
   pip install -r requirements.txt
      ```

5. *Run the Project After installation, you can start the project by running:*
      ```bash
   python face_recognition.py 
      ```
      ---

# huskylens
# Face Recognition LED Trigger with HuskyLens and Arduino

This project uses the **HuskyLens AI camera** and an **Arduino UNO** to detect human faces. When a face is recognized, an LED connected to the Arduino is turned on.

---

## 📸 Features

- Face detection using HuskyLens
- LED activation on face recognition
- Real-time interaction via UART/I2C with Arduino
- Written in C++ (Arduino framework)

---

## 🧰 Hardware Required

- [HuskyLens AI Camera](https://www.dfrobot.com/product-1922.html)
- Arduino UNO (or compatible)
- LED (any color)
- 220Ω resistor
- Jumper wires
- Breadboard

---

## 🔌 Wiring

| Component     | Arduino UNO Pin |
|---------------|------------------|
| HuskyLens TX  | Pin 10 (SoftwareSerial RX) |
| HuskyLens RX  | Pin 11 (SoftwareSerial TX) |
| LED +         | Pin 7            |
| LED -         | GND (via 220Ω resistor) |

> Note: The camera should not be trained to recognize a face.

---

## 🧠 How It Works

1. The HuskyLens detects a pre-learned face.
2. It sends data to the Arduino via UART (SoftwareSerial).
3. Arduino checks if an ID is detected.
4. If a face is detected, the LED turns on; otherwise, it stays off.

---

## 🗂️ Files

- `HUSKYLENS_GET_STARED.ino` - Arduino sketch with the logic for HuskyLens face detection and LED control

---

## 📦 Libraries Used

- [HuskyLens Library](https://github.com/DFRobot/HUSKYLENSArduino)
- SoftwareSerial (built-in with Arduino)

---

## 🚀 Getting Started

1. Connect the components as shown above.
2. Upload the sketch to your Arduino board.
3. Observe the LED turning on when the face is detected.

---

## 📸 Project Results

Here are some real-world shots of the project in action:

📷 Photo 1 – ![صورة واتساب بتاريخ 1447-01-20 في 12 50 24_3da5c7d2](https://github.com/user-attachments/assets/f5212fba-0a70-496b-bbc2-3d1a74ed30f2)

📷 Photo 2 – ![صورة واتساب بتاريخ 1447-01-20 في 12 50 29_7efd30b6](https://github.com/user-attachments/assets/c55f78fd-2fe8-4368-a33d-45d42ed5877a)

---


## 🧑‍💻 Author

- **khaled mahmoud sulaimani** – [@khaledsulimani](https://github.com/khaledsulimani)
