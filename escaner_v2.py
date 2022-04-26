#! /usr/bin/python3
# coding=utf-8

"""
A simple Python Port Scanner with nmap
"""

import sys
import json

try:
    import nmap3
    print("Versión del módulo: " + str(nmap3.__version__))
except ModuleNotFoundError:
    print("Error import nmap, check your python3-nmap instalation.")
    sys.exit(-1)

target = input("Ingrese el host a escanear: ")

scanner = nmap3.Nmap()
results = scanner.scan_top_ports(target)

json_formatted = json.dumps(results, indent = 2)
# print(json_formatted)

print("========= TOP PORTS ==========")
print(results)
print("==============================\n")

os_results = scanner.nmap_os_detection(target)

print("========= OS RESULTS ==========")
print(os_results)
print("==============================\n")

version_result = scanner.nmap_version_detection(target)
print("========= VERSION RESULTS ==========")
print(version_result)
print("==============================\n")

scanner = nmap3.NmapScanTechniques()
syn_scan_result = scanner.nmap_syn_scan(target)
tcp_scan_result = scanner.nmap_tcp_scan(target)
udp_scan_result = scanner.nmap_udp_scan(target)

print("=========== SYN SCAN RESULT ==========")
print(syn_scan_result)
print("==============================\n")
print("=========== TCP SCAN RESULT ==========")
print(tcp_scan_result)
print("==============================\n")
print("=========== UDP SCAN RESULT ==========")
print(udp_scan_result)
print("==============================\n")

scanner = nmap3.NmapHostDiscovery()
arp_discovery_results = scanner.nmap_arp_discovery(target)
print("=========== ARP DISCOVERY RESULT ==========")
print(arp_discovery_results)
print("==============================\n")
