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


#### open cv follows BGR or RGB , acces by pixel
#access the RGB pixel located at x=50, y=100, keepind in mind that  </br>
#OpenCV stores images in BGR order rather than RGB  </br>
**(B, G, R) = image[100, 50]** </br>
print("R={}, G={}, B={}".format(R, G, B))  </br>

#### slicing and cropping
“regions of interest” (ROIs) 

#extract a 100x100 pixel square ROI (Region of Interest) from the
#input image starting at x=320,y=60 at ending at x=420,y=160
**roi = image[60:160, 320:420]** </br>
cv2.imshow("ROI", roi) </br>
cv2.waitKey(0) </br>

**read the tutorial for drawing /putting text**

### alpha beta blenging
https://note.nkmk.me/en/python-opencv-numpy-alpha-blend-mask/#:~:text=Masking%20with%20OpenCV%3A%20cv2.,-bitwise_and()&text=cv2.,a%20mask%20image%20for%20src2%20.

**dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)** 
add two images

bitwise and tow images black remains black
**dst = cv2.bitwise_and(src1, src2)**

### resizing
https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
img= cv.resize(src, dimensions in tupple)
width = 350
height = 450
dim = (width, height)
 
#resize image
**resized = cv2.resize(img, dim)**

#### resize on e image into size of other

src1 = cv2.imread('data/src/lena.jpg')
src2 = cv2.imread('data/src/rocket.jpg')
**src2 = cv2.resize(src2, src1.shape[1::-1])**
