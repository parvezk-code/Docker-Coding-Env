import tkinter as tk
from tkinter import ttk
import time

# https://lobster1234.github.io/2019/04/05/docker-socket-file-for-ipc/
#https://www.postman.com/api-evangelist/workspace/docker/documentation/35240-f3bb4204-5a72-43c6-9bda-f2caed87250d
# https://docs.docker.com/engine/api/v1.37/#operation/ContainerList
# https://docs.docker.com/engine/api/v1.37/#operation/ContainerCreate
# https://docs.docker.com/engine/api/v1.37/#operation/ContainerStart
# https://docs.docker.com/engine/api/v1.37/#operation/ContainerStop
# https://docs.docker.com/engine/api/v1.37/#operation/ContainerRestart
# https://docs.docker.com/engine/api/v1.37/#operation/ContainerPrune
class ServiceComponent:
	
	RUNNING	= "Running"
	STOPPED	= "Stopped"
	STARTING= "Starting"
	STOPPING= "Stopping"
	START	= "Start"
	STOP 	= "STOP"
	
	def __init__(self, name, parent, rowNum, onClickStart):
		self.label		= ttk.Label(parent, text=name)
		self.status		= ttk.Label(parent, text=self.STOPPED)
		self.startButton= ttk.Button(parent, text=self.START, command=onClickStart)
	  
		self.label.grid(column =0, row=rowNum, sticky=tk.NS, padx=5, pady=5)
		self.status.grid(column=1, row=rowNum, sticky=tk.NS, padx=5, pady=5)
		self.startButton.grid(column=2, row=rowNum, sticky=tk.NS, padx=5, pady=5)
		
	  
	def disableStartButton(self):
		self.startButton.state(['disabled'])
	  
	def enableStartButton(self):
		self.startButton.state(['!disabled'])
	
	def setStartButtonText(self, newText):
		self.startButton['text'] = newText 
	
	def setStatusText(self, newText):
		self.status["text"] = newText
	
	def changeUIStateToStarting(self):
		self.setStatusText(self.STARTING)
		self.setStartButtonText(self.STARTING)
		self.disableStartButton()
		
	def changeUIStateToRunning(self):
		self.setStatusText(self.RUNNING)
		self.setStartButtonText(self.STOP)
		self.enableStartButton()

	def changeUIStateToStopping(self):
		self.setStatusText(self.STOPPING)
		self.setStartButtonText(self.STOPPING)
		self.disableStartButton()				

	def changeUIStateToStopped(self):
		self.setStatusText(self.STOPPED)
		self.setStartButtonText(self.START)
		self.enableStartButton()		

	def isComponentStopped(self):
		if(self.status["text"]==self.STOPPED):
			return(True)
		else:
			return(False)

class TestClass(tk.Tk):
	def __init__(self):
		super().__init__()
		self.geometry("300x120")		#specify window size
		self.title('Admin Panel')		#windows title
		self.resizable(0, 0)
		#self.configure(background='black')
		
		# configure the grid for 4 column
		self.columnconfigure(0, weight=1)  # first column
		self.columnconfigure(1, weight=1)  # Second column
		self.columnconfigure(2, weight=1)  # Three column
		#self.columnconfigure(3, weight=1)  # Fourth column
		
		self.create_widgets()
	
	def create_widgets(self):
		#time.sleep(1)
		self.apacheCmp	= ServiceComponent("Apache", self, 0, self.onClickStartApache)

	def updateUI(self):
		self.update()
		
	def onClickStartApache(self):
		if(self.apacheCmp.status["text"]==self.apacheCmp.STOPPED):
			self.apacheCmp.changeUIStateToStarting()
			self.updateUI()
			time.sleep(3)
			self.updateUI()
			self.apacheCmp.changeUIStateToRunning()
		elif(self.apacheCmp.status["text"]==self.apacheCmp.RUNNING):
			self.apacheCmp.changeUIStateToStopping()
			self.updateUI()
			time.sleep(3)
			self.updateUI()
			self.apacheCmp.changeUIStateToStopped()
		else:
			time.sleep(1)


#app = TestClass()
#app.mainloop()
