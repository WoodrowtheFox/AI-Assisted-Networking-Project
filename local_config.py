from socket import *
import requests
import subprocess
import time
import random

def get_IP():
    IP = requests.get('https://ifconfig.me')
    return IP.text

def get_gateway():
    gateway = subprocess.run("ipconfig /all", capture_output=True, text=True)
    with open("gateway.txt", "w") as file:
        file.write(gateway.stdout)
    #Getting the IPv4 of the Default Gateway
    gateway = open("gateway.txt")
    gaetwaydata = {};
    in_block = 0;
    is_next = 0;
    for line in gateway:
        currline = line.split();
        if(in_block == 1):
            if(is_next == 1):
                gateway["IPv4"] = currline
            if("Default" in currline):
                is_next == 1;
        if("Wireless" in currline):
            in_block = 1;
    return gaetwaydata;

print(get_IP())
print(get_gateway())
