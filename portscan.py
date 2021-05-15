import socket
import argparse

parser = argparse.ArgumentParser(description="Network port scanner written in Python!")
parser.add_argument("ip", help="Scan the entered ip address for open ports")
args = parser.parse_args()

def getConsoleArgument():
    if args.ip == "localhost":
        target = "127.0.0.1"
        return target
    
    target = args.ip
    return target

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Scanning " + str(getConsoleArgument()))

def scanner(port):
    try:
        sock.connect((getConsoleArgument(), port))
        return True
    except:
        return False

for portNumber in range(1, 65535):
    if scanner(portNumber):
        print("Port", portNumber, "is open")