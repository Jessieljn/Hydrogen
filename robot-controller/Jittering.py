import time
from naoqi import ALProxy

##
# Jittering.py
#
# Test for changing values on the fly.
##

def main(IP):
    PORT = 9559

    try:
        motionProxy = ALProxy("ALMotion", IP, PORT)
    except Exception.e:
        print "Error."

    motionProxy.setStiffness("Head", 1.0)

    names = "HeadYaw"
    changes = 0.5
    fractionMaxSpeed = 0.05
    motionProxy.changeAngles(names, changes, fractionMaxSpeed)

    time.sleep(2)

    motionProxy.setStiffness("Head", 0)
