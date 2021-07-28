import cv2
img=cv2.imread("chalten.jpg") # Abrir un archivo con una imagen
# print("Dimensiones de la imagen: {}", img.shape) # La última dimensión es el valor de los colores
# print(img.shape[0])
# print(img.shape[1])
alto_medio = int(img.shape[0]/2)
print(type(alto_medio))
img[:alto_medio,:,0]=0 # 0:Blue, 1:Green, 2:Red
img[:alto_medio,:,1]=0 # 0:Blue, 1:Green, 2:Red
img[alto_medio:,:,0]=0
img[alto_medio:,:,2]=0
cv2.imshow('Final', img) # Muestra img en una ventana
cv2.waitKey(0) # espera una tecla para salir
cv2.destroyAllWindows() # Destruye todas las ventanas creadas (si no se va a colgar el kernel!)