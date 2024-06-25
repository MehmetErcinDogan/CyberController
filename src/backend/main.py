from lib.server import Server
import pyuac
import sys

def main():    
    sys.argv.pop(0)  # for removing source code file path
    # just port number can enter when application starting
    if len(sys.argv) <= 1:
        port = 5000  # default port number
        if len(sys.argv) == 1:  # if has one argument
            try:
                port = int(sys.argv[0].strip())
                # try to convert if there are not any problem at given value
                # assign value to current port value which for going to use run
            except:
                # if there are error program continues with default value
                pass
        s1 = Server(port)
        # if do not given port address it selected defaultly as 5000
        s1.run()  # run server
    else:
        print("There are error on arguments . . .")


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()  # Already an admin here.
