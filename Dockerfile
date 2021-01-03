# from alpine:latest
#  slim buster is better apparently
from python:3.8-slim-buster
ENV FLASK_APP=testapp


WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY . /app

#  default port is 5000
# ENV FLASK_RUN_PORT=8000
EXPOSE 5000

RUN flask init-db
CMD ["flask","run","--host=0.0.0.0"]
