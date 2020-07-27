NAME = heater_db
ALL: Dockerfile
	docker build $(OPTS) -t $(NAME) .

run:
	docker run -it --net iot_net --ip 172.19.0.6 --name $(NAME) $(NAME)

clean:
	-docker kill $(NAME)
	-docker rm $(NAME)
