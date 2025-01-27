import cv2
import numpy as np
def empty(a):
    pass
path="images/hotpot.png"
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",19,179,empty)
cv2.createTrackbar("SAT Min","Trackbars",110,255,empty)
cv2.createTrackbar("SAT Max","Trackbars",240,255,empty)
cv2.createTrackbar("VAL Min","Trackbars",153,255,empty)
cv2.createTrackbar("VAL Max","Trackbars",255,255,empty)
while True:
    img = cv2.imread(path)
    imgresize = cv2.resize(img, (400, 500))
    imgHSV = cv2.cvtColor(imgresize, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("SAT Min","Trackbars")
    s_max = cv2.getTrackbarPos("SAT Max","Trackbars")
    v_min = cv2.getTrackbarPos("VAL Min","Trackbars")
    v_max = cv2.getTrackbarPos("VAL Max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgresult=cv2.bitwise_and(imgresize,imgresize,mask=mask)
    imv=np.hstack((imgHSV,imgresult))





    cv2.imshow("output", imgresize)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("result",imgresult)
    cv2.imshow("joined",imv)

    cv2.waitKey(1)

