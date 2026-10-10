import subprocess
import math
import json

def get_route(ip):
    hops = 0
    in_block = 0
    route = subprocess.run(["tracert", "-h", "30", ip], capture_output=True, text=True)
    with open("route.txt", "w") as file:
        file.write(route.stdout)
    hopfile = open("route.txt", "r")

    for line in hopfile:
        currline = line.split()
        if(currline == []):
            in_block = 0
        if(in_block == 1):
            if("Request" not in currline):
                hops += 1
        if(not (currline == []) and currline[0] == "1"):
            in_block = 1
            if("Request" not in currline):
                hops += 1
    return hops
    

def throughput():
    throughput = {}
    result = subprocess.run(["C:\\Projects\\Speedtest\\speedtest.exe", "-f", "json"], capture_output=True, text=True)

    data = json.loads(result.stdout)
    download = data["download"]["bandwidth"] * 8 
    upload = data["upload"]["bandwidth"] * 8

    throughput["Upload"] = upload
    throughput["Download"] = download
    return throughput

def ping(tries, ip):
    results = subprocess.run(["ping", "-n", tries, ip], capture_output=True, text=True)
    with open("pingresults.txt", "w") as file:
            file.write(results.stdout)

def parse_ping(tries, IPS):
    metricdata = {}
    metricdata["Throughput"] = throughput()
    for ip in IPS:
        jitter = []
        ping(tries, ip)
        currip = {}
        currip["Tries"] = tries
        currip["Tested IP"] = ip
        currip["Hops"] = get_route(ip)
        pingfile = open("pingresults.txt", "r")
        i = 0
        for line in pingfile:
            currline = line.split()
            if("Reply" in currline):
                 i += 1
                 for item in currline:
                    if(item.__contains__("bytes=")):
                        currip["Bytes Sent " + str(i)] = item.replace("bytes=", "")
                    if(item.__contains__("time=")):
                        item = item.replace("time=", "")
                        item = item.replace("ms", "")
                        currip["Time " + str(i)] = item
                        jitter.append(item)
            if("Packets:" in currline):
                next = 3
                down = 0
                for item in currline:
                    if(next == 0):
                        item = item.replace("(", "")
                        item = item.replace("%", "")
                        currip["Loss Percent"] = item
                    if(down == 1):
                        next += -1
                    if(item == "Lost"):
                        next += -1
                        down += 1
            if("Minimum" in currline):
                next = 0
                for item in currline:
                    if(next == 2):
                        item = item.replace("ms,", "")
                        currip["Min"] = item
                    if(next == 5):
                        item = item.replace("ms,", "")
                        currip["Max"] = item
                    if(next == 8):
                        item = item.replace("ms", "")
                        currip["Avg"] = item
                    next += 1
        j = 0
        for time in jitter:
            j += int(time)
        if(len(jitter) == 0):
            avg_time = 0
            size = 1
        else:
            avg_time = j/len(jitter)
            size = len(jitter)
        sum_time = 0
        for time in jitter:
            sum_time += ((int(time) - avg_time) * (int(time) - avg_time))
        real_jitter = math.sqrt((1/size) * sum_time)
        currip["Jitter"] = real_jitter
        metricdata[ip] = currip
    return metricdata

def main():
    upload = input("What is your ISPs advertised upload speed?(Mbps):\n")
    download = input("What is your ISPs advertised download speed?(Mbps):\n")
    ips = []
    tries = input("How many ping tries would you like to do?\n")
    exit = 0
    while(exit == 0):
        ip = input("Enter a test IP, if there are no more ips enter(EXIT):\n")
        if(ip == "EXIT"):
             exit = 1
        else:
             ips.append(ip)
    metrics = parse_ping(tries, ips)
    metrics["Expected Upload"] = upload
    metrics["Expected Download"] = download
    return metrics