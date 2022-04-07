#!/bin/bash

#1 copy lab_setup directory inside your $PROJECT_ROOT directory.

source ./.docker/setEnvVar.sh

# for testing uncomment these files
#echo $LAB_1234_ROOT
#echo $LAB_1234_COMPOSE_FILE
#echo $LAB_1234_ENV_FILE
#echo $LAB_1234_LOG_FILE
#echo $LAB_1234_ROOT/$CMD_SCRIPTS_DIR
#exit

#2 copy dir(code) to dir $PROJECT_ROOT directory.
cp -R "$LAB_1234_ROOT/$CODE_DIR_NAME"  "$(dirname "$LAB_1234_ROOT")"/code
chmod 777 -R "$(dirname "$LAB_1234_ROOT")"/code

#3 export environment variables inside the $HOME/.bashrc file
if ! grep -q "$LAB_1234_ENV_FILE" "$HOME/.bashrc"; then
	echo " " >> $HOME/.bashrc
	echo "# following line is added for cse lab setup using docker">> $HOME/.bashrc
	echo "source $LAB_1234_ENV_FILE" >> $HOME/.bashrc
fi

#4 hidden mode. change permissions to read only. can not delete
# chmod 555 -R $DOCKER_DIR_NAME  $CMD_SCRIPTS_DIR  $CODE_DIR_NAME

#5 change the exports inside the file command_scripts/main


