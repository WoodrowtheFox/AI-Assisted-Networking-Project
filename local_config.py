from socket import *
import requests
import subprocess

def get_public_IP():
    IP = requests.get('https://ifconfig.me')
    return IP.text

def get_ipconfig_data():
    gateway = subprocess.run("ipconfig /all", capture_output=True, text=True)
    with open("gateway.txt", "w") as file:
        file.write(gateway.stdout)
    #Getting the IPv4 of the Default Gateway
    gateway = open("gateway.txt", "r")
    gatewaydata = {}
    in_block = 0
    ip_next = 0
    for line in gateway:
        currline = line.split()
        if(in_block == 1):
            if(ip_next == 1):
                gatewaydata["Gateway"] = currline
                ip_next = 0;
                in_block = 0;
            if("Gateway" in currline):
                ip_next = 1;
            if("Gateway" in currline):
                gatewaydata["Gateway"] = currline
            if("Media" in currline and "State" in currline):
                if("disconnected" in currline):
                    gatewaydata["Interface"] = "Wifi"
                else:
                    gatewaydata["Interface"] = "Ethernet"
                in_block = 0;
        if("Wireless" in currline and "Wi-Fi:" in currline):
            in_block = 1;
        if("Ethernet" in currline and "2:" in currline):
            in_block = 1;
    return gatewaydata;


print(get_ipconfig_data())