FROM python:3.6
RUN adduser www-data www-data
RUN apt-get update && apt-get install -y vim nano
RUN apt-get update && \
  apt-get install -y bash netcat-openbsd
COPY ./manage.py /application/manage.py
COPY ./requirements.pip /application/requirements.pip
COPY ./main /application/main
COPY ./cms /application/cms
COPY ./entrypoint.sh /application/entrypoint.sh
COPY ./webpack-stats.json /application/webpack-stats.json
RUN pip install -r /application/requirements.pip
WORKDIR /application
USER www-data
ENTRYPOINT /application/entrypoint.sh
