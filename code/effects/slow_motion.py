import time
import cv2 as cv
cap = cv.VideoCapture('output.avi')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    cv.imshow('frame', frame)
    time.sleep(0.2)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()