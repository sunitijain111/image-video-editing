import cv2
import datetime
import os
import numpy as np
#these are the cascades: thay are already present in the opencv
cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 

#function ot detect the face

# gray image of our face, original image:
def detection(grayscale, img):
    
    #1.3 is the scale factor , 5 is te min neighbours
    face = cascade_face.detectMultiScale(grayscale, 1.3, 5)
    
    #4 corrdinates in faces
    for (x_face, y_face, w_face, h_face) in face:
        
        #draw rectangle
        #cv2.rectangle(img, (x_face, y_face), (x_face+w_face, y_face+h_face), (255, 130, 0), 2)
        
        img_wig= cv2.imread('wig.png',-1)
        #cv2.imshow('image', img_tongue) 
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        # break 
       
        frame= img_wig
        w,h,temp= frame.shape
        for x in range(w):
            for y in range(h):
                try:  
                    a,b,c= frame[x,y]
                    if a>=200 and b>= 200 and c>=200:
                        frame[x,y]=[0,0,0]
                        #print(a,b,c)
                except IndexError:
                   #print('naa')
                   continue
        
        img_wig= frame
        
        ## adjusing the width & dept
        width, depth, _= img_wig.shape
        expected_width= w_face+ w_face/5
        ratio= expected_width/width
        width= int(ratio* width)
        depth= int(ratio* depth)
        img_wig= cv2.resize(img_wig, (width, depth))
        width, depth, _= img_wig.shape
        expected_width= w_face+ w_face/5
        ratio= expected_width/width
        #print(ratio)
        width= int(ratio* width)
        depth= int(ratio* depth)
        img_wig= cv2.resize(img_wig, (width, depth))
        
        ## coordinstes
        centre_x= x_face+ w_face/2
        x_wig= int(centre_x-width/2)
        unit_y= depth/6
        y_wig= int(y_face- unit_y)
        
        ##indexing 
        
        if x_wig<0:
            x_width= centre_x
            width= centre_x
            img_wig= cv2.resize(img_wig, (x_width, depth))
        if y_wig<0    :
            y_dept= int(y_face*5/2)
            depth= y_dept
            img_wig= cv2.resize(img_wig,(img_wig.shape[0], depth))
        y2=int(y_wig+depth)
        if(y2>= img.shape[1]):
            y2= img.shape[1]
        x2= int(x_wig+width)
        if(x2>= img.shape[0]):
            x2= img.shape[0]
            
        ##rois
        roi_wig= img[y_wig: y2, x_wig: x2]
        img_wig= img_wig[0: y2-y_wig, 0:x2-x_wig]    
        
        ##adding
        img= temp
        try:
            dst = cv2.addWeighted(roi_wig, 0.8, img_wig, 0.8, 0)
            img[y_wig: y2, x_wig: x2]= dst
        except:
            print("error")
        # cv2.imshow('image2',img )
        # cv2.waitKey(0) 
        # cv2.destroyAllWindows()

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