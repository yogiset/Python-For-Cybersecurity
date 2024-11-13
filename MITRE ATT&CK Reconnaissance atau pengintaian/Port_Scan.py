# from scapy.all import *

# ports = [25, 80, 53, 443, 445, 8080, 8443]

# def syn_scan(host):
#     """Performs a TCP SYN scan on the specified host for the given ports.

#     Args:
#         host (str): The IP address or hostname of the target host.

#     Prints:
#         List of open ports discovered on the target host.
#     """

#     ans, unans = sr(IP(dst=host) / TCP(sport=RandShort(), dport=ports, flags="S"), timeout=2)

#     # Improved output formatting and error handling
#     if ans:
#         print(f"Open ports on {host}:")
#         for (s, r) in ans:
#             print(s[TCP].dport)
#     else:
#         print(f"No open ports found on {host} within the timeout.")

# def dns_scan(host):
#     """Performs a simple DNS resolution check on the specified host.

#     Args:
#         host (str): The IP address or hostname of the target host.

#     Prints:
#         Confirmation message if a DNS response is received.
#     """

#     try:
#         # Improved reliability and reduced verbosity
#         ans, unans = sr(IP(dst=host) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="9.9.9.9")), timeout=2)
#         if ans:
#             print(f"{host} appears to be a DNS server.")
#     except Exception as e:
#         print(f"Error during DNS scan: {e}")

# if __name__ == "__main__":
#     host = "8.8.8.8"

#     syn_scan(host)
#     dns_scan(host)

from scapy.all import *

ports = [25,80,53,443,445,8080,8443]

def SynScan(host):
    ans,unans = sr(IP(dst=host)/TCP(dport=ports,flags="S"),timeout=2,verbose=0)
    print("Open ports at %s:" % host)
    for (s,r,) in ans:
        if s.haslayer(TCP) and r.haslayer(TCP):
            if s[TCP].dport == r[TCP].sport:
                print(s[TCP].dport)

def DNSScan(host):
    ans,unans = sr(IP(dst=host)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="hum.co.id")),timeout=2,verbose=0)
    if ans:
        print("DNS Server at %s"%host)
    
host = "8.8.8.8"

SynScan(host)
DNSScan(host)