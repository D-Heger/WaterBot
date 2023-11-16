FROM python:3.10.13-alpine3.18

LABEL Maintainer="container@nilsherzig.com"

WORKDIR /waterbot

COPY ./src /waterbot/src
COPY ./usr /waterbot/usr

RUN pip install discord.py

CMD [ "python", "/waterbot/src/main.py"]
