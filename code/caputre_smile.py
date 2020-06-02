
import cv2
import datetime
import os

#these are the cascades: thay are already present in the opencv
cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 
cascade_eye = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml') 
cascade_smile = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')

#function ot detect teh face

# gray image of our face, original image:
def detection(grayscale, img):
    
    #1.3 is the scale factor , 5 is te min neighbours
    face = cascade_face.detectMultiScale(grayscale, 1.3, 5)
    
    #4 corrdinates in faces
    for (x_face, y_face, w_face, h_face) in face:
        
        #draw rectangle
        cv2.rectangle(img, (x_face, y_face), (x_face+w_face, y_face+h_face), (255, 130, 0), 2)
        
        #area of intreset in gray image
        ri_grayscale = grayscale[y_face:y_face+h_face, x_face:x_face+w_face]
        
        #area of intrest in cooloured image
        ri_color = img[y_face:y_face+h_face, x_face:x_face+w_face] 
        
        # smile detection , 1.7 is the scale factor , 20 is the min neighbour
        smile = cascade_smile.detectMultiScale(ri_grayscale, 1.7, 30)
        
        #draw rectangle on smile
        for (x_smile, y_smile, w_smile, h_smile) in smile: 
            cv2.rectangle(ri_color,(x_smile, y_smile),(x_smile+w_smile, y_smile+h_smile), (255, 0, 130), 2)
    
    #return image        
    return img 

vc = cv2.VideoCapture(0) 

while True:
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
    
    #path
    path= "/media/suniti/Windows S/ml/face/data-stats/folder"
    
    #save image
    cv2.imwrite(os.path.join(path, string),final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

vc.release() 
cv2.destroyAllWindows() 
