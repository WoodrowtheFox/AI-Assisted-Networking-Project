def eval(metric):
    eval_data = {}
    upload = metric["Expected Upload"]
    download = metric["Expected Download"]
    metric.pop("Expected Upload")
    metric.pop("Expected Download")
    tested_upload = metric["Throughput"]["Upload"] / 1000000
    tested_download = metric["Throughput"]["Download"] / 1000000

    if(int(upload) < tested_upload):
        eval_data["Upload"] = ["Your upload speed is below advertised.", 
        "The speed found while testing was " + str(tested_upload) + " while you the advertised upload was " + upload]
    else:
        eval_data["Upload"] = ["Your upload speed is above advertised.", 
        "The speed found while testing was " + str(tested_upload) + " while you the advertised upload was " + upload]
    if(int(download) < tested_download):
        eval_data["Download"] = ["Your upload speed is below advertised.", 
        "The speed found while testing was " + str(tested_download) + " while you the advertised download was " + download]
    else:
        eval_data["Download"] = ["Your upload speed is above advertised.",
        "The speed found while testing was " + str(tested_download) + " while you the advertised download was " + download]
    eval_data["Throughput"] = metric["Throughput"]
    metric.pop("Throughput")

    for ip in metric:
        currvalues = metric[ip]
        if(int(currvalues["Avg"]) < 50):
            eval_data["Latency"] = "You have very low latency!"
        elif(50 < int(currvalues["Avg"]) < 150):
            eval_data["Latency"] = "Your latency is average, it could be imporved but, isnt a big deal"
        else:
            eval_data["Latency"] = "You have very bad latency.."

        if(int(currvalues["Jitter"]) < 10):
            eval_data["Jitter"] = "You have very low jitter!"
        elif(10 < int(currvalues["Jitter"]) < 30):
            eval_data["Jitter"] = "You have an average amount  of jitter"
        else:
            eval_data["Jitter"] = "You have very bad jitter.."

        if(int(currvalues["Loss Percent"]) < 1):
            eval_data["Loss"] = "You have very low packet loss!"
        elif(1 < int(currvalues["Loss Percent"]) < 2.5):
            eval_data["Loss"] = "You have an average amount of packet loss"
        else:
            eval_data["Loss"] = "You have very bad packet loss..."

    return eval_data