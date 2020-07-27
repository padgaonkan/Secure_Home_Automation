NAME=room_temp_sensor

ALL: Dockerfile
	docker build $(OPTS) -t $(NAME) .
run:
	docker run -it  --net iot_net --ip 172.19.0.3 -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --name $(NAME) $(NAME)

clean:
	-docker kill $(NAME)
	-docker rm $(NAME)