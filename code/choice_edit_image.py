import cv2
#vertical flip
import datetime
import os
import sys
cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 

def resize(img):
    #returns the face
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    face = cascade_face.detectMultiScale(grayscale, 1.3, 5)
    x_face, y_face, w_face, h_face= 0,0,0,0
    for (a,b,c,d) in face:
       x_face, y_face, w_face, h_face= a,b,c,d 
    if x_face==0 and  y_face==0 and w_face==0 and h_face  ==0:
        print(" no face detected ")
        return img
    
    #extending face dept
    y_face= max(0,y_face-20)
    h_face= min(y_face+h_face+20, img.shape[1])
    
    #extending face width
    x_face= max(0,x_face-20)
    w_face= min(x_face+w_face+20, img.shape[0]) 
    
    roi_face= img[y_face: y_face+ h_face, x_face: x_face+ w_face]
    
    #returning roi
    return roi_face

def flip(img):
    img = cv2.flip(img, 1) #flip horizontlally
    return img

def flip2(img):
    img = cv2.flip(img, 0) #flip vertically
    return img

def rotate(img):
    #rotate 90 degrees
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return img


def view(img):
    cv2.imshow('image press any key to close', img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
        
count=0
stack=[]
def ask_image(): 
    ##user interaction
    print("enter the image name: ")
    img_name= input()
    global count
    img = cv2.imread(img_name)
    if img is None:
        if count==20:
            print("maximum limit reached re-run program")
            sys.exit()
            
        print(" no such image exits\n press 1 to reenter name \n press any other key to exit")    
        x = input()
        if x=="1":
            count+=1          
            ask_image()
        else:
            sys.exit()
    else:
        stack.append(img)
        return [img, img_name]
        
def choice(img,img_name):
    print(" enter 1 to resize\n enter 2 to flip horizontally\n enter 3 to flip vertically\n enter 4 to rotate \n enter 5 to undo\n enter 6 to view image\n enter any other key to exit and save")
    x= input()
    if x=="1":
        curr= stack[-1]
        curr= resize(curr)
        stack.append(curr)
        view(curr)
        choice(img,img_name)
    elif x=="2":
        curr= stack[-1]
        curr= flip(curr)
        stack.append(curr)
        view(curr)
        choice(img,img_name)  
    elif x=="3":
        curr= stack[-1]
        curr=flip2(curr)
        stack.append(curr)
        view(curr)
        choice(img,img_name)
    elif x=="4":
        curr= stack[-1]
        curr= rotate(curr)
        stack.append(curr)
        view(curr)
        choice(img,img_name)    
    elif x=="5":
        if len(stack)== 1:
            print("invalid choice, you are at original image")
            choice(img,img_name)
        else:
            stack.pop()
            view(stack[-1])
            choice(img,img_name)
    elif x=="6"        :
        view(stack[-1])
        choice(img,img_name)
    else:
        cv2.imwrite("edited"+img_name,stack[-1])   
        print(" file saved ")
        sys.exit()
    
[img, img_name]= ask_image()    
choice(img, img_name)