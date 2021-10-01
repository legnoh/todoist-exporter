FROM python:3-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m pip list
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv install

COPY . .

CMD [ "python3", "./main.py" ]
