FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY crypto_logger / app/
WORKDIR /app
EXPOSE 8000


RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN adduser --disabled-password calc_user

USER calc_user