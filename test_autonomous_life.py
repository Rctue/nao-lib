import qi
import numpy as np
import time
#import matplotlib as mpl
#mpl.use('TkAgg')
#import matplotlib.pyplot as plt

# Priority between the Autonomous Abilities
# Each Autonomous Ability has an enabled and a running boolean value:

# enabled value means the Autonomous Ability has right to move the robot.
# running value means the Autonomous Ability is currently running.
# There is some priority between the Autonomous Abilities, that causes constraints in the running boolean values:

# BackgroundMovement will not be running when ListeningMovement or SpeakingMovement is running.
# ListeningMovement will not be running when SpeakingMovement is running.
# SpeakingMovement has the highest autonomous ability priority.
# Note
# AutonomousBlinking and BasicAwareness don’t deal with the priorities between the autonomous abilities because they can run in parallel.

def connect_robot(robot_ip, robot_port):
    print("connecting to robot " + "tcp://" + robot_ip + ":" + str(robot_port))
    return qi.Application(url= "tcp://"+robot_ip+":"+str(robot_port))

def list_activities(aut_life_service):
    activities = ["BasicAwareness", "BackgroundMovement", "ListeningMovement", "SpeakingMovement", "AutonomousBlinking"]
    for activity in activities:
        print(activity + " enabled: " + str(aut_life_service.getAutonomousAbilityEnabled(activity)))
       
    results = aut_life_service.getAutonomousAbilitiesStatus()
    return results

def set_activities(aut_life_service, dict_activities_enabled):
    activities = ["BasicAwareness", "BackgroundMovement", "ListeningMovement", "SpeakingMovement", "AutonomousBlinking"]
    for key,value in dict_activities_enabled.items():
        if key in activities:
            aut_life_service.setAutonomousAbilityEnabled(key, value)
        #print(key + " enabled: " + str(aut_life_service.getAutonomousAbilityEnabled(key)))
       
    results = aut_life_service.getAutonomousAbilitiesStatus()
    return results


def subscribe_to_event(memProxy, event_name):
    subscriber =memProxy.subscriber(event_name)
    subscriber.signal.connect(on_event_detected)
    
def on_event_detected(name, state, id):
    """ Callback for event AutonomousLife/State. It will be called when the state of Autonomous Life changes."""
    #print("Event detected: " + str(value))
    print("Event " + name + " changed to state " + state + " with id " + str(id))

if __name__=="__main__":    
    #pepper_ip = "192.168.0.113"
    pepper_port = 9559
    pepper_ip = "127.0.0.1"
    #pepper_port = 49713
    
    # create proxy on ALMemory
    app = connect_robot(pepper_ip, pepper_port)
    app.start()
    session = app.session
    memProxy = session.service("ALMemory")
    aut_life_service = session.service("ALAutonomousLife")
    subscribe_to_event(memProxy, "AutonomousLife/State") # doesn't seem to work with simulated robot
    
    #autonomous_life_state = memProxy.getData("AutonomousLife/State")
    autonomous_life_state = aut_life_service.getState()
    print("AutonomousLife/State: " + autonomous_life_state)
    if autonomous_life_state == "disabled":
        print("Enabling Autonomous Life")
        #memProxy.insertData("AutonomousLife/State", "solitary")
        aut_life_service.setState("solitary")
        set_activities(aut_life_service, {"BasicAwareness": True, "BackgroundMovement": True, "ListeningMovement": True, "SpeakingMovement": True, "AutonomousBlinking": True})
    else:
        print("Disabling Autonomous Life")
        aut_life_service.setState("disabled")
        set_activities(aut_life_service, {"BasicAwareness": False, "BackgroundMovement": False, "ListeningMovement": False, "SpeakingMovement": False, "AutonomousBlinking": False})
    
    
    
    results = list_activities(aut_life_service)
    for result in results:
        print(result)
   
    
    aut_life_service.setAutonomousAbilityEnabled("All", False)
    print("I am now in " + memProxy.getData("AutonomousLife/State") + " mode, and sleeping for 5 seconds.")
    time.sleep(5)
    print("I am now activating some autonomous life activities")
    aut_life_service.setAutonomousAbilityEnabled("BasicAwareness", True)
    aut_life_service.setAutonomousAbilityEnabled("AutonomousBlinking", True)
    list_activities(aut_life_service)
   
    # time.sleep(3)
    # print("Raising event AutonomousLife/State")
    # memProxy.raiseEvent("AutonomousLife/State", ["key", "value","message"])
    # time.sleep(5)
    
    