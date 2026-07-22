FROM python:3.7-slim-buster

EXPOSE 8051

RUN apt-get update & apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit","run","app.py","--server.port=8051","--server.address=0.0.0.0"]