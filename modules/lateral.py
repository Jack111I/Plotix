#!/usr/bin/env python3
"""SMB / RDP mapping + service discovery"""

import utils
import socket
import subprocess
from tabulate import tabulate

def run(cfg):
    ip = cfg["target"]["ip"]
    if not ip:
        ip = utils.resolve_ip_from_name(cfg["target"]["domain"])

    # 1️⃣ SMB shares
    shares = utils.call_tool("smbclient", {"ip": ip, "user":"guest"})["shares"]
    print(tabulate([ [s] for s in shares ], headers=["SMB Share"]))

    # 2️⃣ RDP targets
    rdp = utils.call_tool("rdp_enum", {"ip": ip})["targets"]
    print(tabulate([ [t] for t in rdp ], headers=["RDP Target"]))