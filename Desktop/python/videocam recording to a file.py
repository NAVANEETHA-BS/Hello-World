import cv2

def main():

    windowName = "Live  Webcam Vdeo Feed Capture"
    cv2.namedWindow(windowName)

    cap = cv2.VideoCapture(0)

    filename = 'output.avi'
    codec = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate = 30
    resolution = (640,480)

    VideoFileOutput = cv2.VideoWriter(filename,codec,framerate,resolution)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:

        ret, frame = cap.read()

        VideoFileOutput.write(frame)
        
        #cv2.imshow("Gray",output)
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    VideoFileOutput.release()
    cap.release()

if __name__=="__main__":
    main()























        
