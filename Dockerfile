FROM python:3.9.7-slim-buster

ENV WORKDIR /app/
WORKDIR ${WORKDIR}
COPY . ${WORKDIR}
RUN pip install pipenv --no-cache-dir && pipenv install

CMD ["python", "main.py"]
