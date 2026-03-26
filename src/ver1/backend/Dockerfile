FROM python:3.14.3-alpine3.23

WORKDIR /app

COPY app.py .

RUN apk add --no-cache curl \
    && addgroup -g 2000 pythonuser \
    && adduser -u 2000 -G pythonuser -s /bin/sh -D pythonuser \
    && chown -R pythonuser:pythonuser /app

USER pythonuser

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
PYTHONPATH=/app

EXPOSE 8080

CMD ["python", "app.py"]