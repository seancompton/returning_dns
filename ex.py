#!/usr/bin/env python3
 
from ipaddress import ip_address
import socket
import sys
import traceback
 
def main():

    with open("ip_address.txt") as ip_address:
        ip_and_dns = get_dns(clean_up_data(ip_address))
        for i in ip_and_dns:
            print(i[0], " ", i[1])
            

def clean_up_data(ip_address):
    address = []
    for line in ip_address:
        striped_line = line.rstrip()
        address.append(striped_line)
    return address


def get_dns(ip_address):
    list_ip_dns = []
    for ip in ip_address:
        try:
            host = socket.gethostbyaddr(str(ip))
            list_ip_dns.append([ip, host])
        except:
            list_ip_dns.append([ip, "Sorry we had issues reaching this ip address please try pasting it into your browser"])

    return list_ip_dns

main() 