import threading
from RandThread import *
from ThreadEventHandler import ThreadEventsHandler
import time
from NewWindow import *
from Tkinter import END

class ParsingThread(threading.Thread):
	
	def __init__(self,fileName1,fileName2,fileName3,searchFile,outputFile):
		self.text = [fileName1,fileName2,fileName3]
		self.eventHandler = ThreadEventsHandler()
		threading.Thread.__init__(self)
		self.searchFile = searchFile
		self.outputFile = outputFile
		self.txtArea = newWindow(self.getName()).initNewTextAreaWindow()
		
	def getHandler(self):
		return self.eventHandler

	def getRandThreadEventsHandler(self,randThreadEventsHandler):
		return self.sTEHandler
		
	def setRandThreadEventsHandler(self,randThreadEventsHandler):
		self.rTEHandler = randThreadEventsHandler
		
	def sendEvent(self,evt):
		if evt == 0:
			self.rTEHandler.set(ThreadEventsHandler.READED_ONE)
			self.txtArea.insert(END,"[+] %s has sent event: READED_ONE...\n" % self.getName())
		elif evt == 1:
			self.rTEHandler.set(ThreadEventsHandler.READED_TWO)
			self.txtArea.insert(END,"[+] %s has sent event: READED_TWO...\n" % self.getName())
		elif evt == 2:
			self.rTEHandler.set(ThreadEventsHandler.READED_THREE)
			self.txtArea.insert(END,"[+] %s has sent event: READED_THREE...\n" % self.getName())
	
	def initConfig(self):
		maxLen = 0
		minLen = 100
		for line in open(self.searchFile,'r').xreadlines():
			if maxLen < len(line[:-1]):
				maxLen = len(line[:-1])
			if minLen > len(line[:-1]):
				minLen = len(line[:-1])
		self.maxLen = maxLen
		self.minLen = minLen
		print "\n[+] WordMaxLen In Word-List: %d\n" % self.maxLen
		print "[+] Word MixLen In Word-List: %d\n" % self.minLen
			
	def run(self):
		self.txtArea.insert(END,"[---------------------------------------------------------------------------------------------]\n\t\t\t\t[+] %s_Message_Window [+]\n[---------------------------------------------------------------------------------------------]\n\n[+] Parsing Started...\n\n" % self.getName())
		self.initConfig()
		lastFound = []
		
		cnt = 0
		cnt2 = 0
		
		while True:
			self.txtArea.insert(END,"[+] %s is waiting a event...\n" % self.getName() )
			eventType = self.eventHandler.wait()
			self.txtArea.insert(END,"[+] %s got the event: %d...\n" % (self.getName(),eventType) )
			if eventType in range(4,7):
				index = eventType - 4
				self.txtArea.insert(END,"[+] %s is parsing: %s...\n" % (self.getName(),self.text[index]) )
				str = ""
				filepars = open(self.text[index],'r')
				while True:
					chr = filepars.read(1)
					if not chr:
						filepars.close()
						self.sendEvent(index)
						self.txtArea.insert(END,"[+] %s has finished to parsing: %s...\n" % (self.getName(),self.text[index]) )
						break
					str += chr
					if len(str) >= self.minLen:
						for line in open(self.searchFile,'r').xreadlines():
							if (line[:-1] in str.lower()):
								if not line[:-1] in lastFound:
									self.txtArea.insert(END,"[+] %s has found the word: %s" % (self.getName(),line))
									cnt += 1
									if self.outputFile[-4] == '.':
										fileName = self.outputFile[:-4] + "%d.txt" % cnt2
									if (cnt % 10000) == 0:
										cnt2+=1
									with open(fileName,'a') as fw:
										# Se si vogliono solo le parole trovate (una per linea)
										fw.write("%s\n" % line[:-1])
										# Se si vogliono le parole trovate e la stringa in cui sono state trovate (rallenta esecuzione)
										#fw.write("%s::in::%s\n" % (line[:-1],str))
									lastFound.append(line[:-1])
									break
					if len(str) == self.maxLen:
						str = str[1:]
					if lastFound:
						if not lastFound[0] in str.lower():
							del lastFound[0]
