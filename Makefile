IMAGE = devlusaja-fastapi:latest
CONTAINER = fastapi_container

build:
	@docker build -t ${IMAGE} .

up:
	@docker run -d --name ${CONTAINER} -p 8000:8000 -v ${PWD}/app:/code/app ${IMAGE}
	@make log

down:
	@docker rm -f ${CONTAINER}

log:
	@docker logs -f ${CONTAINER}

test:
	@docker run --rm -it --name ${CONTAINER}-test -v ${PWD}/app:/code/app ${IMAGE} pytest -vv -s -p no:cacheprovider
