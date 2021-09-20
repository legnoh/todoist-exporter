FROM python:3.9.7-slim-buster@sha256:3ee47e81705deb6000726e9277f796721ddc0bc3ece785a7edb5ec9f49b0dc3a

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
