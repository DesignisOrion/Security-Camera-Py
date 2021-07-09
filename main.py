import cv2

# read the camera
# 0 - default cam, 1 - multiple cam
cam  = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    # destroy the window using the "q" key
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Home Security Camera', frame)
    
    