#!/bin/bash

#echo "Script executed from: ${PWD}"

export COMPOSE_FILE="/home/newuser/zz_mydata/zz_my/study/Linux_help/lab_seup/docker-compose.yml"
export PYTHON_CONTAINER_NAME="python10" 
export GCC_CONTAINER_NAME="gcc11" 
export JAVA_CONTAINER_NAME="java17" 

python_docker () {
	
	file_name=$1
	dir_path=$2
	
	echo "inside python $file_name  $dir_path"
	
	docker-compose --file "$COMPOSE_FILE" up -d "$PYTHON_CONTAINER_NAME"
   
	docker-compose --file "$COMPOSE_FILE" exec -w "$dir_path" "$PYTHON_CONTAINER_NAME"  python3 "$file_name"   
}

gcc_docker () { 
	
	file_name=$1
	dir_path=$2
	
	echo "inside gcc"
	
	docker-compose --file "$COMPOSE_FILE" up -d "$GCC_CONTAINER_NAME"

	docker-compose --file "$COMPOSE_FILE" exec -w "$dir_path" "$GCC_CONTAINER_NAME"  rm -f ./zz.out
   
	docker-compose --file "$COMPOSE_FILE" exec -w "$dir_path" "$GCC_CONTAINER_NAME"  gcc "$file_name"  -w -o ./zz.out
	
	docker-compose --file "$COMPOSE_FILE" exec -w "$dir_path" "$GCC_CONTAINER_NAME" ./zz.out
}


java_docker () { 
	
	file_name=$1
	dir_path=$2
	
	echo "inside java"
	
	docker-compose --file "$COMPOSE_FILE" up -d "$JAVA_CONTAINER_NAME"

	docker-compose --file "$COMPOSE_FILE" exec -w "$dir_path" "$JAVA_CONTAINER_NAME"  rm -f ./zz.out
   
	docker-compose --file "$COMPOSE_FILE" exec -w "$dir_path" "$JAVA_CONTAINER_NAME"  javac "$file_name"
	
	docker-compose --file "$COMPOSE_FILE" exec -w "$dir_path" "$JAVA_CONTAINER_NAME" java  "${file_name%.*}"
}

#geany  %f %d %d/%f %e 
#vscode ${fileBasename} ${fileDirname} ${file} ${fileExtname} 
fullfileName=$1		# ${fileBasename}  %f  
fileDir=$2			# ${fileDirname}   %d
filePath=$3			# ${file}          %d/%f
fileExtension=$4	# ${fileExtname}   "${$1##*.}"
fileName="${fullfileName%.*}" 

#echo $fullfileName
#echo $fileDir
#echo $fileExtension   #echo "${fullfileName##*.}"
#echo $filePath
#echo $fileName


if [ $fileExtension = ".c" ] ; then
	gcc_docker  $fullfileName  $fileDir
elif [ $fileExtension = ".java" ] ; then
	java_docker $fullfileName  $fileDir
elif [ $fileExtension = ".py" ] ; then
	python_docker  $fullfileName  $fileDir
else
   echo "invalid"
fi
