FROM python:3.14-alpine
LABEL maintainer="Ruan Franklin"

ENV PYTHONUNBUFFERED=1 

COPY ./requirements.txt /tmp/requirements.txt
COPY ./back /back

WORKDIR /back
EXPOSE 8000

RUN apk add --no-cache git openssl && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --no-cache libpq && \
    apk add --no-cache --virtual .tmp-build-deps \
    build-base libpq-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/py/bin:$PATH"
USER django-user