#RobotName: Primero

from RobotRL import RobotRL

robot = RobotRL()

while robot.step():
    robot.setVI(50)
    robot.setVD(50)
    if(robot.getColorPiso()>90):
        robot.setVI(-50)
        robot.setVD(-50)
        robot.esperar(0.7)
        robot.setVI(50)
        robot.setVD(-50)
        robot.esperar(0.7)
