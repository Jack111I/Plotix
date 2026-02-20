#!/usr/bin/env python3
"""Full Wi‑Fi scan (channel hopping + packet capture)"""

import wifi
import subprocess
import utils
from tabulate import tabulate

def run(cfg):
    iface = cfg["wifi"]["interface"]
    ch = cfg["wifi"]["channel"]

    print("[*] Scanning Wi‑Fi networks …")
    nets = wifi.Cell.all(iface)
    data = [[n.ssid, n.channel, n.quality, n.encryption_type] for n in nets]
    print(tabulate(data, headers=["SSID","CH","Qual","Enc"]))

    # Optional: capture for a few seconds
    print("[*] Capturing 5 sec on channel", ch)
    subprocess.run(f"sudo iwconfig {iface} channel {ch}", shell=True, check=False)
    subprocess.run(f"sudo tcpdump -i {iface} -c 100 -w /tmp/plotix_wifi.pcap", shell=True, check=False)