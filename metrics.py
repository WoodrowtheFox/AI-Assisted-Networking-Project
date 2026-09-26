import subprocess

def ping(tries, ip):
    results = subprocess.run(["ping", "-n", tries, ip], capture_output=True, text=True)
    with open("pingresults.txt", "w") as file:
            file.write(results.stdout)

def parse_ping(tries, IPS):
      metricdata = {}
      for ip in IPS:
        ping(tries, ip)
        file = open("pingresults.txt", "r")

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