import sys
import naoqi

DEFAULT_PORT = 9559

##
# main():
##
def main():

    # Get IP and port from command line.
    if len(sys.argv) == 2:
        IP = sys.argv[1]
        port = DEFAULT_PORT
    elif len(sys.argv) == 3:
        IP = sys.argv[1]
        port = int(sys.argv[2])
    else:
        sys.exit("usage: ip [port]")

    print IP
    print port

    videoProxy = naoqi.ALProxy("ALVideoDevice", IP, port)

    nameID = videoProxy.subscribe("controller", 0, 11, 15)

    for i in range(10):
        frame = videoProxy.getImageRemote(nameID)
        data = frame[6]
        videoProxy.releaseImage(nameID)

    videoProxy.unsubscribe(nameID)

    print "got video device"

if __name__ == "__main__":
    main()