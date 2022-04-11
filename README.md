# Docker-Coding-Env
Docker Coding Environment

Steps to setup lab
	
	=> install rootless docker
		--> https://rootlesscontaine.rs/getting-started/docker/  
		--> https://docs.docker.com/engine/security/rootless/
	
	=> install rootless docker compose : 
		--> https://github.com/docker/compose/  
		--> https://github.com/docker/compose/releases 
  
		--> curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o $HOME/bin/docker-compose
			
	=> run install.sh script to perform settings to run lab setup
	
	=> pull all images needed by docker-complose.yml
	 
	=> copy vs-codium app image from :  
		--> https://github.com/VSCodium/vscodium/releases

Architecture of this setup

	=> 3-components :  setEnvVar.sh, docker-compose.yml, proxy commands

	=> setEnvVar.sh export environment variables needed by other components.

	=> docker-compose.yml creates/manage conatiners.

	=> proxy commands intercept the actual commands and redirect them to the conatiners.

How does this setup work (docker-compose, set_env_bashrc, proxy cmds )

	=> create conatiners from docker-compose file

	=> scripts inside dir(.command_scripts) intersecpt java, gcc, python commands

	=> these intersecpted(proxy) commands execute actual commands on the conatiners

	=> update $PATH in .bashrc to redirect commands to dir(.command_scripts)

	=> update .bashrc/.profile to expose environment variables needed by proxy script.

	=> create .desktop file for XAMPP UI at Desktop

Steps to install a new language inside this lab setup

	=> export environment variables inside .docker/setEnvVar.sh script
		  LAB_1234_XXX_CONTAINER_NAME
		  LAB_1234_XXX_SHARE_DIR

	=> add the new service inside docker-compose file

	=> create command intersecpter inside directory(command_scripts)

Steps to install a new docker-compose file

	=> add the new docker-compose file to directory  ./poly_cse/.docker

	=> export path of new docker-compose file inside ./poly_cse/.docker/setEnvVar.sh
	      export LAB_1234_MERN_COMPOSE_FILE = ..............
		  export LAB_1234_MERN_CONTINER_NAME= ..............

	=> create proxy scripts for intercepting the commands

Steps To remove this setup

	=> remove line from $HOME/.bashrc and $HOME/.profile
			source /home/........./.docker/setEnvVar.sh

	=> remove directory(code)

	=> docker-compose down

	=> docker rm $(docker ps -a -f status=created -q)

	=> docker rm $(docker ps -a -f status=exited -q)

	=> remove all container images

	=> remove directory containing setup/installation files

	=> remove XAMPP.desktop file from desktop

Copy docker images from one computer to another

	=> docker save  <image_name>  -o $HOME/image_name.tar

	=> docker load -i image_name.tar

The docker-compose.yml containes following container services

	=> apache	(php:7.2-apache)

	=> mariadb	(mariadb:10.7.3-focal)

	=> adminer	(adminer)

	=> python10	(python:3.10.4-bullseye)

	=> gcc11	(gcc:11.2-bullseye)

	=> java17	(openjdk:jdk)

	=> portainer(portainer/portainer-ce)
	
	=> vscodeserver (codercom/code-server) : need more configuration