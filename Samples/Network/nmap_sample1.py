import nmap
from datetime import datetime


HOST = '127.0.0.1'
start = datetime.now()
print('initialize the port scanner')
nmScan = nmap.PortScanner()
print('finish the port scanner')

# scan localhost for ports in range 21-443
# nmScan.scan('127.0.0.1', '21-443')

nmScan.scan(hosts=HOST, arguments='-sU -sT')
all_hosts = nmScan.all_hosts()
# run a loop to print all the found result about the ports
for host in all_hosts:
    print('Host : %s (%s)' % (host, nmScan[host].hostname()))
    print('State : %s' % nmScan[host].state())
    all_protoc = nmScan[host].all_protocols()
    for proto in all_protoc:
        print('----------')
        print('Protocol : %s' % proto)

        ports_data = nmScan[host][proto]

        lport = [x for x in nmScan[host][proto].keys()]
        lport.sort()
        for port in lport:
            if nmScan[host][proto][port]['state'] == 'open':
                state = nmScan[host][proto][port]['state']
                name = nmScan[host][proto][port]['name']
                print(f'port : {port}\tname : {name}\tstate : {state}')

finish = datetime.now()
total = finish - start
print('Tempo total: ', total.total_seconds())
