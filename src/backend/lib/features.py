import socket
import subprocess
from ipaddress import ip_network
from scapy.all import ARP, Ether, srp
from getmac import get_mac_address as gma

def __get_local_ip_and_netmask():
    # Create a socket to connect to the internet to determine the IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Use Google's public DNS server address to determine the local IP
        s.connect(('8.8.8.8', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    
    # Use `ipconfig` on Windows to get the subnet mask
    ifconfig_output = subprocess.check_output("ipconfig", shell=True).decode('latin-1')
    netmask = '255.255.255.0'
    for line in ifconfig_output.split('\n'):
        if ip_address in line:
            index = ifconfig_output.split('\n').index(line)
            netmask_line = ifconfig_output.split('\n')[index + 1].strip()
            if 'Subnet Mask' in netmask_line:
                netmask = netmask_line.split(': ')[1].strip()
                break

    return ip_address, netmask

def __scan_network(ip,ip_range):
    # Create ARP request
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send packet and receive responses
    result = srp(packet, timeout=2, verbose=0)[0]

    # Parse responses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    devices.append({'ip':ip,'mac':gma()})
    return devices

def scan_network(path):
    try:
        ip, netmask = __get_local_ip_and_netmask()
        network_range = str(ip_network(f"{ip}/{netmask}", strict=False))
        print(f"Scanning network range: {network_range}")
        devices = __scan_network(ip,network_range)
        file = open(path,'w')
        for i in devices:
            file.write(str(i)+"\n")
        file.close()
        return devices
    except Exception as e:
        print(f"Error: {str(e)}")
