from naoqi import *
import time

IP='127.0.0.1'
PORT = 58596 #look up in choregraphe settings for simulated robot

broker = ALBroker("pythonBroker",'127.0.0.1',9999,IP,PORT)
memproxy = ALProxy('ALMemory')

# create python module
class myModule(ALModule):
  """ Mandatory docstring.
      comment needed to create a new python module
  """

  def myCallback(self, key, value, message):
    """ Mandatory docstring.
        comment needed to create a bound method
    """
    print key, value, message
    pass


try:

  pythonModule = myModule("pythonModule")
  memproxy = ALProxy("ALMemory")
  memproxy.subscribeToEvent("Dialog/LastInput","pythonModule", "myCallback") #  event is case sensitive !

except Exception as e:
  print "error"
  print e
  exit(1)


count = 0
while count<200:
    time.sleep(0.1)
    count+=1

    
