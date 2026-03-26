FROM nginx:1.29.7-alpine

ENV TZ=Europe/Moscow

RUN chown -R nginx:nginx /etc/nginx/nginx.conf \
    && chown -R nginx:nginx /var/cache/nginx \
    && chown -R nginx:nginx /home \
    && touch /var/run/nginx.pid \
    && chown -R nginx:nginx /var/run/nginx.pid \
    && chmod u-s /bin/su \
    && chmod u-s /bin/mount \
    && chmod u-s /bin/umount \
    && chmod u-s /usr/bin/passwd \
    && apk add --no-cache curl

USER nginx

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=2s --retries=3 \
  CMD curl -fsS http://localhost:8080/ || exit 1

ENTRYPOINT ["../docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]