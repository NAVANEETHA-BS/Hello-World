#importing essential libraries

import cv2
import numpy as np

def emptyFunction():
    pass

def main():

    img1=np.zeros((512,512,3),np.uint8) #resolution+RGB image(black)
    windowName='Opencv BGR Color Palette'
    cv2.namedWindow(windowName)

    cv2.createTrackbar('B',windowName,0,255,emptyFunction)
    cv2.createTrackbar('G',windowName,0,255,emptyFunction)
    cv2.createTrackbar('R',windowName,0,255,emptyFunction)
    #name of color,name of window associatedwith,
    #min value of range,max value of range,func supposed to call when we move slider
    

    while True:
        cv2.imshow(windowName,img1)

        if cv2.waitKey==27:
            break
        
        blue=cv2.getTrackbarPos('B',windowName)
        green=cv2.getTrackbarPos('G',windowName)
        red=cv2.getTrackbarPos('R',windowName)

        img1[:]=[blue,green,red]#create composite img
        print(blue,green,red)

        
    cv2.destroyAllWindows()
        
                   

if __name__=="__main__":
    main()
