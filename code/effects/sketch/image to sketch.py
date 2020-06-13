import cv2
import numpy as np

#images name :  pic.jpeg pic5.jpg
img= cv2.imread('pic.jpeg', -1)
# cv2.imshow('chris',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# cv2.imshow('chris',grayscale)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#inverting an image

#inverted= cv2.bitwise_not(grayscale)
inverted= 255-grayscale
# cv2.imshow('chris',inverted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


blurred= cv2.blur(inverted,(15,15)) 
# cv2.imshow('chris',blurred)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def dodge(front,back): 
    result=front*255/(255-back)  
    result[result>255]=255 
    result[back==255]=255 
    return result.astype('uint8')

blurred= blurred.astype('float')
grayscale= grayscale.astype('float')
final_img= dodge(blurred, grayscale)

cv2.imshow('chris',final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
