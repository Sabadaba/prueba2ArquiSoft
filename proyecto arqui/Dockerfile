FROM python:3.8-slim AS base
RUN apt-get update && apt-get install --no-install-recommends --yes python3
RUN python3 -m pip install --upgrade pip
RUN django, djangorestframework, mysql
RUN pip install mysql-connector-python==8.0.29

ENV PYTHONUNBUFFERED=TRUE
#ARG DATABASE_IP
#ENV DATABASE_IP $DATABASE_IP

COPY API/ API/

CMD ["python",".\connect_mysql.py",".\manage.py"]