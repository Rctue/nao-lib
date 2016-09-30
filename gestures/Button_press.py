# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("LElbowRoll")
times.append([ 0.24000, 0.48000])
keys.append([ [ -0.44328, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ -0.44328, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 0.24000, 0.48000])
keys.append([ [ -1.59694, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ -1.59694, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 0.24000, 0.48000])
keys.append([ [ 0.00028, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.00028, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderPitch")
times.append([ 0.24000, 0.48000])
keys.append([ [ 1.51708, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ 1.51708, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 0.24000, 0.48000])
keys.append([ [ 0.12268, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.12268, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 0.24000, 0.48000])
keys.append([ [ 0.02450, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.02450, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 0.24000, 0.36000, 0.48000])
keys.append([ [ 1.32849, [ 3, -0.08000, 0.00000], [ 3, 0.04000, 0.00000]], [ 1.08909, [ 3, -0.04000, 0.00000], [ 3, 0.04000, 0.00000]], [ 1.32849, [ 3, -0.04000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 0.24000, 0.48000])
keys.append([ [ 1.68889, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ 1.68889, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 0.24000, 0.48000])
keys.append([ [ 0.00543, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.00543, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 0.24000, 0.48000])
keys.append([ [ 0.96493, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.96493, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 0.24000, 0.48000])
keys.append([ [ 0.22392, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.22392, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 0.24000, 0.48000])
keys.append([ [ -1.16742, [ 3, -0.08000, 0.00000], [ 3, 0.08000, 0.00000]], [ -1.16742, [ 3, -0.08000, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
