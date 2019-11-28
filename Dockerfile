FROM python:3.6-slim

COPY . /root

WORKDIR /root

# EXPOSE 5000

RUN pip install flask gunicorn numpy sklearn scipy joblib flask_wtf wtforms werkzeug