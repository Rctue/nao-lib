# -*- coding: utf-8 -*-
from naoqi import ALProxy
import numpy as np

# x is forward in m     wx/AngleX is rotation about x axis with positive meaning elevated left (y-axis)
# y is left             wy/AngleY is rotation about y axis with positive meaning x axis down
# z is up               wz/AngleZ is rotation about z axis

bumpers = ['Device/SubDeviceList/ChestBoard/Button/Sensor/Value'
    , 'Device/SubDeviceList/Platform/FrontRight/Bumper/Sensor/Value'
    , 'Device/SubDeviceList/Platform/FrontLeft/Bumper/Sensor/Value'
    , 'Device/SubDeviceList/Platform/Back/Bumper/Sensor/Value']

gyroscope = ['Device/SubDeviceList/InertialSensorBase/GyroscopeX/Sensor/Value' #	Gyroscope (rad/s)
    , 'Device/SubDeviceList/InertialSensorBase/GyroscopeY/Sensor/Value'     # Gyroscope (rad/s)
    , 'Device/SubDeviceList/InertialSensorBase/GyroscopeZ/Sensor/Value']

accelerometer = ['Device/SubDeviceList/InertialSensorBase/AccelerometerX/Sensor/Value' #	Accelerometer (m/s²)
    , 'Device/SubDeviceList/InertialSensorBase/AccelerometerY/Sensor/Value' #	Accelerometer (m/s²)
    , 'Device/SubDeviceList/InertialSensorBase/AccelerometerZ/Sensor/Value']

laser_shovel = ['Device/SubDeviceList/Platform/LaserSensor/Front/Shovel/Seg01/X/Sensor/Value'	
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Shovel/Seg01/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Shovel/Seg02/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Shovel/Seg02/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Shovel/Seg03/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Shovel/Seg03/Y/Sensor/Value']
    
laser_vertical = ['Device/SubDeviceList/Platform/LaserSensor/Front/Vertical/Right/Seg01/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Vertical/Right/Seg01/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Vertical/Left/Seg01/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Vertical/Left/Seg01/Y/Sensor/Value']

sonars = ['Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value'  #	Sonar/Sensor (m)
    , 'Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value']

infrared = ['Device/SubDeviceList/Platform/InfraredSpot/Left/Sensor/Value'  # 1 if Obstacle present, 0 otherwise
    , 'Device/SubDeviceList/Platform/InfraredSpot/Right/Sensor/Value']

laser_front = ['Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg01/X/Sensor/Value' #	Distances
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg01/Y/Sensor/Value' #	Distances
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg02/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg02/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg03/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg03/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg04/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg04/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg05/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg05/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg06/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg06/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg07/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg07/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg08/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg08/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg09/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg09/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg10/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg10/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg11/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg11/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg12/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg12/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg13/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg13/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg14/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg14/Y/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg15/X/Sensor/Value'
    , 'Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg15/Y/Sensor/Value']

laser_left = [device.replace("Front","Left") for device in laser_front]
laser_right = [device.replace("Front","Right") for device in laser_front]
#print laser_right[0]

def get_sensor_data(sensor_list, header = '', max_count = 3, verbose = True):

    count=0
    if verbose: print header
    data=[]
    while count < max_count:
        values=memProxy.getListData(sensor_list)
        if verbose: print values
        data = data + values
        count+=1
    return data

def get_laser_scan(count=1):
##    data = [[7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5]]
##    
    data_front = get_sensor_data(laser_front, max_count=count, verbose=False)
    data_left = get_sensor_data(laser_left, max_count=count, verbose=False)
    data_right = get_sensor_data(laser_right, max_count=count, verbose=False)

    xdata=[]
    ydata=[]
    for dd in data_front:
        xdata = xdata + dd[0::2]
        ydata = ydata + dd[1::2]
    for dd in data_left:
        ydata = ydata + dd[0::2]
        xdata = xdata + -1*dd[1::2]
    for dd in data_right:
        ydata = ydata + -1*dd[0::2]
        xdata = xdata + dd[1::2]

    scan_data=np.transpose([np.sqrt(np.array(xdata)**2+np.array(ydata)**2),np.arctan2(ydata,xdata)])
##    scan_data=[[7.82623792 7.82623792 7.82623792 7.82623792 7.82623792 7.82623792
##  7.82623792 7.82623792 7.82623792 7.82623792 7.82623792 7.82623792
##  7.82623792 7.82623792 7.82623792]
## [2.03444394 2.03444394 2.03444394 2.03444394 2.03444394 2.03444394
##  2.03444394 2.03444394 2.03444394 2.03444394 2.03444394 2.03444394
##  2.03444394 2.03444394 2.03444394]]
    return scan_data

def get_mimic_sonar(left_range, right_range):
    max_distance = 10 # meters, max range for pepper seems to be 7.82623792 m
    scan_data = get_laser_scan()
    left =  [dat[0] for dat in scan_data if dat[1]>=left_range[0]  and dat[1]<=left_range[1]]
    right = [dat[0] for dat in scan_data if dat[1]>=right_range[0] and dat[1]<=right_range[1]]

    if len(left)>0:
        left_sonar = np.min(left)
    else:
        left_sonar = max_distance
    if len(right)>0:
        right_sonar = np.min(right)
    else:
        right_sonar = max_distance

    return [left_sonar, right_sonar]

if __name__=="__main__":    
    pepper_ip = "192.168.0.119"
    pepper_port = 9559
    #pepper_ip = "127.0.0.1"
    #pepper_port = 52587
    
    # create proxy on ALMemory
    memProxy = ALProxy("ALMemory",pepper_ip,pepper_port)

    get_sensor_data(laser_shovel, "Shovel Seg01 X Y Seg02 X Y Seg03 X Y")
    data = get_sensor_data(laser_vertical, "Vertical Right X Y Left X Y")
    print data

    print "\nget laser scan"
    scan=get_laser_scan()
    print np.transpose(scan)
    
    print "\nmimic sonar:"
    print get_mimic_sonar([-3,0],[0,3])

    import matplotlib as mpl
    import matplotlib.pyplot as plt

##    #plt.ion()
##    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
##    
##    not_done=True
##    while not_done:
##        data = get_laser_scan()
##        ax.plot(data[0],data[1],'ro')
##        plt.show()
##        s=raw_input("press q to quit")
##        if s=='q':
##            not_done = False
##
##    #plt.ioff()
##    plt.close('all')
##        
##
##
##
