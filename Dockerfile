FROM python:3-slim-buster

WORKDIR /usr/src/app
RUN pip3 install --upgrade pip && pip3 install pipenv && pipenv install
COPY . .
CMD [ "python3", "./main.py" ]
