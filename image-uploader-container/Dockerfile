FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /application

COPY ./application/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]