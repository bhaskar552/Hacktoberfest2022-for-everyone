import cv2
import numpy as np
img = cv2.imread("images/Hotpot.png")
width,height=250,350
pts1=np.float32([[77,218],[242,227],[96,434],[242,429]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgoutput=cv2.warpPerspective(img,matrix,(width,height))
print(pts1)
print(pts2)

cv2.imshow("image",img)
cv2.imshow("output",imgoutput)
cv2.waitKey(0)