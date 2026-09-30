import metrics

def eval():
    ##data = metrics.main()
    data = {'Throughput': {'Upload': 949122888, 'Download': 942758328}, '1.1.1.1': {'Tested IP': '1.1.1.1', 'Hops': 18, 'Bytes Sent 1': '32', 'Time 1': '24', 
    'Bytes Sent 2': '32', 'Time 2': '25', 'Loss Percent': '0', 'Min': '24', 'Max': '25', 'Avg': '24', 'Jitter': 0.5}, 
    '8.8.8.8': {'Tested IP': '8.8.8.8', 'Hops': 16, 'Bytes Sent 1': '32', 'Time 1': '23', 'Bytes Sent 2': '32', 
    'Time 2': '23', 'Loss Percent': '0', 'Min': '23', 'Max': '23', 'Avg': '23', 'Jitter': 0.0}}

    upload = input("What is your ISPs advertised upload speed?(Mbps):\n")
    download = input("What is your ISps advertised download speed?(Mbps):\n")
    tested_upload = data["Throughput"]["Upload"] / 1000000
    tested_download = data["Throughput"]["Download"] / 1000000

    if(int(upload) < tested_upload):
        print("Your upload speed is below advertised.\n")
        print("The speed found while testing was " + str(tested_upload) + " while you the advertised upload was " + upload)
    else:
        print("Your upload speed is above advertised.\n")
        print("The speed found while testing was " + str(tested_upload) + " while you the advertised upload was " + upload)
    if(int(download) < tested_download):
        print("Your upload speed is below advertised.\n")
        print("The speed found while testing was " + str(tested_download) + " while you the advertised download was " + download)
    else:
        print("Your upload speed is above advertised.\n")
        print("The speed found while testing was " + str(tested_download) + " while you the advertised download was " + download)

    data.pop("Throughput")

    for ip in data:
        currvalues = data[ip]
        if(int(currvalues["Avg"]) < 50):
            print("You have very low latency!")
        elif(50 < int(currvalues["Avg"]) < 150):
            print("Your latency is average, it could be imporved but, isnt a big deal")
        else:
            print("You have very bad latency!")

        if(int(currvalues["Jitter"]) < 10):
            print("You have very low jitter")
        elif(10 < int(currvalues["Jitter"]) < 30):
            print("You have an average amount  of jitter")
        else:
            print("You have very bad jitter")

        if(int(currvalues["Loss Percent"]) < 1):
            print("You have very low packet loss")
        elif(1 < int(currvalues["Loss Percent"]) < 2.5):
            print("You have an average amount  of packet loss")
        else:
            print("You have very bad packet loss")

eval()