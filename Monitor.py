from nao2 import Nao_Interface
import threading
import time
import matplotlib.pyplot as plt

#Device/SubDeviceList/ChestBoard/Led/Blue/Actuator/Value
#Device/SubDeviceList/Ears/Led/Left/36Deg/Actuator/Value
#Device/SubDeviceList/Face/Led/Blue/Left/45Deg/Actuator/Value
#Device/SubDeviceList/LFoot/Led/Blue/Actuator/Value
#etc

#Device/SubDeviceList/ChestBoard/Button/Sensor/Value
#Device/SubDeviceList/LFoot/Bumper/Left/Sensor/Value
#etc

#Device/SubDeviceList/HeadPitch/Position/Actuator/Value
#Device/SubDeviceList/HeadYaw/Position/Actuator/Value
#Device/SubDeviceList/LAnklePitch/Position/Actuator/Value
#etc
#Device/SubDeviceList/HeadPitch/Hardness/Actuator/Value
#etc
#Device/SubDeviceList/HeadPitch/Position/Sensor/Value
#etc
#Device/SubDeviceList/Battery/Current/Sensor/Value
#Device/SubDeviceList/HeadPitch/ElectricCurrent/Sensor/Value
#etc
#Device/SubDeviceList/Battery/Temperature/Sensor/Value
#Device/SubDeviceList/HeadPitch/Temperature/Sensor/Value

#Device/SubDeviceList/US/Actuator/Value
#Device/SubDeviceList/US/Sensor/Value
#Device/SubDeviceList/US/Left/Sensor/Value
#Device/SubDeviceList/US/Left/Sensor/Value1

#Device/SubDeviceList/InertialSensor/GyroscopeX/Sensor/Value
#Device/SubDeviceList/InertialSensor/GyroscopeY/Sensor/Value
#Device/SubDeviceList/InertialSensor/GyroscopeZ/Sensor/Value

#Device/SubDeviceList/InertialSensor/AccelerometerX/Sensor/Value
#Device/SubDeviceList/InertialSensor/AccelerometerY/Sensor/Value
#Device/SubDeviceList/InertialSensor/AccelerometerZ/Sensor/Value
#Device/SubDeviceList/InertialSensor/AngleX/Sensor/Value
#Device/SubDeviceList/InertialSensor/AngleY/Sensor/Value

#Device/SubDeviceList/LFoot/FSR/FrontLeft/Sensor/Value
#etc
#Device/SubDeviceList/RFoot/FSR/TotalWeight/Sensor/Value

#Device/SubDeviceList/LFoot/FSR/CenterOfPressure/X/Sensor/Value
#Device/SubDeviceList/LFoot/FSR/CenterOfPressure/Y/Sensor/Value
#etc

#Device/SubDeviceList/Head/Touch/Front/Sensor/Value
# etc Middle/Rear
#Device/SubDeviceList/LHand/Touch/Back/Sensor/Value
# etc LHand/RHand Back/Left/Right

class Monitor():
    """Monitor a list of devices of the Nao robot."""
    max_duration=3600  # 1 hr
    min_duration=0.1   # 100 ms
    min_interval=0.001 # 1 ms
    
    def __init__(self, memoryProxy, devicenames):
        self.memoryProxy=memoryProxy
        self.devicenames=devicenames
        self.data=[]
        self.times=[]

    def read(self):
        l=[]
        for dev in self.devicenames:
            l.append(self.memoryProxy.getData(dev))
        return l

    def start(self, interval=0.1, duration=5, use_thread=False):
        if interval<self.min_interval:
            self.interval=self.min_interval
        else:
            self.interval=interval

        if duration<=0:
            self.duration=self.max_duration
        elif duration<self.min_duration:
            self.duration=self.min_duration
        else:
            self.duration=duration

        self.times=[]
        self.data=[]
        if not use_thread:
            self.__monitor__()
        else:
            t=threading.Thread(target=self.__monitor__)
            t.start()
            return t
            

    def __monitor__(self):
        self.timestart=time.time()
        t=0
        while t < self.duration:
            l=self.read()
            t=time.time()-self.timestart
            self.times.append(t)
            self.data.append( l)
            time.sleep(self.interval)
            
            
                     
if __name__=="__main__":
    nao_ip="192.168.0.112"
    n=Nao_Interface("n9",nao_ip)
    m=Monitor(n.memoryProxy,['Device/SubDeviceList/LHand/Touch/Back/Sensor/Value',
                             'Device/SubDeviceList/RHand/Touch/Back/Sensor/Value',
                             'Device/SubDeviceList/LHand/Touch/Left/Sensor/Value',
                             'Device/SubDeviceList/RHand/Touch/Left/Sensor/Value',
                             'Device/SubDeviceList/LHand/Touch/Right/Sensor/Value',
                             'Device/SubDeviceList/RHand/Touch/Right/Sensor/Value'])
##    m=Monitor(n.memoryProxy,['Device/SubDeviceList/HeadYaw/Position/Actuator/Value',
##                             'Device/SubDeviceList/HeadYaw/Position/Sensor/Value'])
    print "Start monitoring left/right hand touch."

    #m.start(interval=0.2, duration=30)

    dur=30
    mythread=m.start(interval=0.2, duration=dur, use_thread=True)
    mythread.join() # time.sleep(dur) werkt ook
    print m.data 

    plt.plot(m.times,m.data)
    plt.legend(['LBack' ,'RBack', 'LLeft','RLeft', 'LRight','RRight'])
    plt.show()
