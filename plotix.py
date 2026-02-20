#!/usr/bin/env python3
"""
Plotix – A modular recon / OSINT / lateral‑movement tool

Usage:
    plotix.py [options]

Options:
    -c, --config FILE   Path to YAML config file (default: config.yaml)
    -t, --target DOMAIN Target domain/IP to start from
    -p, --ports PORTS   Port range to scan (default: 1-1024)
    -s, --start [all|recon|osint|network|wifi|mac]
                        Run a specific stage (default: all)
    -h, --help          Show help

Author: White Hack Labs
"""

import argparse
import yaml
import os
import sys

# Import sub‑modules
from modules import recon, fingerprint, portscan, packet_analyzer, mac_spoof, wifi, osint, lateral, utils

def load_config(path: str):
    with open(path, 'r') as f:
        cfg = yaml.safe_load(f)
    return cfg

def run_stage(stage: str, cfg: dict):
    if stage in ("all", "recon"):
        recon.run(cfg)
    if stage in ("all", "fingerprint"):
        fingerprint.run(cfg)
    if stage in ("all", "ports"):
        portscan.run(cfg)
    if stage in ("all", "packet"):
        packet_analyzer.run(cfg)
    if stage in ("all", "mac"):
        mac_spoof.run(cfg)
    if stage in ("all", "wifi"):
        wifi.run(cfg)
    if stage in ("all", "osint"):
        osint.run(cfg)
    if stage in ("all", "lateral"):
        lateral.run(cfg)

def main():
    parser = argparse.ArgumentParser(description="Plotix – All‑in‑one recon tool")
    parser.add_argument("-c", "--config", default="config.yaml", help="YAML config file")
    parser.add_argument("-t", "--target", help="Override target domain/IP")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range to scan")
    parser.add_argument("-s", "--start", default="all",
                        choices=["all","recon","osint","network","wifi","mac","fingerprint","ports","packet","lateral"],
                        help="Which stage(s) to run")
    args = parser.parse_args()

    cfg = load_config(args.config)

    # Override domain if supplied on CLI
    if args.target:
        cfg["target"]["domain"] = args.target

    cfg["scan"]["ports"] = args.ports

    try:
        run_stage(args.start, cfg)
    except KeyboardInterrupt:
        utils.cleanup()
        sys.exit("\n[!] Interrupted – cleaned up\n")

if __name__ == "__main__":
    main()