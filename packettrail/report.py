from packettrail.analyze import high_usage_ips, non_standard_ports

def generate_report():
    print("\nTop IP Addresses by Usage:")
    for ip, total in high_usage_ips():
        print(f"{ip} -> {total} bytes")

    print("\nNon-standard ports detected:")
    for port in non_standard_ports():
        print(f"Port {port[0]}")
