FROM python:3.10-alpine
RUN apk add --no-cache bash
# copy project
COPY ./ ./app
# set work directory
WORKDIR ./app

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt