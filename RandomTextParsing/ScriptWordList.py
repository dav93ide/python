# Toglie Tutte Le Parole Dalla Word-List Con Lunghezza Inferiore A "n"
import os









if __name__ == '__main__':
	print "[+] Path Corrente: %s\n\n" %os.getcwd()
	print "[+] Eliminazione Parole Da Word-List Con Len(Parola) < n\n+ Inserire Valore Di n"
	n = int(raw_input('#\> '))
	print "\n[+] Inserire Nome File O Path Assoluto Del File \"Word-List\"\n"
	fileName = raw_input('#\> ')
	print "\n[+] Inserire Nome File O Path Assoluto Del NUOVO File \"Word-List\"\n"
	newFile = raw_input('#\> ')
	
	for line in open(fileName,'r').xreadlines():
		if len(line) >= n:
			with open(newFile,'a') as fw:
				fw.write("%s\n" % line[:-1])

	print "\n\n[+] Operazione Completata... Premere Invio Per Uscire..."
	os.system("cls")
	raw_input()