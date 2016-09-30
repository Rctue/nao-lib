# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadYaw")
times.append([ 1.00000])
keys.append([ [ -0.00464, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("HeadPitch")
times.append([ 1.00000])
keys.append([ [ -0.18719, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderPitch")
times.append([ 1.00000])
keys.append([ [ 1.57912, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 1.00000])
keys.append([ [ 0.17572, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 1.00000])
keys.append([ [ -1.23476, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 1.00000])
keys.append([ [ -0.59106, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 1.00000])
keys.append([ [ 0.10887, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 1.00000])
keys.append([ [ 0.00405, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 1.00000])
keys.append([ [ 1.47185, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 1.00000])
keys.append([ [ -0.12235, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 1.00000])
keys.append([ [ 1.18758, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 1.00000])
keys.append([ [ 0.43950, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 1.00000])
keys.append([ [ 0.17330, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 1.00000])
keys.append([ [ 0.00710, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipYawPitch")
times.append([ 1.00000])
keys.append([ [ -0.16103, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipRoll")
times.append([ 1.00000])
keys.append([ [ 0.11202, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipPitch")
times.append([ 1.00000])
keys.append([ [ 0.20406, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LKneePitch")
times.append([ 1.00000])
keys.append([ [ -0.09055, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnklePitch")
times.append([ 1.00000])
keys.append([ [ 0.07052, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnkleRoll")
times.append([ 1.00000])
keys.append([ [ -0.10734, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipRoll")
times.append([ 1.00000])
keys.append([ [ -0.06745, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipPitch")
times.append([ 1.00000])
keys.append([ [ 0.18864, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RKneePitch")
times.append([ 1.00000])
keys.append([ [ -0.07359, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnklePitch")
times.append([ 1.00000])
keys.append([ [ 0.06294, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnkleRoll")
times.append([ 1.00000])
keys.append([ [ 0.06600, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
