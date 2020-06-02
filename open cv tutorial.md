#### https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/ link

import cv2
#load the input image and show its dimensions, keeping in mind that
#images are represented as a multi-dimensional NumPy array with
#shape no. rows (height) x no. columns (width) x no. channels (depth)
**image = cv2.imread("jp.png")**
**(h, w, d) = image.shape**  #h= yaxis, w= x - axis, d= RBG= 3 , 3 color dept default
print("width={}, height={}, depth={}".format(w, h, d))
#display the image to our screen -- we will need to click the window
#open by OpenCV and press a key on our keyboard to continue execution
**cv2.imshow("Image", image)**
cv2.waitKey(0)
