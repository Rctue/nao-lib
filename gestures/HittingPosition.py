# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([ 2.00000])
keys.append([ -0.18719])

names.append("HeadYaw")
times.append([ 2.00000])
keys.append([ -0.00464])

names.append("LAnklePitch")
times.append([ 2.00000])
keys.append([ 0.07052])

names.append("LAnkleRoll")
times.append([ 2.00000])
keys.append([ -0.10734])

names.append("LElbowRoll")
times.append([ 2.00000])
keys.append([ -0.58748])

names.append("LElbowYaw")
times.append([ 2.00000])
keys.append([ -1.22724])

names.append("LHand")
times.append([ 2.00000])
keys.append([ 0.00405])

names.append("LHipPitch")
times.append([ 2.00000])
keys.append([ 0.20406])

names.append("LHipRoll")
times.append([ 2.00000])
keys.append([ 0.11202])

names.append("LHipYawPitch")
times.append([ 2.00000])
keys.append([ -0.16103])

names.append("LKneePitch")
times.append([ 2.00000])
keys.append([ -0.09055])

names.append("LShoulderPitch")
times.append([ 2.00000])
keys.append([ 1.59225])

names.append("LShoulderRoll")
times.append([ 2.00000])
keys.append([ 0.16563])

names.append("LWristYaw")
times.append([ 2.00000])
keys.append([ 0.10887])

names.append("RAnklePitch")
times.append([ 2.00000])
keys.append([ 0.06294])

names.append("RAnkleRoll")
times.append([ 2.00000])
keys.append([ 0.06600])

names.append("RElbowRoll")
times.append([ 2.00000])
keys.append([ 0.43570])

names.append("RElbowYaw")
times.append([ 2.00000])
keys.append([ 1.18114])

names.append("RHand")
times.append([ 2.00000])
keys.append([ 0.00710])

names.append("RHipPitch")
times.append([ 2.00000])
keys.append([ 0.18864])

names.append("RHipRoll")
times.append([ 2.00000])
keys.append([ -0.06745])

names.append("RHipYawPitch")
times.append([ 2.00000])
keys.append([ -0.16103])

names.append("RKneePitch")
times.append([ 2.00000])
keys.append([ -0.07359])

names.append("RShoulderPitch")
times.append([ 2.00000])
keys.append([ 1.13621])

names.append("RShoulderRoll")
times.append([ 2.00000])
keys.append([ -0.11202])

names.append("RWristYaw")
times.append([ 2.00000])
keys.append([ 0.17330])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True);
except BaseException, err:
  print err
