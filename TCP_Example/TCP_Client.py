#------------------#
#    TCP CLIENT    #
#------------------#


import socket

target_host = "0.0.0.0"
target_port = 9999
# Creazione di un oggetto socket
# AF_INET -> utilizzo indirizzo standard IPv4 o hostname
# SOCK_STREAM -> indica client TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send("Ciao!")
response = client.recv(4096)
if(response != ""):
	print response
else:
	print "No Response..."
