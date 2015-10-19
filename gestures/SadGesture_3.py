# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()


names.append("LShoulderPitch")
times.append([ 1.53846, 3.07692])
keys.append([ [ 1.39626, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ 1.39626, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 1.53846, 3.07692])
keys.append([ [ 0.34907, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ 0.34907, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 1.53846, 3.07692])
keys.append([ [ -1.39626, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ -1.39626, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 1.53846, 3.07692])
keys.append([ [ -1.04720, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ -1.04720, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 1.53846, 3.07692])
keys.append([ [ -1.81514, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ 0.00000, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 1.53846, 3.07692])
keys.append([ [ 0.00000, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ 0.00000, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 1.53846, 3.07692])
keys.append([ [ 1.39626, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ 1.39626, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 1.53846, 3.07692])
keys.append([ [ -0.34907, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ -0.34907, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 1.53846, 3.07692])
keys.append([ [ 1.39626, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ 1.39626, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 1.53846, 3.07692])
keys.append([ [ 1.04720, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ 1.04720, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 1.53846, 3.07692])
keys.append([ [ 1.81514, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ -0.00000, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 1.53846, 3.07692])
keys.append([ [ 0.00000, [ 3, -0.51282, 0.00000], [ 3, 0.51282, 0.00000]], [ 0.00000, [ 3, -0.51282, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
