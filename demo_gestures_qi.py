import qi
import sys
import os

def connect_robot(robot_ip, robot_port):
    print("connecting to robot " + "tcp://" + robot_ip + ":" + str(robot_port))
    return qi.Application(url= "tcp://"+robot_ip+":"+str(robot_port))



def GetAvailableGestures():
    """Returns available gestures in a list"""
    list_path = sys.path
    found = 0
    for i in range (0,len(list_path)):
        if os.path.exists(list_path[i]+"/gestures"):
            found = 1
            break

    if found == 0:
        print("Could not find /gestures directory!")
        raise IOError
        return None

    remove = []
    
    list_gestures = os.listdir(list_path[i]+"/gestures")
    for i in range(len(list_gestures)):
        list_gestures[i] = "/gestures/"+list_gestures[i]
        if not list_gestures[i].endswith(".py") and not list_gestures[i].endswith(".ges"):
            remove.append(i)

    ## remove non py files
    remove.reverse()
        
    for i in range(len(remove)):
        list_gestures.pop(remove[i])
        
    return list_gestures

#######################################################################
## This functions executes movements transported from choregraph
## and saved in a *.py file. Make sure to initialize the motion proxy.
#######################################################################
def LoadGesture(file_name):
    """ Give up the filename containing the movement. Needs motion proxy."""

    list_path = sys.path
    filefound = False
    for i in range (0,len(list_path)):
        if os.path.exists(list_path[i]+"/gestures/"+file_name):
            file_name=list_path[i]+"/gestures/"+file_name
            filefound=True
            break
        if os.path.exists(list_path[i]+"/"+file_name):
            file_name=list_path[i]+"/"+file_name
            filefound=True
            break

    if not filefound:
        print("Movement or gesture "+str(file_name)+" not found in PYTHONPATH")
        return

    names = []
    times = []
    keys = []
    file_load = open(file_name)
    lines = file_load.readlines()
    for i in range(0,len(lines)):
        if lines[i].strip().startswith("names.append("):
            exec(lines[i])
        if lines[i].strip().startswith("times.append("):
            exec(lines[i])
        if lines[i].strip().startswith("keys.append("):
            exec(lines[i])       
        if lines[i].strip().startswith("try:"):
            break
    file_load.close()
    
    return (names, times, keys)

def RunMovement(motionProxy, file_name, post = True, to_start_position = True):
    """ Give up the filename containing the movement. Needs motion proxy."""

    names, times, keys = LoadGesture(file_name)
    
    # if to_start_position is true, the robot will first move to the last position of the movement, and then execute the movement. This is usefull for testing movements in random order, but should be set to false if you want to execute a sequence of movements.
    if to_start_position:
        last_key = motionProxy.getAngles(names, True)

        high_time = 0.0
        for i in range(0,len(times)):
            cur_time = times[i][len(times[i])-1]
            if cur_time > high_time:
                high_time = cur_time

        for i in range(0, len(times)):
            times[i].append(high_time+0.1)
            times[i].append(high_time+2)
            keys[i].append(keys[i][len(keys[i])-1])
            keys[i].append([last_key[i],[ 3, -0.55556, 0.00000], [ 3, 0.55556, 0.00000]])

    
    if post:
        motionProxy.post.angleInterpolationBezier(names, times, keys)
    else:
        motionProxy.angleInterpolationBezier(names, times, keys)
        

if __name__ == "__main__":
    #robot_ip="192.168.0.111"
    robot_ip="127.0.0.1"
    robot_port=9559

    app = connect_robot(robot_ip, robot_port)
    app.start()
    session = app.session
    
    motionProxy = session.service("ALMotion")
    motionProxy.wakeUp()
    for g in GetAvailableGestures():
        s = input("Run gesture " + g + "? (y/n) ")
        if s == "y":
            RunMovement(motionProxy, g, post=False, to_start_position=True)
    
    motionProxy.rest()
