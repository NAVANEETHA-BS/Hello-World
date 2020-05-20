import cv2

def main():

    imgpath="dataset\\4.1.04.tiff"
    img=cv2.imread(imgpath)

    #cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Lena',img)
    cv2.waitKey(0)
    #cv2.destroyWindow('Lena')
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
