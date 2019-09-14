FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir /src
COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt