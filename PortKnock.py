import nmap
import sys #for sys.argv down the road

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

def PortList(ports):
    list = ""
    for p in ports:
        list += p +","
    return list

# print(CheckTargetPort(host, '22'))
print(PingKnockOrdered(host, ports))
