import cv2
import matplotlib.pyplot as plt

def main():

    imgpath="dataset\\4.1.04.tiff"
    img=cv2.imread(imgpath,0)

#display image on the console 
    plt.imshow(img) #it going to aplly default colormap
    
    plt.imshow(img,cmap='Spectral')
    plt.title('spectral colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    

    plt.imshow(img,cmap='Reds')
    plt.title('red colormap')
    plt.show()
    

    cv2.imshow('Lena',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
