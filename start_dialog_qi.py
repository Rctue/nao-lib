#Simple dialog in Python
# -*- encoding: UTF-8 -*-

import qi
from requests import session
#import nao_nocv_2_1 as nao

def connect_robot(robot_ip, robot_port):
    print("connecting to robot " + "tcp://" + robot_ip + ":" + str(robot_port))
    # app= qi.Application(url= "tcp://"+robot_ip+":"+str(robot_port))
    # app = connect_robot(robot_ip, robot_port)
    # app.start()
    # session = app.session
    
    # return session

    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(robot_ip, robot_port))
        return session
    except RuntimeError:
        print ("\nCan't connect to Qi at IP {} (port {})".format(robot_ip, robot_port))
        #sys.exit(1)
        return None
    

def unload_all_topics(dialog_p):
    # Unload all topics
    loaded_topics = dialog_p.getAllLoadedTopics()
    print(loaded_topics)
    
    for topic in loaded_topics:
        print("unloading topic: " + topic)
        dialog_p.unloadTopic(topic)
    
    print("done unloading topics")

def mydialog(dialog_p, topf_path):
    
    # Load topic - absolute path is required
    print("loading topic: " + topf_path)
    #topf_path = topf_path.decode('utf-8')
    topic = dialog_p.loadTopic(topf_path.encode('utf-8'))

    # Start dialog
    dialog_p.subscribe('myModule')

    # Activate dialog
    dialog_p.activateTopic(topic)
    print("dialog started, now you can talk to the robot!")
    input(u"Press 'Enter' to exit.")

    # Deactivate topic
    dialog_p.deactivateTopic(topic)

    # Unload topic
    dialog_p.unloadTopic(topic)

    # Stop dialog
    dialog_p.unsubscribe('myModule')

if __name__ == '__main__':

    #dialog_topic = "/home/nao/demos/museum/PSV_enu.top" #/weather_enu.top"  # Absolute path of the dialog topic file (on the robot).
    dialog_topic = "/Users/rcuijper/Library/CloudStorage/OneDrive-TUEindhoven/scripts/choregraphe/mydialog/weather/weather_enu.top"  # Absolute path of the dialog topic file (on the robot).
    
    robot_ip="192.168.0.111" # replace this with the actual ip address of the robot
    robot_ip="127.0.0.1" # replace this with the actual ip address of the robot
    robot_port=9559 # Robot port number
    
     #connect to robot dialog manager
    session = connect_robot(robot_ip, robot_port)
    dialog_p = session.service('ALDialog')
    dialog_p.setLanguage("English")

    unload_all_topics(dialog_p)
    mydialog(dialog_p, dialog_topic)
