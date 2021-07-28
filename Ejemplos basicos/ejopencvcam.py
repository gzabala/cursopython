import numpy as np
from cv2 import cv2
cam=cv2.VideoCapture(1)
while(True):
    ret, img=cam.read()
    alto=img.shape[0]
    ancho=int(img.shape[1]/2)
    img[:,ancho:]=np.flip(img[0:alto,0:ancho],1)
    cv2.imshow("Flip", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cam.release()
cv2.destroyAllWindows()
