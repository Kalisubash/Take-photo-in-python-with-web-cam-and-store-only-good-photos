import cv2
import os

# Directory where photos will be saved
output_dir = r"C://Users//ransu//Documents//Python//outputphoto//subash"
os.makedirs(output_dir, exist_ok=True)

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the webcam
video_capture = cv2.VideoCapture(0)

# Counter to keep track of the number of photos taken
photo_count = 0

while photo_count < 20:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    if not ret:
        print("Failed to capture image")
        break
    
    # Convert frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # If faces are detected
    if len(faces) > 0:
        # Save the current frame as an image file
        photo_filename = os.path.join(output_dir, f"photo_{photo_count+1}.jpg")
        cv2.imwrite(photo_filename, frame)
        print(f"Saved: {photo_filename}")
        
        # Increment the photo counter
        photo_count += 1
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Webcam', frame)
    
    # Display the image until 'q' is pressed or a short delay
    if cv2.waitKey(500) & 0xFF == ord('q'):  # Wait for 500ms between captures
        break

# Release the capture and close the window
video_capture.release()
cv2.destroyAllWindows()

print(f"Finished capturing {photo_count} photos.")
