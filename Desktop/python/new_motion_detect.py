import cv2
import time
import datetime
import imutils
import numpy as np
from matplotlib import pyplot as plt


def motion_detection():
    #VideoCapture()[0]
    video=cv2.VideoCapture(0)
    time.sleep(2)

    frst_frame =None

    while True:
        #frame = VideoCapture.read()[1]
        video = cv2.VideoCapture(1)
        frame = video.read()
        text = 'unoccupied'

        #grayscale_frame = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
        gray = (np.float32(frame), cv2.COLOR_RGB2GRAY)


        gaussian_frame = cv2.GaussianBlur(gray,(21,21),0)

        blur_frame = cv2.blur(gaussian_frame,(5,5))

        grayscale_image = blur_frame

        if frst_frame is None:
            frst_frame = grayscale_image
        else:
            pass

        frame = imutils.resize(frame, width=500)

        frame_delta = cv2.absdiff(frst_frame, grayscale_image)

        thresh = cv2.threshold(frame_delta, 100, 225, cv2.THRESH_BINARY)[1]

        dilate_image = cv2.dilate(thresh, None, iterations=2)

        cnt = cv2.findContours(dilate_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        
        for c in cnt:
            if cv2.contourArea(c) > 800:
                (x, y, w, h) = cv2.boundngRect(c)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0),2)

                text = 'Occupied'
            else:
                pass

        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, f'[+] Room Status:{text}',(10,20),font, 0.5, (0,0,255), 2)

        cv2.putText(frame, datetime.datetime.now().strftime('%A %d %B %Y %I:%M:%S%p'),
            (10, frame.shape[0] - 10), font, 0.35, (0,0,255), 1)

        cv2.imshow('Security Feed',frame)
        cv2.imshow('Threshold(foreground mask)', dilate_image)
        cv2.imshow('Frame_delta', frame_delta)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__=='__main__':
    motion_detection()

        
                    




                    






























                
                



















