#Port Scanner
import socket
import sys

def port_scan():
    """
    Scan a port on the global variable `host`
    """
    try:
        target = input("Please enter target IP: ")
        min_port = int(input("Please enter minimum port number: ")) #min 1
        max_port = int(input("Please enter maximum port number: ")) #max 65,535
        for port in range(min_port,max_port):
            s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        print("Exiting Program")
        sys.exit()
    except AttributeError:
        pass

port_scan()
