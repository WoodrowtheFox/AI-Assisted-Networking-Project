import matplotlib.pyplot as plt
import evaluate as evaluate
import local_config as local_config
import metrics as metrics

def generate_report():
    local = local_config.get_ipconfig_data()
    metric = metrics.main()
    eval = evaluate.eval(metric, local)

    IPs = []
    Hops = []
    Loss_Percent = []
    Avg = []
    Jitter = []

    for key in metric.keys():
        IPs.append(key)
    for ip in IPs:
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
    plt.ylabel("Packets Loss (%)")
    plt.ylim(0, 5)
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
            file.write("\n")
            file.write(f"Interface: {local['NON-DNS']["Interface"]}\n")
            file.write("\n")
            file.write(f"Private IP: {local['NON-DNS']["Private IP"]}\n")
            file.write("\n")
            file.write(f"Gateway: {local['NON-DNS']["Gateway"]}\n")
            file.write("\n")
            file.write("DNS:\n")
            for key in local['DNS'].keys():
                 file.write(str(key) + "\n")
                 file.write(local['DNS'][key] + "\n")
            file.write("\n")
            file.write("Evaluation:\n")
            file.write(f"Upload: {eval['Upload'][0]}\n")
            file.write(f"{eval['Upload'][1]}\n")
            file.write("\n")
            file.write(f"Download: {eval['Download'][0]}\n")
            file.write(f"{eval['Download'][1]}\n")
            eval.pop("Upload")
            eval.pop("Download")
            eval.pop("Throughput")
            for ip in eval: 
                file.write("\n")
                file.write(f"IP: {ip}\n")
                file.write(f"Latency: {eval[ip]['Latency']}\n")
                file.write(f"Improvements: {eval[ip]['Limprove']}\n")
                file.write("\n")
                file.write(f"Jitter: {eval[ip]['Jitter']}\n")
                file.write(f"Improvements: {eval[ip]['Jimprove']}\n")
                file.write("\n")
                file.write(f"Loss: {eval[ip]['Loss']}\n")
                file.write(f"Improvements: {eval[ip]['Pimprove']}\n")
    print("Report is done!")
    

generate_report()