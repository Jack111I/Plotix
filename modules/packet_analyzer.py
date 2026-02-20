#!/usr/bin/env python3
"""Packet capture & basic stats (pyshark + scapy)"""

import pyshark
import utils
import time
from tabulate import tabulate

def run(cfg):
    ip = cfg["target"]["ip"]
    cap = pyshark.LiveCapture(interface=utils.get_default_iface(),
                              bpf_filter=f"host {ip}")
    print(f"[*] Capturing packets to/from {ip} – press CTRL+C to stop")
    try:
        for pkt in cap.sniff_continuously():
            print(format_packet(pkt))
    except KeyboardInterrupt:
        print("\n[+] Capture finished")

def format_packet(pkt):
    try:
        return f"{pkt.sniff_timestamp}\t{pkt.ip.src}->{pkt.ip.dst}\t{pkt.transport_layer}"
    except AttributeError:
        return "Non‑IP packet"