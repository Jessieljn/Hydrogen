import sys
import naoqi
from Definitions import DEFAULT_IP
from Definitions import DEFAULT_PORT
from Definitions import VIDEO_SUBSCRIBE_NAME


##
# Controller.py
#
# Retrieves the user provided IP Address and Port, or gets the default settings.
##
def main():
    IP = DEFAULT_IP
    port = DEFAULT_PORT
    if len(sys.argv) == 2:
        IP = sys.argv[1]
    #END if
    elif len(sys.argv) == 3:
        IP = sys.argv[1]
        port = int(sys.argv[2])
    #END elif
    else:
        sys.exit("Usage: [IP] [port]")
    #END else

    print IP
    print port

    videoProxy = naoqi.ALProxy("ALVideoDevice", IP, port)
    nameID = videoProxy.subscribe(VIDEO_SUBSCRIBE_NAME, 0, 11, 15)
    for i in range(10):
        frame = videoProxy.getImageRemote(nameID)
        data = frame[6]
        videoProxy.releaseImage(nameID)
    #END for
    videoProxy.unsubscribe(nameID)
#END main()

    print "Retrieved the video device."

if __name__ == "__main__":
    main()
#END if