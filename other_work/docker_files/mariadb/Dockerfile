FROM ubuntu:20.04

# export DEBIAN_FRONTEND=noninteractive

RUN apt-get update

#--no-install-recommends 

RUN apt-get install -y curl 

RUN curl -LsS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash -s -- --mariadb-server-version=10.7 --skip-maxscale --skip-tools

RUN apt-get update

RUN apt-get install -y  mariadb-server


# CMD service mysql start

# https://mariadb.com/kb/en/configuring-mariadb-for-remote-client-access/
#https://webdock.io/en/docs/how-guides/database-guides/how-enable-remote-access-your-mariadbmysql-database

#RUN echo "[mysqld]" >> /etc/alternatives/my.cnf
RUN echo "[mariadbd]" >> /etc/alternatives/my.cnf
RUN echo "skip-networking=0" >> /etc/alternatives/my.cnf
RUN echo "skip-bind-address" >> /etc/alternatives/my.cnf
RUN echo "skip-host-cache" >> /etc/alternatives/my.cnf
RUN echo "skip-name-resolve" >> /etc/alternatives/my.cnf

COPY ./docker-entrypoint.sh /usr/local/bin/

RUN chmod a+x /usr/local/bin/docker-entrypoint.sh

COPY ./remote_root.sh /usr/local/bin/

RUN chmod a+x /usr/local/bin/remote_root.sh

ENTRYPOINT ["docker-entrypoint.sh"]

#CMD [ "watch", "uptime" ]

# Building your image 	-   sudo docker build . -t   zmariadb
# docker run -it  zmariadb

# in rootless mode we do not have to create a user. 
# Root of container corrosponds to the local user inside the host
# This container's Root= local host user
# This container runs GUI application(geany), which can be accessed from local machine.
