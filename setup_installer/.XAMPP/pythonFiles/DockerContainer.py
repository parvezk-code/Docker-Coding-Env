import subprocess
import json;

class ContainerException(Exception):
    def __init__(self, returncode, message="Can not start container"):
        self.cmdCode = returncode
        self.message = message
        super().__init__(self.message)
        
class InvalidServiceException(Exception):
    def __init__(self, message="Can not start container"):
        self.message = message
        super().__init__(self.message)


def runShellCmd(cmd):
	#p = subprocess.run(cmd, stdout=subprocess.PIPE, shell=False, text=True)
	p = subprocess.run(cmd, capture_output=True, shell=False, text=True)
	return p

class Container:
	
	# running, stopped, paused, restarting,	 
	
	def __init__(self, serviceName, dkComposeFile):
		self.serviceName	=	serviceName
		self.runCmd			= ["docker-compose", "-f", dkComposeFile, "up", "-d"]
		self.stopCmd		= ["docker-compose", "-f", dkComposeFile, "stop"]
		self.inspectStatusCmd = ["docker", "inspect", "--format={{.State.Status}}"]
		
		self.checkCreatedCmd = ["docker-compose", "-f", dkComposeFile, "ps", "-q"]
		self.runCmd.append(self.serviceName)
		self.stopCmd.append(self.serviceName)
		self.checkCreatedCmd.append(serviceName)
		
	def startContainer(self):
		cmdResult = runShellCmd(self.runCmd)
		if(cmdResult.returncode==0):
			return(True)
		else:
			raise ContainerException(cmdResult.returncode, cmdResult.stderr.strip())
			
	def stopContainer(self):
		cmdResult = runShellCmd(self.stopCmd)
		if(cmdResult.returncode==0):
			return(True)
		else:
			raise ContainerException(cmdResult.returncode, cmdResult.stderr.strip())

	def findContainer(self):
		cmdResult = runShellCmd(self.checkCreatedCmd)
		if(cmdResult.stdout!=""):
			return(cmdResult.stdout.strip())
		else:
			raise ContainerException(cmdResult.returncode, cmdResult.stderr.strip())
		
	def getContainerDetails(self):
		#running, exited, removed, invalid
		details = {}
		try:
			containerId = self.findContainer()
			details['Id'] = containerId
			cmd = self.inspectStatusCmd
			cmd.append(containerId)
			cmdResult = runShellCmd(cmd)
			details['status'] = cmdResult.stdout.strip()
			return(details)
		except ContainerException as e:
			#print(container['message'])
			if("No such service" in e.message):
				message = "service - " + self.serviceName + " does not exist in docker compose file"
				raise InvalidServiceException("nil", message)
				details['status'] ="invalid"
			else:
				details['status'] ="removed"
			return(details)

	def isStatusRunning(self):
		try:
			container = self.getContainerDetails()
			if(container['status']=="running"):
				return(True)
			else:
				return(False)
		except InvalidServiceException as e:
			return(False)
		
		
#a = Container("web", "../docker/docker-compose.yml")
#b = a.stopContainer()
#b = a.findContainer()
#b = a.getContainerDetails()
#print(b)
		
'''
	self.checkRunningCmd= ["docker-compose", "-f", dkComposeFile, "ps", "--filter", "status=running", "--services"]
	
	self.checkStoppedCmd= ["docker-compose", "-f", dkComposeFile, "ps", "--filter", "status=stopped", "--services"]
		
	#self.getStatusCmd	= ["docker", "inspect", "--format={{.State.Status}}", "mdb"]
	
	#self.removeCmd		= ["docker-compose", "-f", dkComposeFile, "rm", "-f"].append(serviceName)
	
	container status = created, running, stopped(exited), 
	runCmd= ["docker-compose", "-f", "../docker/docker-compose.yml", "up", "-d", "mariadb"]
	stop= ["docker-compose", "-f", "../docker/docker-compose.yml", "stop", "mariadb"]
	remove= ["docker-compose", "-f", "../docker/docker-compose.yml", "rm", "-f", "mariadb"]	
	
	stopped
	CompletedProcess(args=['docker-compose', '-f', '../docker/docker-compose.yml', 'ps', '--filter', 'status=stopped', '--services'], returncode=0, stdout='adminer\n', stderr='')
	CompletedProcess(args=['docker-compose', '-f', '../docker/docker-compose.yml', 'ps', '--filter', 'status=stopped', '--services'], returncode=0, stdout='\n', stderr='')
	
	running
	CompletedProcess(args=['docker-compose', '-f', '../docker/docker-compose.yml', 'ps', '--filter', 'status=running', '--services'], returncode=0, stdout='mariadb\nweb\n', stderr='')
	CompletedProcess(args=['docker-compose', '-f', '../docker/docker-compose.yml', 'ps', '--filter', 'status=running', '--services'], returncode=0, stdout='\n', stderr='')
	
	created
	CompletedProcess(args=['docker-compose', '-f', '../docker/docker-compose.yml', 'ps', '-q', 'adminer'], returncode=0, stdout='f8fca37948ce798a47674cc67bd4e8f58634ef5c2a2c8c127d1001d103da6730\n', stderr='')
	CompletedProcess(args=['docker-compose', '-f', '../docker/docker-compose.yml', 'ps', '-q', 'adminer'], returncode=0, stdout='', stderr='')
	
	
	
	self.getStatusCmd	= ["docker", "inspect", "--format={{.State.Status}}", "mdb"]
	runing
	CompletedProcess(args=['docker', 'inspect', '--format={{.State.Status}}', 'mdb'], returncode=0, stdout='running\n')
	CompletedProcess(args=['docker', 'inspect', '--format={{.State.Status}}', 'mdb'], returncode=0, stdout='running\n', stderr='')
	
	exited
	CompletedProcess(args=['docker', 'inspect', '--format={{.State.Status}}', 'admin'], returncode=0, stdout='exited\n')
	CompletedProcess(args=['docker', 'inspect', '--format={{.State.Status}}', 'admin'], returncode=0, stdout='exited\n', stderr='')
	
	no such service
	CompletedProcess(args=['docker', 'inspect', '--format={{.State.Status}}', 'admin'], returncode=1, stdout='\n')
	CompletedProcess(args=['docker', 'inspect', '--format={{.State.Status}}', 'admin'], returncode=1, stdout='\n', stderr='Error: No such object: mdb\n')
	
	
	
'''
