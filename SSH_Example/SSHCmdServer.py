''' Server SSH Per Esecuzione Comandi Su Un Client Connesso '''

import paramiko
import threading
import subprocess
import socket
import sys

host_key = paramiko.RSAKey(filename='test_rsa.key')

class Server(paramiko.ServerInterface):	

	def __init__(self):
		self.event = threading.Event()
	
	def check_channel_request(self, kind, chanid):
		if kind == "session":
			return paramiko.OPEN_SUCCEEDED
		return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

	def check_auth_password(self, username, password):
		if(username == "test") and (password == "pass"):
			return paramiko.AUTH_SUCCESSFUL
		return paramiko.AUTH_FAILED
	

if __name__ == "__main__":
	if (len(sys.argv) == 3 ):
		server_addr = sys.argv[1]
		server_port = int(sys.argv[2])
	else:
		print "+ Invalid Number Of Arguments \n Usage: SSHCmdServer.py address port"
		sys.exit(1)
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind((server_addr,server_port))
		sock.listen(100)
		print "+ Waiting Connections"
		client, addr = sock.accept()
	except Exception, e:
		print "+ Listen Failed : %s" % str(e)
		sys.exit(1)
	print "+ Connected: %s" % str(addr)
	try:
		sshSession = paramiko.Transport(client)
		sshSession.add_server_key(host_key)
		server = Server()
		try:
			sshSession.start_server(server=server)
		except paramiko.SSHException, ex:
			print "+ SSH Failed"
		channel = sshSession.accept(20)
		if channel is None:
			print "+ Channel None"
			sys.exit(1)
		print "+ Authenticated"
		print "Got: %s" % channel.recv(1024)
		channel.send("WeLCoMe")
		print "+ Starting Commands Loop, Digit \"exit\" To End"
		while True:
			try:
				command = raw_input("+ Enter Command: ").strip("\n")
				if command != "exit":
					channel.send(command)
					print "Got: \n"
					got=channel.recv(1024)
					while ("~|EnD|~" not in got) and ("returned non-zero exit status" not in got):
						print got
						got=channel.recv(1024)
					print "+ Got All"
				else:
					channel.send("exit")
					print "+ Exit"
					sshSession.close()
					raise Exception("exit")
			except KeyboardInterrupt:
				sshSession.close()
	except Exception, e:
		print "+ Exception: %s" % str(e)
		try:
			sshSession.close()
		except:
			pass
		sys.exit(1)
