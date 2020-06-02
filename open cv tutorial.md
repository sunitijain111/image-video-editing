#### https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/ link

import cv2 </br>
#load the input image and show its dimensions, keeping in mind that</br>
#images are represented as a multi-dimensional NumPy array with</br>
#shape no. rows (height) x no. columns (width) x no. channels (depth)</br>
**image = cv2.imread("jp.png")** </br>
**(h, w, d) = image.shape**  #h= yaxis, w= x - axis, d= RBG= 3 , 3 color dept default </br>
print("width={}, height={}, depth={}".format(w, h, d)) </br>
#display the image to our screen -- we will need to click the window </br>
#open by OpenCV and press a key on our keyboard to continue execution </br>
**cv2.imshow("Image", image)** </br>
cv2.waitKey(0) </br>
