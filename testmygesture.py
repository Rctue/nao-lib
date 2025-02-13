import nao_nocv_2_1 as nao

nao.InitProxy('192.168.0.112')

nao.InitPose()

nao.RunMovement('mynewgesture.py')
nao.sleep(1)
nao.Say("It is time to go to the dentist")


nao.Crouch()
