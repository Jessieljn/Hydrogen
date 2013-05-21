import socket


def jitter(addr, port = 9555, bhvName = 'Name', boxName = 'Name', startFrame = 0, endFrame = -1, joints = []):
    data = ""
    data += "in=/home/nao/behaviors/" + bhvName + "/behavior.xar|"
    data += "out=/home/nao/behaviors/jitter/behavior.xar|"
    data += "box=" + boxName + "|"
    data += "start=" + startFrame + "|"
    data += "end=" + endFrame + "|"

    for j in joints:
        data += "joint=" + j[0] + "," + j[1] + "," + j[2] + "|"
    #END for

    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sck.connect((addr, port))
        sck.send(data)
        #Disconnect Signal
        sck.send("\0")
    #END try
    finally:
        sck.close()
    #END finally
#END jitter

