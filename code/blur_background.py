import cv2
import datetime
import os
#these are the cascades: thay are already present in the opencv
cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 

#function ot detect the face

# gray image of our face, original image:
def detection(grayscale, img):
    
         #1.3 is the scale factor , 5 is te min neighbours
        face = cascade_face.detectMultiScale(grayscale, 1.3, 5)
    
        #4 corrdinates in faces
        for (x_face, y_face, w_face, h_face) in face:
            #storing face
            roi_face= img[y_face: y_face+ h_face, x_face: x_face+ w_face]
            img = cv2.blur(img,(10,10))
            img[y_face: y_face+ h_face, x_face: x_face+ w_face]=roi_face

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