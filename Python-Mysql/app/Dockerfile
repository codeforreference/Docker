FROM python:3.7

RUN apt-get update && apt-get install -y python3-pip 

RUN mkdir -p /app

ADD . /app

WORKDIR /app

RUN pip3 install mysql-connector-python-rf 

CMD [ "python", "/app/scheduler.py" ]






