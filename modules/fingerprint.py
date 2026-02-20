#!/usr/bin/env python3
"""Nmap + SSL/TLS diagnostics"""

import nmap
import subprocess
import utils

def run(cfg):
    ip = cfg["target"]["ip"]
    ports = cfg["scan"]["ports"]
    nm = nmap.PortScanner()
    print(f"[*] Nmap scan: {ip}:{ports}")
    nm.scan(hosts=ip, ports=ports, arguments="-sS -sV -O")
    for host in nm.all_hosts():
        print(f"[+] {host} ({nm[host].state()})")
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            print(f"    {proto.upper()} ports: {len(lport)}")
        # SSL scan
        sslscan(host)

def sslscan(host):
    """Run sslscan via subprocess and pretty‑print output."""
    out = utils.run_cmd(f"sslscan {host}").splitlines()
    for line in out:
        if line.startswith("Certificate") or line.startswith("TLS"):
            print("      " + line)