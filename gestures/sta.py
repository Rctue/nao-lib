names = list()
times = list()
keys = list()

names.append("HeadYaw")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("HeadPitch")
times.append([ 2.00000])
keys.append([ [ -0.30000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderPitch")
times.append([ 2.00000])
keys.append([ [ 1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 2.00000])
keys.append([ [ 0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 2.00000])
keys.append([ [ -1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 2.00000])
keys.append([ [ -1.04720, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 2.00000])
keys.append([ [ 1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 2.00000])
keys.append([ [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 2.00000])
keys.append([ [ 1.39626, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 2.00000])
keys.append([ [ 1.04720, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipYawPitch")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipRoll")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipPitch")
times.append([ 2.00000])
keys.append([ [ -0.43633, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LKneePitch")
times.append([ 2.00000])
keys.append([ [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnklePitch")
times.append([ 2.00000])
keys.append([ [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnkleRoll")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipRoll")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipPitch")
times.append([ 2.00000])
keys.append([ [ -0.43633, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RKneePitch")
times.append([ 2.00000])
keys.append([ [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnklePitch")
times.append([ 2.00000])
keys.append([ [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnkleRoll")
times.append([ 2.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  motion = ALProxy("ALMotion")
  moveId = motion.post.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  pass

