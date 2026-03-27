FROM python:3.14.3-alpine3.23 AS builder

COPY requirements.txt .

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev

RUN mkdir /install && \
  pip3 install --prefix=/install -r requirements.txt

FROM python:3.14.3-alpine3.23

WORKDIR /app

COPY app.py .
COPY --from=builder /install /usr/local

RUN apk add --no-cache curl \
    && apk add --no-cache libpq \
    && addgroup -g 2000 pythonuser \
    && adduser -u 2000 -G pythonuser -s /bin/sh -D pythonuser \
    && chown -R pythonuser:pythonuser /app

USER pythonuser

EXPOSE 8080

CMD ["python", "app.py"]