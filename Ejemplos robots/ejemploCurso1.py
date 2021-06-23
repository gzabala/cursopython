#RobotName: EjemploCurso1
#NO SE PUEDEN USAR TILDES EN LOS COMENTARIOS
from RobotRL import RobotRL

robot = RobotRL()

while robot.step():
    # Todo el codigo que esta por encima de esta linea es obligatorio, debe estar en todo lo que programes.

    # El robot simplemente gira sobre su propio eje
    # Si te aparece texto rojo en la consola (parte inferior del simulador) es que algo esta mal...
    # robot.setVel(30,30)
    # robot.esperar(1)
    # robot.setVel(30,-30)
    # robot.esperar(0.51)
    # print(robot.tiempoActual())
    robot.setVel(50,50)
    piso=robot.getColorPiso()
    if piso>75:
        robot.setVel(-50,-50)
        robot.esperar(1)
        robot.setVel(50, -50)
        robot.esperar(1)
    
