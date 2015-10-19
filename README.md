# nao-lib
master commit of nao-lib

# Description
nao.py contains a set of frequently used routines that build on Aldebaran's naoqi.py for interfacing with the Nao robot.
nao_nocv.py is the same without the routines that use openCV
/gestures contains some gestures for the robot, which are made with the export to python function of Choregraphe
/led contains led patterns for the basic emotions (according to Ekman)
/dialogs contains dialog scripts for the dialog manager with support of gestures and speech
/modules is an outdated attempt to do the same

The opencv version uses the haarcascade file for face detection
The headpose estimation uses a neural network, the parameters of which are contained in PythonNN.mat
