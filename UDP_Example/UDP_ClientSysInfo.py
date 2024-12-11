#-------------------------------#
#	SYS INFO UDP CLIENT	#
#-------------------------------#

import socket
import sys

target_host = 'localhost'
target_port = 9999
clientID = 'AA948'

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

list = ['ID: '+clientID, sys.platform , sys.version , sys.api_version]

for n in list:
	client.sendto( str(n) ,(target_host,target_port))

client.sendto("END",(target_host,target_port))

data,addr = client.recvfrom(4096)
print "Ricevuto %s   \\  Da  -> %s" % (data,addr)
client.close()