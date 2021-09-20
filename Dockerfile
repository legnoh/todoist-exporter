FROM python:3.9.7-slim-buster

ENV WORKDIR /app/
WORKDIR ${WORKDIR}
COPY . $WORKDIR
RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy && \
    pip uninstall -y pipenv virtualenv-clone virtualenv

CMD ["python", "main.py"]
