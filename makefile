IMAGE?=nilsherzig/waterbot
VERSION?=$(shell git rev-parse HEAD | head -c 8)

TAG_VERSION=$(IMAGE):$(VERSION)
TAG_LATEST=$(IMAGE):latest

build-version: 
	docker build . -t $(TAG_VERSION)

push-version: 
	docker push $(TAG_VERSION)

build-latest: 
	docker build . -t $(TAG_LATEST)

push-latest: 
	docker push $(TAG_LATEST)

version: build-version push-version
latest: build-latest push-latest

run-latest: 
	docker run -e REMINDER_INTERVAL=60 -e USER_ID=123456789 -e MESSAGE="Time to drink water!" -e BOT_TOKEN=abcd1234 $(TAG_LATEST)

.PHONY: build push
