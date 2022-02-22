#!/usr/bin/env python3
 
from ipaddress import ip_address
import socket
import sys
import traceback
 
def main():
    #opens the text file that contains all of the ip address
    with open("ip_address.txt") as ip_address:

        #cleans up all the data and then returns an array with all the data
        ip_and_dns = get_dns(clean_up_data(ip_address))

        #writes all the data to a txt file
        create_text_file(ip_and_dns)    

def create_text_file(data):
    f = open("IP_address_and_DNS.txt", "w+")

    for line in data:
        f.write("IP: {0:60} DNS: {1}\n".format(str(line[2]), str(line[0])))
        f.write("\n")

# a function that takes all the data and cleans it up
def clean_up_data(ip_address):
    address = []
    for line in ip_address:
        striped_line = line.rstrip()
        address.append(striped_line)
    return address

#gets the dns from the ip address and returns an array with all the dnss
def get_dns(ip_address):
    
    list_ip_dns = [None] * len(ip_address)

    for i in range(len(ip_address)):
        try:
            host = socket.gethostbyaddr(str(ip_address[i]))
            list_ip_dns[i] = host
        except:
            list_ip_dns[i] = [None, None, f"Sorry we had issues reaching {ip_address[i]} IP address please try pasting it into your browser."]

    return list_ip_dns

main() 