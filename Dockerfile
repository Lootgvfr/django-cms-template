FROM python:3.6
RUN adduser www-data www-data
RUN apt-get update && apt-get install -y vim nano
RUN apt-get update && \
  apt-get install -y bash netcat-openbsd
RUN mkdir /var/www/
RUN chmod 777 -R /var/www
RUN apt-get update && \
    apt-get install -y curl git && \
    curl -sL https://deb.nodesource.com/setup_9.x | /bin/bash - && \
    apt-get install -y nodejs build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY ./manage.py /application/manage.py
COPY ./requirements.pip /application/requirements.pip
COPY ./main /application/main
COPY ./cms /application/cms
COPY ./entrypoint.sh /application/entrypoint.sh
COPY ./webpack-stats.json /application/webpack-stats.json
COPY ./package.json /application/package.json
COPY ./webpack.config.js /application/webpack.config.js
COPY ./.env /application/.env
RUN pip install -r /application/requirements.pip
RUN chmod 777 -R /application/
WORKDIR /application
USER www-data
ENTRYPOINT /application/entrypoint.sh
