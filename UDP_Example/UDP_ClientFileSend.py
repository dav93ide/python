#------------------------------------#
#    	UDP CLIENT SEND FILE	     #
#------------------------------------#

import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Creo Oggetto File In Modalita` Lettura E Leggo Prima Riga
in_file = open("/root/Desktop/File","r")
text = in_file.readline()
i = 1;
while True :
	if text == "":
		break
	text = text[:-1]					# Tolgo Il Carattere A Capo
	sckt.sendto(("%d]"%i)+text,('localhost',9999))
	i+=1
	text = in_file.readline()
in_file.close()
sckt.sendto("END",('localhost',9999))
answer,addr = sckt.recvfrom(4096)
print "Ricevuto %s   \\  Da -> %s" % (answer,addr)