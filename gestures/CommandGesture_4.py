# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()


names.append("LShoulderPitch")
times.append([ 2.00000, 4.00000])
keys.append([ [ 1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 2.00000, 4.00000])
keys.append([ [ 0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 2.00000, 4.00000])
keys.append([ [ -1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 2.00000, 4.00000])
keys.append([ [ -1.04720, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -1.04720, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 2.00000, 4.00000])
keys.append([ [ -0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 2.00000, 4.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 2.00000, 4.00000])
keys.append([ [ 1.63886, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 2.00000, 4.00000])
keys.append([ [ -0.00873, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 2.00000, 4.00000])
keys.append([ [ 2.08567, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 2.00000, 4.00000])
keys.append([ [ 0.63006, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.04720, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 2.00000, 4.00000])
keys.append([ [ 1.82387, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 2.00000, 4.00000])
keys.append([ [ 0.01745, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
