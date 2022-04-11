import tkinter as tk
import time
from pythonFiles.DockerContainer import Container
from pythonFiles.DockerContainer import ContainerException
from pythonFiles.UiComponent import ServiceComponent		
import os

class App(tk.Tk):
	def __init__(self, dockComposeFile):
		super().__init__()
		self.geometry("300x120")			#specify window size
		self.title('Admin Panel')			#windows title
		self.resizable(0, 0)
		
		# configure the grid for 4 column
		self.columnconfigure(0, weight=1)  	# first column
		self.columnconfigure(1, weight=1)  	# Second column
		self.columnconfigure(2, weight=1)  	# Three column
		#self.columnconfigure(3, weight=1)  # Fourth column
		self.createServices(dockComposeFile)
		self.create_widgets()

	def createServices(self, dockComposeFile):		
		self.apacheService		= Container("apache",  dockComposeFile)
		self.databaseService	= Container("mariadb", dockComposeFile)
		self.adminerService		= Container("adminer", dockComposeFile)

	def create_widgets(self):		 
		self.apacheCmp		= ServiceComponent("Apache",   self, 0, self.startStopApache)
		self.databaseCmp	= ServiceComponent("MySQL" ,   self, 1, self.startStopDatabase)
		self.AdminerCmp		= ServiceComponent("Adminer" , self, 2, self.startStopAdminer)
		
		self.updateComponent(self.apacheService,   self.apacheCmp)
		self.updateComponent(self.databaseService, self.databaseCmp)
		self.updateComponent(self.adminerService,  self.AdminerCmp)		
	
	def updateComponent(self, service, component):
		if(service.isStatusRunning()):
			component.changeUIStateToRunning()
			self.updateUI()	
	
	def updateUI(self):
		self.update()
	
	def startStopDatabase(self):
		self.startStopService(self.databaseService, self.databaseCmp)
		
	def startStopAdminer(self):
		self.startStopService(self.adminerService, self.AdminerCmp)
		
	def startStopApache(self):
		self.startStopService(self.apacheService, self.apacheCmp)

	def startStopService(self, service, component):
		if(component.isComponentStopped()):
			component.changeUIStateToStarting()
			self.updateUI()
			try:
				service.startContainer()
				self.updateUI()
				component.changeUIStateToRunning()
				self.updateUI()
			except ContainerException as e:
				print(e.message, e.cmdCode)
				self.updateUI()
				component.changeUIStateToStopped()
				self.updateUI()
		else:
			component.changeUIStateToStopping()
			self.updateUI()
			try:
				service.stopContainer()
				self.updateUI()
				component.changeUIStateToStopped()
				self.updateUI()
			except ContainerException as e:
				print(e.message, e.cmdCode)
				self.updateUI()
				component.changeUIStateToRunning()
				self.updateUI()

if __name__ == "__main__":
	
	try:
		docker_compose_file = os.environ["LAB_1234_COMPOSE_FILE"]
		app = App(docker_compose_file)
		app.mainloop()
	except KeyError as e:
		print("key missing ", e)
		print("Check $HOME/.profile and .bascrc for environment variables")
	except Exception as e:
		print(e)
