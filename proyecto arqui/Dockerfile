FROM python:3.8-slim AS base
RUN apt-get update && apt-get install --no-install-recommends --yes python3
RUN apt-get -y install default-libmysqlclient-dev
RUN python3 -m pip install --upgrade pip
RUN pip install django
RUN pip install djangorestframework 
RUN pip install mysql-connector-python==8.0.29

ENV PYTHONUNBUFFERED=TRUE
#ARG DATABASE_IP
#ENV DATABASE_IP $DATABASE_IP

COPY reservas reservas
RUN python reservas/connect_mysql.py
CMD ["python",".\connect_mysql.py","runserver"]
