#Simple dialog in Python
# -*- encoding: UTF-8 -*-

from naoqi import ALProxy
#import nao_nocv_2_1 as nao


def main(robot_ip, robot_port, topf_path):
    #nao.InitProxy(robot_ip,[0],robot_port)
    #nao.Say("Hello Class.")
    dialog_p = ALProxy('ALDialog', robot_ip, robot_port)
    dialog_p.setLanguage("English")

    # Load topic - absolute path is required
    topf_path = topf_path.decode('utf-8')
    topic = dialog_p.loadTopic(topf_path.encode('utf-8'))

    # Start dialog
    dialog_p.subscribe('myModule')

    # Activate dialog
    dialog_p.activateTopic(topic)

    raw_input(u"Press 'Enter' to exit.")

    # Deactivate topic
    dialog_p.deactivateTopic(topic)

    # Unload topic
    dialog_p.unloadTopic(topic)

    # Stop dialog
    dialog_p.unsubscribe('myModule')

if __name__ == '__main__':

    dialog_topic = "/home/nao/group_12/weather_enu.top"  # Absolute path of the dialog topic file (on the robot).
    robot_ip="192.168.0.102" # replace this with the actual ip address of the robot
    port=9559 # Robot port number

    main(robot_ip, port, dialog_topic)
