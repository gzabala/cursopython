import numpy as np
from cv2 import cv2
img=cv2.imread("chalten.jpg")
alto=img.shape[0]
ancho=int(img.shape[1]/2)
# img[0:int(alto/2),:,0]=0
# img[0:int(alto/2),:,1]=0
# img[int(alto/2):,:,0]=0
# img[int(alto/2):,:,2]=0

img[:,ancho:]=np.flip(img[0:alto,0:ancho],1)
cv2.imshow('Chalten', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()