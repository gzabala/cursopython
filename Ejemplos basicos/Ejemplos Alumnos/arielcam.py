import cv2
import numpy as np

cam=cv2.VideoCapture(1) #Qué camara voy a capturar?
while(True):
    ret, cuadro=cam.read()
    if ret:
        img_invertida=np.flip(cuadro, 1)
        ancho_medio = int(cuadro.shape[1]/2)
        cuadro[:,ancho_medio:]=img_invertida[:,ancho_medio:]
        cv2.imshow('Final', cuadro) # Muestra img en una ventana
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()