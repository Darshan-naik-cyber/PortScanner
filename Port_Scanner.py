import socket as socket #socket library to use the ports 
from IPy import IP #to convert the domain name into IP we required this library 


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-+-..] Scanning Target' +str(target))
    for port in range(1,1000):
        port_scan(converted_ip,port)
    
    
def check_ip(ip): #function to convert Domain into the IP address 
    try:
        IP(ip)
        return ip # simple , if use input the IP then only IP will scan 
    except ValueError:
        return socket.gethostbyname(ip) #otherwise the this parameter will convert the IP into IP

def get_banner(s):
    return s.recv(1024)


def port_scan(ipaddress, port): #here we define function to scan a port
    try:
        sock = socket.socket() # socket will fucntion from library will run here
        sock.settimeout(0.5)
        sock.connect(ipaddress , port)
        try:
            banner = get_banner(sock)
            print('[+] Open Port' +str(port)+ str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port' +str(port)) 
    except:
        pass # here if port is closed then simply it will pass 
if __name__  == "__main__":
    targets = input('[+] Enter Target/s IP address (enter by , ): ') #user input 
    #port_num = input('[+] Enter The Ports Number you want to scan: ') 
# In the above line we have to Scan Multiple target then we will seperate them by comma   
# converted_ip = check_ip(ipaddress)  #converted IP , where the Check ip will check and convert the IP into this variable
    if ',' in targets: # here if we found the ',' in IP then we split it with ',' into each target
        for ip_add in targets.split(','):
            scan(ip_add(strip(' '))) # In strip function we have passed ' ' . to remove unwanted space
            #above scan() function is called 
    else:
        scan(targets) # If the target is the single target 

