from RandThread import RandThread
from ParsingThread import ParsingThread
from ThreadEventHandler import ThreadEventsHandler
import os

if __name__ == '__main__':
	os.system("cls")
	print \
	"/-----------------------------------------------------------------------------\\\n" \
	"\t\t\t=[>     Ordo Ab Chao      <]=\n" \
	"\\-----------------------------------------------------------------------------/\n\n\n" \
	"/-----------------------------------------------------------------------------\\\n" \
	"\t< Searching Words Of A Word-List From 3 Text-File\n\t\t Which Contains n Pseudo-Random Generated Characters >\n" \
	"\\-----------------------------------------------------------------------------/\n\n\n"
	print "[+] The Current Path Is: %s\n" %os.getcwd()
	print "[+] Use An Absolute Path When Declaring The Files In Order To Change The Final Directory...\n\n\n"
	Error = ""
	while True:
		if Error:
			print "\n\n[+] Sono Stati Incontrati I Seguenti Errori Negli Input Precedenti:\n%s" % Error
		Error = ""
		print "[+] Welcome!\n\n We're Going To Take Some Inputs Now!\n Please Digit help Or pass If U Need Help Or U Already Know How It Works And U Want To Continue...\n"
		chs = raw_input("#\> ")
		if chs == 'help':
			print \
			"\n\n\n/-----------------------------------------------------------------------------\\\n" \
			"[+] Usage:\n\t- The words file, the one used to finds words in the random-files, must has only one word for each line with an empty line in the end of the file...\n\t- The ParsingThread will parse all the random-files one by one and he will send a message, using the ThreadEventHandler, to the RandThread in order to say to him that he has finish to parse a file. When the RandThread receives an event-message he will check the type of this message so he can replace the already parsed random-file with a new file consist of random characters...\n\t- Idk why I had use 3 random-files to do these operations, but well maybe it will decrease the random approximation (it's a pseudo-random algorithm so after a long spin he will start to generate sometimes the same numbers...) Otherwise it's easy to change this configuration, you only need to delete the event-messages for the files that u don't want will be created ;)\n\n\t- I'm Really Sorry For My Bad English >:( \n\n" \
			"\\-----------------------------------------------------------------------------/\n\n\n"
		print "[+] Insert name or absolute path for output random file01 [.txt]...\n"
		fileName1 = raw_input('#\> ')
		print "[+] Insert name or absolute path for output random file02 [.txt]...\n"
		fileName2 = raw_input('#\> ')
		print "[+] Insert name or absolute path for output random file03 [.txt]...\n"
		fileName3 = raw_input('#\> ')
		print "[+] Insert the name or the absolute path for the word-list file (.txt)...\n\t[+] The one used to finds words in the random-files...\n"
		searchFile = raw_input("#\> ")
		print "[+] Insert the name or the absolute path for the output file (.txt)...\n"
		outputFile = raw_input("#\> ")
		print "[+] Insert the number of characters to print in the random-files...\n"
		rangChr = raw_input("#\> ")
		for i in (fileName1[-4:],fileName2[-4:],fileName3[-4:],searchFile[-4:],outputFile[-4:]):
			if '.txt' != i:
				Error += "+ Input Error: %s Has Not .txt Extension!\n" % i
		if not os.path.isfile(searchFile):
			Error += "+ Input Error: The words file must exist!\n"
		list = [fileName1,fileName2,fileName3,searchFile,outputFile]
		for n in list:
			list2 = list
			del list[list.index(n)]
			if n in list2:
				Error += "+ Input Error: %s, Another File Has The Same Name, All Files Must Have Different Names!\n" % n
		try: 
			rangChr = int(rangChr)
		except:
			Error += "+ Input Error: The Number Of Characters Must Be An Integer Number!\n"
		if not Error:
			break;
	print "\n[+] All Inputs Have Been Confirmed...\n"
	RandT = RandThread(fileName1,fileName2,fileName3,rangChr)
	RandT.setName("RandThread")
	ParsT = ParsingThread(fileName1,fileName2,fileName3,searchFile,outputFile)
	ParsT.setName("ParseThread")
	RandT.setParsingEventHandler(ParsT.getHandler())
	ParsT.setRandThreadEventsHandler(RandT.getHandler())
	RandT.start()
	ParsT.start()


	while True:
		print "\n[+] All Threads Started...\n[+] Close The Window To Stop The Parsing...\n"
		i = int(raw_input())
		if i:
			print "[+] No Input Allowed...\n"