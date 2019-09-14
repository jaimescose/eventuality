FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update

COPY docker-entrypoint.sh /

RUN mkdir /src
COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

# RUN adduser even
# USER even
