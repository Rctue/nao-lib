# nao-lib
nao-lib contains a set of Python files for interfacing with the Nao robot.

## Description
* nao.py contains a set of frequently used routines that build on Aldebaran's naoqi.py for interfacing with the Nao robot.
* nao_nocv.py is the same without the routines that use openCV
* /gestures contains some gestures for the robot, which are made with the export to python function of Choregraphe
* /led contains led patterns for the basic emotions (according to Ekman)
* /dialogs contains dialog scripts for the dialog manager with support of gestures and speech
* /modules is an outdated attempt to do the same

The opencv version uses the haarcascade file for face detection

## Under development
* nao2.py is a rewrite of nao.py which separates the broker and proxies from the interface and adds event functionality.
* NaoScript.py contains the scripting routines.
* Monitor.py contains tools to record the state of the robot.
