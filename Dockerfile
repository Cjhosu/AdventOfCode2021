FROM python:3.8.3
RUN apt-get update
RUN apt-get install -y vim
WORKDIR /usr/app/AoC
COPY . .
CMD bash


