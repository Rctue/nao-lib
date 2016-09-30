names = list()
times = list()
keys = list()

names.append("LShoulderRoll")
times.append([ 2.00000])
keys.append([ [ 0.24435, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 2.00000, 2.40000])
keys.append([ [ -0.07679, [ 3, -0.66667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.07679, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 2.00000, 2.40000, 3.93333, 4.46667, 4.80000, 5.33333, 5.66667])
keys.append([ [ 0.28623, [ 3, -0.66667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.28623, [ 3, -0.13333, 0.00000], [ 3, 0.51111, 0.00000]], [ 0.52185, [ 3, -0.51111, -0.08417], [ 3, 0.17778, 0.02928]], [ 0.62657, [ 3, -0.17778, -0.04260], [ 3, 0.11111, 0.02663]], [ 0.72955, [ 3, -0.11111, -0.04005], [ 3, 0.17778, 0.06408]], [ 0.93899, [ 3, -0.17778, 0.00000], [ 3, 0.11111, 0.00000]], [ 0.80809, [ 3, -0.11111, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 2.00000, 2.40000, 3.00000, 3.93333, 4.46667, 5.66667])
keys.append([ [ -0.00873, [ 3, -0.66667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.00873, [ 3, -0.13333, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.81681, [ 3, -0.20000, 0.00000], [ 3, 0.31111, 0.00000]], [ -0.29496, [ 3, -0.31111, -0.16771], [ 3, 0.17778, 0.09583]], [ -0.02618, [ 3, -0.17778, 0.00000], [ 3, 0.40000, 0.00000]], [ -0.23562, [ 3, -0.40000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 2.00000, 2.40000, 3.46667, 3.93333, 4.46667, 4.80000, 5.66667])
keys.append([ [ 0.95120, [ 3, -0.66667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.95120, [ 3, -0.13333, 0.00000], [ 3, 0.35556, 0.00000]], [ 1.82911, [ 3, -0.35556, -0.26306], [ 3, 0.15556, 0.11509]], [ 2.08567, [ 3, -0.15556, 0.00000], [ 3, 0.17778, 0.00000]], [ 0.43808, [ 3, -0.17778, 0.40384], [ 3, 0.11111, -0.25240]], [ 0.11694, [ 3, -0.11111, 0.04056], [ 3, 0.28889, -0.10546]], [ 0.00000, [ 3, -0.28889, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 2.00000, 2.40000, 3.00000, 3.46667, 3.93333, 4.46667, 4.80000, 5.66667])
keys.append([ [ 1.28107, [ 3, -0.66667, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.28107, [ 3, -0.13333, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.94073, [ 3, -0.20000, 0.15119], [ 3, 0.15556, -0.11759]], [ 0.47473, [ 3, -0.15556, 0.15039], [ 3, 0.15556, -0.15039]], [ 0.03840, [ 3, -0.15556, 0.00000], [ 3, 0.17778, 0.00000]], [ 0.95993, [ 3, -0.17778, -0.20106], [ 3, 0.11111, 0.12566]], [ 1.08559, [ 3, -0.11111, 0.00000], [ 3, 0.28889, 0.00000]], [ 0.20246, [ 3, -0.28889, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 2.40000, 3.46667, 3.93333, 4.46667, 4.80000, 5.33333])
keys.append([ [ -1.82387, [ 3, -0.80000, 0.00000], [ 3, 0.35556, 0.00000]], [ -1.39277, [ 3, -0.35556, -0.33389], [ 3, 0.15556, 0.14608]], [ -0.38397, [ 3, -0.15556, -0.34317], [ 3, 0.17778, 0.39219]], [ 0.81332, [ 3, -0.17778, 0.00000], [ 3, 0.11111, 0.00000]], [ -0.43982, [ 3, -0.11111, 0.33810], [ 3, 0.17778, -0.54096]], [ -1.82387, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  motion = ALProxy("ALMotion")
  moveId = motion.post.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  pass
