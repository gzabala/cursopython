import cv2
import numpy as np
franja=20
cam=cv2.VideoCapture(0) #Qué camara voy a capturar?
while(True):
    cuadro=[]
    for i in range(0,franja):
        ret, cuadro_indi=cam.read()
        cuadro.append(cuadro_indi)
    alto = int((cuadro[0].shape[0])/franja)
    nueva = cuadro[0]
    for j in range(1,franja):
        nueva[alto*j:,:,:]=cuadro[j][alto*j:,:,:]
    cv2.imshow("Nueva", nueva)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()