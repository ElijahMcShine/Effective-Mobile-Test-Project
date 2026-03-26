FROM alpine:3.23.3 AS build

ENV TZ=Europe/Moscow

RUN apk update \
    && apk add --no-cache --upgrade fcgi-dev \
    && apk add --no-cache fcgi \
    && apk add --no-cache musl-dev\
    && apk add --no-cache gcc \
    && mkdir /fastcgi

COPY mini_web.c /fastcgi/

RUN gcc -o /fastcgi/mini_web.fcgi /fastcgi/mini_web.c -lfcgi 

FROM alpine:3.23.3

ENV TZ=Europe/Moscow

WORKDIR /fastcgi

COPY --from=build /fastcgi/mini_web.fcgi /fastcgi/mini_web.fcgi

RUN apk add --no-cache spawn-fcgi \
    && apk add --no-cache fcgi \
    && addgroup -g 2000 fastcgi \
    && adduser -u 2000 -G fastcgi -s /bin/sh -D fastcgi

USER fastcgi

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=2s \
  CMD nc -z -w 2 127.0.0.1 8080 || exit 1

CMD ["spawn-fcgi", "-p", "8080", "-n", "/fastcgi/mini_web.fcgi"]