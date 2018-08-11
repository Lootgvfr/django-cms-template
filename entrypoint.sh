#!/usr/bin/env bash
waitForDatabase() {
    while ! nc -z postgres 5432;
        do
          echo waiting for PostgreSQL ready...;
          sleep 1;
        done;
    echo PostgreSQL has been ready to accept messages!;
}

waitForDatabase
echo "Install node modules"
cd /application && npm install

echo "Webpack build.."
cd /application && npm run webpack-local

echo "Apply database migrations"
python /application/manage.py migrate

echo "Starting server"
python /application/manage.py runserver 0.0.0.0:8080