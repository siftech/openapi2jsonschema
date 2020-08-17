FROM debian:stable-slim
MAINTAINER Gareth Rushgrove "gareth@morethanseven.net"
RUN apt update
RUN apt install python3 python3-pip python3-venv -y

RUN pip3 install poetry

COPY . /src

WORKDIR /src
RUN poetry build
RUN poetry install

ENTRYPOINT ["poetry", "run", "openapi2jsonschema"]
