#! /usr/bin/python3
# coding=utf-8

"""
A simple Python Port Scanner with Python: python-nmap y python3-nmap
"""

import sys
import json
#import csv
from datetime import datetime
#import colorama
from colorama import Fore #Back, Style

timestamp = datetime.now()

try:
    import nmap
    print("Versión del módulo: " + str(nmap.__version__))
except ModuleNotFoundError:
    print("Error import nmap, check your python-nmap instalation.")
    sys.exit(-1)

try:
    import nmap3
    print("Versión del módulo: " + str(nmap3.__version__)) #nmap3.nmap_version()
except ModuleNotFoundError:
    print("Error import nmap, check your python3-nmap instalation.")
    sys.exit(-1)

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

def escaner_nmap_tipo1():
    """
    Function escaner with python-nmap
    """
    print("python-nmap")

    target = input("Ingrese direccion IP o rango a escanear: ")

    tipo_escaneo_text = "Ingrese el tipo de escaneo: \n"
    opcion1 = "1. -sV \n"
    opcion2 = "2. -sC \n"
    opcion3 = "3. Disable DNS resolution (-n) \n "
    tipo_escaneo = input(tipo_escaneo_text + opcion1 + opcion2 + opcion3)

    ports = input("Ingrese los puertos o rango a escanear: ")

    if tipo_escaneo == "1":
        nmap_arguments = "-sV -p " + ports
    elif tipo_escaneo == "2":
        nmap_arguments = "-sC -p " + ports
    elif tipo_escaneo == "3":
        nmap_arguments = "-n -p " + ports
    else:
        print("Ingrese una de las opciones del menú")

    scanner = nmap.PortScanner()
    results = scanner.scan(hosts=target, arguments=nmap_arguments)
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

def escaner_nmap3_tipo2():
    """
    Function escaner with python3-nmap
    """
    print("python3-nmap")
    target = input("Ingrese direccion IP o rango a escanear: ")
    #tipo_escaneo = input("Ingrese el tipo de escaneo: ej: -n -sV -sC -p ")

    tipo_escaneo_text = "Ingrese el tipo de escaneo: \n"
    opcion1 = "1. Only port scan (-Pn) \n"
    opcion2 = "2. Only host discover (-sn) \n"
    opcion3 = "3. Arp discovery on a local network (-PR) \n"
    opcion4 = "4. Disable DNS resolution (-n) \n "
    tipo_escaneo = input(tipo_escaneo_text + opcion1 + opcion2 + opcion3 + opcion4)

    ports = "-p" + input("Ingrese los puertos o rango a escanear: ej: 1-100 [1..100], 443 [443]: ")

    scanner = nmap3.Nmap()
    #results = scanner.scan_top_ports(target)

    scanner = nmap3.NmapHostDiscovery()
    if tipo_escaneo == "1":
        portscan_results = scanner.nmap_portscan_only(target, args=ports) #portscan_only
    elif tipo_escaneo == "2":
        portscan_results = scanner.nmap_no_portscan(target, args=ports) #no_portscan
    elif tipo_escaneo == "3":
        portscan_results = scanner.nmap_arp_discovery(target, args=ports)
    elif tipo_escaneo == "4":
        portscan_results = scanner.nmap_disable_dns(target, args=ports)
    else:
        print("Ingrese una de las opciones del menú")

    print(portscan_results)
    json_formatted = json.dumps(portscan_results, indent = 2)
    print(json_formatted)
    write_csv(json_formatted)

def banner():
    """
    Function banner bienvenidad
    """
    print(Fore.GREEN+"""
__________.__                                 .__    .___      
\\______   \\__| ____   _______  __ ____   ____ |__| __| _/____  
 |    |  _/  |/ __ \\ /    \\  \\/ // __ \\ /    \\|  |/ __ |/  _ \\ 
 |    |   \\  \\  ___/|   |  \\   /\\  ___/|   |  \\  / /_/ (  <_> )
 |______  /__|\\___  >___|  /\\_/  \\___  >___|  /__\\____ |\\____/ 
        \\/        \\/     \\/          \\/     \\/        \\/       
\n""" + Fore.BLUE + """escaner_de_puertos v1. Copyright (c) 2022 @mafeave\n""")

def main():
    """
    Function main
    """
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+"+Fore.GREEN+"+")

    opcion = input("Seleccione la opción a utilizar: \n 1. python-nmap \n 2. python3-nmap \n")
    print(opcion)
    if opcion == "1":
        escaner_nmap_tipo1()
    elif opcion == "2":
        escaner_nmap3_tipo2()
    else:
        print("Ingrese una de las opciones del menú")

banner()
main()
