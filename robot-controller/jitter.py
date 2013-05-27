import socket


def jitter(addr, bhvName, boxName, startFrame = 0, endFrame = -1, joints = []):
    data = ""
    data += "in=/home/nao/behaviors/" + bhvName + "/behavior.xar|"
    data += "out=/home/nao/behaviors/jitter/behavior.xar|"
    data += "box=" + boxName + "|"
    data += "start=" + str(startFrame) + "|"
    data += "end=" + str(endFrame) + "|"
    for j in joints:
        data += "joint=" + j[0] + "," + str(j[1]) + "," + str(j[2]) + "|"
    #END for

    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sck.connect((addr, 9555))
        sck.send(data)
        # Disconnect Signal
        sck.send("\0")
    finally:
        sck.close()
#END jitter


if __name__ == "__main__":
    jitter(addr = "140.193.228.26", bhvName = "rightHandPointing", boxName = "PointDirectionR", joints = [["RWristYaw",
                                                                                                           -50, 50]])
