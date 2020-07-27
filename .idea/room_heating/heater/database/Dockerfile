FROM influxdb

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

RUN pip3 install paho-mqtt

RUN apt-get -y install net-tools

RUN pip3 install influxdb

COPY starter.sh /root/
COPY bridge.py /root/
COPY influxdb.conf /etc/influxdb/
COPY certificates/ca/* /root/
RUN chmod u+x /root/starter.sh


CMD ["/root/starter.sh"]