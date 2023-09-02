import socket
from IPy import IP

def scan(target):
    converted_ip=resolve_ip(target)
    print('\n'+'[-_0 Sccanning Target]' + str(target))
    for port in range(1,65535):
        port_Scan(converted_ip,port)        

def resolve_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)  #resolve the domain into it's IP
def get_banner(s):
    return s.recv(1024) 
        

def port_Scan(ipaddress,port):
    try:
        sock=socket.socket()
        sock.settimeout(0.5)  #Let the program to run only for 0.5 seconds to connect to port
        sock.connect((ipaddress,port))
        try:
            banner=get_banner(sock) #to find out the service each corresponding port is using
            print("[+] Open Port "+ str(port) +" : "+ str(banner.decode().strip('\n')))
        except:
            print("[+] Open Port " + str(port))

    except:
        pass

targets= input('[+] Enter Target/s to scan (Split multiple targets by comma):')
if ',' in targets:
    for ip_address in targets.split(','):
        scan(ip_address.strip(' ')) #for multiple target
else:
    scan(targets) #for single target
        



    
 
