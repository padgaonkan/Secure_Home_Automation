FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install openssh-server sudo
RUN apt-get -y install man
RUN apt-get -y install iputils-ping net-tools


RUN apt-get update && apt-get -y install python3-pip
RUN pip3 install paho-mqtt
RUN pip3 install astral
RUN pip3 install datetime

COPY starter.sh /root/
COPY garden.py /root/
COPY certificates/ca/* /root/
RUN chmod u+x /root/starter.sh

CMD ["/root/starter.sh"]