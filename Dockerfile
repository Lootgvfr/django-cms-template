FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PROJECT_NAME=dancing_school
RUN mkdir /$PROJECT_NAME
WORKDIR /$PROJECT_NAME
RUN pip install -r requirements.txt
