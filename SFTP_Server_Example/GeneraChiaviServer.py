import sys
import os
import paramiko

rsa_bits = 3072
dss_bits = 1024

rsa_NomeFileChiave = "server_rsa_key"
dss_NomeFileChiave = "server_dss_key"

def show_progress(s):
	sys.stdout.write("... " + s)
    sys.stdout.flush()
	
def main():
	stato = 0
	
	# Controllo Se Il File Con Chiave RSA Privata E Pubblica Esiste
	if os.path.exists(rsa_NomeFileChiave):
		print >>sys.stderr, "%s Esiste Gia'.  Non Sara' Creata Chiave Host RSA." % (rsa_NomeFileChiave)
        stato = 2
		
	elif os.path.exists(rsa_NomeFileChiave + ".pub"):
		print >>sys.stderr, "%s Esiste Gia'.  Non Sara' Creata Chiave Host DSS." % (rsa_NomeFileChiave + ".pub")
        stato = 2
	else:
		print "Creando %d-bit Chiave Host RSA ..." % (rsa_bits,)
		# Genero La Chiave RSA Passando Grandezza In Bits E Funzione Progresso Operazione
        chiaveRsa = paramiko.RSAKey.generate(bits=rsa_bits, progress_func=show_progress)
        print "... Scrivendo %s" % (rsa_NomeFileChiave)
		# Scrivo La Chiave RSA Privata Su File
        chiaveRsa.write_private_key_file(rsa_NomeFileChiave)
        print "... Scrivendo %s" % (rsa_NomeFileChiave + ".pub")
		# Scrivo La Chiave RSA Pubblica In Formato: NomeChiave ChiaveCodificataBase64
        open(rsa_NomeFileChiave + ".pub", "w").write("%s %s\n" % (chiaveRsa.get_name(), chiaveRsa.get_base64()))
		# Cancello La Chiave
        del chiaveRsa
        print "... Eseguito!"
		
	# Controllo Se Il File Con Chiave DSS Privata E Pubblica Esiste
	if os.path.exists(dss_NomeFileChiave):
        print >>sys.stderr, "%s already exists.  Not generating DSS host key." % (dss_NomeFileChiave)
        stato = 2
    elif os.path.exists(dss_NomeFileChiave + ".pub"):
        print >>sys.stderr, "%s already exists.  Not generating DSS host key." % (dss_NomeFileChiave + ".pub")
        stato = 2
    else:
        print "Creando %d-bit Chiave Host DSS ..." % (dss_bits,)
		# Genero La Chiave DSS Passando Grandezza In Bits E Funzione Progresso Operazione
        chiaveDss = paramiko.DSSKey.generate(bits=dss_bits, progress_func=show_progress)
        print "... Scrivendo %s" % (dss_NomeFileChiave)
		# Scrivo La Chiave DSS Privata Su File
        chiaveDss.write_private_key_file(dss_NomeFileChiave)
        print "... Scrivendo %s" % (dss_NomeFileChiave + ".pub")
		# Scrivo La Chiave DSS Pubblica Su File
        open(dss_key_filename + ".pub", "w").write("%s %s\n" % (chiaveDss.get_name(), chiaveDss.get_base64()))
        del chiaveDss
        print "... Eseguito!"
	
	sys.exit(stato)
		
if __name__ == '__main__':
	main()
	