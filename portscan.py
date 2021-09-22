import socket
import argparse
import time

parser = argparse.ArgumentParser(description="Network port scanner written in Python!")
parser.add_argument("ip", help="Scan the entered ip address and see for open ports")
args = parser.parse_args()

def getConsoleArgument():
    if args.ip == "localhost":
        target = "127.0.0.1"
        return target
    
    target = args.ip
    return target
    
print("Scanning " + str(getConsoleArgument()))

startTime = time.time()

for portNumber in range(1, 65536):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portConnection = sock.connect_ex((getConsoleArgument(), portNumber))
    if (portConnection == 0):
        print("Port:%d OPEN" % (portNumber,))
        sock.close()

print("Time taken: ", time.time() - startTime)