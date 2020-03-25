import nmap
import sys #for sys.argv down the road
import os

# hard coded for quick testing
# host = "192.168.21.201"
host = '127.0.0.0'
ports = [ "2348", "3173", "9252", "1532" ]

def BasicKnock(host, ports): # nmap -oX - -p {ports} -sV {host}
    scanner = nmap.PortScanner()

def PingKnockRandom(host, ports):
    scanner = nmap.PortScanner()
    res = scanner.scan(host, str(PortList(ports)), arguments='-Pn' )
    return res

def PingKnockOrdered(host, ports):
    scanner = nmap.PortScanner()
    for p in ports:
        res = scanner.scan(host, p, arguments='-Pn')
        status = res.get('scan').get(host).get('tcp').get(int(p)).get('state')
        print("[!] {0}:{1} - {2}".format(host, p, status))
    return "[+] Knock Complete"

def CheckTargetPort(host, port):
    scanner = nmap.PortScanner()
    res = scanner.scan(host, port)
    status = res.get('scan').get(host).get('tcp').get(int(port))
    return status.get('state')

def LoginSSH(user, host):
    os.system("ssh {0}@{1}".format(user, host))

def PortList(ports):
    list = ""
    for p in ports:
        list += p +","
    return list

try:
    host = str(sys.argv[1])
    ports = str(sys.argv[2]).split(",")
    print("Target aquired >> {0}:{1}".format(host, ports))
    print(PingKnockOrdered(host, ports)) # Default for now ig
except:
    print("[-] Error")
    print("USAGE: python PortKnock.py {host} {ports} {options}")
    print("   EX: python PortKnock.py 127.0.0.0 22,23,80")
# testing
# print(CheckTargetPort(host, '22'))
# print(PingKnockOrdered(host, ports))
# LoginSSH("super", "192.168.0.27")
