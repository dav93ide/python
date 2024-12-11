import os


def parse_and_write(parsefilename, writefilename, verbose):
	if not os.path.exists("%s//%s" % (os.path.dirname(os.path.abspath(__file__)), writefilename)):
		final = open(writefilename,'w')
		print "- %s Opened In Write Mode" % writefilename
	else:
		final = open(writefilename,'a')
		print "- %s Opened In Append Mode" % writefilename
	c = 1
	count = 0
	for checkline in open( parsefilename, 'r').xreadlines():
		control = False
		if verbose:
			print "- Start Checking Word Number %d :: %s" % (c, checkline)
		elif count%5000 == 0:
			print "\n[{%d} Entry Controllate ]\n" % count
		for line in open( writefilename, 'r'):
			if checkline == line:
				control = True
		if not control:
			final.write("%s\n" % checkline[:-2])
			count+=1
		c += 1
	return count
	
def setting_up_input():
	numList = int(raw_input("[+] Please Insert Number Of WordList Files: "))
	print "[+]Setting Della Configurazione Per Parsing Delle %d Wordlists...\n\n\n" % numList
	choose = raw_input("[?]Wordlist Con Nome Diverso O In Path Differenti Rispetto Alla Work Directory? [y/n]\n ")
	wlists = []
	for n in range(1,numList):
		if choose == "y":
			if raw_input("[?]Usare Percorso Della Work Directory? [y/n]\n") == "y":
				t = raw_input("# Inserire Nome Della Wordlist (filepath/filename)\n=> ")
				wlists.append(t)
			else:
				t = raw_input("# Inserire Percorso E Nome Della Wordlist? (filepath/filename)\n=> ")
				n = 0;
				for l in t:
					if l == "/":
						t = "%s/%s" (t[:n],t[n:])
					n++1
				wlists.append(t)
		else:
			wlists.append("wordlist%d"%n)
	return wlists

def setting_up_output():
	if raw_input("[?]Personalizzare Nome File Finale? [y/n]\n ") == "y":
		t = raw_input("# Inserire Nome Del File\n=> ")
		finalname = t
	else:
		finalname = "finalwordlist"
	return finalname	

if __name__ == '__main__':
	print "########################################################################################" \
	"\n" \
	"				|x| WordList Parser |x|" \
	"\n\n" \
	"#Features:\n" \
	"	Parsing Di n Wordlist E Generazione Finale Di Una Wordlist Priva Di Parole Doppie\n" \
	"#Usage:\n" \
	"	Le Wordlist Devono Contenere Una Sola Parola Per Riga"	\
	"\n\n" \
	"########################################################################################" \
	"\n\n"
	while True:
		wlists = setting_up_input()
		finalname = setting_up_output()
		print "\n\n[+]Setting Delle Opzioni Completato.\n"
		print "[+]Nomi Delle Wordlist In Input:"
		n = 0
		print "#########################"
		for nl in wlists:
			print "#%d]	%s" % (n,nl)
			n += 1
		print "#########################\n"
		print "[+]La Wordlist Finale Verra` Generata In: %s\n\n\n" % ("%s/%s" % (os.path.dirname(os.path.abspath(__file__)),finalname))
		if raw_input("[?]Verbose Mode? [y/n]\n") == "y":
			verbose = True
		else:
			verbose = False
		if raw_input("[?]Avviare Il Processo? [y/n]\n") == "y":
			break
		
	os.system("clear");
	print "[>!<] Processo Avviato [>!<]\n\n"
	for nl in wlists:
		print "[+]Avvio Parsing Della Wordlist %s...\n\n" % nl
		c = parse_and_write(nl, "temp", verbose)
		os.system("clear");
		print "[+]Parsing Della Wordlist Numero %d Completato!\n" % n
		print "[+]Numero Di Parole Aggiunte Alla Wordlist Finale: %d.\n\n" % c
		n += 1
	print "[+]Avvio Parsing Della Wordlist Finale..."
	c = parse_and_write("temp", finalname, verbose)
	os.remove("temp")
	print "[+]Parsing Della Wordlist Finale Completato!"
	print "[+]Numero Di Entry Nella Wordlist Finale: %d." % n
	





			
