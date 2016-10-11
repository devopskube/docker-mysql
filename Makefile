all: build

build:
	@docker build --tag=devopskube/mysql .
