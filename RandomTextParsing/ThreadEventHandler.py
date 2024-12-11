import threading
import time
import random

class ThreadEventsHandler():
	NONE = 0
	READED_ONE = 1
	READED_TWO = 2
	READED_THREE = 3
	ONE_READY = 4
	TWO_READY = 5
	THREE_READY = 6
	
	def __init__(self):
		self.event = threading.Event()
		self.eventQueue = []
		self.wordQueue = []
	
	def set(self,event_type):
		self.eventQueue.append(event_type)
		return self.event.set()
		
	def setWord(self,word):
		print "Word Added: %s\n" % word
		self.wordQueue.append(word)
	
	def getWord(self):
		print "Word Poped\n"
		return self.wordQueue.pop(0)
		
	def wait(self,case=0):
		while not self.eventQueue:
			self.event.wait()
		return self.eventQueue.pop(0)
