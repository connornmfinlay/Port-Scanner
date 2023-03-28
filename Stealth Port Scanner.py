#Port Scanner
import socket
import sys

host = input("Please enter target IP: ")
min_port = int(input("Please enter minimum port number: "))
max_port = int(input("Please enter maximum port number: "))

def port_scan(port):
    """
    Scan a port on the global variable `host`
    """
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        with print_lock:
            print(f"{GRAY}{host:15}:{port:5} is closed  {RESET}", end='\r')
    else:
        with print_lock:
            print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")
    finally:
        s.close()


# try:
#     for port in range(min_port,max_port):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         print("Socket successfully created")
#         socket.setdefaulttimeout(2)

#         result = s.connect_ex((host,port))
#         if result ==0:
#             print("Port {} is open".format(port))
#         s.close()
         
# except KeyboardInterrupt:
#         print("\n Exiting Program !!!!")
#         sys.exit()
# except socket.gaierror:
#         print("\n Hostname Could Not Be Resolved !!!!")
#         sys.exit()
# except socket.error:
#         print("\ Server not responding !!!!")
#         sys.exit()