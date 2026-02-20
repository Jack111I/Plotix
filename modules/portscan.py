#!/usr/bin/env python3
"""Async TCP/UDP port scanner using Python‑Nmap"""

import nmap
import utils
from concurrent.futures import ThreadPoolExecutor
from tabulate import tabulate

def run(cfg):
    ip = cfg["target"]["ip"]
    ports = cfg["scan"]["ports"]
    threads = cfg["scan"]["threads"]
    nm = nmap.PortScanner()
    print(f"[*] Scanning {ip} ports {ports}")
    nm.scan(hosts=ip, ports=ports, arguments="-T4", thread_count=threads)
    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                state = nm[host][proto][port]["state"]
                results.append([host, port, proto, state])
    print(tabulate(results, headers=["Host","Port","Proto","State"]))