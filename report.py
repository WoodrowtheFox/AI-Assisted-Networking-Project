import matplotlib.pyplot as plt
import evaluate as evaluate
import local_config as local_config
import metrics as metrics

def generate_report():
    local = local_config.get_ipconfig_data()
    metric = metrics.main()
    eval = evaluate.eval(metric)
    
    IPs = []
    Hops = []
    Bytes = []
    Time = []
    Loss_Percent = []
    Avg = []
    Jitter = []

    for key in metric.keys():
        IPs.append(key)
    for ip in IPs:
        tries = int(metric[ip]["Tries"])
        i = 0
        while(tries > i):
            i += 1
            Bytes.append(metric[ip][f"Bytes Sent {i}"])
            Time.append(metric[ip][f"Time {i}"])
        Loss_Percent.append(int(metric[ip]["Loss Percent"]))
        Hops.append(int(metric[ip]["Hops"]))
        Avg.append(int(metric[ip]["Avg"]))
        Jitter.append(metric[ip]["Jitter"])

    plt.figure(figsize=(12, 6))
    plt.bar(IPs, Avg)
    plt.title("Latency by IP")
    plt.xlabel("Target")
    plt.ylabel("Latency (ms)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("Latency.png")
    plt.close()

    plt.figure(figsize=(12, 6))
    plt.bar(IPs, Jitter)
    plt.title("Jitter by IP")
    plt.xlabel("Target")
    plt.ylabel("Jitter (ms)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("Jitter.png")
    plt.close()

    plt.figure(figsize=(12, 6))
    plt.bar(IPs, Hops)
    plt.title("Hops by IP")
    plt.xlabel("Target")
    plt.ylabel("Hops")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("Hops.png")
    plt.close()

    plt.figure(figsize=(12, 6))
    plt.bar(IPs, Loss_Percent)
    plt.title("Packet Loss by IP")
    plt.xlabel("Target")
    plt.ylabel("Packets")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("Packet.png")
    plt.close()

    upload = eval['Throughput']["Upload"]/1000000 
    download = eval['Throughput']["Download"]/1000000
    fig, ax = plt.subplots(figsize=(5, 2))
    ax.axis('tight')
    ax.axis('off')

    throughput = ax.table(
        cellText=[[upload, download]],
        colLabels=["Upload(Mbps)", "Download(Mbps)"],
        cellLoc='center',
        loc='center'
    )

    plt.savefig("Throughput.png")
    plt.close()

    with open("report.txt", "w") as file:
            file.write("Report:\n")
            file.write(f"Public IP: {local['Public IP']}\n")
            file.write(f"Interface: {local['NON-DNS']["Interface"]}\n")
            file.write(f"Private IP: {local['NON-DNS']["Private IP"]}\n")
            file.write(f"Gateway: {local['NON-DNS']["Gateway"]}\n")
            file.write("DNS:\n")
            for key in local['DNS'].keys():
                 file.write(str(key) + "\n")
                 file.write(local['DNS'][key] + "\n")
            file.write("Evaluation:\n")
            file.write(f"Upload: {eval['Upload'][0]}\n")
            file.write(f"{eval['Upload'][1]}\n")
            file.write(f"Download: {eval['Download'][0]}\n")
            file.write(f"{eval['Download'][1]}\n")
            file.write(f"Latency: {eval['Latency']}\n")
            file.write(f"Jitter: {eval['Jitter']}\n")
            file.write(f"Loss: {eval['Loss']}\n")
    print("Report is done!")
    

generate_report()