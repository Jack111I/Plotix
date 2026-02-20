#!/usr/bin/env python3
"""Phone + email + leak collection"""

import utils
import requests
import yaml
from tabulate import tabulate

def run(cfg):
    target = cfg["target"]["domain"]

    # 1️⃣ Phone OSINT – pretend we have a list of numbers
    numbers = utils.read_numbers_from_file("numbers.txt")  # user‑supplied
    for num in numbers:
        basic = utils.call_tool("phone_basic_info", {"number": num})
        details = utils.call_tool("get_phone_details", {"number": num})
        print(f"📞 {num} → {basic['region']}, {details['address']}")

    # 2️⃣ Email discovery
    emails = utils.call_tool("emailbook", {"domain": target})["emails"]
    print(tabulate([ [e] for e in emails ], headers=["Email"]))

    # 3️⃣ Credential / credential‑leak search
    for email in emails:
        leaks = utils.call_tool("leaks_search", {"email": email})["leaks"]
        if leaks:
            print(f"[!] {email} found in {len(leaks)} leaks")