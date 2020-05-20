import cv2              #import opencv-python module
#img=cv2.imread("img.jpg",1)#Read the image in RGB/colored format
#img=cv2.imread("img.jpg",0)#Read the image in GRay scale/black and white
img=cv2.imread("img.jpg",0)
#print(img)
#cv2.imshow("img",img)#open a window to display the image/name of the window
#resized=cv2.resize(img,(650,500))
#resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
resized=cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))
cv2.imshow("img",resized)
cv2.waitKey(0) #wait untill a user presses a key
#cv2.waitkey(2000) #wait for 2000 milliseconds
cv2.destroyAllWindows()



