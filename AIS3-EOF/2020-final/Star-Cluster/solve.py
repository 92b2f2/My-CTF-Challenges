#!/usr/bin/python3
from scapy.utils import rdpcap
from scapy.layers.inet import TCP
import sys

def process_pcap(file_name):
    head = '424d36d51b0000000000360000002800000060090000be00000001002000000000000000000000000000000000000000000000000000'
    f = [b'' for _ in range(22)]
    of = open('fparse.bmp','wb')
    
    s = rdpcap(file_name).sessions()
    for s_name in s:
        recflag = False
        idx = 0
        for p in s[s_name]:
            try:
                raw = p[TCP].load
                if recflag and len(raw) > 1000:
                    f[idx] += raw

                if raw.startswith(b'\x42\x01') and len(raw) == 40:  #MPI (BTL) header
                    idx = raw[12]
                    recflag = True
            except:
                pass
        f[idx] = f[idx][24:]
    of.write(bytes.fromhex(head))
    for d in f:
        of.write(d)
    of.close()

if __name__ == '__main__':
    f = sys.argv[1]
    process_pcap(f)
