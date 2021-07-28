import cv2
import numpy as np
 
img=cv2.imread("chalten.jpg") # Abrir un archivo con una imagen
img_invertida=np.flip(img, 1)
ancho_medio = int(img.shape[1]/2)
print(type(ancho_medio))
img[:,ancho_medio:]=img_invertida[:,ancho_medio:]
cv2.imshow('Final', img) # Muestra img en una ventana
cv2.waitKey(0) # espera una tecla para salir
cv2.destroyAllWindows() # Destruye todas las ventanas creadas (si no se va a colgar el kernel!)