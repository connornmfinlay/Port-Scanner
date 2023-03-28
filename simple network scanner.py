from scapy.all import *

# create a packet capture filter for HTTP traffic
filter = "tcp port 80"

# start capturing packets
pkts = sniff(filter=filter, count=10)

# loop through each packet and print the contents
for pkt in pkts:
    print(pkt.show())