FROM python:3.7-alpine

ENV DJANGOAPP=/usr/src/clima_api
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install psycopg2 and pillow dependencies
RUN apk update \
    && apk add build-base musl-dev linux-headers postgresql-dev python3-dev py3-setuptools


WORKDIR $DJANGOAPP/

RUN pip install --upgrade pip
COPY ./requirements.txt $DJANGOAPP/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . $DJANGOAPP
#CMD ["flask", "run"]
