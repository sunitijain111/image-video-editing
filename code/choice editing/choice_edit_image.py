import cv2
import sys
cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 

def resize(img):
    x,y,w,d= map(int, input("enter the x-y coordinates , width ad height\n").split())
    
    if y+d>img.shape[0]:
         d= img.shape[0]-y
         
    if x+ w>img.shape[1]    :
        w= img.shape[1]-x
        
    roi_face= img[y :y+ d, x: x+ w]
    return roi_face

def flip(img):
    img = cv2.flip(img, 1) #flip horizontally
    return img

def flip2(img):
    img = cv2.flip(img, 0) #flip vertically
    return img
	
def flip3(img):
    img = cv2.flip(img, -1) #flip on both axes
    return img

def rotate(img):
    #rotate 90 degrees
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return img

c=0
def view(img):
    cv2.imshow('image press any key to close', img)
    global c
    cv2.imwrite("edited"+str(c)+img_name,stack[-1])
    c+=1
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
    print(" enter 1 to resize\n enter 2 to flip horizontally\n enter 3 to flip vertically\n enter 4 to flip on both axes \n enter 5 to rotate \n enter 6 to undo\n enter 7 to view image\n enter any other key to exit and save")
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
        curr=flip3(curr)
        stack.append(curr)
        view(curr)
        choice(img,img_name)
    elif x=="5":
        curr= stack[-1]
        curr= rotate(curr)
        stack.append(curr)
        view(curr)
        choice(img,img_name)    
    elif x=="6":
        if len(stack)== 1:
            print("invalid choice, you are at original image")
            choice(img,img_name)
        else:
            stack.pop()
            view(stack[-1])
            choice(img,img_name)
    elif x=="7"        :
        view(stack[-1])
        choice(img,img_name)
    else:
        cv2.imwrite("edited"+img_name,stack[-1])   
        print(" file saved ")
        sys.exit()
    
[img, img_name]= ask_image()    
choice(img, img_name)