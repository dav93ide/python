#------------------#
#    UDP CLIENT    #
#------------------#

import socket

target_host = 'localhost'
target_port = 9999

# SOCK_DGRAM -> UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Invio Dati Senza Creare Connessione
client.sendto("END",(target_host,target_port))

#Ricevo Indirizzo E Dati
data,addr = client.recvfrom(4096)

print "Ricevuto %s   \\  Da  -> %s" % (data,addr)

client.close()