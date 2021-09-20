FROM python:3.9.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip list
RUN python3 -m pip list
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
