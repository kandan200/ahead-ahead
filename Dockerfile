# syntax=docker/dockerfile:1
FROM python:3.10.13-bookworm as base

WORKDIR /app

COPY requirements.txt /app

RUN  python3 -m pip install -r requirements.txt
COPY . /app
EXPOSE 8000
CMD bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
