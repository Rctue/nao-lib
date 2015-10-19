# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadYaw")
times.append([ 0.13333, 0.66667, 1.33333, 2.00000])
keys.append([ [ 0.00000, [ 3, -0.04444, 0.00000], [ 3, 0.17778, 0.00000]], [ 0.00000, [ 3, -0.17778, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00000, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00000, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("HeadPitch")
times.append([ 0.13333, 0.66667, 1.33333, 2.00000])
keys.append([ [ 0.00000, [ 3, -0.04444, 0.00000], [ 3, 0.17778, 0.00000]], [ -0.17453, [ 3, -0.17778, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00000, [ 3, -0.22222, -0.05818], [ 3, 0.22222, 0.05818]], [ 0.17453, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
