# https://phoenixnap.com/kb/how-to-install-anaconda-ubuntu-18-04-or-20-04

FROM debian:bullseye
RUN apt-get update
RUN apt-get install -y spyder

CMD ["spyder"]


# Building your image 	-   sudo docker build . -t   python
# list all images     	-   sudo docker images
# Run the image 
# docker run -it --net=host -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:ro   -v  $HOME/.Xauthority:$HOME/.Xauthority:ro -v ~/Music:/home/newuser python

# in rootless mode we do not have to create a user. 
# Root of container corrosponds to the local user inside the host
# This container's Root= local host user
# This container runs GUI application(geany), which can be accessed from local machine.
