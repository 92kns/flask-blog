# from alpine:latest

# RUN apk add --no-cache python3-dev py3-pip \
#     && pip3 install --upgrade pip

# WORKDIR /app

# ENV FLASK_APP=testapp

# COPY . /app

# RUN pip3 --no-cache-dir install -r requirements.txt

from python:3.8-slim-buster
ENV FLASK_APP=testapp
# ENV FLASK_RUN_PORT=8000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY . /app

# ENV FLASK_RUN_PORT=8000
EXPOSE 5000


# ENTRYPOINT ["python"]
RUN flask init-db
CMD ["flask","run","--host=0.0.0.0"]
# ENTRYPOINT ["python"]
# CMD ["-m","flask","init-db","&&","flask","run"]