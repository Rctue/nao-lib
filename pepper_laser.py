# -*- coding: utf-8 -*-
from naoqi import ALProxy
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


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

# laser beam is approx 60 degrees wide, with 15 segments of 4 degrees each
# actual estimates show it to be closer to 3.7125 degrees per segment, total of 50.56875 degrees from -26.22 to +20.98 degrees.
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

data_laser_horizontal_front = np.array([6.536083698272705, 2.5059142112731934, 0.8789654970169067, 0.27891576290130615, 0.8938462138175964, 0.22674506902694702, 0.9894917011260986, 0.18988201022148132, 2.7259786128997803, 0.35847848653793335, 4.316259860992432, 0.3109394311904907, 1.2001124620437622, 0.015692872926592827, 1.1989585161209106, -0.05490745231509209, 1.2993327379226685, -0.13641250133514404, 2.55708646774292, -0.421699196100235, 2.6818032264709473, -0.6061331629753113, 3.7950096130371094, -1.095881462097168, 6.599373817443848, -2.3341526985168457, 1.7752439975738525, -0.7480522990226746, 1.4224181175231934, -0.7005590796470642])

# def get_sensor_data(sensor_list, header = '', max_count = 3, verbose = True):

#     count=0
#     if verbose: print(header)
#     data=[]
#     while count < max_count:
#         values=memProxy.getListData(sensor_list)
#         if verbose: print(values)
#         data.append(values)
#         count+=1
#     return data

# def get_laser_scan(count=1):
# ##    data = [[7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
# ##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
# ##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
# ##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
# ##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
# ##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
# ##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
# ##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
# ##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5],
# ##            [7.0, -3.5, 7.0, -3.5, 7.0, -3.5]]
# ##    
#     data_front = get_sensor_data(laser_front, max_count=count, verbose=False)
#     data_left = get_sensor_data(laser_left, max_count=count, verbose=False)
#     data_right = get_sensor_data(laser_right, max_count=count, verbose=False)

#     xdata=[]
#     ydata=[]
#     for dd in data_front:
#         print(dd)
#         xdata = xdata + dd[0::2]
#         ydata = ydata + dd[1::2]
#     for dd in data_left:
#         ydata = ydata + dd[0::2]
#         xdata = xdata + -1*dd[1::2]
#     for dd in data_right:
#         ydata = ydata + -1*dd[0::2]
#         xdata = xdata + dd[1::2]

#     scan_data=[np.sqrt(np.array(xdata)**2+np.array(ydata)**2),np.arctan2(ydata,xdata)]
# ##    scan_data=[[7.82623792 7.82623792 7.82623792 7.82623792 7.82623792 7.82623792
# ##  7.82623792 7.82623792 7.82623792 7.82623792 7.82623792 7.82623792
# ##  7.82623792 7.82623792 7.82623792]
# ## [2.03444394 2.03444394 2.03444394 2.03444394 2.03444394 2.03444394
# ##  2.03444394 2.03444394 2.03444394 2.03444394 2.03444394 2.03444394
# ##  2.03444394 2.03444394 2.03444394]]
#     return scan_data

def get_mimic_sonar(left_range, right_range):
    max_distance = 10 # meters, max range for pepper seems to be 7.82623792 m
    # scan_data = get_laser_scan().T
    # left =  [dat[1] for dat in scan_data if dat[0]>=left_range[0]  and dat[0]<=left_range[1]]
    # right = [dat[1] for dat in scan_data if dat[0]>=right_range[0] and dat[0]<=right_range[1]]
    scan_data = get_laser_scan()
    left  = scan_data[1][(scan_data[0]>=left_range[0])  & (scan_data[0]<=left_range[1])] 
    right = scan_data[1][(scan_data[0]>=right_range[0]) & (scan_data[0]<=right_range[1])]
    
    if len(left)>0:
        left_sonar = np.min(left)
    else:
        left_sonar = max_distance
    if len(right)>0:
        right_sonar = np.min(right)
    else:
        right_sonar = max_distance

    return [left_sonar, right_sonar]

def get_sensor_data(sensor_list, verbose = False):

    values=memProxy.getListData(sensor_list)
    if verbose: 
        print(values)

    return np.array(values)

def get_laser_scan(polar=True):
    
    data_front = get_sensor_data(laser_front, verbose=False)
    data_left = get_sensor_data(laser_left,  verbose=False)
    data_right = get_sensor_data(laser_right, verbose=False)

    # data_front = data_laser_horizontal_front # for testing without robot
    # data_left = data_laser_horizontal_front # for testing without robot
    # data_right = data_laser_horizontal_front # for testing without robot
    
    x_front = data_front[0::2]
    y_front = data_front[1::2]
    y_left = data_left[0::2]
    x_left = data_left[1::2]*(-1.0) # only works with numpy arrays
    y_right = data_right[0::2]*(-1.0)
    x_right = data_right[1::2]
    
    xdata = np.concatenate((x_left, x_front, x_right))
    ydata = np.concatenate((y_left, y_front, y_right))
    
    if polar:
        scan_data=np.stack((np.arctan2(ydata,xdata), np.sqrt((xdata)**2 + (ydata)**2)))
    else:
        scan_data = np.stack((xdata, ydata))
##    scan_data=[[7.82623792 7.82623792 7.82623792 7.82623792 7.82623792 7.82623792
##  7.82623792 7.82623792 7.82623792 7.82623792 7.82623792 7.82623792
##  7.82623792 7.82623792 7.82623792]
## [2.03444394 2.03444394 2.03444394 2.03444394 2.03444394 2.03444394
##  2.03444394 2.03444394 2.03444394 2.03444394 2.03444394 2.03444394
##  2.03444394 2.03444394 2.03444394]]
    return scan_data

if __name__=="__main__":    
    #pepper_ip = "192.168.0.116"
    #pepper_port = 9559
    pepper_ip = "127.0.0.1"
    pepper_port = 49713
    
    # create proxy on ALMemory
    memProxy = ALProxy("ALMemory",pepper_ip,pepper_port)

    print( "Shovel Seg01 X Y Seg02 X Y Seg03 X Y")
    data = get_sensor_data(laser_shovel,True)
    print( "Vertical Right X Y Left X Y")
    data = get_sensor_data(laser_vertical, True)
    print( "Front Laser")
    data = get_sensor_data(laser_front, True) 

    print("\nget laser scan")
    scan=get_laser_scan()
    print(scan)
    
    print("\nmimic sonar:")
    print(get_mimic_sonar([-3,0],[0,3]))

    plt.ion()
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    
    count=0
    while count<1:
        data = get_laser_scan()
        if count==0:
            print(data)
        ax.plot(data[0],data[1],'r-o') 
        plt.draw()
        plt.pause(0.1) 
        count+=1

    
    #plt.waitforbuttonpress(0)
    plt.ioff()
    plt.show() #needed to catch close window as plt.close does not work
 
        



