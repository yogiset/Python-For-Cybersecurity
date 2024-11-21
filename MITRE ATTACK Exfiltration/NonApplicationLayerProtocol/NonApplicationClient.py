from scapy.all import *

def transmit(message, host):
    for m in message:
        packet = IP(dst=host)/ICMP(code = ord(m))
        send(packet)

host = "112.78.32.202"
message = "Hello"
transmit(message,host)