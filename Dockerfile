FROM python:3

RUN mkdir /code

ENV PYTHONUNBUFFERED 1

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/
