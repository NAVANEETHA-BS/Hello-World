import cv2

#create a cascade classifier object
face_cascade=cv2.CascadeClassifier("data\haarcascade_frontalface_default.xml")
#add path in the file explorer
#print(cv2.__file__)
#C:/Users/Neetha/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/cv2/data

#reading the image as it is
img=cv2.imread("img.jpg")

#reading the image as garyscale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#search the coordinates of the image
face=face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)
print(type(face))
print(face)

for x,y,w,h in face:
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,2),3)

img=cv2.resize(img, (int(img.shape[1]),int(img.shape[0])))

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
