
import cv2
import numpy as np

#create a black image and a window
windowName='Drawing'
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowName)

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),-1)

#bind the callback function to window
cv2.setMouseCallback(windowName,draw_circle)

def main():
    #events=[i for i in dir(cv2) f 'EVENT' in i]
    #print(events)
    while(True):
        cv2.imshow(windowName,img
                   )
        if cv2.waitKey(20)==27:
            break
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
