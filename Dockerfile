FROM ubuntu:18.04

MAINTAINER Huang Sammy "lianghuang@ebay.com"


RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev


RUN apt-get install  stress


COPY . /opt/

RUN pip3 install flask

EXPOSE 8080

CMD [ "python3", "/opt/main.py" ]
