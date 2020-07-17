import socket
import subprocess
import sys
from datetime import datetime

def clear():
    subprocess.call('clear', shell=True)
    
    
clear()

remoteServer = input("Remote host: ")
remoteServerIp = socket.gethostbyname(remoteServer)

start_time = datetime.now()

open_ports = []

stop = False

try:
    for port in range(79, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)

        clear() #So text does not fill whole screen
        print("Remote host: {} - {}".format(remoteServer, remoteServerIp))
        if not stop:
            print("\n- Scanning: Port {}\n".format(port))
            print("|--------------------|")
        else:
            print("\n- Stopped scanning. Reached port {}\n".format(port))
            print("|--------------------|")
            input("\nPress Enter to exit.")
            sys.exit()
        for open_port in open_ports:
            print("|Port {}: open".format(open_port))

  

        if not sock.connect_ex((remoteServerIp, port)):
            open_ports.append(port)
            sock.close()
        else:
            sock.close()

except KeyboardInterrupt:
    stop = True

except socket.gaierror:
    print("Hostname could not be found")
    sys.exit()

except socket.error:
    print("Couldn't connect to the server")
    sys.exit()

end_time= datetime.now()
scan_duration = start_time - end_time

print("Scanning completed in {}".format(scan_duration))
input("\nPress Enter to exit.")

