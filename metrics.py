import subprocess

def ping(tries, ip):
    results = subprocess.run(["ping", "-n", tries, ip], capture_output=True, text=True)
    with open("pingresults.txt", "w") as file:
            file.write(results.stdout)

def parse_ping(tries, IPS):
    metricdata = {}
    for ip in IPS:
        ping(tries, ip)
        currip = {}
        currip["Tested IP"] = ip
        pingfile = open("pingresults.txt", "r")
        i = 0
        for line in pingfile:
            oldline = line
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
            if("Packets:" in currline):
                next = 2
                down = 0
                for item in currline:
                    if(next == 0):
                        item = item.replace("ms", "")
                        currip["Loss"] = item
                    if(down == 1):
                        next += -1
                    if(item == "Lost"):
                        next += -1
                        down += 1
            if("Minimum" in currline):
                next = 0
                for item in currline:
                    if(next == 2):
                        item = item.replace("ms", "")
                        currip["Min"] = item
                    if(next == 5):
                        item = item.replace("ms", "")
                        currip["Max"] = item
                    if(next == 8):
                        item = item.replace("ms", "")
                        currip["Avg"] = item
                    next += 1
        metricdata[ip] = currip
    print(metricdata)

def main():
    ips = []
    tries = input("How many ping tries would you like to do?\n")
    i = 1
    exit = 0
    while(exit == 0):
        ip = input("Enter a test IP, if there are no more ips enter(EXIT):\n")
        if(ip == "EXIT"):
             exit = 1
        else:
             ips.append(ip)
        i += 1
    parse_ping(tries, ips)

main()