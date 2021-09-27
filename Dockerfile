FROM python:3.9.7-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m pip list
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./main.py" ]
