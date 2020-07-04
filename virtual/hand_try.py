import cv2
import datetime
import os
import numpy as np


# face_cascade_name= '/palm.xml'
# face_cascade = cv2.CascadeClassifier()
# if not face_cascade.load(face_cascade_name):
#     print('--(!)Error loading face cascade')
    

#cascade_hand = cv2.CascadeClassifier("/media/suniti/Windows\ S/ml/data-stats/use\ case\ 3/palm.xml") 

#for fist use hand.xml

hand_cascade = cv2.CascadeClassifier('palm.xml')

hand= cv2.imread("hand2.jpg", -1)   
# cv2.imshow("hand", hand)
# cv2.waitKey(0) 
# cv2.destroyAllWindows() 

gray= cv2.cvtColor(hand, cv2.COLOR_BGR2GRAY) 
# cv2.imshow("hand", gray)
# cv2.waitKey(0) 
# cv2.destroyAllWindows() 

detected= hand_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in detected: 
      cv2.rectangle(hand, (x, y), (x + w, y + h), (0, 255, 0), 2) 
      cv2.imshow("hand", hand)
      cv2.waitKey(0) 
      cv2.destroyAllWindows()
 