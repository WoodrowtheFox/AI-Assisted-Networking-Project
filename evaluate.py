def eval(metric, local):
    eval_data = {}
    upload = metric["Expected Upload"]
    download = metric["Expected Download"]
    metric.pop("Expected Upload")
    metric.pop("Expected Download")
    tested_upload = metric["Throughput"]["Upload"] / 1000000
    tested_download = metric["Throughput"]["Download"] / 1000000

    if(int(upload) > tested_upload):
        eval_data["Upload"] = ["Your upload speed is below advertised.", 
        "The speed found while testing was " + str(tested_upload) + " while your the advertised upload was " + upload]
    else:
        eval_data["Upload"] = ["Your upload speed is above advertised.", 
        "The speed found while testing was " + str(tested_upload) + " while your the advertised upload was " + upload]
    if(int(download) > tested_download):
        eval_data["Download"] = ["Your download speed is below advertised.", 
        "The speed found while testing was " + str(tested_download) + " while your the advertised download was " + download]
    else:
        eval_data["Download"] = ["Your download speed is above advertised.",
        "The speed found while testing was " + str(tested_download) + " while your the advertised download was " + download]
    eval_data["Throughput"] = metric["Throughput"]
    metric.pop("Throughput")

    for ip in metric:
        ipresults = {}
        currvalues = metric[ip]
        if(int(currvalues["Avg"]) <= 50):
            ipresults["Latency"] = "You have very low latency!"
            ipresults["Limprove"] = "There is nothing for you to do!"
        elif(50 < int(currvalues["Avg"]) <= 150):
            ipresults["Latency"] = "You have an average amount of latency."
            ipresults["Limprove"] = "There is no need to look into it."
        else:
            ipresults["Latency"] = "You have very bad latency.."
            ipresults["Limprove"] = "This is likely due to distance, if possible switch to using a server closer to you."

        if(int(currvalues["Jitter"]) <= 10):
            ipresults["Jitter"] = "You have very low jitter!"
            ipresults["Jimprove"] = "There is nothing for you to do!"
        elif(10 < int(currvalues["Jitter"]) <= 30):
            ipresults["Jitter"] = "You have an average amount of jitter."
            ipresults["Jimprove"] = "There is no need to look into it."
        else:
            ipresults["Jitter"] = "You have very bad jitter.."
            if(local['NON-DNS']["Interface"] != "Ethernet"):
                ipresults["Jimprove"] = "Try switching to using a wired connection instead of Wi-Fi."
            else:
                ipresults["Jimprove"] = "Try reduce the congestion on your network."

        if(int(currvalues["Loss Percent"]) <= 1):
            ipresults["Loss"] = "You have very low packet loss!"
            ipresults["Pimprove"] = "There is nothing for you to do!"
        elif(1 < int(currvalues["Loss Percent"]) <= 2.5):
            ipresults["Loss"] = "You have an average amount of packet loss."
            ipresults["Pimprove"] = "There is no need to look into it."
        else:
            ipresults["Loss"] = "You have very bad packet loss..."
            if(local['NON-DNS']["Interface"] != "Ethernet"):
                ipresults["Pimprove"] = "Try switching to using a wired connection instead of Wi-Fi."
            else:
                ipresults["Pimprove"] = "Try reducing the number of applications you have running in the background."
        eval_data[ip] = ipresults

    return eval_data