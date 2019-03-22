import nmap
from datetime import datetime

start = datetime.now()
print('initialize the port scanner')
try:
    nmScan = nmap.PortScanner()
except Exception as e:
    print(e)
print('finish the port scanner')
print(nmScan)

# scan localhost for ports in range 21-443
nmScan.scan('127.0.0.1', '21-443')

# run a loop to print all the found result about the ports
all_hosts = nmScan.all_hosts()
for host in all_hosts:
    print('Host : %s (%s)' % (host, nmScan[host].hostname()))
    print('State : %s' % nmScan[host].state())
    all_protoc = nmScan[host].all_protocols()
    for proto in all_protoc:
        print('----------')
        print('Protocol : %s' % proto)

        lport = nmScan[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' %
                  (port, nmScan[host][proto][port]['state']))

finish = datetime.now()
total = finish - start
print('Tempo total: ', total.total_seconds())
