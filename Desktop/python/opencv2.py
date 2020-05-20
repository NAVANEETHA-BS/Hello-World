import cv2   [doubt]
import numpy as np

MIN_MATCH_COUNT=30

detector=cv2.SIFT()
FLANN_INDEX_KDTREE=0
flannparam=dict(algorithm=FLANN_INDEX_KDTREE,tree=5)
flann=cv2.FlannBaseMatcher(flannParam,{})

trainImg=cv2.imread('TrainingData/Training.jpg',0)
trainKP,trainDecs=detector.detectAndCompute(trainImg,None)

cam=cv2.VideoCapture(0)
while True:
    ret,QueryImgBGR=cam.read()
    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
    matches=flann.KnnMatch(queryDesc,trainDecs,k=2)

    goodMatch=[]
    for m,n in matches:
        if(m.distance<0.75*n.distance):
            goodMatch.append(m)

        if len(goodMatch)>MIN_MATCH_COUNT:
            tp=[]
            qp=[]
            for m in goodMatch:
                tp.append(trainKP[m.trainidx].pt)
                qp.append(queryKP[m.queryidx].pt)
            tp,qp=np.float32(tp,qp)

























                
