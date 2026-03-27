FROM postgres:18.3-alpine3.23

USER postgres

COPY ./model.sql /docker-entrypoint-initdb.d/
