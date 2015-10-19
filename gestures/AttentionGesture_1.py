# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("LShoulderPitch")
times.append([ 0.50000, 1.00000])
keys.append([ [ 1.39626, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ 1.39626, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 0.50000, 1.00000])
keys.append([ [ 0.34907, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ 0.34907, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 0.50000, 1.00000])
keys.append([ [ -1.39626, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ -1.39626, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 0.50000, 1.00000])
keys.append([ [ -1.04720, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ -1.04720, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 0.50000, 1.00000])
keys.append([ [ -0.00000, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ -0.00000, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 0.50000, 1.00000])
keys.append([ [ 0.00000, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ 0.00000, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 0.50000, 1.00000])
keys.append([ [ 0.82030, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ 1.39626, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 0.50000, 1.00000])
keys.append([ [ -0.03840, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ -0.34907, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 0.50000, 1.00000])
keys.append([ [ 1.51669, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ 1.39626, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 0.50000, 1.00000])
keys.append([ [ 1.56207, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ 1.04720, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 0.50000, 1.00000])
keys.append([ [ -1.45910, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ 0.00000, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 0.50000, 1.00000])
keys.append([ [ 0.01745, [ 3, -0.16667, 0.00000], [ 3, 0.16667, 0.00000]], [ 0.00000, [ 3, -0.16667, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
