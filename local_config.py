from socket import *
import requests
import subprocess

def get_public_IP():
    IP = requests.get('https://ifconfig.me')
    return IP.text

def get_ipconfig_data():
    configfiledata = {}
    dns_data = {}
    configfiledata["Public IP"] = get_public_IP()
    configfile = subprocess.run("ipconfig /all", capture_output=True, text=True)
    with open("configfile.txt", "w") as file:
        file.write(configfile.stdout)
    #Getting the IPv4 of the Default Gateway
    configfile = open("configfile.txt", "r")
    in_block = 0
    ip_next = 0
    dns = 0
    for line in configfile:
        currline = line.split()
        if(in_block == 1):
            if(ip_next == 1):
                for item in currline:
                    configfiledata["Gateway"] =  item
                ip_next = 0
                in_block = 0
            if("Gateway" in currline):
                ip_next = 1
            if("Media" in currline and "State" in currline):
                if("disconnected" in currline):
                    configfiledata["Interface"] = "Wifi"
                else:
                    configfiledata["Interface"] = "Ethernet"
                in_block = 0
        if("Wireless" in currline and "Wi-Fi:" in currline):
            in_block = 1
        if("Ethernet" in currline and "2:" in currline):
            in_block = 1
        if("IPv4" in currline):
            currline = [word.replace("(Preferred)", "") for word in currline]
            for item in currline:
                configfiledata["Private IP"] = item
        if(dns > 0 and "NetBIOS" not in currline):
            dns += 1
            for item in currline:
                dns_data[dns] = item
        if("NetBIOS" in currline):
            dns = 0
        if("DNS" in currline and "Servers" in currline):
            dns = 1
            for item in currline:
                dns_data[dns] = item
    configfiledata["DNS"] = dns_data
    return configfiledata


print(get_ipconfig_data())