import nmap
import sys #for sys.argv down the road
import os
import itertools

# hard coded for quick testing
# host = "192.168.21.201"
host = '127.0.0.0'
ports = [ "2348", "3173", "9252", "1532" ]

class PortKnock():

    def __init__(self, host, ports):
        self.host = host
        self.ports = str(ports).split(",")
        self.scanner = nmap.PortScanner()

    def ShowOptions(self):
        print("[~] Showing Options")
        print("[H]     Target Host: " + self.host)
        print("[P]    Target Ports: "+ self.PortList())

    # def BasicKnock(self, host, ports): # nmap -oX - -p {ports} -sV {host}
    #     scanner = nmap.PortScanner()

    def PingKnockRandom(self):
        res = self.scanner.scan(self.host, str(PortList(ports)), arguments='-Pn' )
        return res

    def PingKnockOrdered(self):
        # scanner = nmap.PortScanner()
        for p in self.ports:
            res = self.scanner.scan(host, p, arguments='-Pn')
            status = res.get('scan').get(host).get('tcp').get(int(p)).get('state')
            print("[!] {0}:{1} - {2}".format(host, p, status))
        return "[+] Knock Complete"

    # def BrutePortListKnock(self):
    #     pports = itertools.permutations(self.ports)
    #     for perm in pports:
    #         print(PingKnockOrdered(host, perm))
    #         LogginSSH("derek", host)

    def CheckTargetPort(self):
        # scanner = nmap.PortScanner()
        res = self.scanner.scan(self.host, self.port)
        status = res.get('scan').get(host).get('tcp').get(int(port))
        return status.get('state')

    def LoginSSH(self, user, host):
        print("[!] Trying SSH Loggin")
        os.system("ssh {0}@{1}".format(user, host))

    def PortList(self):
        list = ""
        for p in self.ports:
            list += p +","
        return list

# try:
#     host = str(sys.argv[1])
#     ports = str(sys.argv[2]).split(",")
#     print("Target aquired >> {0}:{1}".format(host, ports))
#     scanner = PortKnock(host, ports)
#     print(scanner.PingKnockOrdered())
# except:
#     print("[-] Error")
#     print("USAGE: python PortKnock.py {host} {ports} {options}")
#     print("   EX: python PortKnock.py 127.0.0.0 22,23,80")

# testing
# print(CheckTargetPort(host, '22'))
# print(PingKnockOrdered(host, ports))
# LoginSSH("super", "192.168.0.27")
