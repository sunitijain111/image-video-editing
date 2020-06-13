import cv2
import datetime
import os
import numpy as np
#these are the cascades: thay are already present in the opencv
cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 
cascade_smile = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')

#function ot detect the face

# gray image of our face, original image:
def detection(grayscale, img):
    
    #1.3 is the scale factor , 5 is te min neighbours
    face = cascade_face.detectMultiScale(grayscale, 1.3, 5)
    
    #4 corrdinates in faces
    for (x_face, y_face, w_face, h_face) in face:
        
        #draw rectangle
        #cv2.rectangle(img, (x_face, y_face), (x_face+w_face, y_face+h_face), (255, 130, 0), 2)
       
        # ears
        ear_width= w_face
        img_ear= cv2.imread('bunny2.png',-1)
        # cv2.imshow('image', img_ear)
        # cv2.waitKey(0) 
        # cv2.destroyAllWindows()
       
        h,w,c= img_ear.shape
        ratio= ear_width/w
        w= int(w*ratio)
        d= int(h*ratio)
        img_ear= cv2.resize(img_ear, (w,d))

                
        roi_ear= img[y_face-d: y_face,x_face:x_face+w]
           
        min_d= min(roi_ear.shape[0], img_ear.shape[0])
        min_w= min(roi_ear.shape[1], img_ear.shape[1])
        roi_ear= img[y_face-min_d: y_face,x_face:x_face+min_w]
        img_ear= img_ear[0: min_d,0: min_w]
            
        # print(roi_ear.shape)
        # print(img_ear.shape)
        
        
        bg = img[y_face-min_d: y_face,x_face:x_face+min_w]
        sg = np.atleast_3d(255 - img_ear[:, :, 3])/255.0
        np.multiply(bg, sg, out=bg, casting="unsafe")
        np.add(bg, 255-img_ear[:, :, 0:3] * np.atleast_3d(img_ear[:, :, 3]), out=bg)
        # put the changed image back into the scene
        img[y_face-min_d: y_face,x_face:x_face+min_w] = bg    
        
       
    #return image        
    return img 





vc = cv2.VideoCapture(0) 
#path
path= os.getcwd()

# Create directory
dirName = 'tempimage_folder'
try:
        os.mkdir(dirName)
except FileExistsError:
        print("Directory " , dirName ,  " already exists")
path= path+'/'+dirName
cnt=0
while cnt<500:
    #read status of camera and frame
    _, img = vc.read() 
    
    #convert image ot grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    #reuslt from detection function
    final = detection(grayscale, img) 
    
    #showing captured image
    cv2.imshow('Video', final) 
    
    #name of our image, wiht current time , so that it has new name each time.
    string = "pic"+str(datetime.datetime.now())+".jpg"
    
    
    #save image
    cv2.imwrite(os.path.join(path, string),final)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
    
    cnt+=1

vc.release() 
cv2.destroyAllWindows() 
