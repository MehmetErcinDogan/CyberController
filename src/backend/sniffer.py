import socket
import pyuac
import os

def main():
    try:
        s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.nthons(3))
        while True:
            print(s.recvfrom(65565))
    except Exception as e:
        print(e)
    finally:    
        os.system("pause>0")

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main()  # Already an admin here.

# SCAPY araştır