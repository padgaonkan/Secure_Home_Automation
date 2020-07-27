#Download the latest image of Ubuntu
FROM ubuntu:latest

#Initial packages to be installed
RUN apt-get update
RUN apt-get -y install openssh-server sudo
RUN apt-get -y install man
RUN apt-get -y install iputils-ping net-tools
RUN apt-get -y install mosquitto mosquitto-dev mosquitto-clients

#Create directories for certificates
WORKDIR /etc/mosquitto
RUN ls

#Copying all files and SSL certificates into Mosquitto directory
COPY starter.sh /root/
WORKDIR /etc/mosquitto/
COPY password.conf /etc/mosquitto/
COPY password.txt /etc/mosquitto/
COPY certificates/ca/* /etc/mosquitto/ca_certificates/
COPY certificates/broker/* /etc/mosquitto/certs/

#Run the configurations
RUN mosquitto_passwd -U password.txt
RUN cat password.txt
RUN chmod u+x /root/starter.sh
CMD ["/root/starter.sh"]