import cv2
cam  = cv2.VideoCapture(0)
while cam.isOpened():
    # detecting the camera
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    # converts the different colors above to grayscale below
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    # converts the gray to a blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # reducing noise in the video detection
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    #
    dilated = cv2.dilate(thresh, None, iterations=3)
    #
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    # detection of the right parts within the contour once detected
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue

        # detection of bigger things that move
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Orion Security Camera', frame1)