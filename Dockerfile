from python:3.10

WORKDIR /app

copy . .

RUN pip install -r requirements.txt




