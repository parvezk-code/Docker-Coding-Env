#!/bin/sh 

# this file is entry point for docker image created by installing the mariadb

service mariadb start

# enable root user login for remote access 
RESULT_VARIABLE="$(mysql -uroot -sse "SELECT EXISTS(SELECT 1 FROM mysql.user WHERE User = 'root' AND Host='%')")"

if [ "$RESULT_VARIABLE" = 1 ]; then
  echo "FALSE"
else
mysql -u root <<MYSQL_SCRIPT
CREATE USER 'root'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
flush privileges;
MYSQL_SCRIPT
fi

service mariadb stop

#exec mariadbd --user=root

watch uptime
