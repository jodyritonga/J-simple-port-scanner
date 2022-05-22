
import socket
import termcolor

def scan(target, ports):
	print('\n'  + 'Mulai scanning untuk ip = ' + str(target))
	for port in range(1,ports):
		scan_port(target, port)
	

def scan_port (ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port terbuka " + str(port))
		sock.close()
	except:
		pass

targets = input("[*] Masukan taget yang akan di scan  : " )
ports = int(input ("[*} Masukkan berapa port yang akan di scan: "))

if ',' in targets:
	print(termcolor.colored(("[*] Scan banyak target"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)

else:
	scan(targets,ports)
