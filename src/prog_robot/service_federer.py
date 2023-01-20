from pyniryo import *

def service_fed() :

    robot = NiryoRobot("172.20.10.14")


    robot.calibrate_auto()

    joints_read = robot.get_joints()
    print(joints_read)
    son = robot.get_sounds()
    print(son)


    robot.set_volume(200)
    robot.set_arm_max_velocity(100)

    #robot.say("Je suis Roger Federer, c'est à moi de servir !", 1)

    robot.move_joints(0, 0.5, -1.25, 0, 0, 0) #home position

    fw_kine = robot.forward_kinematics(0, 0.5, -1.25, 0, 0, 0)
    print(fw_kine)

    robot.move_joints(-0.801, 0.228, -0.921, 1.109, 0.627, -0.114) #pos sécurité
    robot.move_joints(-0.263, -1.008, -0.572, 1.259, 1.530, 1.555) #devant balle
    robot.move_joints(-0.263, -1.008, -0.572, 1.711, 1.530, 1.555) #prépare le service
    robot.play_sound("Service.mp3", wait_end=False, start_time_sec=0, end_time_sec=0)
    robot.move_joints(-0.263, -1.008, -0.572, 0.353, 1.530, 1.555) #tape la balle

    robot.move_joints(0, 0.5, -1.25, 0, 0, 0) #home position

    robot.close_connection()