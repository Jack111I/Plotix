#!/usr/bin/env python3
"""Domain, subdomain, WHOIS & IP resolution"""

import subprocess
import socket
import netifaces
import utils
import yaml
import json
from tabulate import tabulate
import requests

def run(cfg):
    domain = cfg.get("target", {}).get("domain")
    if not domain:
        utils.err("No domain supplied – aborting.")
        return

    print("[*] Resolving IP …")
    try:
        ip = socket.gethostbyname(domain)
    except Exception as e:
        utils.err(f"DNS resolve failed: {e}")
        return

    cfg["target"]["ip"] = ip
    print(f"[+] {domain} → {ip}")

    print("[*] Subdomain enumeration …")
    subdomains = subfinder(domain)
    print(tabulate([(i+1, d) for i, d in enumerate(subdomains)], headers=["#", "Subdomain"]))

    print("[*] WHOIS lookup …")
    whois_info = whois_lookup(domain)
    print(json.dumps(whois_info, indent=2))

def subfinder(target):
    """Simple subfinder wrapper (subfinder CLI)."""
    out = subprocess.check_output(f"subfinder -d {target} -o -", shell=True)
    return out.decode().splitlines()

def whois_lookup(target):
    """Return raw whois dictionary."""
    return utils.run_cmd(f"whois {target}").strip()