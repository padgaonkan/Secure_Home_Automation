FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install openssh-server sudo
RUN apt-get -y install man
RUN apt-get -y install iputils-ping net-tools


RUN apt-get update && apt-get -y install python3-pip
RUN pip3 install paho-mqtt
RUN pip3 install pyowm
RUN pip3 install datetime
RUN apt-get -y install python3-tk

WORKDIR /root/
COPY certificates/ca/ca.crt /root/
RUN ls
COPY starter.sh /root/
COPY temperature_sensor.py /root/
RUN chmod u+x /root/starter.sh
CMD ["/root/starter.sh"]