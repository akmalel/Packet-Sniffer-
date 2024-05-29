import argparse
from scapy.all import sniff, wrpcap

def packet_callback(packet):
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        print(f"IP Packet: {ip_src} -> {ip_dst}")

def main():
    parser = argparse.ArgumentParser(description="Simple Packet Sniffer")
    parser.add_argument('-i', '--interface', type=str, help='Network interface to sniff on', required=True)
    parser.add_argument('-c', '--count', type=int, help='Number of packets to capture', default=10)
    parser.add_argument('-f', '--filter', type=str, help='BPF filter for packet capture', default='')
    parser.add_argument('-o', '--output', type=str, help='Output file to save packets', default='')

    args = parser.parse_args()

    packets = sniff(iface=args.interface, prn=packet_callback, filter=args.filter, count=args.count)

    if args.output:
        wrpcap(args.output, packets)

if __name__ == '__main__':
    main()

