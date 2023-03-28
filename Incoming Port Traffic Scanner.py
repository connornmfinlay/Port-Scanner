import os
os.environ['SCAPY_PCAP'] = r'C:\Program Files\Npcap'
from scapy.all import *
from prettytable import PrettyTable

# prompt the user to input the port number
port = input("Enter the port number to listen to: ")

# validate the port number
if not port.isdigit() or int(port) < 1 or int(port) > 65535:
    print("Invalid port number!")
    exit()

# create a packet capture filter for the specified port
filter = f"tcp port {port}"

# start capturing packets
pkts = sniff(filter=filter, count=10)

# create a table to display the packet information
table = PrettyTable()
table.field_names = ["Time", "Source", "Destination", "Protocol", "Length"]

# loop through each packet and add a row to the table
for pkt in pkts:
    time = pkt.time
    src = pkt[IP].src
    dst = pkt[IP].dst
    proto = pkt.sprintf("%IP.proto%")
    length = len(pkt)
    table.add_row([time, src, dst, proto, length])

# print the table
print(table)