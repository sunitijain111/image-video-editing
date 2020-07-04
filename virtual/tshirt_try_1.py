import cv2
import datetime
import os
import numpy as np
import time
#these are the cascades: thay are already present in the opencv
cascade_upper_body = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_upperbody.xml') 
#cascade_lower_body = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_lowerbody.xml') 

#function ot detect the face

# gray image of our face, original image:
def detection(grayscale, img):
    
    arrUpperBody = cascade_upper_body.detectMultiScale( grayscale, scaleFactor = 1.3, minNeighbors = 5, minSize = (50, 100),flags = cv2.CASCADE_SCALE_IMAGE   )
    y1,y2,x1,x2=0,0,0,0
    for (x,y,w,h) in arrUpperBody:
        # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # cv2.imshow("tshirt preview",img)
        # cv2.waitKey(0) 
        # cv2.destroyAllWindows() 
        y1= int(y+(3/5)*h) #taking last 2/5th part
        # cv2.rectangle(img,(x,y1),(x+w,y+h),(255,0,0),2)
        # cv2.imshow("tshirt preview",img)
        # cv2.waitKey(0) 
        # cv2.destroyAllWindows() 
        
        y2= (h-y1)*3
        y2= int(y1+y2)
        x1=int( x+w/12)
        x2= int(x+w - w/12)
        cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
        # cv2.imshow("tshirt preview",img)
        # cv2.waitKey(0) 
        # cv2.destroyAllWindows()
        
        #transparet tshirt else tshirt2
        tshirt= cv2.imread("tshirt0.png", -1)        
        #cv2.imshow("tshirt preview",img)
        if x2-x1>0 and y2-y1>0:
            # print("insider")	
            if(y2>img.shape[0]):
                y2= img.shape[0]
            if(x2> img.shape[1])    :
                x2= img.shape[1]
                
            tshirt= cv2.resize(tshirt, (x2-x1,y2-y1))
            frame= img[y1:y2, x1:x2]             
            for x in range(tshirt.shape[0]):
                 for y  in range(tshirt.shape[1]):
                     a,b,c=tshirt[x,y]
                     if not(a>=200 and b>=200 and c>=200):
                        frame[x,y]   = a,b,c
                        
            img[y1:y2, x1:x2]= frame   
            # cv2.imshow("tshirt preview",img)
            # cv2.waitKey(0) 
            # cv2.destroyAllWindows()        
           
        #return [img,1]
    return [img,0]
    
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
while cnt<5000:
    #read status of camera and frame
    _, img = vc.read() 
    
    #convert image ot grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    #reuslt from detection function
    final,ans = detection(grayscale, img) 
    
    if final is not None:
        if ans:
            cv2.imshow('tshirt preview', final)
        else:
            cv2.imshow('tshirt preview', final) 
             
    
    #name of our image, wiht current time , so that it has new name each time.
    string = "pic"+str(datetime.datetime.now())+".jpg"
    
    
    #save image
    cv2.imwrite(os.path.join(path, string),final)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
    
    cnt+=1
        
vc.release()
cv2.destroyAllWindows() 


# img= cv2.imread("person3.jpg", -1)   
   
# grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# detection(grayscale, img)
# cv2.destroyAllWindows() 
