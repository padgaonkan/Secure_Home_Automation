NAME = dashboard
CWD=$(shell pwd)
ALL: Dockerfile
	-mkdir -p storage
	-chmod a+rwx storage
	docker build $(OPTS) --no-cache -t $(NAME) .

run:
	docker run -it --net iot_net --ip 172.19.0.10 --name $(NAME) -v $(CWD)/storage:/var/lib/grafana $(NAME)

clean:
	-docker kill $(NAME)
	-docker rm $(NAME)


