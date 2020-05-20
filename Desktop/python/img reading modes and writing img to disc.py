import cv2

def main():
     imgpath="dataset\\4.1.04.tiff"
     img=cv2.imread(imgpath,0) #image read in gray scale mode
     #img=cv2.imread(imgpath,1) #default mode,read as it is
     #img=cv2.imread(imgpath,-1) #it reads asitis and loads alpha transperancy channels

     outpath="output\\4.1.04.jpg"

     cv2.imshow('Lena',img)
     cv2.imwrite(outpath,img)
     cv2.waitKey(0)
     cv2.destroyWindow('Lena')

if __name__=="__main__":
    main()
