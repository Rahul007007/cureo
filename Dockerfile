FROM python:3-alpine3.10

WORKDIR /app

COPY . /app

CMD [ "python" , "file.py"]