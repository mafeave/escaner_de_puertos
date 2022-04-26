#! /usr/bin/python3
# coding=utf-8

"""
A simple Python Port Scanner with nmap3
"""

import sys
import json

try:
    import nmap3
    print("Versión del módulo: " + str(nmap3.__version__)) #nmap3.nmap_version()
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

os_results = scanner.nmap_os_detection(target) # MOST BE ROOT

print("========= OS RESULTS ==========")
print(os_results)
print("==============================\n")

version_result = scanner.nmap_version_detection(target) ### Identifying service version # Must be root
print("========= VERSION RESULTS ==========")
print(version_result)
print("==============================\n")

#Nmap Dns-brute-script( to get subdomains )
dns_results = scanner.nmap_dns_brute_script("domain")
print(dns_results)

#Nmap list scan
results_list_scan = scanner.nmap_list_scan(target)
print(results_list_scan)

#Nmap subnet scan
results_subnet_scan = scanner.nmap_subnet_scan(target) #Must be root
print(results_subnet_scan)

scanner = nmap3.NmapScanTechniques()
syn_scan_result = scanner.nmap_syn_scan(target) #nmap_syn_scan
tcp_scan_result = scanner.nmap_tcp_scan(target)
udp_scan_result = scanner.nmap_udp_scan(target)
idle_scan_result = scanner.nmap_idle_scan(target) #nmap_idle_scan
ping_scan_result = scanner.nmap_ping_scan(target) #nmap_ping_scan
fin_scan_result = scanner.nmap_fin_scan(target) #nmap_fin_scan

print("=========== SYN SCAN RESULT ==========")
print(syn_scan_result)
print("==============================\n")
print("=========== TCP SCAN RESULT ==========")
print(tcp_scan_result)
print("==============================\n")
print("=========== UDP SCAN RESULT ==========")
print(udp_scan_result)
print("==============================\n")

"""""
- Only port scan    (-Pn)
- Only host discover    (-sn)
- Arp discovery on a local network  (-PR)
- Disable DNS resolution    (-n)
""""

scanner = nmap3.NmapHostDiscovery()

portscan_only_results = scanner.nmap_portscan_only(target) #portscan_only
print(portscan_only_results)

no_portscan_results = scanner.nmap_no_portscan(target) #no_portscan
print(no_portscan_results)

arp_discovery_results = scanner.nmap_arp_discovery(target)
print("=========== ARP DISCOVERY RESULT ==========")
print(arp_discovery_results)
print("==============================\n")

disable_dns_results = scanner.nmap_disable_dns(target)
print(disable_dns_results)

### Using custom nmap command line arguments.
scanner = nmap3.Nmap()
results = scanner.scan_top_ports(target, args="-sV")