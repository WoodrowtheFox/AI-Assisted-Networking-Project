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
    dns = 0
    ipnot = 1
    for line in configfile:
        oldline = line
        currline = line.split()
        if(in_block == 1):
            if("IPv4" in currline):
                currline = [word.replace("(Preferred)", "") for word in currline]
                if(ipnot == 1):
                    ipnot = 0
                    for item in currline:
                        currblock["Private IP"] = item
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
            if("Gateway" in currline):
                gatewayfail = ["Default", "Gateway", ".", ":"]
                for item in currline:
                    if(item not in gatewayfail):
                        currblock["Gateway"] =  item
                        configfiledata["NON-DNS"] = currblock
        if("Wireless" in currline and "Wi-Fi:" in currline):
            in_block = 1
            ipnot = 1
            currblock = {}
            currblock["Interface"] = "Wifi"
        if("Ethernet" in currline and "adapter" in currline and oldline.rstrip().endswith(":") and oldline == oldline.lstrip()):
            in_block = 1
            ipnot = 1
            currblock = {}
            currblock["Interface"] = "Ethernet"
    configfiledata["DNS"] = dns_data
    return configfiledata


print(get_ipconfig_data())