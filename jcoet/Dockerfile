# syntax=docker/dockerfile:1

# FROM python:3

# RUN pip install --upgrade pip

# ENV PYTHONUNBUFFERED=1

# RUN mkdir /IMS
# WORKDIR /IMS
# COPY requirements.txt requirements.txt
# RUN pip3 install --default-timeout=100 -r requirements.txt

# COPY api IMS nginx static .env docker-compose.yml Dockerfile entrypoint.sh manage.py /IMS/

# COPY entrypoint.sh .



FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1# Creating working directory
RUN mkdir /jcoet
WORKDIR /jcoet
# Copying requirements
COPY canteentokensystem jcoet home media pollingbooth nginx static .env docker-compose.yml requirements.txt Dockerfile entrypoint.sh manage.py /jcoet/
COPY entrypoint.sh .

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \

    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

ENTRYPOINT ["sh","entrypoint.sh"]
