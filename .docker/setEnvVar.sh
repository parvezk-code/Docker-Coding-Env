#!/bin/bash

# ROOT(lab_setup) ---> {install.sh, docker, command_scripts, code}

CUREENT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
CODE_DIR_NAME=".code"
CMD_SCRIPTS_DIR=".command_scripts"
DOCKER_DIR_NAME=".docker"
XAMPP_DIR_NAME=".XAMPP"
XAMPP_DESKTOP_FILE="XAMPP.desktop"
COMPOSE_FILE_NAME="docker-compose.yml"
ENV_FILE_NAME="setEnvVar.sh"
LOG_FILE_NAME="labContainer.log"

export LAB_1234_ROOT="$(dirname "$CUREENT_DIR")"

export LAB_1234_COMPOSE_FILE=$LAB_1234_ROOT/$DOCKER_DIR_NAME/$COMPOSE_FILE_NAME

export LAB_1234_ENV_FILE=$LAB_1234_ROOT/$DOCKER_DIR_NAME/$ENV_FILE_NAME

export PATH=$LAB_1234_ROOT/$CMD_SCRIPTS_DIR:$PATH 

export LAB_1234_PYTHON_CONTAINER_NAME="python10" 

export LAB_1234_GCC_CONTAINER_NAME="gcc11" 

export LAB_1234_JAVA_CONTAINER_NAME="java17" 

export LAB_1234_CONTAINER_USER_HOME="/home/newuser"

export LAB_1234_LOG_FILE="$(dirname "$LAB_1234_ROOT")"/$LOG_FILE_NAME

export LAB_1234_XAMPP_FILE=$LAB_1234_ROOT/$XAMPP_DIR_NAME/App.py

