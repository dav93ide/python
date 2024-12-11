import Tkinter

class newWindow(Tkinter.Frame):
	
	def __init__(self,name):
		self.tk = Tkinter.Tk()
		self.tk.title(name)
		self.tk.protocol("WM_DELETE_WINDOW", self.tk.iconify)
		
	def initNewTextAreaWindow(self):
		Scrllbar = Tkinter.Scrollbar(self.tk)
		Txt = Tkinter.Text(self.tk, height=25,width=100)
		Scrllbar.pack(side=Tkinter.RIGHT,fill=Tkinter.Y)
		Scrllbar.config(command=Txt.yview)
		Txt.config(yscrollcommand=Scrllbar.set)
		Txt.pack(side=Tkinter.LEFT,fill=Tkinter.X)
		Txt.insert(Tkinter.END,"\n")
		
		return Txt