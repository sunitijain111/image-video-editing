#it captures 50 images
import cv2
import os

cnt= 0
vc = cv2.VideoCapture(0)

path= os.getcwd()
dirName = 'tempimage_folder'
try:
    os.mkdir(dirName)
except:
    print("folder exists")    
string= path+ '/'+ dirName

while cnt<50:
    _, img = vc.read() 
    name = "pic"+str(cnt)+".jpg"
    cv2.imwrite(os.path.join(string, name),img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
    cnt+=1
vc.release() 
cv2.destroyAllWindows() 