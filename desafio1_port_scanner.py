#! /usr/bin/python3
# coding=utf-8

"""
A simple Python Port Scanner with Python: python-nmap y python3-nmap
"""

from datetime import datetime
#import colorama
from colorama import Fore #Back, Style

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

def escaner_nmap_tipo1():
    """
    Function escaner with python-nmap
    """

def escaner_nmap3_tipo2():
    """
    Function escaner with python3-nmap
    """

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
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")

banner()
main()
