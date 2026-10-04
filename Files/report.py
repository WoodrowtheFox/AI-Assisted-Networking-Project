import matplotlib.pyplot as plt
import evaluate as evaluate
import Files.local_config as local_config
import Files.metrics as metrics

def generate_report():
    #metric = metrics.main()
    #eval = evaluate.eval(metric)
    #local = local_config.get_ipconfig_data()

    metric = {'8.8.8.8': {'Tries': '2', 'Tested IP': '8.8.8.8', 'Hops': 16, 'Bytes Sent 1': '32', 'Time 1': '23', 'Bytes Sent 2': '32', 'Time 2': '23', 'Loss Percent': '0', 
                        'Min': '23', 'Max': '23', 'Avg': '23', 'Jitter': 0.0}, '1.1.1.1': {'Tries': '2', 'Tested IP': '1.1.1.1', 'Hops': 16, 'Bytes Sent 1': '32', 
                        'Time 1': '23', 'Bytes Sent 2': '32', 'Time 2': '24', 'Loss Percent': '0', 'Min': '23', 'Max': '24', 'Avg': '23', 'Jitter': 0.5}}
    eval = {'Upload': ['Your upload speed is below advertised.', 'The speed found while testing was 948.705896 while you the advertised upload was 600'], 
            'Download': ['Your upload speed is below advertised.', 'The speed found while testing was 941.758104 while you the advertised download was 500'], 
            'Throughput': {'Upload': 948705896, 'Download': 941758104}, 'Latency': 'You have very low latency!', 'Jitter': 'You have very low jitter', 
            'Loss': 'You have very low packet loss'}
    local = {'Public IP': '69.24.170.60', 'NON-DNS': {'Interface': 'Ethernet', 'Private IP': '192.168.1.81', 'Gateway': '192.168.1.1'}, 
             'DNS': {1: 'fdbf:f6a0:b231:0:3531:83e0:6665:7ca4', 2: '192.168.1.1', 3: 'fdbf:f6a0:b231:0:3531:83e0:6665:7ca4'}}
    
    IPs = []
    Hops = []
    Bytes = []
    Time = []
    Loss_Percent = []
    Min = []
    Max = []
    Avg = []
    Jitter = []

    for key in metric.keys():
        IPs.append(key)
    for ip in IPs:
        tries = int(metric[ip]["Tries"])
        i = 0
        while(tries > i):
            i += 1
            Bytes.append(metric[ip][f"Bytes Sent {tries}"])
            Time.append(metric[ip][f"Time {tries}"])
        Loss_Percent.append(metric[ip]["Loss Percent"])
        Hops.append(metric[ip]["Hops"])
        Min.append(metric[ip]["Min"])
        Max.append(metric[ip]["Max"])
        Avg.append(metric[ip]["Avg"])
        Jitter.append(metric[ip]["Jitter"])

    plt.bar(IPs, Avg)
    plt.title("Latency by IP")
    plt.xlabel("Target")
    plt.ylabel("Latency (ms)")
    plt.savefig("Latency.png")
    plt.clf

    plt.bar(IPs, Jitter)
    plt.title("Jitter by IP")
    plt.xlabel("Target")
    plt.ylabel("Jitter (ms)")
    plt.savefig("Jitter.png")
    plt.clf

    plt.bar(IPs, Hops)
    plt.title("Hops by IP")
    plt.xlabel("Target")
    plt.ylabel("Hops")
    plt.savefig("Hops.png")
    plt.clf

    plt.bar(IPs, Loss_Percent)
    plt.title("Packet Loss by IP")
    plt.xlabel("Target")
    plt.ylabel("Packets")
    plt.savefig("Packet.png")
    plt.clf

    TP = [[eval['Throughput']["Upload"]/1000000], [eval['Throughput']["Download"]/1000000]]
    fig, ax = plt.subplots(figsize=(5, 2))
    ax.axis('tight')
    ax.axis('off')

    throughput = ax.table(
        cellText=TP,
        colLabels=["Upload, Download"],
        cellLoc='center',
        loc='center'
    )

    plt.savefig("Throughput.png")
    plt.clf

    eval = {'Upload': ['Your upload speed is below advertised.', 'The speed found while testing was 948.705896 while you the advertised upload was 600'], 
                'Download': ['Your upload speed is below advertised.', 'The speed found while testing was 941.758104 while you the advertised download was 500'], 
                'Throughput': {'Upload': 948705896, 'Download': 941758104}, 'Latency': 'You have very low latency!', 'Jitter': 'You have very low jitter', 
                'Loss': 'You have very low packet loss'}

    with open("report.txt", "w") as file:
            file.write("Report:")
            file.write(f"Public IP: {local['Public IP']}")
            file.write(f"Interface: {local['NON-DNS']["Interface"]}")
            file.write(f"Private IP: {local['NON-DNS']["Private IP"]}")
            file.write(f"Gateway: {local['NON-DNS']["Gateway"]}")
            file.write("DNS:")
            for key in local['DNS'].keys():
                 file.write(str(key))
                 file.write(local['DNS'][key])
            file.write("Evaluation:")
            file.write(f"Upload: {eval['Upload'][0]}")
            file.write(f"{eval['Upload'][1]}")
            file.write(f"Download: {eval['Download'][0]}")
            file.write(f"{eval['Download'][1]}")
            file.write(f"Latency: {eval['Latency'][0]}")
            file.write(f"{eval['Latency'][1]}")
            file.write(f"Jitter: {eval['Jitter']}")
            file.write(f"Loss: {eval['Loss']}")
    

generate_report()