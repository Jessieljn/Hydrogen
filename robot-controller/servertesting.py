import socket
import select

if __name__ == "__main__":
    PRINT_HEADER = "[ServerTesting] "
    addrSrv = ("0.0.0.0", 9555)
    sckServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sckServer.bind(addrSrv)
    sckServer.listen(1)
    print PRINT_HEADER, "listening on ", addrSrv
    sckList = [sckServer]
    while True:
        readable, writable, error = select.select(sckList, [], [], 5)
        for sck in readable:
            if sck is sckServer:
                sckClient, addrCli = sckServer.accept()
                sckList.append(sckClient)
                print PRINT_HEADER, "connection from ", addrCli
            else:
                data = sck.recv(2048)
                if data is None or not isinstance(data, str) or (data == "" or data == "\0"):
                    print PRINT_HEADER, "connection closing. . ."
                    sck.close()
                    sckList.remove(sck)
                else:
                    print PRINT_HEADER, "data received ", data
            #end if
        #end for
    #end while
#end __name__
