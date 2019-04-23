FROM python:3.7-alpine

WORKDIR /opt/socketserver

RUN pip install -U pip && pip install pytest pytest-xdist
RUN apk update && apk add rsync

ADD ./tests /opt/socketserver/tests

