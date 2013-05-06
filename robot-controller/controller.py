import sys
import naoqi

DEFAULT_PORT = 9559


def main():

    # Get IP and port from command line.
    if len(sys.argv) == 2:
        IP = sys.argv[1]
        port = DEFAULT_PORT
    #END if
    elif len(sys.argv) == 3:
        IP = sys.argv[1]
        port = int(sys.argv[2])
    #END elif
    else:
        sys.exit("usage: ip [port]")
    #END else

    print IP
    print port

    videoProxy = naoqi.ALProxy("ALVideoDevice", IP, port)

    nameID = videoProxy.subscribe("controller", 0, 11, 15)

    for i in range(10):
        frame = videoProxy.getImageRemote(nameID)
        data = frame[6]
        videoProxy.releaseImage(nameID)
    #END for

    videoProxy.unsubscribe(nameID)
#END main()

    print "got video device"

if __name__ == "__main__":
    main()
#END if
