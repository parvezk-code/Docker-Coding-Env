#!/bin/sh 

# change user:group inside mariadb.service from mysql user to root user
sed -i 's/User=mysql/User=root/g' /etc/systemd/system/multi-user.target.wants/mariadb.service
sed -i 's/Group=mysql/Group=root/g' /etc/systemd/system/multi-user.target.wants/mariadb.service


# Change to not start the mariadb service. Commented the line exec "$@"
sed -i 's/exec "$@"/#exec "$@"/g'  /usr/local/bin/docker-entrypoint.sh

# run the default docker-entrypoint.sh with change done above
/bin/bash  /usr/local/bin/docker-entrypoint.sh mariadbd

gosu root chown -R root:root /var/lib/mysql /var/run/mysqld;

#gosu root chmod 777 -R /var/lib/mysql

exec "$@"

# exec mariadbd --user=root

#exec "$@"

#watch uptime
