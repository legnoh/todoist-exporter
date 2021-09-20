FROM python:3-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN rm /usr/bin/lsb_release
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
