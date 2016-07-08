import nao_nocv as nao

IP='192.168.0.115'
#IP='marvin.local' #use this for the real robot

#connect to robot
nao.InitProxy(IP, [1, 3, 4, 6, 7, 10]) #default is [0] for all proxies, [1,3,4,6,7,10]  are the basic proxies that work with the simulated Nao

#Stiffen the motors and stand up
nao.InitPose()

#do your stuff
nao.Say("Hello I am Marvin" )


#Go back to resting pose and remove stiffness
nao.Crouch()
