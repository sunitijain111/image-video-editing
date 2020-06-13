
import cv2
import os
import numpy as np
path= os.getcwd()+ '/'+  'tempimage_folder'
#'tempimage_folder'
#'folder2'

# f= cv2.imread(path+'/'+'WhatsApp Image 2020-06-13 at 12.02.03 AM.jpeg', -1)
# if f is not None:
#     cv2.imshow('image',f)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows() 

files = list([os.path.join(path, f) for f in os.listdir(path)])

f= files[0]
image= cv2.imread(f).astype(np.float)
cnt=1
for temp in files[1:]:
    temp_img= cv2.imread(temp)
    image+=temp_img
    cnt+=1
    
image/=cnt
      
image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
cv2.imwrite('output.png', image)
cv2.imshow('after',cv2.imread('output.png'))
cv2.imshow('before',cv2.imread(files[0]))
cv2.waitKey(0)
cv2.destroyAllWindows()     