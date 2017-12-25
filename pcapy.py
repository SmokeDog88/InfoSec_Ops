# Written by Miguel Bigueur
# pcapy packet capture
# Security Scripting w/Python
# Dec 24, 2017


import pcapy

devs = pcapy.findalldevs()
print(devs)

#  interface, bytes per packet, mode = promiscuous, timeout in (ms)
cap = pcapy.open_live("eth0", 65536 , 1 , 0)

count = 1
while count:
    (header, payload) = cap.next()
    print(count)
    count = count + 1
