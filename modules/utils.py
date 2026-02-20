#!/usr/bin/env python3
"""Common helper functions – CLI, config & tool wrappers"""

import yaml, subprocess, sys, os, json

def err(msg):
    print(f"[✗] {msg}", file=sys.stderr)

def get_default_iface():
    """Return the first non‑loopback interface."""
    import netifaces
    for iface in netifaces.interfaces():
        if iface != "lo":
            return iface
    return None

def resolve_ip_from_name(name):
    try:
        return socket.gethostbyname(name)
    except:
        return None

def call_tool(name, params):
    """Very thin wrapper around internal modules (for demo only)."""
    import importlib
    mod = importlib.import_module(f"modules.{name}")
    return getattr(mod, "run")(params)

def run_cmd(cmd):
    """Return stdout / stderr of a shell command."""
    return subprocess.check_output(cmd, shell=True, text=True)