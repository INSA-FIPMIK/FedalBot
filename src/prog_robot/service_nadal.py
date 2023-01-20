from pyniryo import *

def service_nad() :

    robot = NiryoRobot("172.20.10.13")


    robot.calibrate_auto()

    joints_read = robot.get_joints()
    print(joints_read)
    son = robot.get_sounds()
    print(son)


    robot.set_volume(200)
    robot.set_arm_max_velocity(100)

    #robot.say("Je suis Raphaël Nadal, c'est à moi de servir !", 1)

    robot.move_joints(0, 0.5, -1.25, 0, 0, 0) #home position

    fw_kine = robot.forward_kinematics(0, 0.5, -1.25, 0, 0, 0)
    print(fw_kine)

    robot.move_joints(-0.801, 0.228, -0.921, 1.109, 0.627, -0.114) #pos sécurité
    robot.move_joints(-0.135, -0.706, -0.487, 1.339, 1.558, 1.715) #devant balle
    robot.move_joints(-0.135, -0.706, -0.487, 1.791, 1.558, 1.715) #prépare le service
    robot.play_sound("Service.mp3", wait_end=False, start_time_sec=0, end_time_sec=0)
    robot.move_joints(-0.135, -0.706, -0.487, 0.433, 1.558, 1.715) #tape la balle

    robot.move_joints(0, 0.5, -1.25, 0, 0, 0) #home position

    robot.close_connection()