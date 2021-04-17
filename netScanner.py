#!/usr/bin/env python

import subprocess


class color:
    BLUE = '\033[96m'
    DEFAULT = '\033[0m'
    GREEN = '\033[92m'
    RED = '\033[91m'


###############packet : arp request directed to broadcast MAC asking for IP########################
def scanner(ip):
    arpRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpRequestBroadcastComb = broadcast / arpRequest  # new packet combines both arpRequest & Broadcast

    ########################Sends packet & Recieves response############################################
    answer = scapy.srp(arpRequestBroadcastComb, timeout=1, verbose=False)[0]
    print("\n<==============================[ Results ]==============================>\n")
    print("   IP\t\t\t\tMAC\n+-------------------------------------------------------+")
    for element in answer:
        print(color.GREEN + "  IP: " + color.DEFAULT + element[1].psrc + "  " + color.RED + "MAC: " + color.DEFAULT +
              element[1].hwsrc)

        print("+-------------------------------------------------------+")
    print("\n<=======================================================================>\n")
def updater():
    subprocess.call("sudo apt update", shell=True);
    subprocess.call("sudo apt install python3-pip", shell=True);
    subprocess.call("sudo apt install scapy", shell=True);
    subprocess.call("sudo pip install --pre scapy", shell=True);


####################################MAIN########################################

print(color.RED + """\
888  ,d8   ,d8PPPP 888888888 88888888  doooooo ,8b.     888  ,d8 888  ,d8   ,d8PPPP   ,dbPPPp 
888_dPY8   d88ooo     '88d   88ooooPp  d88     88'8o    888_dPY8 888_dPY8   d88ooo    d88ooP' 
8888' 88 ,88'        '888           d8 d88     88PPY8.  8888' 88 8888' 88 ,88'      ,88' P'   
Y8P   Y8 88bdPPP   '88p      8888888P  d888888 8b   `Y' Y8P   Y8 Y8P   Y8 88bdPPP   88  do  
""" + color.DEFAULT)

print(color.BLUE + "[*] Installing/Updating scapy.." + color.DEFAULT)
updater();
import scapy.all as scapy
print("")
print(color.BLUE + "[*] Running 'route -n' for you.." + color.DEFAULT)
subprocess.call("sudo route -n", shell=True);
print("")
scanner(input(color.BLUE + "Give ip or range to scan: " + color.DEFAULT))
print("")

