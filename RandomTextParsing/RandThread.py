import threading
import random
import os
from Tkinter import END
from NewWindow import *
from ThreadEventHandler import ThreadEventsHandler

class RandThread(threading.Thread):

	def __init__(self,fileName1,fileName2,fileName3,charNum):
		self.text = [fileName1,fileName2,fileName3]
		self.eventHandler = ThreadEventsHandler()
		threading.Thread.__init__(self)
		self.rangChr = charNum
		self.txtArea = newWindow(self.getName()).initNewTextAreaWindow()

	def getHandler(self):
		return self.eventHandler
		
	def getParsingEventHandler(self):
		return self.pEHandler
		
	def setParsingEventHandler(self,parsingThreadEventsHandler):
		self.pEHandler = parsingThreadEventsHandler
	
	def firstRun(self,rng):
		for tx in self.text:
			if not os.path.isfile(tx):
				self.txtArea.insert(END, "[+] The document: \"%s\" has not been found...\n\t[+] Generating: \"%s\"...\n" % (tx,tx))
				file = open(tx,'w')
				for i in range(0,self.rangChr):
					file.write(chr(random.choice(rng)))
				file.close()
				self.txtArea.insert(END, "\t[+] The document: \"%s\" has been generated...\n" % tx)
			else:
				self.txtArea.insert(END, "[+] The document: \"%s\" has been found...\n" % tx)
				pass
			self.sendEvent(self.text.index(tx))
		self.txtArea.insert(END, "[+] firstRun Function execution ended...\n\n" +
				"[---------------------------------------------------------------------------------------------]\n\n\n")
	
	def sendEvent(self,evt):
		if evt == 0:
			self.pEHandler.set(ThreadEventsHandler.ONE_READY)
			self.txtArea.insert(END,"[+] %s has sent event: ONE_READY...\n" % self.getName())
		elif evt == 1:
			self.pEHandler.set(ThreadEventsHandler.TWO_READY)
			self.txtArea.insert(END,"[+] %s has sent event: TWO_READY...\n" % self.getName())
		elif evt == 2:
			self.pEHandler.set(ThreadEventsHandler.THREE_READY)
			self.txtArea.insert(END,"[+] %s has sent event: THREE_READY...\n" % self.getName())
	
	def run(self):
		self.txtArea.insert(END,"[---------------------------------------------------------------------------------------------]\n\t\t\t\t[+] %s_Message_Window [+]\n[---------------------------------------------------------------------------------------------]\n\n" % self.getName() )
		rng = range(48,58)
		rng.extend(range(65,91))
		rng.extend(range(97,122))
		self.firstRun(rng)
		while True:
			numReaded = None
			self.txtArea.insert(END,"[+] %s is waiting a event...\n" % self.getName())
			eventType = self.eventHandler.wait()
			self.txtArea.insert(END,"[+] %s got the event: %d...\n" % (self.getName(),eventType) )
			if eventType == ThreadEventsHandler.READED_ONE:
				self.txtArea.insert(END,"[+] %s has received event: 'READED_ONE'\n" % self.getName())
				numReaded = 0
			elif eventType == ThreadEventsHandler.READED_TWO:
				self.txtArea.insert(END,"[+] %s has received event: 'READED_TWO'\n" % self.getName())
				numReaded = 1
			elif eventType == ThreadEventsHandler.READED_THREE:
				self.txtArea.insert(END,"[+] %s has received event: 'READED_THREE'\n" % self.getName())
				numReaded = 2
			if numReaded != None:
				self.txtArea.insert(END,"\t[+] %s is re-making: %s...\n" % (self.getName(),self.text[numReaded]))
				file = open(self.text[numReaded],'w')
				for i in range(0,self.rangChr):
					file.write(chr(random.choice(rng)))
				file.close()
				self.sendEvent(numReaded)
				


