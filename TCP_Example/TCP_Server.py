#------------------#
#    TCP SERVER    #
#------------------#

import socket
import threading
bind_ip = "0.0.0.0"
bind_port = 9999

# Creo la Socket E Passiamo IP,Porta Al Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))

# Ascolta Per Un Massimo Di 5 Connessioni
server.listen(5)

print "[*] In Ascolto Su %s:%d" % (bind_ip,bind_port)

# Thread Gestione Client
def handle_client(client_socket):
	request = client_socket.recv(1024)
	print "[*] Ricevuto : %s" % request
	client_socket.send("ACK!")
	client_socket.close()

while True:
	client,addr = server.accept()
	print "[*] Accettata Connessione Da %s:%d" % (addr[0],addr[1])
	# Avviamo Il Thread Per Il Client
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()