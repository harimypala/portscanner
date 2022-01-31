import socket
import termcolor
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print(termcolor.colored(('\n' + '[ (0*0) Scanning Target] ' + str(target) + '\n   \~/'), 'green'))
    for port in range(0,65535):
        scan_port(converted_ip, port)
    print('<THE_END>\nThanks for using the tool.')
    print(termcolor.colored((' - harimypala'), 'green'))

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print(termcolor.colored(('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n'))), 'red'))
        except:
            print(termcolor.colored(('[+] Open Port ' + str(port) + ' : '), 'red'))
    except:
        pass


targets = input(termcolor.colored(('[+] Enter Target/s To Scan(split mulitple targets with ","): '), 'green'))
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
