from lib.server import Server
import sys

if __name__ == "__main__":
    # just port number can enter when application starting
    if len(sys.argv) <= 1:
        port = 5000 # default port number
        if len(sys.argv) == 1: # 
            try:
                port = int(sys.argv[0])
            except:
                pass
        s1 = Server(port)
        # if do not given port address it selected defaultly as 5000
        s1.run()  # run server
    else:
        print("There are error on arguments . . .")
