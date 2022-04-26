#! /usr/bin/python3
# coding=utf-8

"""
A simple Python Port Scanner with nmap
"""

from datetime import datetime

try:
    import nmap
    #print("Versión del módulo: %s" % (nmap.__version__))
    print("Versión del módulo: " + str(nmap.__version__))
    #print(f"Versión del módulo: {nmap.__version__}")
except ModuleNotFoundError:
    print("Error import nmap, check your python-nmap instalation.")
    sys.exit(-1)

timestamp = datetime.now()

def write_csv(data):
    """
    Function to export the scan results to a CSV file.
    """
    year = str(timestamp.year)
    month = str(timestamp.month)
    day = str(timestamp.day)
    hour = str(timestamp.hour)
    minute = str(timestamp.minute)
    second = str(timestamp.second)

    file_time = year + month + day + hour + minute + second

    with open("scan-report" + file_time + ".csv", "w", encoding='utf-8') as report:
        report.write(data)

# Formato NMAP
# 192.168.75.128
# 192.168.75.1/24
# 192.168.75.1-55
target = input("Ingrese direccion IP o rango a escanear: ")
# 80
# 22-443 --> {22,23,24...441,442,443}
# 22,443 --> {22,443}
ports = input("Ingrese los puertos o rango a escanear: ")
scanner = nmap.PortScanner()
NMAP_ARGUMENTS = "-n -sV -sC -p " + str(ports)
results = scanner.scan(hosts=target, arguments=NMAP_ARGUMENTS)
print(results)

print("Comando utilizado: " + scanner.command_line())

for host in scanner.all_hosts():
    print("----------------------------------------------")
    print('Host: ' + host + " (" + scanner[host].hostname() + ")")
    print('Status: ' + scanner[host].state())

    for protocol in scanner[host].all_protocols():
        print("----------------------------------------------")
        print('Protocol: ' + protocol)
        ports_list = list(scanner[host][protocol].keys())
        ports_list.sort()
        for port in ports_list:
            print(port)
            print('Port: ' + str(port) + '\t Status: ' + scanner[host][protocol][port]['state'])

print("Exporting results to CSV file...")
write_csv(scanner.csv())
