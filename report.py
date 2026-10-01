import matplotlib
import evaluate
import local_config

def generate_report():
    report_stats = evaluate.eval()
    local = local_config.get_ipconfig_data()
    print(report_stats)
    print(local)

generate_report()