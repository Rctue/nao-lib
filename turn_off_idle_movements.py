import nao_nocv_2_1 as nao
nao.InitProxy("192.168.0.115")
#amp=nao.ConnectProxy('ALAutonomousMoves')#equivalent to
amp=nao.naoqi.ALProxy('ALAutonomousMoves',"192.168.0.115",9559)

print "Expressive listening enabled is", amp.getExpressiveListeningEnabled()
# The chain name ["Body", "Legs", "Arm", "LArm", "RArm", "Head"].
chain_names =["Body", "Legs", "Arms", "LArm", "RArm", "Head"]
for n in chain_names:
    print "Breath enabled for", n , nao.motionProxy.getBreathEnabled(n) 
    print "IdlePosture enabled for", n , nao.motionProxy.getIdlePostureEnabled(n)


amp.setExpressiveListeningEnabled(False)
nao.motionProxy.setBreathEnabled("Body",False)
nao.motionProxy.setIdlePostureEnabled("Body",False)
nao.Say("I'm done.")
