#!/usr/bin/env python3
"""
Simple TCP Port Scanner
Use only on systems you own or have explicit permission to test.
"""

import socket
import sys

def scan_host(host, start_port, end_port):
    print(f"\nScanning {host} ({start_port}-{end_port})...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port, "tcp")
                except OSError:
                    service = "unknown"
                print(f"[+] Port {port:5} OPEN  ({service})")
        except socket.gaierror:
            print("[-] Could not resolve the host.")
            return
        finally:
            sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <authorized-host>")
        sys.exit(1)

    target = sys.argv[1]
    scan_host(target, 1, 1024)
