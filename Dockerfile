# from alpine:latest
#  slim buster is better apparently
from python:3.8-slim-buster
ENV FLASK_APP=testapp
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080


WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY . /app

#  default port is 5000
# ENV FLASK_RUN_PORT=8000
EXPOSE 8080
ENV PORT 8080

RUN flask init-db
CMD ["flask","run","--host=0.0.0.0"]

# production ready server 
# might switch it up to Waitress package as it is light-weight
# RUN pip install Flask gunicorn

# # gunicorn server one worker process and 8 threads.
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app