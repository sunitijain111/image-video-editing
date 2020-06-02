# face-detection

#1 used the haar cascade the breif usage and summary is here: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html


#2. cascade files are already present "cv2.data.haarcascades " here.
   call lilke this: cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 
   
#3. cascade_face.detectMultiScale(grayscale, 1.3, 5) function:
   grasacle is te area fo intreset or where we are wokring
   othe two arre **scale factor and min neighbours**
    
   ##**scale facotor**
      The scaleFactor parameter determines a trade-off between detection accuracy and speed. The detection window starts out at size minSize, and after testing all windows of that size, the window is scaled up by scaleFactor and re-tested, and so on until the window reaches or exceeds maxSize. If scaleFactor is large (eg. 2.0), of course there will be fewer steps, so detection is faster, but you may miss objects whose size is in between two tested scales. But Haar-like features are inherently robust to some small variation in scale, so there's no need to make scaleFactor very small (eg. 1.001); that just wastes time with needless steps. That is why the default is 1.3 and not something smaller.
      
   ##**min neighbours**
     it tells how many nieghbours u need with the current neighbour to aprove it. example if min neighbour is 0 : a lot of false positives are detected but as we increase they will decrease since they false positives have no/ less eighbours.
    links: https://stackoverflow.com/questions/51132674/meaning-of-parameters-of-detectmultiscalea-b-c
    
