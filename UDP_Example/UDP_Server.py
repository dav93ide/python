#------------------#
#    UDP SERVER    #
#------------------#

import socket
import threading

bind_host = 'localhost'
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((bind_host,bind_port))
	
	

while True:
	data,addr = server.recvfrom(4096)
	if data != 'END':
		print "[*] Ricevuto %s  \\ Da -> %s" % (data,addr)
	else:
		print "END Ricevuto, Invio Risposta"
		server.sendto("ACK!",addr)
