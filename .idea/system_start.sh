#!/bin/bash

gnome-terminal -e `docker run -it --net iot_net --ip 172.19.0.2 --name server server` #Start the server
#gnome-terminal -e `docker run -it  --net iot_net --ip 172.19.0.3 -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --name room_temp_sensor room_temp_sensor` #Temperature Sensor
#gnome-terminal -e `docker run -it --net iot_net --ip 172.19.0.4 --name room_db room_db`
#gnome-terminal -e `docker run -it  --net iot_net --ip 172.19.0.5 --name heater heater`
#gnome-terminal -e `docker run -it  --net iot_net --ip 172.19.0.6 --name heater_db heater_db`
#gnome-terminal -e `docker run -it  --net iot_net --ip 172.19.0.7 --name garden_lights garden_lights`
#gnome-terminal -e `docker run -it  --net iot_net --ip 172.19.0.8 --name garden_db garden_db`
#gnome-terminal -e `docker run -it  --net iot_net --ip 172.19.0.9 -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw  --name panel panel`
#gnome-terminal -e `docker run -it --net iot_net --ip 172.19.0.10 --name dashboard -v $(CWD)/storage:/var/lib/grafana dashboard`


