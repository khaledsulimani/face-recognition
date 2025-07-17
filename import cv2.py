import cv2

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Initialize video capture with better camera settings (optional)
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open video source")
    exit()

# Optionally, set camera resolution (width x height)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Read frame from camera
    ret, frame = video_capture.read()
    
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces with optimized parameters
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,       # Can adjust this value to improve detection accuracy
        minNeighbors=5,        # Can adjust this value to fine-tune face detection
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle for better visibility

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
video_capture.release()
cv2.destroyAllWindows()